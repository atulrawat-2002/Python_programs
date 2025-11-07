import os

TASK_FILE = "task.txt"
tasks = []

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding='utf-8') as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks

def save_task(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['text']} || {status} \n")

    
def display_tasks(tasks):
    if not tasks:
        print(f"No task found ")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i} {checkbox} {task['text']}")


def task_manager():
    tasks = load_tasks()

    while True:
        print("\n----------Taks list Manager----------")
        print("1. Add task")
        print("2. View Task")
        print("3. Mark Task as complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Please enter your choice 1-5: ").strip()



        match choice:

            case "1":
                text = input("Enter the task: ")
                if text:
                    tasks.append({"text": text, "done": False})
                    save_task(tasks)
                else:
                    print("Empty task ")

            case "2":
                display_tasks(tasks)

            case "3":
                display_tasks(tasks)

                try:
                    num = int(input("Enter the taks number: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        save_task(tasks)
                        print("Marked done ")
                    else:
                        print("Inavlid operation ")
                except ValueError:
                    print("A value error ")

            case "4":
                display_tasks(tasks)

                try:
                    num = int(input("Enter the taks number pt be delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_task(tasks)
                        print(f"{removed['text']} task removed ")
                    else:
                        print("Inavlid operation ")
                except ValueError:
                    print("A value error ")

            case "5":
                print("Exiting Task manager ")
                break   
            
            
task_manager()


                
