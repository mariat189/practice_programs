a=input("Enter the string")
s=input("Enter the character")
count=0
for i in a:
    if i==s:
        count=count+1
print("Count of character",s,"is",count)