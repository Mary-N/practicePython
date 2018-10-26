def isogram():
    word = input("enter word: ")
    if len(word) == len(set(word)):
        return f"{word} is an isogram"
    else:
        return f"{word} is not an isogram"

print(isogram())

