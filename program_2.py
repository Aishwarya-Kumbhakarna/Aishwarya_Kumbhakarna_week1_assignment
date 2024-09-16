'''Create a program that uses conditional statements to determine if a number is positive, negative, or zero'''


num = float(input("Enter a number: "))

if num > 0:
    print(num," is a positive number.")
elif num < 0:
    print(num," is a negative number.")
else:
    print("The number is zero.")

