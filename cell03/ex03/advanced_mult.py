i = 0
while i <= 10:
    j = 0
    output = ""
    while j <= 10:
        output += str(i * j) + " "
        j += 1
    print(f"Table de {i}: {output}")
    i += 1