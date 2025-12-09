import datetime

birth_year=int(input('what year were you born:'))
current_year=datetime.datetime.now().year
age=current_year-birth_year
print(f'you are {age} years old')

# second miniproject
firstname=str(input('what is your firstname:'))
secondname=str(input('what is your secondname:'))
surname=str(input('what is your surname:'))
print(f'my name is {firstname} {secondname} {surname}')
print(f'{firstname} {secondname}'.capitalize())
