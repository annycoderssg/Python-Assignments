# Python Assignments

A comprehensive collection of Python programming assignments and practice exercises — from core fundamentals through advanced concurrency, OOP, file handling, cryptography, and automation with ML.

---

## Prerequisites

| Tool | Version | Download |
|------|---------|----------|
| Python | 3.10+ | https://www.python.org/downloads/ |
| pip | Latest | Bundled with Python |

Verify your installation:
```bash
python --version
pip --version
```

---

## Setup — Virtual Environment

### 1. Navigate to the project folder
```bash
cd "\Projects\Python-Assignments"
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

> Your terminal prompt will change to `(venv)` once activated.

### 4. Install required packages
```bash
pip install -r requirements.txt
```

### 5. Deactivate when done
```bash
deactivate
```

---

## Dependencies

All assignment folders use **Python standard library only**. The `requirements.txt` packages are only needed for the `Automation/` scripts:

| Package | Used In | Purpose |
|---------|---------|---------|
| `numpy` | `Automation/ML/` | Numerical computing |
| `scikit-learn` | `Automation/ML/` | Machine learning (Iris dataset, decision tree) |
| `psutil` | `Automation/ProcessAutomation/` | System & process monitoring |
| `schedule` | `Automation/` | Job scheduling |

> **All assignment folders (Assignments/ through Assignments_13/) require zero third-party packages.**

---

## Repository Structure

```
Python-Assignments/
│
├── Assignments/            # Batch 1  — Functions & Basic I/O
├── Assignments_2/          # Batch 2  — Reduce & Arithmetic utilities
├── Assignments_3/          # Batch 3  — Lambda & Functional programming
├── Assignments_4/          # Batch 4  — OOP Basics
├── Assignments_5/          # Batch 5  — Classes & Encapsulation
├── Assignments_6/          # Batch 6  — Inheritance & Polymorphism
├── Assignments_7/          # Batch 7  — Multithreading
├── Assignment_8/           # Batch 8  — Recursion & Patterns
├── Assignment_9/           # Batch 9  — File Handling & OS module
├── Assignment10/           # Batch 10 — System programming
├── Assignments_11/         # Batch 11 — Cryptography & Hashing
├── Assignments_12/         # Batch 12 — Advanced OOP
├── Assignments_13/         # Batch 13 — Concurrency (Threads, Processes, Async)
│
├── File_Handling/          # File create, read, write, delete exercises
├── Automation/             # File, Process, Mail & ML automation scripts
│   ├── FileAutomation/
│   ├── ProcessAutomation/
│   ├── Mails/
│   └── ML/
├── DJango/                 # Django web framework exercises
│
├── *.py                    # Root-level practice scripts (see table below)
├── requirements.txt        # Third-party dependencies
└── README.md
```

---

## Running the Assignments

### General Pattern
```bash
python <filename>.py
```

---

### Batch 1 — `Assignments/` : Functions & Basic I/O

| File | Description | Input Required |
|------|-------------|----------------|
| `Assignment1.py` | Function returning a greeting string | No |
| `Assignment2.py` | Basic arithmetic function | No |
| `Assignment3.py` | Function with parameters | No |
| `Assignment5.py` | Countdown loop from 10 to 1 | No |
| `Assignment10.py` | Get string length from user | Yes — enter a string |

```bash
cd Assignments
python Assignment1.py
```

---

### Batch 2 — `Assignments_2/` : Reduce & Arithmetic Utilities

| File | Description | Input Required |
|------|-------------|----------------|
| `Assignment1.py` | Sum of user-provided numbers using `reduce` | Yes — enter numbers |
| `Assignment2.py` | Arithmetic operations using local module | Yes |
| `Assignment3.py` | Functional reduce operations | Yes |

```bash
cd Assignments_2
python Assignment1.py
```

---

### Batch 3 — `Assignments_3/` : Lambda & Functional Programming

| File | Description | Input Required |
|------|-------------|----------------|
| `Assignment1.py` | `reduce` with a custom Add function on a list | No |
| `Assignment2.py` | Filter with lambda | No |
| `Assignment3.py` | Map with lambda | No |
| `Assignment4.py` | Lambda-based power calculation using `reduce` | No |
| `Assignment5.py` | Combined filter, map, reduce | No |

```bash
cd Assignments_3
python Assignment1.py
```

---

### Batch 4–6 — OOP (Basics → Inheritance → Polymorphism)

| Folder | Concepts |
|--------|---------|
| `Assignments_4/` | Classes, objects, methods, constructors |
| `Assignments_5/` | Encapsulation, class variables, instance variables |
| `Assignments_6/` | Inheritance, method overriding, polymorphism |

```bash
cd Assignments_4
python Assignment1.py

cd ../Assignments_5
python Assignment1.py

