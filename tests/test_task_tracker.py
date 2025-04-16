from lib.task_list import *
from lib.task import *

"""
When user adds multiple tasks
And the user calls #incomplete *without* any being marked complete
The entries will be listed out
"""
def test_adding_tasks_to_lists_stores_tasks():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Clean the dishes")
    task_list.add(task_1)
    task_list.add(task_2)
    assert task_list.incomplete() == [task_1, task_2]

"""
When user adds multiple tasks
And the user marks one as completed
When the user calls #incomplete, only the incomplete entries will be listed out
"""
def test_only_incomplete_tasks_are_returned_when_calling_incomplete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Clean the dishes")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    assert task_list.incomplete() == [task_2]

"""
When user adds multiple tasks
And the user marks one as completed
When the user calls #completed, only the completed entries will be listed out
"""
def test_only_completed_tasks_are_returned_when_calling_complete():
    task_list = TaskList()
    task_1 = Task("Walk the dog")
    task_2 = Task("Clean the dishes")
    task_list.add(task_1)
    task_list.add(task_2)
    task_1.mark_complete()
    assert task_list.completed() == [task_1]