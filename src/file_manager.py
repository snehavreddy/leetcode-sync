import os


BASE_DIR = "leetcode-solutions"
LANGUAGE_MAP = {
    "python3": ("python", ".py"),
    "csharp": ("csharp", ".cs"),
    "mysql": ("sql", ".sql"),
}


class FileManager:

    def __init__(self):
        self.create_folders()

    def create_folders(self):
        for folder, _ in LANGUAGE_MAP.values():
            os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)

    def get_language_info(self, lang):
        return LANGUAGE_MAP.get(lang, (None, None))

    def save_code(self, folder, filename, code):
        path = os.path.join(BASE_DIR, folder, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(code)