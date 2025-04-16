class Task():
    # User-facing properties:
    # todo - a string representing a task
    # completed - a boolean: True if task is completed, False if incomplete

    def __init__(self, todo):
        self.todo = todo
        self.completed = False
    
    def mark_complete(self):
        self.completed = True