"""
word_counter.py

Description:
This Python script counts the number of words in a given text file. 
It reads the file, splits the text into words, and prints the total word count.
It also handles the case where the file does not exist, giving an appropriate error message.

Usage:
1. Run the script in a Python environment.
2. Enter the full path to the text file when prompted.
3. The script will output the total number of words in the file.

Example:
$ python word_counter.py
Enter the path to the file: sample.txt
Total words: 125
"""

def count_words(file_path):
    """Counts the number of words in a file."""
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"Total words: {len(words)}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    count_words(file_path)
