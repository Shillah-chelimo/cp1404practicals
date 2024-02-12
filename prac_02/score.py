"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""

import random

def main():
    """Entry point of the program."""
    user_score = float(input("Enter score: "))
    print_result(user_score)

    # Generate a random score and print the result
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print_result(random_score)


def print_result(score):
    """
    Determine and print the status of the score.

    Args:
        score (float): The score to be evaluated.
    """
    if 0 <= score <= 100:
        if score >= 90:
            result = "Excellent"
        elif score >= 50:
            result = "Passable"
        else:
            result = "Bad"
        print(result)
    else:
        print("Invalid score")


if __name__ == "__main__":
    main()

