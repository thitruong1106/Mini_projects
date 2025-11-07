from helpers import load_json, save_json

def add_task(path, title, priority = 'med'):
    tasks = load_json(path) #load path files 
    tasks.append({
        "title": title.strip(), 
        "priority": priority, #default status med
        "status": "pending"
    })
    save_json(path, tasks)
    return True 

def list_task(path):
    return load_json(path)

def mark_done(path, index): 
    tasks = load_json(path)
    if 0 <= index < len(tasks):
        tasks[index]['status'] = "done"
        save_json(path, tasks)
        return True
    return False 

def delete_tasks(path, index):
    tasks = load_json(path)
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_json(path, tasks)
        return True 
    return False 
