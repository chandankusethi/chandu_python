# check a number is positive,nagetive or zero

num=int(input("énter a number"))

if num>0:
     print("positive")
elif num<0:
     print("negative")

else:
     print("Zero")


# check a greater number from three numbers.

num1=int(input("enter the 1st number"))
num2=int(input("enter the 2nd number"))
num3=int(input("enter the 3rd number"))

if (num1 > num2) and (num1 >num3):
     print("num1 is greater")
elif(num2>num1)and(num2>num3):
     print("num2 is greater")
else:
     print("num3 is greater")



a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
print("enter choice\n1.add\n2.sub\n3.mul\n4.div")
choice=input("enter choice")
if choice=="add":
     print(a+b)
elif choice=="sub":
     print(a-b)
elif choice=="mul":
     print(a*b)
elif choice=="div":
     print(a/b)
