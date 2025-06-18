import re
import shlex

user_input = input().strip()
parts = shlex.split(user_input)

if len(parts) != 2:
    print("none")
else:
    keyword, text = parts
    pattern = r'\b' + re.escape(keyword) + r'\b'
    matches = re.findall(pattern, text)
    print(len(matches) if matches else "none")
