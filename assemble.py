import os
import json

def assemble():
    data_dir = "data"
    template_path = "template.html"

    if not os.path.exists(template_path):
        print(f"Error: {template_path} not found!")
        return

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    all_lessons = []
    for i in range(1, 16):
        file_path = os.path.join(data_dir, f"module{i}.json")
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f_mod:
                    lessons = json.load(f_mod)
                    all_lessons.extend(lessons)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                return
        else:
            print(f"Warning: {file_path} does not exist.")

    lessons_json = json.dumps(all_lessons, ensure_ascii=False, indent=2)
    base_assembled = template.replace("__LESSON_DATA_PLACEHOLDER__", lessons_json)

    index_en = base_assembled.replace("__DEFAULT_LANG__", "en")
    index_en = index_en.replace("__APP_TITLE__", "DeutschMeister — A2.1 bis B1 Alltag & Goethe-Zertifikat")
    index_en = index_en.replace("__APP_DESCRIPTION__", "Complete German A2.1, A2.2 & B1 Academy for Real-World Conversation in Germany and Official Goethe-Zertifikat Exam Training.")

    with open("index.html", "w", encoding="utf-8") as f_en:
        f_en.write(index_en)
    print(f"Successfully assembled index.html with {len(all_lessons)} lessons!")

if __name__ == "__main__":
    assemble()
