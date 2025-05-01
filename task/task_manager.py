from storage.json_store import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        for i, task in enumerate(self.tasks):
            status = "Complete!" if task["done"] else "Incomplete!"
            print(f"{i+1}. [{status}] {task['title']} - Due: {task.get('due', 'N/A')}")

    def add_task(self, title, due=None):
        self.tasks.append({"title": title, "due": due, "done": False})
        save_tasks(self.tasks)
        print("Task added!")

    def complete_task(self, index):
        try:
            self.tasks[index]["done"] = True
            save_tasks(self.tasks)
            print("Task complete!")
        except IndexError:
            print("Invalid Selection!")
