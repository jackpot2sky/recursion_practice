num1,num2=1,2
def func(num1,num2):
    num1+=num1
    num2+=num2
    print(num1,num2)
print('outside:',num1,num2,'\ninside:',func(num1,num2))