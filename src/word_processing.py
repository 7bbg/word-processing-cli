import sys

# ANSI Escape Sequences for Colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'  # back to default color

# Word Processing class for file processing
class WORD_PROCESSING:
    def __init__(self, filename=None):
        self.filename = filename
        self.byte_count = 0
        self.char_count = 0
        self.word_count = 0
        self.line_count = 0

        # Initialize data processing
        if filename:
            self.process_file(filename)
        else:
            # If no filename is provided, use stdin
            self.process_stream()

    def process_file(self, filename):
        """ Process a file and count relevant metrics """
        try:
            with open(filename, 'rb', buffering=8192) as file:  # Open file in binary mode to handle all encodings
                self.read_data(file)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error processing file '{filename}': {e}")

    def process_stream(self):
        """ Process data from stdin (if no filename is provided) """
        print("Processing from standard input (Ctrl+D to end)...")
        self.read_data(sys.stdin)

    def read_data(self, data_source):
        """ Read and process data (either file or stdin) """
        for line in data_source:
            self.byte_count += len(line)
            self.word_count += len(line.split())
            self.char_count += len(line.decode(errors='ignore')) if self.filename  else len(line)  # Handle any encoding issues
            self.line_count += 1

    def count_bytes(self):
        return self.byte_count

    def count_lines(self):
        return self.line_count

    def count_words(self):
        return self.word_count

    def count_characters(self):
        return self.char_count

    def display_results(self, args):
        """ Display results based on flags set by the user """
        result = []
        if self.filename:
            print(f"file <'{self.filename}'> : ", end=' ')

        if args.count:
            result.append(f"{GREEN}Bytes: {self.count_bytes()}{RESET}")
        if args.lines:
            result.append(f"{BLUE}Lines: {self.count_lines()}{RESET}")
        if args.words:
            result.append(f"{RED}Words: {self.count_words()}{RESET}")
        if args.characters:
            result.append(f"{YELLOW}Characters: {self.count_characters()}{RESET}")

        # If no flags were set, display all counts
        if not result:
            result = [
                f"{GREEN}Bytes: {self.count_bytes()}{RESET}",
                f"{BLUE}Lines: {self.count_lines()}{RESET}",
                f"{RED}Words: {self.count_words()}{RESET}",
                f"{YELLOW}Characters: {self.count_characters()}{RESET}"
            ]
        
        # Print results for the current file/stream
        print(", ".join(result), end=' ')
        print()
