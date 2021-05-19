#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ''
for letter in range(nr_letters):
  letter = random.choice(letters)
  password += letter
for symbol in range(nr_symbols):
  symbol = random.choice(symbols)
  password += symbol
for number in range(nr_numbers):
  number = random.choice(numbers)
  password += number
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []

for letter in range(nr_letters):
  # password_list.append(random.choice(letters))
  password_list += random.choice(letters)
for symbol in range(nr_symbols):
  password_list += random.choice(symbols)
for number in range(nr_numbers):
  password_list += random.choice(numbers)

#test list
# print(password_list) 

random.shuffle(password_list)

#test shuffle list
# print(password_list) 

password = ''
for char in password_list:
  password += char
print(f"Your password is: {password}")