cd ../Assignments_6
python Assignment1.py
```

---

### Batch 7 — `Assignments_7/` : Multithreading

| File | Description |
|------|-------------|
| `Assignment_1.py` | Two threads printing even and odd numbers concurrently |
| `Assignment_2.py` | Threading with even/odd factor calculations |
| `Assignment_3.py` | Thread synchronization using shared state |
| `Assignment_4.py` | String analysis across multiple threads |
| `Assignment_5.py` | Advanced thread coordination |

```bash
cd Assignments_7
python Assignment_1.py
```

---

### Batch 8 — `Assignment_8/` : Recursion & Patterns

| File | Description | Input Required |
|------|-------------|----------------|
| `Assignment_1.py` | Recursive star pattern generator | Yes — enter row count |
| `Assignment_2.py` | Number pyramid pattern | Yes |
| `Assignment_3.py` | Recursive factorial | Yes |
| `Assignment_4.py` | Recursive Fibonacci | Yes |
| `Assignment_5.py` | Advanced pattern | Yes |

```bash
cd Assignment_8
python Assignment_1.py
# Enter: 5
```

---

### Batch 9 — `Assignment_9/` : File Handling & OS Module

| File | Description | Input Required |
|------|-------------|----------------|
| `Assignment_1.py` | Check if a file exists using `os.path.exists()` | Yes — enter a filename |
| `Assignment_2.py` | List files in a directory | Yes — enter a path |
| `Assignment_3.py` | Read file contents safely | Yes — enter a filename |
| `Assignment_4.py` | Write and append to files | Yes |

```bash
cd Assignment_9
python Assignment_1.py
# Enter: C:\Users\Anand S\Study\Projects\Python-Assignments\README.md
```

---

### Batch 10 — `Assignment10/` : System Programming

```bash
cd Assignment10
python Assignment1.py
```

---

### Batch 11 — `Assignments_11/` : Cryptography & Hashing

| File | Description | How to Run |
|------|-------------|-----------|
| `Assignment1.py` | Directory traversal + SHA-256 checksum calculator | `python Assignment1.py <directory_path>` |
| `Assignment2.py` | Recursive duplicate file finder using SHA-256 | `python Assignment2.py <directory_path>` |
| `Assignment3.py` | Duplicate file deleter (prompts before deletion) | `python Assignment3.py <directory_path>` |
| `Assignment4.py` | File integrity checker | `python Assignment4.py <file_path>` |

```bash
cd Assignments_11

# Show help
python Assignment1.py -h

# Run on a directory
python Assignment1.py "C:\Users\Anand S\Study\Projects\Python-Assignments\Assignments_11\Demo"

# Find duplicates
python Assignment2.py "C:\Users\Anand S\Study\Projects\Python-Assignments\Assignments_11\Demo"

