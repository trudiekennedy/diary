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

    def format(self):
        # Returns:
        #   A string of the form "{title}: {contents}"
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

    def extract(self, wpm, mins):
        # Parameters:
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
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
