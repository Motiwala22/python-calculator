
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")

choice = input("Enter your chocie here : ")

num1 = float(input("Input Value: "))
num2 = float(input("Input Value: "))

if choice == "1":
    print( num1, "+", num2, "=", (num1+num2))

elif choice == "2":
    print( num1, "-", num2, "=", (num1-num2))

elif choice == "3":
    print( num1, "*", num2, "=", (num1*num2))

elif choice == "4":
    if num2 == 0.0:
        print("Divided by 0; Error 404")
    else:
        print( num1, "/", num2, "=", (num1/num2))

else:
    print("Invaild choice")


     
