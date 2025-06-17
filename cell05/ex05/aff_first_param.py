import shlex

if user := input(""):
    words = shlex.split(user)
    if len(words) >= 1:
        print(words[0])  # Print the first word (e.g. "Code Ninja")
    else:
        print("none")

 