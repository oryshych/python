from art import logo
from replit import clear

def add (n1, n2):
  """adding n1 + n2"""
  return n1 + n2

def subtraction (n1, n2):
  """subtraction n1 - n2"""
  return n1 - n2

def multiply (n1, n2):
  """multiplication n1 * n2"""
  return n1 * n2

def division (n1, n2):
  """division n1 / n2"""
  return n1 / n2

# Var_1
calc_new = True
while calc_new is True:
  print (logo)

  calc_continue = True

  n1 = float(input("What is the first number? "))

  print ("+\n-\n*\n/\n")

  while calc_continue is True:

    operation = input("Pick an operation: ")
    n2 = float(input("What is the next number? "))

    if operation == "+":
      result = add(n1, n2)
    elif operation == "-":
      result = subtraction(n1, n2)
    elif operation == "*":
      result = multiply (n1, n2)
    elif operation == "/":
      result = division (n1, n2)

    print (f"{n1} {operation} {n2} = {result}")

    new_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.\n ")
    if new_calc == "y":
      calc_continue = True
      n1 = result
    else:
      calc_continue = False
      clear() 
  calc_new = True
# End Var_1

# Var_2
# operations = {
#   "+" : add,
#   "-" : subtraction,
#   "*" : multiply,
#   "/" : division
# }

# def calculator():
#   print (logo)

#   num1 = float(input("What is the first number? "))
#   for symbols in operations:
#     print (symbols)

#   calc_continue = True  
#   while calc_continue is True:
#     operation = input("Pick an operation: ")
#     num2 = float(input("What is the next number? "))
#     operation_function = operations[operation]
#     result = operation_function (num1, num2)

#     print (f"{num1} {operation} {num2} = {result}")

#     if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.\n ") == "y":
#       calc_continue = True
#       num1 = result
#     else:
#       calc_continue = False
#       clear()
#       calculator()

# calculator()
# End Var_2