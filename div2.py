def divide(a,b):
    if a<b:
        return a
    return divide(a-b,b)
a = int(input('a: '))
b = int(input('b: '))
print(r'a%b =',divide(a,b))