from lib.diary_entry import DiaryEntry

"""
When a diary entry is added
Title and entry will be stored in diary entry
"""
def test_diary_entry_is_stored():
    entry = DiaryEntry("My Title", "My Contents")
    assert entry.title == "My Title"
    assert entry.contents == "My Contents"


"""
When a diary entry is added 
And #count_words is called
It will return the number of words in the content string

"""
def test_count_words_in_diary_entry():
    entry = DiaryEntry("My Title", "My Contents")
    assert entry.count_words() == 2