# imports
from score import print_result


def main():
    """Entry point of the program."""
    score = get_valid_score()
    # Menu loop
    while True:
        display_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid input. Please try again.")


def display_menu():
    """Display the main menu."""
    print("\nMain Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """
    Get a valid score from the user.

    Returns:
        float: The valid score entered by the user.
    """
    while True:
        score = input("Enter a valid score (0-100): ")
        if score.isdigit():
            score = float(score)
            if 0 <= score <= 100:
                return score
        print("Invalid score. Please enter a number between 0 and 100.")


def show_stars(score):
    """
    Print stars based on the given score.

    Args:
        score (float): The score for which stars are to be printed.
    """
    print("*" * int(score))


if __name__ == "__main__":
    main()

