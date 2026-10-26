import os
import json

def assemble():
    data_dir = "data"
    template_path = "template.html"
    index_path = "index.html"

    if not os.path.exists(template_path):
        print(f"Error: {template_path} not found!")
        return

    # Read template.html
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Load and combine all lessons in order (module1 to module15)
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

    # Replace placeholder with lessons data formatted as JSON
    lessons_json = json.dumps(all_lessons, ensure_ascii=False, indent=2)
    base_assembled = template.replace("__LESSON_DATA_PLACEHOLDER__", lessons_json)

    # 1. Compile index.html (English default)
    index_en = base_assembled.replace("__DEFAULT_LANG__", "en")
    index_en = index_en.replace("__APP_TITLE__", "DeutschMeister — Dein A2 Deutschkurs")
    index_en = index_en.replace("__APP_DESCRIPTION__", "Interactive German A2 course with 20 lessons, exercises, and exams. Learn German with DeutschMeister!")
    
    with open("index.html", "w", encoding="utf-8") as f_en:
        f_en.write(index_en)
    print("Successfully assembled index.html (English default)!")

    # 2. Compile index_vi.html (Vietnamese default)
    index_vi = base_assembled.replace("__DEFAULT_LANG__", "vi")
    index_vi = index_vi.replace("__APP_TITLE__", "DeutschMeister — Khóa học tiếng Đức A2")
    index_vi = index_vi.replace("__APP_DESCRIPTION__", "Khóa học tiếng Đức A2 tương tác với 20 bài học, bài tập và bài thi. Học tiếng Đức cùng DeutschMeister!")
    
    with open("index_vi.html", "w", encoding="utf-8") as f_vi:
        f_vi.write(index_vi)
    print("Successfully assembled index_vi.html (Vietnamese default)!")

if __name__ == "__main__":
    assemble()
