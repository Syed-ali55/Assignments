def add(num_1, num_2):
    return num_1+num_2

def sub(num_1, num_2):
    return num_1-num_2

def div(num_1, num_2):
    return num_1/num_2

def mul(num_1, num_2):
    return num_1*num_2

print("choose your desired operation")
print("1 addition\n","2 subtraction\n","3 multiplication\n","4 division\n")
choice = input("enter your choice")
num_1 = input("enter the first number\n")
num_2 = input("enter the second number\n")
if choice == "1":
    print(add(num_1,num_2))
elif choice == "2":
    print(sub(num_1, num_2))
elif choice == "3":
    print(mul(num_1, num_2))
elif choice == "4":
    print(div(num_1, num_2))
else:
    print("choose the correct option")

