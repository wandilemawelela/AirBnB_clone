# AirBnB Clone Project

Welcome to the AirBnB clone project! This project aims to build an AirBnB web application by implementing a command interpreter. This initial step is crucial, as it establishes the foundation for subsequent tasks such as HTML/CSS templating, database storage, API development, and front-end integration.

## Project Overview

### Task List
1. Implement a parent class (BaseModel) responsible for the initialization, serialization, and deserialization of future instances.
2. Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
3. Define classes for essential AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel.
4. Develop the first abstracted storage engine for the project: File storage.
5. Create comprehensive unit tests to validate all classes and the storage engine.

## Command Interpreter

### What's a Command Interpreter?

The command interpreter is similar to a shell but tailored for a specific use case. In this project, it allows the management of AirBnB objects, including:

- Creating a new object (e.g., User, Place).
- Retrieving an object from a file, database, etc.
- Performing operations on objects (e.g., counting, computing stats).
- Updating attributes of an object.
- Destroying an object.

### Execution

#### Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

$ cat test_help
help
$

$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Getting Started
1. Clone the repository.

```bash
Copy code
git clone https://github.com/your-username/AirBnB-Clone.git
cd AirBnB-Clone
```

2. Run the command interpreter in interactive mode.

```bash
Copy code
./console.py
```

3. Explore the documented commands and start managing your AirBnB objects!

