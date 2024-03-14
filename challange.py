# name = input("Enter your name: ")

# name = len(name)

# if name <= 4:
#   print("Your name is too short")
# elif name <= 6:
#   print("Your name is above to 5 and smaller to 6")
# else:
#   print("Your name is too long")
  
# ##
  
# time = input("what time is it? ")
# time = int(time)

# if time >= 0 and time <= 11:
#   print("Good Morning!")
# elif time >= 12 and time <= 17:
#   print("Good Afternoon")
# elif time >= 18 and time <= 23:
#   print("Good night")



def OddOrEven():
  try:
    number = input("Enter a integer number: ")
    number = int(number)
    number_even = number % 2
    if number_even == 0:
      print(f"{number} is even")
    else:
      print(f"{number} is odd")
  except:
    return OddOrEven()
  
OddOrEven()