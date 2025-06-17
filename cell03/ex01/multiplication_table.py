num =  input("Enter a number\n" ).strip()
if num.isdigit():
 num = int(num)
 for i in range(0, 13):
  print(f"{i} x {num} = {i * num}")