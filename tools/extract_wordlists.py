"""
Extract headwords + first example sentence from the Goethe / textbook PDF word lists.

Usage:  python tools/extract_wordlists.py <folder-with-pdfs> <output-folder>

Output: raw_A1.json, raw_A2.json, raw_B1.json  (lists of entries)
Each entry: {"de": "der Ausflug, -e", "lemma": "Ausflug", "forms": "", "example": "...", "level": "B1"}

Note: the file the user called "b2_word_list.pdf" turned out to contain the same B1 alphabetical list
(Goethe-Zertifikat B1 'Prüfungsziele, Testbeschreibung'), so it is used as a second B1 source only to
fill in missing example sentences.
"""
import sys, re, json, os
import fitz  # pymupdf

sys.stdout.reconfigure(encoding="utf-8")

SRC = {
    "A1": "media_1794426556681_89bd6bc3.pdf",  # Start Deutsch 1 (tab layout)
    "A2": "media_1794426551624_8ad3a79b.pdf",  # Goethe A2 (2 columns, example at +71)
    "B1": "media_1794426546097_44eac992.pdf",  # Goethe B1 (2 columns, example at +97)
    "B1b": "media_1794426524233_226d4dcf.pdf",  # 'b2_word_list' (really B1 again)
}

NOUN_PREFIX = re.compile(r"^(der|die|das|r|e|s|r/e|e/r|das/der|der/das)\s+", re.I)
CONT_END = re.compile(r"(,|→|\()\s*$")
HYPH_END = re.compile(r"^(der|die|das|r|e|s)\s+\S+-\s*$", re.I)


def is_continued(raw):
    return bool(CONT_END.search(raw) or HYPH_END.match(raw))


def clean_example(txt):
    txt = re.sub(r"\s+", " ", txt).strip()
    txt = re.sub(r"^\d+\.\s*", "", txt)
    return txt


def join_wrapped(lines):
    out = ""
    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        if out.endswith("-") and ln[:1].islower() and not out.endswith(" -"):
            out = out[:-1] + ln
        else:
            out = (out + " " + ln).strip()
    return out


def first_example(example_lines):
    if not example_lines:
        return ""
    numbered = bool(re.match(r"^\s*\d+\.\s", example_lines[0]))
    groups, cur = [], []
    if numbered:
        for ln in example_lines:
            if re.match(r"^\s*\d+\.\s", ln) and cur:
                groups.append(cur)
                cur = [ln]
            else:
                cur.append(ln)
        if cur:
            groups.append(cur)
    else:
        acc = []
        for ln in example_lines:
            acc.append(ln)
            if re.search(r"[.!?\"“”)]\s*$", ln):
                groups.append(acc)
                acc = []
        if acc:
            groups.append(acc)
    if not groups:
        return ""
    return clean_example(join_wrapped(groups[0]))


def split_headword(raw):
    raw = re.sub(r"\s+", " ", raw).strip()
    raw = re.sub(r"\s*→.*$", "", raw)
    raw = re.sub(r"\((?:D|A|CH|D, A|A, CH|D, CH|A, D|CH, A|D, CH, A)\)", "", raw)
    raw = re.sub(r"\s+,", ",", raw).strip(" ,;")
    parts = [p.strip() for p in raw.split(",")]
    first = parts[0]
    rest = ", ".join(parts[1:])
    if NOUN_PREFIX.match(first):
        art = {"r": "der", "e": "die", "s": "das"}
        m = NOUN_PREFIX.match(first)
        head = first
        a = m.group(1).lower()
        if a in art:
            head = art[a] + " " + first[m.end():]
        de = head + ((", " + rest) if rest else "")
        lemma = first[m.end():]
        return de, lemma, ""
    return first, first, rest


BAD = re.compile(r"[0-9=→•©@]|ISBN|Goethe|Modellsatz|Prüfung|Testbeschreibung|Seite|Notizen|www|\.\.\.")


def valid_head(h):
    h = h.strip()
    if len(h) < 2 or len(h) > 55:
        return False
    if BAD.search(h):
        return False
    if h.startswith("(z.") or h.startswith("(z "):
        return False
    if not re.match(r"^[A-Za-zÄÖÜäöüß(/]", h):
        return False
    if len(h.split()) > 5:
        return False
    # must not look like a sentence
    if re.search(r"[.!?]$", h):
        return False
    return True


def page_lines_words(page, split_x=297, ymin=62, ymax=782):
    """Group words into lines per column. Returns {0: [(y, [(x, text)...])], 1: [...]}"""
    cols = {0: [], 1: []}
    words = page.get_text("words")
    for w in words:
        x0, y0, txt = w[0], w[1], w[4]
        if y0 < ymin or y0 > ymax or x0 < 25:
            continue
        cols[0 if x0 < split_x else 1].append((x0, y0, txt))
    out = {}
    for c, ws in cols.items():
        ws.sort(key=lambda r: (round(r[1]), r[0]))
        lines = []
        for x, y, t in ws:
            if lines and abs(lines[-1][0] - y) <= 2.5:
                lines[-1][1].append((x, t))
            else:
                lines.append([y, [(x, t)]])
        out[c] = lines
    return out


