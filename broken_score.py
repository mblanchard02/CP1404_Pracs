"""
broken_score program
CP1404/CP5632 - Practical
Broken program to determine score status
use if elif else
"""
# TODO: Fix this!

score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("not valid")
elif score >= 90:
    print("excellent")
elif score >= 50:
    print("passable")
else:
    print("bad")