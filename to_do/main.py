from tasks import add_task, list_task, mark_done, delete_tasks

PATH = "tasks.json"

def show_menu(): 
    print("1.Add Tasks \n 2.List Tasks \n 3.Mark Done \n 4.Delete Tasks \n 5.Quit")

def prompt_priority():
    while True:
        p = input("Priority (low/med/high) [med]: ").strip().lower() or "med"
        if p in {"low", "med", "high"}:
            return p
        print("Please enter low/med/high.")

def run():
    while True: 
        show_menu()
        choice = input("Choose 1-5").strip()
        if choice == "1":
            title = input("Task title: ").strip()
            if not title: 
                print("Task name cannot be empty")
                continue
            priority = prompt_priority()
            add_task(PATH, title, priority)
            print(f"Task: {title} has been added")
        elif choice == "2":
            tasks = list_task(PATH)
            if not tasks: #if empty 
                print("No tasks")
            else: #if there task
                for i,t in enumerate(tasks):
                    print(f"{i:>2} | {t['status']:<7} | {t['priority']:<8} | {t['title']}")
        elif choice == "3":
            idx = input("Task # to mark done: ").strip()
            if idx.isdigit() and mark_done(PATH, int(idx)):
                print("✅ Marked done.")
            else:
                print("⚠️ Invalid index.")
        elif choice == "4":
            idx = input("Task # to delete: ").strip()
            if idx.isdigit() and delete_tasks(PATH, int(idx)):
                print("🗑️ Deleted.")
            else:
                print("⚠️ Invalid index.")
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Choose 1-5.")

if __name__ == "__main__":
    run()