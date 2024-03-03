# recursive implementation of division to find the quotient
def divide(m,n):
    if(m<n):
        return 0
    return 1 + divide(m-n,n)
m = int(input('a: '))
n = int(input('b: '))
print(r'm/n =',divide(m,n))