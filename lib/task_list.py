class TaskList():
    def __init__(self):
        self.task_list = []
    
    def add(self, entry):
        self.task_list.append(entry)

    def incomplete(self):
        return [item for item in self.task_list if item.completed == False]

    def completed(self):
        return [item for item in self.task_list if item.completed == True]
        