# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_int = int(age)

age_left_years = 90 - age_int

month_left = age_left_years * 12
week_left = age_left_years * 52
day_left = age_left_years * 365

message = f"You have {day_left} days, {week_left} weeks, and {month_left} month left."
print(message)




