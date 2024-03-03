num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))
n1 = []
n2 = []
# hcf = -1
for i in range(0,num1):
    if(num1%(i+1)==0):
        n1.append(i+1)   
for i in range(0,num2):
    if(num2%(i+1)==0):
        n2.append(i+1)
for e in n1:
    if e in n2:
        hcf = e
print(hcf)