"""
Combine raw_A1/A2/B1 into one ordered, de-duplicated list and cut it into batches of 100.

Order: A1 first, then A2 words that are new, then B1 words that are new.
Inside each level the words are shuffled with a fixed seed so every batch mixes nouns, verbs and
adjectives instead of being "all words starting with Ab-".

Usage: python tools/build_batches.py scratch/raw scratch/entries_all.json
"""
import sys, re, json, random

sys.stdout.reconfigure(encoding="utf-8")


def key_of(e):
    k = e["lemma"].lower()
    k = re.sub(r"\(.*?\)", "", k)
    k = re.sub(r"^sich\s+", "", k)
    k = re.sub(r"[-\s]+", "", k)
    return k


def tidy(e):
    de = e["de"]
    de = re.sub(r"\s*/\s*(die|der|das)\s*$", "", de)
    de = re.sub(r"\s*,\s*-?$", "", de)
    de = re.sub(r"\s+", " ", de).strip()
    e["de"] = de
    ex = e.get("example", "").strip()
    words = ex.split()
    ok = len(words) >= 3 and re.search(r"[.!?\"“”)]$", ex) and not re.match(r"^[a-zäöüß]", ex)
    e["example"] = ex if ok else ""
    return e


def main(raw_dir, out_file):
    seen = set()
    ordered = []
    per_level = {}
    for lv in ("A1", "A2", "B1"):
        ents = json.load(open(f"{raw_dir}/raw_{lv}.json", encoding="utf-8"))
        fresh = []
        for e in ents:
            e = tidy(e)
            k = key_of(e)
            if not k or len(k) < 2 or k in seen:
                continue
            seen.add(k)
            fresh.append(e)
        rnd = random.Random(2026)
        rnd.shuffle(fresh)
        per_level[lv] = len(fresh)
        ordered.extend(fresh)
    out = []
    counters = {}
    for e in ordered:
        lv = e["level"]
        counters[lv] = counters.get(lv, 0) + 1
        out.append({
            "id": f"{lv}-{counters[lv]:04d}",
            "level": lv,
            "de": e["de"],
            "forms": e.get("forms", ""),
            "example": e["example"],
        })
    # cut into batches of 100 *within* each level (last batch of a level may be smaller)
    batches = []
    for lv in ("A1", "A2", "B1"):
        lv_items = [x for x in out if x["level"] == lv]
        for i in range(0, len(lv_items), 100):
            chunk = lv_items[i:i + 100]
            batches.append({"batchId": f"{lv}-B{i // 100 + 1:02d}", "level": lv, "number": i // 100 + 1, "items": chunk})
    json.dump(batches, open(out_file, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(per_level, "total", len(out), "batches", len(batches))
    print("without example:", sum(1 for x in out if not x["example"]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
