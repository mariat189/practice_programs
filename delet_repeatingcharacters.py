a=input("Enter the string:")
b = []
for i in a:
    if i not in b:
        b.append(i)
b = ''.join(b)
print("The string after deletion of repeated characters is",b)