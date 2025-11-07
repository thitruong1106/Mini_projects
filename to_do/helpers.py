{
  "title": "Fix monitor setup",
  "priority": "high",      # "low" | "med" | "high"
  "status": "pending"      # "pending" | "done"
}

import json, os 

def load_json(path): 
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return [] 
    try: 
        with open(path, 'r', encoding='utf-8') as file: 
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return [] 
    
def save_json(path, data): 
    with open(path, 'w', encoding='utf-8') as file: 
        json.dump(data, file, indent=4, ensure_ascii=False)