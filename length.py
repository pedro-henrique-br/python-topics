user_password = input("Enter a password here: ")
user_password_lenght = len(user_password)

if user_password_lenght > 10 and user_password_lenght < 20:
  print("password create with sucess")
else: 
  print("try again") 