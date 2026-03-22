# Python Assignments

A collection of Python programming assignments and practice exercises covering core and advanced Python concepts.

## Repository Structure

### Assignment Batches

| Folder | Topics Covered |
|--------|---------------|
| `Assignments/` | Functions, arithmetic operations, basic I/O |
| `Assignments_2/` | Functions with `reduce`, arithmetic utilities |
| `Assignments_3/` | Lambda functions, functional programming |
| `Assignments_4/` | Object-Oriented Programming (OOP) basics |
| `Assignments_5/` | Classes, encapsulation, class variables |
| `Assignments_6/` | OOP — inheritance and polymorphism |
| `Assignments_7/` | Multithreading |
| `Assignment_8/` | Patterns and loops |
| `Assignment_9/` | File handling, OS module |
| `Assignment10/` | System programming, advanced topics |
| `Assignments_11/` | Cryptography, hashing (`hashlib`) |
| `Assignments_12/` | OOP advanced — encapsulation, abstract classes, multiple inheritance, operator overloading, `@staticmethod`, `@classmethod` |
| `Assignments_13/` | Multithreading, multiprocessing, and multitasking (asyncio) — synchronization, pools, shared memory, async/await |

### Practice Scripts (Root Level)

| Category | Files |
|----------|-------|
| Basics | `Hello.py`, `First.py`, `Variable.py`, `Starter.py` |
| Control Flow | `For.py`, `For1-4.py`, `While.py`, `Range.py`, `Sequence.py` |
| Functions | `Function1-13.py`, `Functions.py`, `DefaultArgument.py`, `Keyword.py`, `Positional.py`, `VariableArguments.py` |
| Data Structures | `List1-6.py`, `ListDemo.py`, `ListFilter.py`, `ListAsDict.py`, `TupleDemo.py`, `SetDemo.py`, `Disctionary.py`, `DisctionaryDemo.py`, `DisctionaryDuplicate.py` |
| OOP | `Oop.py`, `Oop1.py`, `Oop2.py` |
| Decorators | `Decorator.py`, `Decorator1.py`, `Decorator2.py` |
| File & I/O | `InputOutput.py`, `File_Handling/` |
| Modules | `Module1.py`, `Module2.py` |
| Multithreading | `MultiThreading1.py`, `MultiThreading2.py`, `Multi1-4.py`, `Multicore.py` |
| Multiprocessing | `Process1.py` |
| Networking | `Client.py`, `Serial1-3.py` |
| Algorithms | `Factors.py`, `FactorsWhile.py`, `ReverseArray.py`, `SortArray.py`, `Selection1-3.py` |
| FMR Series | `FMR.py`, `FMR2-11.py`, `MarvellousFMR.py` |
| Miscellaneous | `Demo.py`, `Marvellous.py`, `Special.py`, `Pop.py`, `Addition.py`, `Command1.py`, `Command2.py` |

## Topics Covered

- Python fundamentals (variables, control flow, functions)
- Data structures (lists, tuples, sets, dictionaries)
- Object-Oriented Programming (classes, inheritance, polymorphism)
  - Encapsulation (`_protected`, `__private`, `@property`)
  - Inheritance with `super()`
  - Method overriding and runtime polymorphism
  - Abstract classes (`abc.ABC`, `@abstractmethod`)
  - Multiple inheritance and MRO
  - Operator overloading (`__add__`, `__str__`, `__eq__`, `__len__`, etc.)
  - `@staticmethod` and `@classmethod`
- Functional programming (lambda, `map`, `filter`, `reduce`)
- Decorators and closures
- File I/O and OS operations
- Multithreading — `Lock`, `RLock`, `Event`, `Semaphore`, `queue.Queue`, `ThreadPoolExecutor`, daemon threads
- Multiprocessing — `Process`, `Queue`, `Pipe`, `Pool`, `ProcessPoolExecutor`, shared `Value`/`Array`, `Lock`
- Multitasking / Async I/O — `asyncio`, `async/await`, `gather`, `create_task`, `asyncio.Queue`
- Network programming
- Sorting and searching algorithms
- Cryptography basics

## Requirements

- Python 3.x

## Usage

Run any script directly:

```bash
python <filename>.py
```

## Assignments_13 — Multithreading, Multiprocessing & Multitasking

| File | Topic | Key Features |
|------|-------|-------------|
| `Assignment1.py` | Thread Synchronization | `Lock`, `RLock`; race condition demo vs. safe counter |
| `Assignment2.py` | Thread Communication | `Event` (signal between threads), `Semaphore` (limit concurrency), `queue.Queue` (producer-consumer) |
| `Assignment3.py` | Thread Pool & Daemon Threads | `ThreadPoolExecutor`, `submit()`, `map()`, `as_completed()`, daemon thread |
| `Assignment4.py` | Multiprocessing Basics | `Process`, `Queue` (IPC), `Pipe` (bidirectional), `os.getpid()` |
| `Assignment5.py` | Process Pool | `Pool.map()`, `Pool.starmap()`, `Pool.apply_async()`, `ProcessPoolExecutor` |
| `Assignment6.py` | Shared Memory & Process Sync | `multiprocessing.Lock`, `Value`, `Array`; race condition vs. safe parallel sum |
| `Assignment7.py` | Async I/O (Multitasking) | `async def`, `await`, `asyncio.sleep()`, `gather()`, `create_task()`, `asyncio.Queue` |

