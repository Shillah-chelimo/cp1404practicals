"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""
import csv
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    try:
        with open('languages.csv', 'r') as in_file:
            for line in in_file:
                print(line.strip()
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()
