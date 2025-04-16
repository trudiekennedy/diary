from lib.task import Task

# Task
"""
When a task is added
The to-do will be stored & a False boolean to show it is incomplete
"""
def test_task_is_initially_stored_as_incomplete():
    task = Task("Clean the dishes")
    assert task.todo == "Clean the dishes"
    assert task.completed == False

"""
When a task is added
And the user marks it as complete
The completed boolean will be set to True 
"""
def test_task_boolean_updated_to_true_when_marked_complete():
    task = Task("Walk the dog")
    task.mark_complete()
    assert task.completed == True