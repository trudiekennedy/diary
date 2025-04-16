Recipe template - Multi-class planned design recipe

# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌───────────────────────────────────────┐           ┌──────────────────────────────────────────────────────┐
│Phone number extractor                 │           │Readable entry finder                                 │
│Takes an instance of diary             │           │Takes an instance of diary                            │
│Extracts telephone numbers from entries│           │Extracts entries that can be read on time (wpm * mins)│
│Returns list of tel numbers            │           │Returns readable entries                              │
└───────────────────────────────────┬───┘           └─────────────┬────────────────────────────────────────┘
                                    │                             │                                         
                                    ▼                             ▼                                         
                             ┌───────────────────────────────────────────┐                                  
                             │ Diary                                     │                                  
                             │ add(): takes an instance of DiaryEntry    │                                  
                             │ adds to a list of diary entries           │                                  
                             │ all(): returns list of all diary instances│                                  
                             └────────────────────┬──────────────────────┘                                  
                                                  ▼                                                         
                              ┌────────────────────────────────────────┐                                    
                              │DiaryEntry                              │                                    
                              │Takes a title string and contents string│                                    
                              │representing a diary entry              │
                              │format(): formats diary entry           │                                    
                              └────────────────────────────────────────┘                                    
                                                                                                            
┌─────────────────────────────────────┐                                                                     
│TaskList                             │                                                                     
│add(): takes an instance of Task     │                                                                     
│and adds ot a list of tasks          │                                                                     
│incomplete(): shows incomplete tasks │                                                                     
│complete(): shows completed tasks    │                                                                     
└─────────────────┬───────────────────┘                                                                     
                  │                                                                                         
                  ▼                                                                                         
┌───────────────────────────────────────────┐                                                               
│Task                                       │                                                               
│Takes a string representing a to-do        │                                                               
│mark_complete(): sets the task to complete │                                                               
└───────────────────────────────────────────┘                                                               

```

_Also design the interface of each class in more detail._

```python
class Diary:
    # User-facing properties:
    #   entries: list of diary entries

    def __init__(self):
        # self.entries = []
        pass

    def add(self, entry)
        # Parameters:
        # entry: an instance of DiaryEntry
        # Side effects:
        # adds entry to the entries property of the self object
        pass

    def all(self):
        # Parameters:
        #   none
        # Side-effects:
        #   returns a list of diary entries to the user
        pass 


class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        # Side-effects:
        #   Sets the title and artist properties
        pass 


class PhoneNoExtractor:
    # User-facing properties:
    # numbers: list of strings

    def __init__(self):
        # Parameters: None
        # numbers: a list of strings
        pass

    def extract(self, diary):
        # Parameters:
        # diary: takes an instance of Diary
        # Returns:
        # A list of phone numbers
        # Side-effects:
        # Adds numbers to a list in the self object
        pass


class ReadableEntry():
    def __init__(self):
        # Parameters: None
        # entries: a list of diary entries that are readable in specified timeframe
        pass

    def extract(self, diary, wpm, mins):
        # Parameters:
        # diary: takes an instance of Diary
        # wpm: integer representing the number of words per minute user can read
        # mins: integer representing the number of mins the user has to read
        # Returns:
        # A list of entries the user should be able to read within alloted timeframe
        # Side-effects:
        # Adds entries to a list in the self object
        pass


class TaskList():
    def __init__(self):
        # Parameters: None
        # Entries: List of diary entries
        pass
    
    def add(self, entry):
        # Parameters:
        # entry: takes an instance of Task
        # Returns: nothing
        # Side-effects:
        # Adds entry to entries list in the self object
        pass

    def incomplete(self):
        # Returns list of incomplete tasks to user
        pass

    def completed(self):
        # Returns list of completed tasks to user
        pass


class Task():
    # User-facing properties:
    # todo - a string representing a task
    # completed - a boolean: True if task is completed, False if incomplete

    def __init__(self, todo):
        # Parameters:
        # todo: string representing a single task
        # property completed: indicates if task is completed (defaults to False)
        pass
    
    def mark_complete(self)
        # Parameters: NONE
        # Updates completed property in the self object to True when user calls it
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
When user adds multiple diary entries
And user calls #all
The entries will be listed out in the order they were added
"""
diary = Diary()
entry_1 = DiaryEntry("A cool title", "This is my diary entry")
entry_2 = DiaryEntry("Another cool title", "These entries are very unimaginative. Is that the best you can do?")
diary.add(entry_1)
diary.add(entry_2)
diary.all() # => [entry_1, entry_2]

"""
When user adds multiple tasks
And the user calls #incomplete *without* any being marked complete
The entries will be listed out
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Clean the dishes")
task_list.add(task_1)
task_list.add(task_2)
task_list.incomplete() => [task_1, task_2]