# Delete duplicates (prompts for confirmation)
python Assignment3.py "C:\Users\Anand S\Study\Projects\Python-Assignments\Assignments_11\Demo"
```

---

### Batch 12 — `Assignments_12/` : Advanced OOP

| File | Concept | Key Highlights |
|------|---------|----------------|
| `Assignment1.py` | Encapsulation | `_protected`, `__private`, `@property` with validation |
| `Assignment2.py` | Inheritance & `super()` | `Person → Student / Teacher`, `isinstance()`, `issubclass()` |
| `Assignment3.py` | Polymorphism | `Shape → Circle / Rectangle / Triangle` — same `Area()`, different result |
| `Assignment4.py` | Abstract Classes | `abc.ABC`, `@abstractmethod`, `Vehicle → Car / ElectricCar / Truck` |
| `Assignment5.py` | Multiple Inheritance & MRO | `Flyable`, `Swimmable`, `Walkable` → `Duck`; Mixin pattern; `__mro__` |
| `Assignment6.py` | Operator Overloading | `Vector` with `__add__`, `__sub__`, `__mul__`, `__eq__`, `__lt__`, `__len__`, `__str__` |
| `Assignment7.py` | Static & Class Methods | `Temperature` with `@staticmethod` conversions, `@classmethod` constructor |

```bash
cd Assignments_12
python Assignment1.py
python Assignment4.py
python Assignment6.py
```

---

### Batch 13 — `Assignments_13/` : Concurrency

| File | Topic | Imports |
|------|-------|---------|
| `Assignment1.py` | Thread Synchronization | `threading.Lock`, `RLock` — race condition demo |
| `Assignment2.py` | Thread Communication | `Event`, `Semaphore`, `queue.Queue` — producer/consumer |
| `Assignment3.py` | Thread Pools & Daemon Threads | `ThreadPoolExecutor`, `submit()`, `as_completed()` |
| `Assignment4.py` | Multiprocessing Basics | `Process`, `Queue`, `Pipe`, `os.getpid()` |
| `Assignment5.py` | Process Pools | `Pool.map()`, `Pool.starmap()`, `ProcessPoolExecutor` |
| `Assignment6.py` | Shared Memory | `multiprocessing.Value`, `Array`, `Lock` — safe parallel sum |
| `Assignment7.py` | Async I/O | `asyncio`, `async/await`, `gather()`, `create_task()`, `asyncio.Queue` |

```bash
cd Assignments_13
python Assignment1.py   # Thread safety demo
python Assignment3.py   # ThreadPoolExecutor demo
python Assignment7.py   # Async I/O demo
```

---

### `File_Handling/` : File Operations

| File | Description | Input Required |
|------|-------------|----------------|
| `File_Create.py` | Create a new file | Yes — enter filename |
| `File_Open.py` | Open and read file | Yes — enter filename |
| `File_Read.py` | Read full file contents | Yes — enter filename |
| `File_ReadLine.py` | Read file line by line | Yes — enter filename |
| `File_Write.py` | Write content to file | Yes — enter filename & content |
| `File_Overwrite.py` | Overwrite existing file | Yes |
| `File_Delete.py` | Delete a file | Yes — enter filename |

```bash
cd File_Handling
python File_Create.py
python File_Write.py
python File_Read.py
```

---

### Root-Level Practice Scripts

#### Basics
```bash
python Hello.py           # Print Hello
python Variable.py        # Variable types demo
python Starter.py         # Getting started
python Addition.py        # User input arithmetic
```

#### Control Flow
```bash
python For.py             # For loop basics
python While.py           # While loop
python Range.py           # range() usage
python Selection1.py      # if/elif/else
```

#### Functions
```bash
python Function1.py       # Basic function
python Function5.py       # Return values
python DefaultArgument.py # Default parameters
python Keyword.py         # Keyword arguments
python VariableArguments.py # *args and **kwargs
```

#### Data Structures
```bash
python List1.py           # List basics
python TupleDemo.py       # Tuples
python SetDemo.py         # Sets
python Disctionary.py     # Dictionaries
python ListFilter.py      # Grouping with dict
```

#### OOP
```bash
python Oop.py             # Class with user input
python Hdfc.py            # Bank account OOP system
```

#### Functional Programming (FMR Series)
```bash
python FMR.py             # Filter, Map, Reduce intro
python FMR2.py            # Filter examples
python FMR5.py            # Map examples
python FMR8.py            # Reduce examples
python MarvellousFMR.py   # Custom FMR utilities
```

#### Decorators
```bash
python Decorator.py       # Basic decorator
python Decorator1.py      # Decorator with args
python Decorator2.py      # Stacked decorators
```

#### Multithreading
```bash
python MultiThreading1.py  # Two concurrent threads
python MultiThreading2.py  # Thread with sleep
python Multicore.py        # Multi-core usage
```

#### Multiprocessing
```bash
python Process1.py         # Process basics
```

#### Algorithms
```bash
python ReverseArray.py    # Reverse an array
python SortArray.py       # Sort an array
python Factors.py         # Find factors of a number
```

---

### `Automation/` Scripts

> **Requires virtual environment with packages installed** (`numpy`, `scikit-learn`, `psutil`, `schedule`)

```bash
# Activate venv first
venv\Scripts\activate

# File Automation
cd Automation/FileAutomation
python Automation.py

# Process Automation
cd ../ProcessAutomation
python <script>.py

# ML
cd ../ML
python <script>.py
```

---

## Topics Covered

| Category | Topics |
|----------|--------|
| **Fundamentals** | Variables, data types, control flow, I/O |
| **Functions** | Default args, keyword args, `*args`, `**kwargs`, closures |
| **Data Structures** | Lists, tuples, sets, dictionaries |
| **Functional Programming** | `lambda`, `map`, `filter`, `functools.reduce` |
| **Decorators** | Basic, stacked, parameterised |
| **OOP — Core** | Classes, objects, constructors, methods |
| **OOP — Advanced** | Encapsulation, inheritance, polymorphism, `super()` |
| **OOP — Expert** | Abstract classes (`abc`), multiple inheritance, MRO, operator overloading, `@staticmethod`, `@classmethod` |
| **File I/O** | Create, read, write, append, delete with `os.path` |
| **Algorithms** | Sorting, searching, factorisation, recursion |
| **Cryptography** | SHA-256 hashing, file checksums, duplicate detection (`hashlib`) |
| **Multithreading** | `Lock`, `RLock`, `Event`, `Semaphore`, `Queue`, `ThreadPoolExecutor`, daemon threads |
| **Multiprocessing** | `Process`, `Queue`, `Pipe`, `Pool`, `ProcessPoolExecutor`, shared `Value`/`Array` |
| **Async I/O** | `asyncio`, `async/await`, `gather()`, `create_task()`, `asyncio.Queue` |
| **Automation** | File ops, process monitoring (`psutil`), email (`smtplib`), scheduling |
| **Machine Learning** | Iris dataset, decision tree (`scikit-learn`, `numpy`) |

---

## Python Version

Tested with **Python 3.10+**. All standard library features used are stable across Python 3.8+.
