class ReadableEntry():
    def __init__(self):
        self.entries = []

    def extract(self, diary, wpm, mins):
        # Parameters:
        # diary: takes an instance of Diary
        # wpm: integer representing the number of words per minute user can read
        # mins: integer representing the number of mins the user has to read
        # Returns:
        # A list of entries the user should be able to read within alloted timeframe
        # Side-effects:
        # Adds entries to a list in the self object
        words_user_can_read = wpm * mins

        # finds entries where word count is less than or equal to what the use can read
        self.entries = [entry for entry in diary.entries if entry.count_words() <= words_user_can_read]

        if not self.entries:
            return None
        
        # looks for the entry with the highest word count amongst the entries
        return max(self.entries, key=lambda entry: len(entry.contents.split())).contents
