# # # # # # l=["shubham",2,3,4,5]
# # # # # # i=0
# # # # # # while i<=4:
# # # # # #     print("\n",l[i])
#     # i=i+1
# # # # # # for x in range(1,6):
# # # # # #     if x==1:
# # # # # #         continue
# # # # # #     print(x)
# # # # # a=int(input("Enter a number :"))
# # # # # print("The multiple of %d is\n"%a)
# # # # # for i in range(1,11):
# # # # #     print("%dx%d=%d"%(a,i,a*i))
# # # # a=int(input("Enter a number:"))
# # # # i=1
# # # # while i<=10:
# # # #     print("\n%dx%d=%d"%(a,i,a*i))
# # # #     i=i+1
# # # a=int(input("Enter a number :"))
# # # fact=1
# # # for i in range(1,a+1):
# # #     fact=fact*i
# # # print("The factorial of a given number is:",fact)
# # l1=["harry","sonam","sachin","rashul"]
# # l2=[]
# # check = 's'
# # for i in l1:
# #    if(i.find(check)==0):
# #         l2.append(i)
# # print("The matching names",l2)
# a=int(input("Enter a number :"))
# for i in reversed(range(1,11)):
#     print("\n%dx%d=%d"%(a,i,a*i))
for j in range(1,5):
    for i in range(1,j+1):
        print(i,end=" ")
    print()

