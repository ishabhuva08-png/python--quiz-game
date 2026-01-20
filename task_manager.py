class Taskmanager:
    def __init__(self):
        self.tasks = []
        
    def add_task(self,title):
        tasks ={
            "title":title,
            "status":"pending"
        }
        self.tasks.append(tasks)
        print("Task added successfully!✔️")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available")
            return
        print("\n Your Tasks:")
        for index,tasks in enumerate(self.tasks,start=1):
            print(f"{index}.{tasks['title']}-{tasks['status']}")
