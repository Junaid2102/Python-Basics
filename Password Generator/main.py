import random
name = input("Enter your name: ")
gender = input("Choose your gender(m/f): ")
if gender == 'm':
    print("Mr.{} your password is as under:- ".format(name))
elif gender == 'f':
    print("Ms.{} your password is as under:- ".format(name))
size = 12
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
characters = "{}[]_;*@,#$"
sum = lower + upper + numbers + characters
password = "".join(random.sample(sum,size))
print(password)