import shlex
user = input("")
if user.upper(): 
	print("none")
else:
    words = shlex.split(user)
    for word in words:
        print(" " + word.lower())