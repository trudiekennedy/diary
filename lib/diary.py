class Diary:
    # User-facing properties:
    #   entries: list of diary entries

    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries