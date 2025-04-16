from lib.readable_entry import *

# ReadableEntry
"""
Initially, there will be no readable entries in the list
"""

def test_readable_entries_returns_empty_list_when_no_entries():
    readable = ReadableEntry()
    assert readable.entries == []