def parse_columns_words(doc, level, first_page, last_page, ex_offset):
    entries = []
    for pno in range(first_page, last_page):
        cols = page_lines_words(doc[pno])
        for c, lines in cols.items():
            if not lines:
                continue
            col_left = min(x for _, ws in lines for x, _ in ws)
            cut = col_left + ex_offset - 12
            cur_list = []
            for y, ws in lines:
                head = " ".join(t for x, t in ws if x < cut).strip()
                ex = " ".join(t for x, t in ws if x >= cut).strip()
                if head:
                    if cur_list and is_continued(cur_list[-1]["raw"]):
                        cur_list[-1]["raw"] += " " + head
                    elif len(head) == 1 and head.isupper():
                        pass  # letter heading
                    else:
                        cur_list.append({"raw": head, "ex": []})
                if ex and cur_list:
                    cur_list[-1]["ex"].append(ex)
            for e in cur_list:
                if not valid_head(e["raw"]):
                    continue
                de, lemma, forms = split_headword(e["raw"])
                entries.append({"de": de, "lemma": lemma, "forms": forms,
                                "example": first_example(e["ex"]), "level": level})
    return entries


def parse_tab(doc, level, first_page, last_page):
    entries = []
    cur = None
    for pno in range(first_page, last_page):
        page = doc[pno]
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                x0, y0 = l["bbox"][0], l["bbox"][1]
                txt = "".join(s["text"] for s in l["spans"]).replace("\t", " ").strip()
                if y0 < 70 or y0 > 770 or not txt:
                    continue
                if x0 < 200:
                    if len(txt) == 1:
                        continue
                    if cur is not None and is_continued(cur["raw"]):
                        cur["raw"] += " " + txt
                        continue
                    cur = {"raw": txt, "ex": []}
                    entries.append(cur)
                elif cur is not None:
                    cur["ex"].append(txt)
    out = []
    for e in entries:
        if not valid_head(e["raw"]):
            continue
        de, lemma, forms = split_headword(e["raw"])
        out.append({"de": de, "lemma": lemma, "forms": forms,
                    "example": first_example(e["ex"]), "level": level})
    return out


def find_first_page(doc, start, test):
    for i in range(start, len(doc)):
        if test(doc[i].get_text()):
            return i
    return start


def dedupe(entries):
    seen, uniq = set(), []
    for e in entries:
        key = e["lemma"].lower()
        if key in seen:
            continue
        seen.add(key)
        uniq.append(e)
    return uniq


def main(src_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    res = {}
    # A1
    doc = fitz.open(os.path.join(src_dir, SRC["A1"]))
    start = find_first_page(doc, 0, lambda t: "abfahren" in t)
    res["A1"] = dedupe(parse_tab(doc, "A1", start, len(doc)))
    # A2
    doc = fitz.open(os.path.join(src_dir, SRC["A2"]))
    start = find_first_page(doc, 5, lambda t: "das Angebot" in t)
    res["A2"] = dedupe(parse_columns_words(doc, "A2", start, len(doc), 71))
    # B1
    doc = fitz.open(os.path.join(src_dir, SRC["B1"]))
    start = find_first_page(doc, 7, lambda t: "abfahren" in t and "abbiegen" in t)
    b1 = dedupe(parse_columns_words(doc, "B1", start, len(doc), 97))
    # second B1 source, to fill missing examples
    doc2 = fitz.open(os.path.join(src_dir, SRC["B1b"]))
    b1b = dedupe(parse_columns_words(doc2, "B1", 0, len(doc2), 107))
    ex_map = {e["lemma"].lower(): e["example"] for e in b1b if e["example"]}
    filled = 0
    for e in b1:
        if not e["example"] and e["lemma"].lower() in ex_map:
            e["example"] = ex_map[e["lemma"].lower()]
            filled += 1
    # words only in b1b
    have = {e["lemma"].lower() for e in b1}
    extra = [e for e in b1b if e["lemma"].lower() not in have]
    res["B1"] = b1 + extra
    print("B1 start", start + 1, "filled examples", filled, "extra from second source", len(extra))
    for lv, ents in res.items():
        with open(os.path.join(out_dir, f"raw_{lv}.json"), "w", encoding="utf-8") as f:
            json.dump(ents, f, ensure_ascii=False, indent=1)
        print(lv, len(ents), "without example:", sum(1 for e in ents if not e["example"]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
