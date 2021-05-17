# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1+name2
lower_case_name = combined_name.lower()

#true count
num1 = 0
num1 += lower_case_name.count("t")
num1 += lower_case_name.count("r")
num1 += lower_case_name.count("u")
num1 += lower_case_name.count("e")

#love count 
num2 = 0
num2 += lower_case_name.count("l")
num2 += lower_case_name.count("o")
num2 += lower_case_name.count("v")
num2 += lower_case_name.count("e")

love_score = 0
love_score = int(f"{num1}{num2}")

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
  print(f"our score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}")


