#Write your code below this line ๐
def prime_checker(number):
  count = []
  for i in range(2, n):
    modul = (n % i)
    count.append(modul)
  if 0 in count:
    print("It's NOT prime number.")
  else:
    print("It's a prime number.")
#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)