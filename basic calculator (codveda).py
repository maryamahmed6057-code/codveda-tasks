def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def div(a,b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

print("\nsimple calculator")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exit")

choice=input("enter your option:")

a=int(input("enter first number:"))
b=int((input("enter second number:")))

if choice=="1":
    print('the result is=',add(a,b))
elif choice=="2":
    print('the result is=',sub(a,b))
elif choice=="3":
    print('the result is=',multiply(a,b))
elif choice=="4":
    print('the result is=',div(a,b))
else:
    print('invalid choice,thank you for using calculator')


