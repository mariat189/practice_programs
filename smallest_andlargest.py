arr=[]
n=int(input("Enter the count of numbers"))
print("Enter elements:")
for i in range(0,n):
    i=int(input())
    arr.append(i)
print("Maximum=",max(arr),"Minimum=",min(arr))