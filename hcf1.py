# hcf of 2 numbers
num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))
def hcf(n1,n2):
    mi = min(n1,n2)
    ma = max(n1,n2)
    if ma%mi==0: return mi
    return hcf (ma%mi,mi)
print(hcf(num1,num2))