num1=int(input())
if num1 > 1:  
   for x in range(2, num1//2): 
       if (num1 % x) == 0: 
           print("yes") 
           break
   else: 
       print("no") 
  
else: 
   print("yes")
