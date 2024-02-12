def ask_for_password(min_length):
    while True:
        password = input("Please enter a password: ")
        if len(password) < min_length:
            print(f"Password must be at least {min_length} characters long. Try again.")
        else:
            return password


def print_asterisks(word):
    print('*' * len(word))


def main():
    min_length = 8
    password = ask_for_password(min_length)
    print_asterisks(password)


if __name__ == "__main__":
    main()
