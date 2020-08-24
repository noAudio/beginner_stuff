username = input('Type in your username:\n')
password = input('Type in your password:\n')

hidden_password = ''

for i in password:
    hidden_password += '*'

print(f'{username}, your password {hidden_password} is {len(password)} characters long.')