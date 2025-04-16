from lib.diary_entry import DiaryEntry

"""
When a diary entry is added
Title and entry will be stored in diary entry
"""
def test_diary_entry_is_stored():
    entry = DiaryEntry("My Title", "My Contents")
    assert entry.title == "My Title"
    assert entry.contents == "My Contents"
