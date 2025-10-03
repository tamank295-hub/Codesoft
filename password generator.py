import string
import random
str1 = list(string.ascii_lowercase)
str2 = list(string.ascii_uppercase)
str3 = list(string.digits)
str4 = list(string.punctuation)

all_characters = str1 + str2 + str3 + str4

pass_lenght = int(input("enter your password length"))

password = ''.join(random.sample(all_characters,pass_lenght))

print("Your generated password is:",password)