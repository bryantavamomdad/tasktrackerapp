from colorama import Fore, Style

tasks = []

def add_task():
    task_name = input(Fore.GREEN+"Enter task name: ")
    priority = int(input("Enter priority level (1 - Low, 2 - Medium, 3 - High): "))
    tasks.append({"task_name": task_name, "completed": False, "priority": priority})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks added yet!")
    else:
        sorted_tasks = sorted(tasks, key=lambda x: x['priority'], reverse=True)
        print(Fore.LIGHTCYAN_EX + "Tasks:"+Style.RESET_ALL)
        for index, task in enumerate(sorted_tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            priority = "Low" if task["priority"] == 1 else "Medium" if task["priority"] == 2 else "High"
            
            # Set text color based on priority
            if task["priority"] == 3:
                print(f"{index}. {Fore.RED}{task['task_name']} - Priority: {priority} - {status}{Style.RESET_ALL}")
            elif task["priority"] == 2:
                print(f"{index}. {Fore.YELLOW}{task['task_name']} - Priority: {priority} - {status}{Style.RESET_ALL}")
            else:
                print(f"{index}. {Fore.GREEN}{task['task_name']} - Priority: {priority} - {status}{Style.RESET_ALL}")


def mark_completed():
    view_tasks()
    if tasks:
        task_index = int(input(Fore.BLUE+"Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["completed"] = True
            print(Fore.LIGHTMAGENTA_EX+"Task marked as completed!")
        else:
            print("Invalid task number.")
    else:
        print("No tasks added yet!")

def delete_task():
    view_tasks()
    if tasks:
        task_index = int(input(Fore.YELLOW+"Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print(Fore.LIGHTYELLOW_EX+"Task deleted successfully!")
        else:
            print("Invalid task number.")
    else:
        print("No tasks added yet!")

def display_menu():
    print(Fore.MAGENTA+"\nTo-Do List Menu:"+Style.RESET_ALL)
    print(Fore.BLUE+"1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input(Fore.BLUE+"Enter your choice (1-5): ")

        if choice == "1":
            print(Fore.CYAN + "Add Task" + Style.RESET_ALL)
            add_task()
        elif choice == "2":
            print(Fore.CYAN + "View Tasks" + Style.RESET_ALL)            
            view_tasks()
        elif choice == "3":
            print(Fore.CYAN + "Complete Task" + Style.RESET_ALL)
            mark_completed()
        elif choice == "4":
            print(Fore.CYAN + "Delete Task" + Style.RESET_ALL)
            delete_task()
        elif choice == "5":
            print(Fore.LIGHTBLUE_EX+"Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
