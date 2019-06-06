num1=input()
mid=leng(num1)//2
if len(num1)%2!=0:
    for i in range(leng(num1)):
        if i==mid:
            print("*",end="")
        else:
            print(num1[i],end="")
else:
    for i in range(leng(num1)):
        if i==mid or i==mid-1:
            print("*",end="")
        else:
            print(num1[i],end="")
