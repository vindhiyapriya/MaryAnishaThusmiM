a=float(input("a:"))
b=float(input("b:"))
op=input("type of operation:")
if op=="+":
    print("result=",a+b)
elif op=="-":
    print("result=",a-b)
elif op=="*":
    print("result=",a*b)
elif op=="/":
    if b!=0:
         print("result=",a/b)
    else:
        print("Cannot divided by Zero")
else:
    print("invalid Operation")