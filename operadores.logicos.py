# And, Or, Not
# In E In

if 8 > 7 and 9 > 8:
  print(True)
else: 
  print(False)


if 8 < 7 or 9 > 8:
  print(True)
else: 
  print(False)


if not 2 > 3:
  print(True)
else: 
  print(False)


if not 4 > 3:
  print(True)
else: 
  print(False)


if "Pe" in "Pedro":
  print("Pedro contém Pe")
else:
  print("não contém")

if "pe" in "Pedro":
  print("Pedro contém Pe")
else:
  print("não contém")

if "pe" not in "Pedro":
  print("Pedro contém Pe")
else:
  print("não contém")


email_input = input("Enter your email: ")
password_input = input("Enter your password: ")

user_email = "@gmail.com"
user_password = "123"

if user_email in email_input and password_input == user_password:
  print("Welcome!")
else:
  print("User or password are invalids")