"""
When user adds multiple tasks
And the user marks one as completed
When the user calls #incomplete, only the incomplete entries will be listed out
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Clean the dishes")
task_list.add(task_1)
task_list.add(task_2)
task_1.mark_complete()
task_list.incomplete() => [task_2]

"""
When user adds multiple tasks
And the user marks one as completed
When the user calls #completed, only the completed entries will be listed out
"""
task_list = TaskList()
task_1 = Task("Walk the dog")
task_2 = Task("Clean the dishes")
task_list.add(task_1)
task_list.add(task_2)
task_1.mark_complete()
task_list.completed() => [task_1]

"""
Where the diary has diary entries
AND the user calls #ReadableEntries with wpm + mins
Only the entries that can be read in time will be presented
"""
diary = Diary()
entry_1 = DiaryEntry("A cool title", "This is my diary entry")
entry_2 = DiaryEntry("Another cool title", "These entries are very unimaginative. Is that the best you can do?")
diary.add(entry_1)
diary.add(entry_2)
readable = ReadableEntry()
readable.extract(diary, 1, 5) => "This is my diary entry"

"""
Where the diary has diary entries
AND the user calls #ReadableEntries with wpm + mins but there are no entries readable in time
It returns None
"""
diary = Diary()
entry_1 = DiaryEntry("A cool title", "This is my diary entry and I am underwhelmed by it")
entry_2 = DiaryEntry("Another cool title", "These entries are very unimaginative. Is that the best you can do?")
diary.add(entry_1)
diary.add(entry_2)
readable = ReadableEntry()
readable.extract(diary, 1, 5) => None


"""
Where the diary has no diary entries
AND the user calls #ReadableEntries with wpm + mins
None is returned
"""
diary = Diary()
readable = ReadableEntry()
readable.extract(diary, 1, 5) => None

"""
Where the diary has entries containing phone numbers
AND the user calls PhoneNoExtractor
A list of phone numbers will be returned 
"""
diary = Diary()
entry_1 = DiaryEntry("A cool title", "This is my diary entry. Katie's number is 01254 000000")
entry_2 = DiaryEntry("Another cool title", "My mum changed her number today to 07000 000000")
diary.add(entry_1)
diary.add(entry_2)
numbers = PhoneNoExtractor()
numbers.extract(diary) => ["01254 000000", "07000 000000"]

"""
Where the diary has entries containing valid and invalid phone numbers
AND the user calls PhoneNoExtractor
A list of valid phone numbers will be returned 
"""
diary = Diary()
entry_1 = DiaryEntry("A cool title", "This is my diary entry. Katie's number is 01254 00000")
entry_2 = DiaryEntry("Another cool title", "My mum changed her number today to 07000 0000001 & 01254 396354")
diary.add(entry_1)
diary.add(entry_2)
numbers = PhoneNoExtractor()
numbers.extract(diary) => ["01254 396354"]

"""
Where the diary has no entries containing phone numbers
When the user calls PhoneNoExtractor
An empty string is returned
"""
diary = Diary()
entry_1 = DiaryEntry("A cool title", "This is my diary entry.")
entry_2 = DiaryEntry("Another cool title", "My mum is fantastic x 100!")
diary.add(entry_1)
diary.add(entry_2)
numbers = PhoneNoExtractor()
numbers.extract(diary) => "[]"
"""
Where the diary has no entries
When the user calls PhoneNoExtractor
An empty string is returned
"""
diary = Diary()
numbers = PhoneNoExtractor()
numbers.extract(diary) => "You've not written any diary entries yet!"
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# Diary
"""
Initially, diary holds no entries
"""
diary = Diary()
diary.all() # => []

"""
When a diary entry is added
Title and entry will be stored in diary entry
"""
entry = DiaryEntry("My Title", "My Contents")
entry.title # => "My Title"
entry.contents # => "My Contents"

# TaskList
"""
Initially, tasklist holds no tasks
"""
task_list = TaskList()
task_list.entries => []

"""
Initially, tasklist holds no incomplete tasks
"""
task_list = TaskList()
task_list.incomplete() => []

"""
Initially, tasklist holds no complete tasks
"""
task_list = TaskList()
task_list.completed => []

# Task
"""
When a task is added
The to-do will be stored & a False boolean to show it is incomplete
"""
task = Task("Clean the dishes")
task.todo => "Clean the dishes"
task.completed => False

"""
When a task is added
And the user marks it as complete
The completed boolean will be set to True 
"""
task = Task("Walk the dog")
task.mark_complete()
task.completed() => True

# PhoneNoExtractor
"""
Initially, there will be no phone numbers stored in list
"""
numbers = PhoneNoExtractor()
numbers.numbers => []

# ReadableEntry
"""
Initially, there will be no readable entries in the list
"""
readable = ReadableEntry()
readable.entries => []
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
