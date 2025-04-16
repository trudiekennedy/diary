class ReadableEntry():
    def __init__(self):
        self.entries = []

    def extract(self, diary, wpm, mins):
        words_user_can_read = wpm * mins

        # finds entries where word count is less than or equal to what the use can read
        self.entries = [entry for entry in diary.entries if entry.count_words() <= words_user_can_read]

        if not self.entries:
            return None
        
        # looks for the entry with the highest word count amongst the entries
        return max(self.entries, key=lambda entry: len(entry.contents.split())).contents
