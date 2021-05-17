# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#names_list.extend([names])
import random

quantity_names = (len(names) - 1)

choice = random.randint(0, quantity_names)
person_who_pay = names[choice]

print(f"{person_who_pay} is going to by the meal today!")
