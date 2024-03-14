user_password = input("Enter a password here: ")
user_password_lenght = len(user_password)

if user_password_lenght > 10 and user_password_lenght < 20:
  print("password create with sucess")
else: 
  print("try again") 

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

try:
  num1 = int(num1)
  num2 = int(num2)
  print(num1 + num2)
except: 
  print("Error")

