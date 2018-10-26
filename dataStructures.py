#Lists

mary = [1,4,8,12,16,20]
print(mary[:])
mary.append(24)
mary.append([3,5,6])
print(mary)
mary.extend("Nakanjako")
print (mary)
mary.extend((3,6,9))
print(mary)
books = {"author" : "George Owell", "book" : "Animal farm"}
mary.extend(books.keys())
print(mary)
mary.extend(books.values())
print(mary)

mary.insert(0, 100)
print(mary)
mary.insert(2, 90)
print(mary)


ages = [4,6,7,12,8,3,4]
ages.remove(12)
print(ages)
ages.pop()
print(ages)
print("-"*20)
b = ages.pop()
c = b+7
print(c)
print(b)
ages.pop(2)
print(ages)

horses = ["billy", "milly", "pilly", "gilee", "sili", "swilly" ]
print(horses.index("sili"))
print(horses.index("sili", 3))
print(horses.index("sili", 2, len(horses)))
