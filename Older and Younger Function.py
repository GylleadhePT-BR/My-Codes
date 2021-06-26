from datetime import date

def person(age):
    nasc = currentyear - age
    if age >= 18 :
        print(f'{name} born in {nasc} and have {age} years old ,thats why its older')
    elif age <= 18:
        print(f'{name} born in {nasc} and have {age} years old ,thats why its older')

currentyear = date.today().year
name = str(input('What is your name : '))
person(age = int(input('How years yours old : ')))