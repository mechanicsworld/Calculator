#This is calculator program in github project
def add(a,b):
  s=a+b
  return s 
def sub(a,b):
  s=a-b
  return s 
def mul(a,b):
  s=a*b
  return s 
def div(a,b):
  s=a/b
  return s 

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("Enter the respective number to carry out respective operation ")
ch=int(input("Enter the choice: "))
if ch==1:
  a=add(a,b)
  print("Addition of two numbers is",a)
elif ch==2:
  a=sub(a,b)
  print("Subtraction of two numbers is",a)
elif ch==3:
  a=mul(a,b)
  print("Multiplication of two numbers is",a)
elif ch==4:
  a=div(a,b)
  print("Division of two numbers is",a)
else:
  print("Wrong Operator entered.")
  print("Thanks.")
  
