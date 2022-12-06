# names = ["Matt", "Mason", "Lachlan", "Jess", "Maddie"]
#
# number = int(input(f"Enter a number, up to {len(names)}: "))
#
# try:
#     print(names[number - 1])
# except IndexError:
#     print("Invalid number")


# from operator import itemgetter
#
# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
#
# new_score = input("Please enter a name and a score: ") .split()
#
# new_score[1] = int(new_score[1])
#
# score_pairs.append(new_score)
# score_pairs.sort(key = itemgetter(1), reverse = True)
#
# print(score_pairs)
# x = str(int('1.0'))
# x[-1] = '2'

# words = ["aye", "bee", "sea", "bee"]
# words.remove("bee")
# print(words.pop())

# things = list("one two three")
# print("{}-{}".format(*things))
# print("*".join([len(word) for word in "one*two*three".split('*')]))
string = "CP1404 is good"
print(string[::-1])