# Ugit 

`ugit` is something i am building from scratch. WHY? i am just exploring interesting stuff!
Next is some generalized stuff but i will update it all soon enough!

## Core Functionalities

- `init`: Initializes a new ugit repository. This creates a `.ugit` directory in the current folder, which will store all the necessary files for version control.
- `hash-object <file>`: Computes the SHA-1 hash of a given file and stores it as an object in the ugit object database. This is similar to `git hash-object`.
- `cat-file <hash>`: Retrieves and displays the content of an object from the object database, identified by its hash. This is similar to `git cat-file -p`.

## Project Structure

The project is organized as follows:

- `setup.py`: The setup script for the project, which handles packaging and distribution. It also defines the `ugit` command-line entry point.
- `ugit/`: The main package directory containing the core logic.
  - `cli.py`: The command-line interface for `ugit`. It parses user arguments and executes the corresponding commands.
  - `data.py`: This module is responsible for handling the data of the ugit repository. It manages the object database, including storing and retrieving objects.

## Usage

To start using `ugit`, you first need to initialize a repository:

```bash
ugit init
```

This will create a `.ugit` directory.

To add a file to the object database, use the `hash-object` command:

```bash
ugit hash-object my_file.txt
```

This will output the hash of the file, which can then be used to retrieve it:

```bash
ugit cat-file <hash_of_my_file>
```
