# find a^b using recursion
def exp(a,b):
    def mul(a,b):
        if a==0 or b==0: return 0
        return a+mul(a,b-1)
    return mul(a,exp(a,b-1)) if b>0 else 1
print(exp(3,5))