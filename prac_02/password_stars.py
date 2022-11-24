"""Module docstring"""

MINIMUM_LENGTH = 4


def version_1():
    """Get a password of valid size and print asterisks"""
    password = input(f"Enter a password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter a password of at least {MINIMUM_LENGTH} characters: ")

    print('*' * len(password))

def main():
    """Get and print password using functions"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensuring it meets the length requirements"""
    password = input(f"Enter a password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password is too short")
        password = input(f"Enter a password of at least {minimum_length} characters: ")
    return password


def print_asterisks(sequence):
    """Print the correct amount of asterisks"""
    print('*' * len(sequence))


main()
