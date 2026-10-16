
# File Automation Tool 

A Python-based file organizer that automatically sorts files into folders based on their file extensions.

##  Project Overview

Managing files manually can be time-consuming when many different file types are stored in one folder.

This tool organizes files into categories such as Images, PDFs, Documents, Spreadsheets, Python Files, Videos, Audio, Archives, and Others.

It also avoids overwriting files when a file with the same name already exists in the destination folder.

##  Features

- Automatically organize files by extension
- Create category folders when needed
- Support common file types
- Move unknown file types into an Others folder
- Skip files when the destination filename already exists
- Display a summary of moved, skipped, and failed files
- Handle file operation errors
- Use a test folder to safely test the program

##  Technologies Used

- Python
- pathlib
- shutil
- File and folder handling
- Dictionaries, lists, and loops
- Exception handling
- Functions

##  Project Structure

```text
file-automation-tool/
├── file_organizer.py
├── README.md
└── test_files/
    ├── Documents/
    ├── Images/
    ├── PDFs/
    ├── Python_Files/
    ├── Spreadsheets/
    └── Others/
```

The `test_files` folder is used for testing. The program organizes files directly inside this folder into category subfolders.

##  How to Run

### 1. Install Python

Install Python if it is not already available on your computer.

### 2. Prepare test files

Create a folder named `test_files` in the same directory as `file_organizer.py`.

Add some sample files to test the organizer, such as:

- `notes.txt`
- `assignment.pdf`
- `photo.jpg`
- `marks.xlsx`
- `program.py`

### 3. Run the program

Open a terminal in the project directory and run:

```bash
python file_organizer.py
```

### 4. Check the results

The program creates category folders and moves the files into the appropriate locations.

##  Testing

The following tests were performed:

| Test | Result |
|---|---|
| Organize common file types | Passed |
| Handle unknown extensions | Passed |
| Skip duplicate filenames | Passed |

All three manual tests passed with zero reported errors.

##  Sample Output

```text
Starting file organization...

Moved: notes.txt -> Documents/
Moved: photo.jpg -> Images/
Moved: program.py -> Python_Files/

========== ORGANIZATION SUMMARY ==========
Files found: 5
Files moved: 5
Files skipped: 0
Errors: 0
```

The exact output depends on the files present in `test_files`.

##  Learning Outcomes

Through this project, I practiced:

- Working with file paths using `pathlib`
- Moving files using `shutil`
- Organizing files based on extensions
- Creating directories automatically
- Checking for existing files
- Handling file operation errors
- Writing reusable Python functions
- Testing automation scripts

##  Future Improvements

- Add a dry-run mode to preview changes before moving files
- Allow users to select a source folder
- Add logging to record file operations
- Add automated unit tests
- Support recursive folder organization

##  Author

**Anveshka Kushwah**

GitHub: [anveshkakushwah](https://github.com/anveshkakushwah)

LinkedIn: [Connect with me](https://www.linkedin.com/in/anveshkakushwah-0b54443b1/)
