from lib.task_list import TaskList

"""
Initially, tasklist holds no tasks
"""
def test_task_list_is_initially_empty():
    task_list = TaskList()
    assert task_list.task_list == []

"""
Initially, tasklist holds no incomplete tasks
"""
def test_task_no_incomplete_tasks_initially():
    task_list = TaskList()
    assert task_list.incomplete() == []

"""
Initially, tasklist holds no complete tasks
"""
def test_task_no_complete_tasks_initially():
    task_list = TaskList()
    assert task_list.completed() == []