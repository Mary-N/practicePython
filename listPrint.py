a = [1,1,2,3,5,8,13,21,34,55,89]
b =[]
print("Hey, we are doing list today")
num = int(input("Enter a max number that you want for your new list: "))
for x in a:
    if x < num:
        print(x, end =' ')
        b.append(x)

print("\n" + str(b))

