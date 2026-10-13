import os

FILE_NAME = "tasks.txt"

# Load tasks from the text file
def load_tasks():
    tasks = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, completed = line.strip().rsplit("|", 1)
                tasks.append({
                    "task": task,
                    "completed": completed == "True"
                })

    return tasks


# Save tasks to the text file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(
                task["task"] + "|" + str(task["completed"]) + "\n"
            )


# Display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['task']} - {status}")
