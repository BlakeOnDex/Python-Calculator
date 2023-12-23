import time
x=float(input("Enter First Number:"))
y=float(input("Enter Second Number"))
operation =input("Enter Operation")

if operation == "+":
     print(x + y)
elif operation == "-":
     print(x-y)
elif operation == "*":
     print(x*y)
elif operation == "/":
     print(x/y)
else:
     print("incorrect symbol")
