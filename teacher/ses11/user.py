from api import api

gen = api()
x = input(f'What is {next(gen)}?')
if x == '2':
    x = input(f'What is {next(gen)}?')
if x == '3':
    x = input(f'What is {next(gen)}?')
    

