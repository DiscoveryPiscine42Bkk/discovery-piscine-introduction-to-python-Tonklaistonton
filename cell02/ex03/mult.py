first_num =  input ("Enter the first number:").strip()
second_num =  input ("Enter the second number:").strip()
first_num = int(first_num)
second_num = int(second_num)
whole_num = first_num * second_num
print("", first_num, "x", second_num, "=", whole_num)
if whole_num > 0:
    print("The result is positive.")
if whole_num < 0:
    print("The result is negative.")
else:   
    print("The result is positive and negative.")