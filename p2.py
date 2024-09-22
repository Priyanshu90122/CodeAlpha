tasks = []

def add_task():
    print("\nTask Categories:")
    print("1. Developing Applications")
    print("2. Writing Scripts for Data Analysis")
    print("3. Building Web Applications with Frameworks like Django")
    print("4. Solving Algorithmic Challenges")

    category = input("Choose a category (1-4): ")

    if category in ['1', '2', '3', '4']:
        task_name = input("Enter the task description: ")
        tasks.append({"task": task_name, "completed": False, "category": category})
        print(f"Task added: {task_name}")
    else:
        print("Invalid category choice.")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTask List:")
        for idx, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            category = task["category"]
            category_name = {
                '1': 'Developing Applications',
                '2': 'Writing Scripts for Data Analysis',
                '3': 'Building Web Applications with Django',
                '4': 'Solving Algorithmic Challenges'
            }.get(category, "Unknown Category")
            print(f"{idx}. {task['task']} [Category: {category_name}] - {status}")

def mark_completed():
    view_tasks()
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTask List Menu:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            print("Exiting Task List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
