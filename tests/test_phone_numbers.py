from lib.phone_no_extractor import *
from lib.diary import *
from lib.diary_entry import *

"""
Where the diary has entries containing phone numbers
AND the user calls PhoneNoExtractor
A list of phone numbers will be returned 
"""
def test_returns_standard_numbers_across_two_entries():
    diary = Diary()
    entry_1 = DiaryEntry("A cool title", "This is my diary entry. Katie's number is 01254 000000")
    entry_2 = DiaryEntry("Another cool title", "My mum changed her number today to 07000 000000")
    diary.add(entry_1)
    diary.add(entry_2)
    numbers = PhoneNoExtractor()
    assert numbers.extract(diary) == ["01254 000000", "07000 000000"]

"""
Where the diary has entries containing valid and invalid phone numbers
AND the user calls PhoneNoExtractor
A list of valid phone numbers will be returned 
"""
def test_only_return_valid_numbers_from_strings():
    diary = Diary()
    entry_1 = DiaryEntry("A cool title", "This is my diary entry. Katie's number is 01254 00000")
    entry_2 = DiaryEntry("Another cool title", "My mum changed her number today to 07000 0000001 & 01254 396354")
    diary.add(entry_1)
    diary.add(entry_2)
    numbers = PhoneNoExtractor()
    assert numbers.extract(diary) == ["01254 396354"]

"""
Where the diary has no entries containing phone numbers
When the user calls PhoneNoExtractor
An empty string is returned
"""
def test_empty_list_returned_if_no_numbers_included_in_strings():
    diary = Diary()
    entry_1 = DiaryEntry("A cool title", "This is my diary entry.")
    entry_2 = DiaryEntry("Another cool title", "My mum is fantastic x 100!")
    diary.add(entry_1)
    diary.add(entry_2)
    numbers = PhoneNoExtractor()
    assert numbers.extract(diary) == []

"""
Where the diary has no entries
When the user calls PhoneNoExtractor
An empty string is returned
"""
def test_empty_diary_returns_none():
    diary = Diary()
    numbers = PhoneNoExtractor()
    assert numbers.extract(diary) == []