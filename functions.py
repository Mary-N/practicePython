def fib(n): #write fibonacci series upto n
    """Return a list containing the Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
    print()
#Now call the fib() function that we created
fib(2000)

i = 5
def f(arg = i):
    print(arg)
    i = 6
f()

def f2(a, L = []):
    L.append(a)
    return L
print(f2(2))
print(f2(3))
print(f2(4))

def f3(a, L = None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f3(2))
print(f3(3))
print(f3(4))

def cheeseshop(kind, *arguments, **keywords):
    print("-- DO you have any", kind, "?")
    print("-- Am sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    
print(cheeseshop("Limburger", "It's very runny, sir", "It's really very, VERY runny, sir", 
shopkeeper = "Michael Palin", client = "John Clesse", sketch = "CHeese Shop Skecth"))