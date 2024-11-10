# File Handling Assignment

## Overview

This assignment involves creating a Python script that demonstrates basic file operations: creating a file, writing to it, reading from it, appending to it, and handling potential errors. You will implement a series of tasks that focus on file manipulation in Python using different file modes and error-handling mechanisms.

## Instructions

### 1. **File Creation**
   - Create a Python script named `file_handling_assignment.py`.
   - Within the script, perform the following actions:
   - Create a new text file named `my_file.txt` using write mode (`'w'`).
   - Write at least three lines of text to the file. The text should include a mix of strings and numbers.

### 2. **File Reading and Display**
   - Enhance the script to read the contents of `my_file.txt`.
- After reading, display the contents of the file on the console.

### 3. **File Appending**
   - Modify your script to open `my_file.txt` in append mode (`'a'`).
   - Append three additional lines of text to the file without overwriting the existing content.

### 4. **Error Handling**
   - Implement error handling for potential file-related issues.
   - Use `try`, `except`, and `finally` blocks to manage exceptions such as:
   - `FileNotFoundError`: Raised if the file doesn't exist when attempting to read or write.
   - `PermissionError`: Raised if there is a permissions issue when accessing the file.
   - Ensure that the script can handle errors gracefully and always closes the file in the `finally` block, even if an error occurs.

---

