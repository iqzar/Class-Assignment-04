print("Welcome to password generator")

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'

number = input("Amount of passwords generate")
number = int(number)
length = input("Enter length for password")
length = int(length)

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)
