from datetime import date

year = date.today().year

birth_year = input('What year were you born?')

age = year - int(birth_year)

print(f'Your age is {age}!')