## Assignments_12 — Advanced OOP Exercises

| File | Concept | Key Features |
|------|---------|-------------|
| `Assignment1.py` | Encapsulation | `_protected`, `__private`, `@property` getter/setter with validation |
| `Assignment2.py` | Inheritance + `super()` | `Person` → `Student` / `Teacher`; `super().__init__()`, `isinstance()`, `issubclass()` |
| `Assignment3.py` | Method Overriding & Polymorphism | `Shape` → `Circle` / `Rectangle` / `Triangle`; same `Area()` call, different result |
| `Assignment4.py` | Abstract Classes | `abc.ABC` + `@abstractmethod`; `Vehicle` → `Car` / `ElectricCar` / `Truck` |
| `Assignment5.py` | Multiple Inheritance & MRO | `Flyable`, `Swimmable`, `Walkable`; `Duck` inherits all three; Mixin pattern; `__mro__` |
| `Assignment6.py` | Operator Overloading | `Vector` with `__add__`, `__sub__`, `__mul__`, `__eq__`, `__lt__`, `__len__`, `__str__` |
| `Assignment7.py` | `@staticmethod` & `@classmethod` | `Temperature` conversions (static); `FromFahrenheit` alternative constructor (classmethod) |

## Changelog

### Bug Fixes

#### `Assignments_6/Assignment_2.py` — BankAccount
- Fixed `Withdrow` typo → renamed to `Withdraw`
- Fixed critical bug in `CalculateInterest`: was overwriting balance instead of adding interest (`=` → `+=`)

#### `Assignments_6/Assignment_3.py` — Numbers (Prime/Perfect)
- Fixed prime checker logic: `ChkPrime` was returning `True` when a divisor was found (meaning not prime) and had an unreachable `break` — corrected to return `False` on divisibility, `True` otherwise
- Replaced explicit `True ==` boolean comparisons with Pythonic `if condition:` style

#### `Assignments_11/Assignment1.py` — Checksum Tool
- Replaced `from sys import *` with `import sys`
- Upgraded hash algorithm from MD5 to SHA-256 for stronger file integrity
- Fixed path construction in `os.walk` loop (used `path` instead of `dirName`, breaking subdirectory traversal)
- Fixed typo: `exits` → `exists`
- Used context manager (`with open(...)`) for safe file handling

#### `Assignments_11/Assignment2.py` — Duplicate File Finder
- Replaced `from sys import *` with `import sys`
- Upgraded hash algorithm from MD5 to SHA-256
- Fixed path variable shadowing inside `os.walk` loop (`path` → `filepath`)
- Fixed function name typo: `LogDiplicateFiles` → `LogDuplicateFiles`
- Fixed print message typo: `"Diplicate"` → `"Duplicate"`
- Fixed misleading message: "deleted" → "found"
- Fixed `iFound` counter (was never incremented)
- Used context manager for file writes

#### `Assignments_11/Assignment3.py` — Duplicate File Deleter
- Replaced `from sys import *` with `import sys`
- Upgraded hash algorithm from MD5 to SHA-256
- Fixed path variable shadowing inside `os.walk` loop (`path` → `filepath`)
- Added per-file confirmation prompt before deletion to prevent accidental data loss
- Fixed deletion logic to preserve the first copy and only delete true duplicates
- Updated help message to accurately describe the script's purpose
- Used context manager for file writes

#### `Assignments_7/Assignment_2.py` — Threading (Even/Odd Factors)
- Removed duplicate `if` conditions inside `EvenFactor` and `OddFactor` loops

#### `Assignments_7/Assignment_4.py` — Threading (String Analysis)
- Replaced `if True == strString[i].islower()` with `if strString[i].islower()`
- Fixed `Digits` function: was printing total string length instead of digit count

#### `Assignments_4/Assignment2.py` — Lambda Multiplication
- Fixed copy-paste error in input prompt: second prompt said "Enter Number 1" → corrected to "Enter Number 2"

#### `MultiThreading1.py`
- Fixed copy-paste error in `Task2`: loop was printing `"Task1"` → corrected to `"Task2"`

#### `Disctionary.py`
- Fixed author name typos: `"Dennis Riche"` → `"Dennis Ritchie"`, `"Stroustrp"` → `"Bjarne Stroustrup"`, `"Guido Van Rusum"` → `"Guido Van Rossum"`
- Fixed variable name typo: `Aouthers` → `Authors`
- Removed unnecessary trailing semicolons

#### `Oop.py`
- Removed dead assignments (`Ans = 0`) immediately overwritten on the next line

#### `Function10.py`
- Fixed variable name typo: `Adition` → `Addition`
