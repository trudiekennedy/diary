# """
# Where the diary has entries containing phone numbers
# AND the user calls PhoneNoExtractor
# A list of phone numbers will be returned 
# """
# diary = Diary()
# entry_1 = DiaryEntry("A cool title", "This is my diary entry. Katie's number is 01254 000000")
# entry_2 = DiaryEntry("Another cool title", "My mum changed her number today to 07000 000000")
# diary.add(entry_1)
# diary.add(entry_2)
# numbers = PhoneNoExtractor()
# numbers.extract(diary) => ["01254 000000", "07000 000000"]

# """
# Where the diary has entries containing valid and invalid phone numbers
# AND the user calls PhoneNoExtractor
# A list of valid phone numbers will be returned 
# """
# diary = Diary()
# entry_1 = DiaryEntry("A cool title", "This is my diary entry. Katie's number is 01254 00000")
# entry_2 = DiaryEntry("Another cool title", "My mum changed her number today to 07000 0000001 & 01254 396354")
# diary.add(entry_1)
# diary.add(entry_2)
# numbers = PhoneNoExtractor()
# numbers.extract(diary) => ["01254 396354"]

# """
# Where the diary has no entries containing phone numbers
# When the user calls PhoneNoExtractor
# An exception is raised
# """
# diary = Diary()
# entry_1 = DiaryEntry("A cool title", "This is my diary entry.")
# entry_2 = DiaryEntry("Another cool title", "My mum is fantastic x 100!")
# diary.add(entry_1)
# diary.add(entry_2)
# numbers = PhoneNoExtractor()
# numbers.extract(diary) => "No phone numbers found in your entries."
# """
# Where the diary has no entries
# When the user calls PhoneNoExtractor
# An exception is raised
# """
# diary = Diary()
# numbers = PhoneNoExtractor()
# numbers.extract(diary) => "You've not written any diary entries yet!"