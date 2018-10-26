import time
import datetime

print("Hello")
name = input("What's your name? ")
age = input("How old are you? ")
yr = datetime.datetime.now()
current_yr = yr.strftime("%Y")
future_yr = (int(current_yr) - int(age)) + 100
future_yr = str(future_yr)
print( 2 * ("\n" + name + ", you will be 100 years old in the year " + future_yr ))

count = 0
while (count < 4):
    print("\nenter a differnt age and see if am accurate")
    age = input("age: ")
    yr = datetime.datetime.now()
    current_yr = yr.strftime("%Y")
    future_yr = (int(current_yr) - int(age)) + 100
    future_yr = str(future_yr)
    print(name + ", you will be 100 years old in the year " + future_yr )
    count = count + 1
print("I hope that was enough to prove my accuracy, good bye")
