import json, os

def load_students(path):
    if not os.path.exists(path):
        return []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []

def save_student(path, data):
    with open(path, 'w', encoding='utf-8') as file: 
        json.dump(data, file, indent=2, ensure_ascii=False)
