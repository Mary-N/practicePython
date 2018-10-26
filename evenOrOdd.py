num = input("Enter a number and I will tell you whether it's even or odd: ")
num = int(num)
if (num % 2 == 0):
    print(str(num) + " is an even number")
    if (num % 4 == 0):
        print(str(num) + " is also a multiple of 4")
else:
    print(str(num) + " is an odd number")

print("Now enter two numbers and see if they are divisible")
num1 = input("Enter number to be divided: ")
divisor = input("Enter divisor: ")
if (int(num1)%int(divisor) == 0):
    print(num1 + " is evenly divisble by " + divisor)
else:
    print(num1 + " is not evenly divisible by " + divisor)
