""""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert number of students to an integer
        data.append(parts)  # Append the parts to the data list
    input_file.close()
    return data


def display_subject_details(data):
    """Display subject details."""
    for subject_info in data:
        subject_code, lecturer, num_students = subject_info
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


def main():
    data = get_data()
    print(data)  # For testing purposes
    display_subject_details(data)


main()
