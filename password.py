import string
import random


password = ''
for i in range(2):
    # select 1 lowercase
    password += random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)
    # select 1 digit
    password += random.choice(string.digits)
    # select 1 punctuation
    password += random.choice(string.punctuation)

    password_gen = list(password)
    # shuffle all characters
    random.shuffle(password_gen)
    password = ''.join(password_gen)
print(password)
