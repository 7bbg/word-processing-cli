import argparse
import asyncio
import os
import sys
import time
from word_processing import WORD_PROCESSING


# Argument parser setup

parser = argparse.ArgumentParser(
    prog='Word-Processing-CLI',
    description=(
        'A CLI that handles text input from either files or file streams. '
        'This is a clone of the unix command "wc" (word count).'
    ),
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)

# Argument definitions
parser.add_argument(
    'filenames', nargs='*', help='List of filenames to process. If none are provided, stdin is used.'
)
parser.add_argument('-c', '--count', action='store_true', help='Count bytes in a file')
parser.add_argument('-l', '--lines', action='store_true', help='Count lines in a file')
parser.add_argument('-w', '--words', action='store_true', help='Count words in a file')
parser.add_argument('-m', '--characters', action='store_true', help='Count characters in a file')
parser.add_argument('-r', '--watch', action='store_true', help='Monitor files for real-time changes')

args = parser.parse_args()

# Asynchronous file watching
async def watch_file(file_path, last_modified):
    try:
        while True:
            current_modified = os.path.getmtime(file_path)
            if current_modified != last_modified:
                print(f"\nFile {file_path} has been modified.")
                wp = WORD_PROCESSING(file_path)
                wp.display_results(args)
                last_modified = current_modified
            await asyncio.sleep(1)  # Poll asynchronously every second
    except FileNotFoundError:
        print(f"\nFile {file_path} not found.")
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting gracefully...")
        sys.exit(0)


async def watch_multiple_files(files):
    tasks = []
    for file in files:
        try:
            last_modified = os.path.getmtime(file)
            tasks.append(watch_file(file, last_modified))
        except FileNotFoundError:
            print(f"File {file} not found and cannot be monitored.")
    await asyncio.gather(*tasks)


# Main file processing logic
def process_files(args):
    if args.filenames:
        for filename in args.filenames:
            try:
                wp = WORD_PROCESSING(filename)
                wp.display_results(args)
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
    else:
        # No filenames provided, process stdin
        print("No filenames provided. Using input from stdin.")
        wp = WORD_PROCESSING()
        wp.display_results(args)


# Main execution loop
def main():

    if args.watch:
        if not args.filenames:
            print("No filenames provided. Watching stdin for changes not currently supported.")
            wp = WORD_PROCESSING()  # Read from stdin by default if no files are provided
            wp.display_results(args)  # Initial display of the results

        else:
            print("Watching files for changes...")
            try:
                asyncio.run(watch_multiple_files(args.filenames))
            except KeyboardInterrupt:
                print("\nProcess interrupted. Exiting gracefully...")
                sys.exit(0)
    else:
        process_files(args)


main()
