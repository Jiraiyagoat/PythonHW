num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num2 != 0:
    quotient = num1 // num2
    remainder = num1 % num2
    print(num1, " / ", num2, " = ", quotient, " (", remainder, ")")
else:
    print("Divison by 0 is not allowed")