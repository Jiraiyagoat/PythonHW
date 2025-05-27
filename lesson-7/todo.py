import json
import csv
from abc import ABC, abstractmethod

# Task Class
class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["task_id"],
            data["title"],
            data["description"],
            data["due_date"],
            data["status"]
        )

# Storage Interface
class StorageInterface(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, tasks):
        pass

# JSON Storage
class JSONStorage(StorageInterface):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except:
            return []

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

# CSV Storage
class CSVStorage(StorageInterface):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, newline='') as f:
                reader = csv.DictReader(f)
                return [Task.from_dict(row) for row in reader]
        except:
            return []

    def save(self, tasks):
        with open(self.filename, mode="w", newline='') as f:
            fieldnames = ["task_id", "title", "description", "due_date", "status"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

# ToDo Manager
class ToDoManager:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task: Task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def update_task(self, task_id, title, description, due_date, status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                task.due_date = due_date
                task.status = status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        original = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        if len(self.tasks) < original:
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    def filter_by_status(self, status):
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        for task in filtered:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved.")

    def load_tasks(self):
        self.tasks = self.storage.load()
        print("Tasks loaded.")

# Main CLI
def main():
    print("Welcome to the To-Do Application!")
    storage_type = input("Choose storage format (json/csv): ").strip().lower()
    if storage_type == "csv":
        storage = CSVStorage()
    else:
        storage = JSONStorage()

    manager = ToDoManager(storage)

    while True:
        print("\n1. Add a new task\n2. View all tasks\n3. Update a task\n4. Delete a task\n5. Filter tasks by status\n6. Save tasks\n7. Load tasks\n8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            manager.add_task(Task(task_id, title, description, due_date, status))

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title: ")
            description = input("Enter new Description: ")
            due_date = input("Enter new Due Date (YYYY-MM-DD): ")
            status = input("Enter new Status: ")
            manager.update_task(task_id, title, description, due_date, status)

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)

        elif choice == "5":
            status = input("Enter status to filter by: ")
            manager.filter_by_status(status)

        elif choice == "6":
            manager.save_tasks()

        elif choice == "7":
            manager.load_tasks()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
