"""Module docstring"""


# imports
import random
# CONSTANTS

def main():
    """Function docstring"""
    # statements...
    score = input("What is the score? ")
    score = float(score)
    do_stuff(score)
    ranscore = random.randrange(0, 100, 1)
    print("Random Score is ",ranscore)


def do_stuff(score):
    """Function docstring"""
    # statements...
    if score < 0 or score > 100:
        print("not valid")
    elif score >= 90:
        print("excellent")
    elif score >= 50:
        print("passable")
    else:
        print("bad")


main()


