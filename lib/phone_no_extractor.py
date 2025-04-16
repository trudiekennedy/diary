import re

class PhoneNoExtractor():
    # User-facing properties:
    # numbers: list of strings

    def __init__(self):
        self.numbers = []

    def extract(self, diary):
        # Use regex to find pattern of 5 numbers d{5} whitespace \s and 6 numbers d{6}
        pattern = r'\b\d{5}\s\d{6}\b'

        # Check the each diary entry to find a number within contents + extend to numbers
        for item in diary.entries:
            phone_nos = re.findall(pattern, item.contents)
            self.numbers.extend(phone_nos)

        return self.numbers