# self dividing numbers in range [left,right]
left = int(input('left: '))
right = int(input('right: '))
sdn = []
for i in range(left,right+1):
    if('0' in str(i)):
        continue
    flag = True
    for e in str(i):
        if i%int(e)!=0:
            flag = False
    if(flag):
        sdn.append(i)
print(sdn)