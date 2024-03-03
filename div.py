# recursive implementation of division to find the remainder
def divide(a,b):
    # if(a<b): return a
    if((a-b)>b):
        return divide(a-b,b)
    return a-b if a>b else a
m=int(input('enter a: '))
n=int(input('enter b: '))
print(r'a%b =',divide(m,n))