# == > >= < <= !=

# print( 2 == 2)
# print( 2 >= 1)
# print( 3 <= 4)
# print( 3 <= 3)
# print( 4 > 3)
# print( 2 > 3)
# print( 4 != 4)
# print( 4 != 2)
# print( 4 != "2") #int != string
# print( 2 != "2") #int != string
# print("2" != "2") #string != string

limit_age = 18
credit_new_user = "200,00"

age = input(f"Enter your age: ")
user_name = input(f"Enter your name: ")

age = int (age)

if age >= limit_age:
  print(f"Hey {user_name}, welcome to our bank your credit limit is ${credit_new_user}")
else:
  print(f"Hey {user_name} can not have a credit card, until your 18 years")