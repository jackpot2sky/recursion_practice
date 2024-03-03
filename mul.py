def mul(a,b):
    if a==0 or b==0: return 0
    return a+mul(a,b-1)
print(mul(3,13))