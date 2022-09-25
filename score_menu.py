"""Module docstring"""


score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("not valid")
elif score >= 90:
    print("excellent")
elif score >= 50:
    print("passable")
else:
    print("bad")

def main():
    """Function docstring"""
    for i in range(score):
        print('*', end=' ')
    print()


main()
