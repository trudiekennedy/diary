from lib.readable_entry import *
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
Where the diary has 2 diary entries
AND the user calls #ReadableEntries with wpm + mins
Only the entry that can be read in time will be presented
"""
def test_readable_only_returns_entries_readable_in_timeframe():
    diary = Diary()
    entry_1 = DiaryEntry("A cool title", "This is my diary entry")
    entry_2 = DiaryEntry("Another cool title", "These entries are very unimaginative. Is that the best you can do?")
    diary.add(entry_1)
    diary.add(entry_2)
    readable = ReadableEntry()
    assert readable.extract(diary, 1, 5) == entry_1.contents

"""
Where the diary has diary entries
AND the user calls #ReadableEntries with wpm + mins but there are no entries readable in time
It returns None
"""
def test_where_no_entries_are_readable_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("A cool title", "This is my diary entry and I am underwhelmed by it")
    entry_2 = DiaryEntry("Another cool title", "These entries are very unimaginative. Is that the best you can do?")
    diary.add(entry_1)
    diary.add(entry_2)
    readable = ReadableEntry()
    assert readable.extract(diary, 1, 5) == None


"""
Where the diary has no diary entries
AND the user calls #ReadableEntries with wpm + mins
It returns None
"""
def test_where_there_are_no_entries_at_all():
    diary = Diary()
    readable = ReadableEntry()
    assert readable.extract(diary, 1, 5) == None

"""
Where the diary has multiple diary entries
AND the user calls #ReadableEntries with wpm + mins
Only the longest entry that can be read in time will be presented
"""
def test_readable_only_returns_longest_entry_readable_in_timeframe():
    diary = Diary()
    entry_1 = DiaryEntry("A cool title", "This is my diary entry")
    entry_2 = DiaryEntry("Another cool title", "These entries are very unimaginative. Is that the best you can do?")
    entry_3 = DiaryEntry("Another cool title point 2", "Test drivers are test driving...")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    readable = ReadableEntry()
    assert readable.extract(diary, 3, 5) == entry_2.contents
