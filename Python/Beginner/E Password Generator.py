import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

nr_characters=nr_numbers+nr_letters+nr_symbols
password=""

for num in range(0,nr_letters):
    password+=random.choice(letters)
for num in range(0,nr_symbols):
    password+=random.choice(symbols)
for num in range(0,nr_numbers):
    password+=random.choice(numbers)

print(f"Password 1: {password}")

password=""
passwordList=[]

for num in range(0,nr_letters):
    passwordList.append(random.choice(letters))
for num in range(0,nr_symbols):
    passwordList.append(random.choice(symbols))
for num in range(0,nr_numbers):
    passwordList.append(random.choice(numbers))

random.shuffle(passwordList)
for num in range(len(passwordList)):
    password+=passwordList[num]

print(f"Password 2: {password}")

password=""

for num in range(0,nr_characters):
    if nr_letters!=0 and nr_symbols!=0 and nr_numbers!=0:
        char=random.randint(1,3)
        if char==1:
            password+=random.choice(letters)
            nr_letters-=1
        elif char==2:
            password+=random.choice(symbols)
            nr_symbols-=1
        else:
            password+=random.choice(numbers)
            nr_numbers-=1
    elif nr_letters==0 and nr_symbols!=0 and nr_numbers!=0:
        char = random.randint(1, 2)
        if char == 1:
            password += random.choice(symbols)
            nr_symbols -= 1
        else:
            password += random.choice(numbers)
            nr_numbers -= 1
    elif nr_letters!=0 and nr_symbols==0 and nr_numbers!=0:
        char = random.randint(1, 2)
        if char == 1:
            password += random.choice(letters)
            nr_letters -= 1
        else:
            password += random.choice(numbers)
            nr_numbers -= 1
    elif nr_letters!=0 and nr_symbols!=0 and nr_numbers==0:
        char = random.randint(1, 2)
        if char == 1:
            password += random.choice(letters)
            nr_letters -= 1
        else:
            password += random.choice(symbols)
            nr_symbols -= 1
    elif nr_letters!=0 and nr_symbols==0 and nr_numbers==0:
            password += random.choice(letters)
            nr_letters -= 1
    elif nr_letters==0 and nr_symbols!=0 and nr_numbers==0:
            password += random.choice(symbols)
            nr_symbols -= 1
    elif nr_letters==0 and nr_symbols==0 and nr_numbers!=0:
            password += random.choice(numbers)
            nr_numbers -= 1

print(f"Password 3: {password}")


