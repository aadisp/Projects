import random
import pyperclip
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen():
    pass_len=12

    nr_letters = random.randint(1,pass_len-4)
    pass_len-=nr_letters
    nr_symbols = random.randint(1,pass_len-2)
    pass_len-=nr_symbols
    nr_numbers = pass_len

    password=""
    pass_list=[random.choice(letters) for num in range(0,nr_letters)]
    pass_list+=[random.choice(symbols) for num in range(0,nr_symbols)]
    pass_list+=[random.choice(numbers) for num in range(0,nr_numbers)]
    for c in pass_list:
        password+=c

    pyperclip.copy(password)

    return password
gen()
