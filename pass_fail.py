a=int(input("Enter marks 1:"))
b=int(input("Enter marks 2:"))
c=int(input("Enter marks 3:"))
tot=a+b+c
per=(tot/300)*100
if(per>=40 and (a or b or c)>=33):
    print("Pass")
else:
    print("Fail")
    
