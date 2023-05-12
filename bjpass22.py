import random
print('Password Generator')


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters=int(input('How many letter do you want : \n '))
nr_numbers=int(input(f'How many numbers do you want : \n'))
nr_symbols=int(input(f'How many symbols do you want : \n '))

password =[]

#For char in range(nr_letters)
#we are looping through all the letters in the list.. this is for line 16

for char in range(1, nr_letters +1):
    password += random.choice(letters)
#print(password)


#For char in range(nr_numbers)
#we are looping through all the letters in the list.. this is for line 26

for char2 in range (1, nr_numbers +1):
    password += random.choice(numbers)

#print(password)


#For char in range(nr_numbers)
#we are looping through all the letters in the list.. this is for line 34

for char3 in range(1, nr_symbols +1):
    password += random.choice(symbols)
#print(password)

random.shuffle(password)
#print(password)

f_password = ""
for char in password:
    f_password +=char
print(f'your password is {f_password}')