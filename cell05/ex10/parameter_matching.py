import sys
args = sys.argv[1:]
if len(args) != 1:
 print("none")
else:
 user_input = input("Enter a word: ")
if user_input == args[0]:
 print("Good job!")
else:
 print("Nope, sorry...")