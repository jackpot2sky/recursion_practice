# find a^b using recursion
def exp(a,b):
    return a*exp(a,b-1) if b>0 else 1
print(exp(10,4))