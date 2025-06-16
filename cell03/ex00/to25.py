num =  input("Enter a number less than 25\n" ).strip()
if num >= "25":
 print("error")
else:
 while int(num) < 25:
  num = int(num) + 1
  print("Inside the loop, my variable is",num)