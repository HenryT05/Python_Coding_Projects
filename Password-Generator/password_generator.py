import random
import string

generated = string.ascii_letters + string.digits + string.punctuation

password_length = int(input("How long do you want the password?"))

password_list = []
for i in range(password_length):
    password_list.append(random.choice(generated))

password = ''.join(password_list)

print("Your Generated Password is:",password)