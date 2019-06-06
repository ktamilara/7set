import math
num1,num2=map(int,input().split())
num3=num1*num2
root = math.sqrt(num3)
if int(root + 0.5) ** 2 == num3:
    print("yes")
else:
    print("no")
