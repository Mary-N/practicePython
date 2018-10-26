dict1 = dict(sape=4139, guido=4127, jack=4098, pemba=8888)
print(dict1)

dict2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4089)])
print(dict2)

#looping through dictionary1 i.e dict1
for k, v in dict1.items():
    print(k, v)

list1 = ['tic', 'tac', 'toe']

#looping through list1 using enumerate() function
for i, v in enumerate(list1):
    print(i, v)

#looping through a string using enumerate() function
string = "mary"
for i, v in enumerate(string):
    print(i, v)
#looping through a turple using the enumerate() function
tuple1 = ('seed', 'sun', 'moon')
for i, v in enumerate(tuple1):
    print(i, v)

#looping through a set using enumerate() function
for i, v in enumerate(set(tuple1)):
    print(i, v)

#looping over two or more sequences using zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is your {q}? It is {a}')

#This is another way of using a string format
print("#"*40)
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q, a))

#looping through a sequence using the reversed function
for i in reversed(tuple1):
    print(i)

#looping through a sequence of numbers using the reversed function
for i in reversed(range(1, 10, 2)):
    print(i)

#looping over a sequence in sorted orfer uisng the sorted() function
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)