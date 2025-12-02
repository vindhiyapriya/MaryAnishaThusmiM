a=int(input("enter the number:"))
if a%2==0:
    a=a-1
else:
    a=a
for i in range (a):
    print(2*i+1,end=" ")