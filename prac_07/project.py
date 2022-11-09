import csv
from collections import namedtuple

from project_management import ProjectManagement

def main():
    projects = []
    in_file = open('projects.txt', 'r')
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Reflection is stored as a string (Yes/No) and we want a Boolean
        reflection = parts[2] == "Yes"
        # Pointer is stored as a string (Yes/No) and we want a Boolean
        pointer = parts[4] == "Yes"
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        project = ProjectManagement(parts[0], parts[1], reflection, pointer, int(parts[3]))
        # Add the language we've just constructed to the list
        projects.append(project)
    # Close the file as soon as we've finished reading it
    in_file.close()
    # Loop through and display all languages (using their str method)
    for project in projects:
        print(project)

def menu():
    print(f"Menu: \n{'(L)oad Projects'} \n{'(S)ave Projects'} \n{'(D)isplay Projects'} \n{'(F)ilter Projects by date'} \n{'(A)dd Project'} \n{'(U)pdate Project'} \n{'(Q)uit'}")
    option = input(">>>").upper()
    if option == "L":
        print("You have chosen Load")
        main()
    elif option == "S":
        print("You have chosen Save")
    elif option == "D":
        print("You have chosen Display")
    elif option == "F":
        print("You have chosen Filter")
    elif option == "A":
        print("You have chosen Add")
    elif option == "U":
        print("You have chosen Update")
    elif option == "Q":
        print("You have chosen Quit")
    else:
        print("Please choose valid option")

menu()