from lib.diary import *
from lib.diary_entry import *

"""
When user adds multiple diary entries
And user calls #all
The entries will be listed out in the order they were added
"""

def test_entries_added_to_diary():
    diary = Diary()
    entry_1 = DiaryEntry("A cool title", "This is my diary entry")
    entry_2 = DiaryEntry("Another cool title", "These entries are very unimaginative. Is that the best you can do?")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]
