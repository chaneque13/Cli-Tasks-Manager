import json
from typing import List, Dict, Optional

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict[str, str]]:
    """Load tasks from JSON file. Return empty list if file doesn't exist."""
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks: List[Dict[str, str]]) -> None:
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def create_task(tasks: List[Dict[str, str]]) -> None:
    """Add a new task."""
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    tasks.append({"title": title, "description": description})
    save_tasks(tasks)
    print("✅ Task added!")

def view_tasks(tasks: List[Dict[str, str]]) -> None:
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['title']}: {task['description']}")

def update_task(tasks: List[Dict[str, str]]) -> None:
    """Update an existing task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_idx = int(input("Enter task number to update: ")) - 1
        if 0 <= task_idx < len(tasks):
            new_title = input("New title (press Enter to keep current): ").strip()
            new_desc = input("New description (press Enter to keep current): ").strip()
            if new_title:
                tasks[task_idx]["title"] = new_title
            if new_desc:
                tasks[task_idx]["description"] = new_desc
            save_tasks(tasks)
            print("✅ Task updated!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks: List[Dict[str, str]]) -> None:
    """Delete a task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_idx < len(tasks):
            deleted_task = tasks.pop(task_idx)
            save_tasks(tasks)
            print(f"✅ Deleted: {deleted_task['title']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main() -> None:
    """Main CLI loop."""
    tasks = load_tasks()
    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            create_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()