import shlex
user_input = input()
args = shlex.split(user_input)
if len(args) == 0:
    print("$")
else:
    print(f"parameters: {len(args)}$")
for param in args:
    print(f"{param} : {len(param)}$")

# ignored  it UwU
