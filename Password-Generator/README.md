# Password Generator 

A simple command-line password generator built with Python. 
This was my first Python project, built to practice core concepts 
like modules, loops, and user input.

---

## How It Works

The program asks the user how long they want their password, then randomly 
picks characters from a pool of letters, numbers, and symbols to build it.

---

## The Code

```python
import random
import string
```
We import two built-in Python modules. `random` lets us pick random characters,
and `string` gives us pre-built sets of characters to choose from.

```python
generated = string.ascii_letters + string.digits + string.punctuation
```
We build a character pool by combining all letters (a-z, A-Z), digits (0-9), 
and special symbols (!@#$ etc.) into one big string of ~94 possible characters.

```python
password_length = int(input("How long do you want the password? "))
```
We ask the user to enter a number for the password length. `input()` always 
returns text, so we wrap it with `int()` to convert it to a number.

```python
password_list = []
for i in range(password_length):
    password_list.append(random.choice(generated))
```
We create an empty list, then loop once for every character we need. Each 
loop picks one random character from our pool using `random.choice()` and 
adds it to the list.

```python
password = ''.join(password_list)
```
We join the list of individual characters into one single string. The `''` 
means there is no separator between characters.

```python
print("Your Generated Password is:", password)
```
Finally, we print the finished password to the screen.

---
## Full Code
```
import random
import string

generated = string.ascii_letters + string.digits + string.punctuation

password_length = int(input("How long do you want the password?"))

password_list = []
for i in range(password_length):
    password_list.append(random.choice(generated))

password = ''.join(password_list)

print("Your Generated Password is:",password)
```

## Example Output

```
How long do you want the password? 16
Your Generated Password is: kR#9mXq!2Lp$vN@w
```

---

## How to Run

Make sure Python 3 is installed, then run:

```bash
python3 password_generator.py
```

---

## Built With

- Python 3
- `random` module
- `string` module

---

## Author

Henry | University of Washington | Sophomore  
Interests: Cybersecurity, Data Science, GovTech
