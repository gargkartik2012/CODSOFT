# Task 1 To-Do-list Application

# A list to store the tasks
tasks = []

# A function to display the menu options
def display_menu():
    print("To Do List Menu")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

# A function to add a task to the list
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

# A function to view the tasks in the list
def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("Tasks in the list:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# A function to remove a task from the list
def remove_task():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        view_tasks()
        index = int(input("Enter the task number to remove: "))
        if index < 1 or index > len(tasks):
            print("Invalid task number.")
        else:
            task = tasks.pop(index-1)
            print(f"Task '{task}' removed successfully.")

# A loop to run the application until the user exits
while True:
    display_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        print("Thank you for using the to do list application.")
        break
    else:
        print("Invalid choice. Please try again.")
