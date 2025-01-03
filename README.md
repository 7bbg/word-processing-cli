# Word-Processing-CLI

A simple Python command-line tool that mimics the functionality of the Unix `wc` (word count) command. It can process text from files or standard input, counting bytes, lines, words, and characters. Additionally, it supports real-time monitoring of file changes, allowing you to watch files for modifications and display updated results.

## Features

- **Word Count**: Count the number of words in a file.
- **Line Count**: Count the number of lines in a file.
- **Character Count**: Count the number of characters in a file.
- **Byte Count**: Count the number of bytes in a file.
- **Real-time File Monitoring**: Watch multiple files for changes and display updated results as files are modified.
- **Standard Input (stdin)**: Process input from stdin if no file is provided.
  
## Installation

### Prerequisites

- Python 3.6 or later
- `asyncio` (standard library in Python 3.6+)
- `word_processing.py` (custom module)

### Clone the Repository

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/7bbg/yourusername/word-processing-cli.git
   cd word-processing-cli
   ```
2. **Make a virtual environment**:  `python3 -m venv venv`
3. **Activate virtual environment**:
    
    Linux or Mac
    ```bash
    source venv/bin/activate
    ```
    Windows
    ```bash
    ./venv/Scripts/activate
    ```

4. **Install require packages**:  `python -m pip install --editable`

### Ensure `word_processing.py` Exists
This project relies on a custom module, `word_processing.py`, which contains the logic for counting words, lines, bytes, etc. Make sure the `word_processing.py` file exists and is located in the same directory as your `main.py`. It should define a class `WORD_PROCESSING` with a `display_results()` method.

## Usage
### Basic Usage
Run the script from the command line with the desired options. The general syntax is:

```bash
python src/main.py [options] [filenames...] 
```
### Options
- `-c`, `--count`: Count bytes in the file.
- `-l`, `--lines`: Count lines in the file.
- `-w`, `--words`: Count words in the file.
- `-m`, `--characters`: Count characters in the file.
- `-r`, `--watch`: Monitor files for real-time changes.


### Examples
#### Count Words in a File
```bash
python main.py -w example.txt
```

#### Count Lines and Words in Multiple Files
```bash

python main.py -l -w file1.txt file2.txt
```
#### Count Bytes and Characters in a File
```bash
python main.py -c -m example.txt
```
Monitor File Changes in Real-Time
```bash
python main.py -r file1.txt file2.txt
```

This command will watch `file1.txt` and `file2.txt` for any changes. When a file is modified, the tool will re-display the results.


#### Use stdin for Input
If no filenames are provided, the program will use stdin as input. You can type the input directly or pipe content to the program.

```bash
echo "Hello World" | python main.py -w
```
Or you can simply run the program and input data manually:
``` bash
python main.py -w
```

Press Ctrl+D to end the input and display the results.


#### Watching stdin (No files provided) [Future Implementation]
```bash
python main.py -r
```
This command will wait for changes from stdin input, re-processing whenever new data is typed.



## Code Structure
### Main Components
- Argument Parser (`argparse`): Parses and processes command-line arguments.
- `WORD_PROCESSING` class: A custom class used to process files or stdin input. It provides methods to count words, lines, characters, and bytes.
- Real-Time File Monitoring: Using `asyncio`, the script can watch multiple files for changes and re-process them when modified.


### Main Functions
- `watch_file()`: Watches a specific file for changes and re-runs the word-processing logic.
- `watch_multiple_files()`: Watches multiple files asynchronously for changes.
- `process_files()`: Processes files or stdin, depending on user input.
- `main()`: The main execution loop, handling user input, file watching, and displaying results.


---
### **Future Implementation**:

1. **Dynamic Output**:
   - Allow the tool to update the terminal output dynamically. The terminal should clear and refresh its content as new data is processed, providing a real-time experience to the user.

2. **Graceful Handling of Errors**:
   - If a file becomes inaccessible or is deleted while being monitored, the program should notify the user about the error instead of crashing.


3. **Track and Process Only Modified Parts of a File**:
   - Process the newly modified parts of the file instead of recalculating everything.
---
