import secrets
import string

words = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

alphabet = words + numbers + symbols

pwd_chars = int(input("Введіть кількість символів пароля: "))
pwd = ""

for i in range(pwd_chars):
    pwd += ''.join(secrets.choice(alphabet))

print("Згенерований пароль: " + pwd)