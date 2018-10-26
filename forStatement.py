words = ['cat', 'window', 'defenestrate', 'deforestation']
for w in words:
    print(w + str(len(w)))
    print(w, len(w), "\n")

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

'''for w in words:
    if len(w) > 6:
        words.insert(0, w)
print(words)'''

print(words[0])

for x in range(2,2):
    print(x)