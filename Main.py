tasks = []

#prompt to add a task
def create_tasks():
    title = input("Enter your task title: ")
    description = input("Enter your task description: ")
    tasks.append({"Task title": title, "Task Description": description})
    print("Task created successfully")
#See tasks
def see_tasks():
    if tasks:
        print("Available tasks: ")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. Task title: {task['Task title']}, Task Description: {task['Task Description']}")
        else:
            print("No tasks available")
#update tasks
def update_tasks():
    see_tasks()
    if tasks: 
        tasks_index = int(input("Provide the index of your task to be update: "))-1
        if 0 <= tasks_index < len(tasks):
            new_task_title = input("Provide me a title or press enter to keep current title: ")
            new_task_description = input("Provide me a description or press enter to keep current description: ")        
            if new_task_title:  ""
            tasks[tasks_index]['task title'] = new_task_title
            if new_task_description: ""
            tasks[tasks_index]['task description'] = new_task_description
            print("Task updated")
        else:
            print("ERROR INVALID INDEX")
            
    else:
        
        print("No tasks available")
#delete tasks
def delete_tasks():
    see_tasks()
    if tasks: 
        tasks_index = int(input("Provide the index of the task to be deleted: ")) -1 
        if 0 <= tasks_index < len(tasks):
            deleted_task = tasks.pop(tasks_index)
            print(f"task ' {deleted_task['Task title']}' Deleted successfully")
        else:
            print("Invalid index")
    else: 
        print("No tasks available")


#Menu
while True: 
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Select an option from (1-5): ")

    if choice == ('1'): 
        create_tasks()
    elif choice ==('2'):
        see_tasks()
    elif choice==('3'):
        update_tasks()
    elif choice == ('4'):
        delete_tasks()
    elif choice == ('5'):
        print("Exiting from task manager...")
        break
    else:
        print("Invalid option. Please select between 1 and 5")

