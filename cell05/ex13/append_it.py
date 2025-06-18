import sys
import re
args = sys.argv[1:]
if len(args) == 0:
 print("none")
else:
 for arg in args:
  if not re.search(r'ism$', arg):
   print(arg + "ism")