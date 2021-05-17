# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# way1
# if year % 4 != 0:
#   print("Not leap")
# elif year % 100 != 0:
#   print("Leap")
# elif year % 400 != 0:
#   print("Not leap")
# else:
#   print("Leap")

#way2
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap")
    else:
      print("Not leap")
  else:
    print("Leap")
else:
  print("Not leap")