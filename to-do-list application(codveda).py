import json

file_name = "tasks.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({
        "task": task,
        "done": False
    })
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if len(tasks)==0:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['task']} [{status}]")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        tasks.pop(task_num - 1)
        save_tasks(tasks)
        print("Task deleted successfully!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number: "))
        tasks[task_num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    tasks = load_tasks()

    while True:
        print("\n------TO-DO LIST -------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task Done")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            mark_done(tasks)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main()