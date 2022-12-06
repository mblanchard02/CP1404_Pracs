"""
menu program
CP1404/CP5632 - Practical - Suggested Solution
Menu using the standard while loop pattern
"""
menu = "(H)ello\n(G)oodbye\n(Q)uit"  #used from suggested soln
name = input("Enter name: ")
print(menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Not valid")
    print(menu)
    choice = input(">>> ").upper()
print("completed.")