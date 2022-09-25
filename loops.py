"""
loops program
"""

# odd numbers to 20 (2 is used to count up every second no. from 1 on to 19
for i in range(1, 21, 2):
    print(i, end=' ')
print()
# going up in 10's from 0 to 100, note-101 is used so 100 is included
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# going down from 20, which is why 20 goes first
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# displaying no. input as stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()
# d. print n number of lines of increasing stars in increasing rows until n is reached
for i in range(1, number_of_stars + 1):
    print('*' * i)
print()
