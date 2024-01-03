# for adding two numbers 

def add(x,y):
    return x+y

# for subtraction of a number 
def sub(x,y):
    return x-y

# for multiplication of a number
def mul(x,y):
    return x*y

# for division of a number
def div(x,y):
    return x/y

print("select a operation")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

while True:
   choice=input("enter your operation(1/2/3/4): ")
   if choice in('1','2','3','4'):
      try:
         num1=float(input("enter a number one: "))
         num2=float(input("enter a number two: "))
      except ValueError:
         print("please enter a valid input")
         continue
      
      if choice =='1':
         print(num1,"+",num2,"=",add(num1,num2))

      elif choice =='2':
         print(num1,"-",num2,"=",sub(num1,num2))

      elif choice =='3':
         print(num1,"*",num2,"=",mul(num1,num2))

      elif choice =='4':
          print(num1,"/",num2,"=",div(num1,num2))

      next_calculation=input("do you want to do next calculation:yes/no ")
      if next_calculation=="no":
        break
else:
 print("invalid output")
 





