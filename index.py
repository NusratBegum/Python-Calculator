# create Calculator

#this function will create addition

def add(x,y):
    return x+y

#this function will create subtraction

def sub(x,y):
    return x-y

#this function will create multiplication

def mul(x,y):
    return x*y

#this function will create division

def div(x,y):
    return x/y

def main():
    print("Select Operation.")
    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1','2','3','4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1,num2))

            elif choice == '2':
                print(num1, "-", num2, "=", sub(num1,num2))

            elif choice == '3':
                print(num1, "*", num2, "=", mul(num1,num2))

            elif choice == '4':
                print(num1, "/", num2, "=", div(num1,num2))
            break
        else:
            print("Invalid Input")

main()            