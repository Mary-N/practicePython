#prompt user to input a word(string) in which no single letter is repeated
#loop through the string, create two variables a and b that are to be compared each time the string is looped
# a, b, c, d

#def isogram(word):
'''input_value = input("Input a word with no letter repeating itself: ")
for x in input_value:
    if input_value.count(x) > 1:
        print("You got this wrong. ", x , " is repeated", input_value.count(x), "times" )
        print("bye bye")'''

singleton = ('hello',)
print(singleton)

tuple1 = 12345, 45321, 'hello!'
x, y, z = tuple1
print(x)
print(tuple1[1])

basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(len(basket))