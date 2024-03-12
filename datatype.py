r=range(10)
for i in r:
     print(i)

# operator  
# arethmetic operator

a=10
b=3
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)
print(a**b)
print(a//b)

branch ="\nCSE"
print(branch*4)
a=b=50
print(a,b)

a,b=50,60
print(a,b)
print(b,a)


a=10
a+=20
print(a)

# relational operator
a=10
b=5
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

a='aa'
b='bb'
print(a<b)
print(a>b)
print(10<20<30<40)

# logical operator
print(True and True)
print(True or False)

print(0 and 15)
print(10 and 15)
print(10 or 15)
print(0 or 15)


# identi operator
a=50
b=60
print(a is not b)
print(id(a))
print(id(b))

# memborship operator

name="NIT"
print('N' in name)
print('IT'in name)
print('NIT' not in name)

# How to take input from Keyboard user
a=int(input("enter value in a"))
b=int(input("enter value in b"))
c=a+b
print("result",c)



username=input("enter user name")
print(username)

# conditional statement

mark=int(input("enter mark"))
if mark<=33:
     print("you are fail")

else :
     print("you are pass")


# greading system
mark=int(input("enter mark"))
if mark>=90:
     print("o gread")
elif mark>=80:
     print("E gread")
elif mark>=70:
     print("A gread")
elif mark>=60 and mark<=69:
     print("just pass")

else:
     print("fail")
    

