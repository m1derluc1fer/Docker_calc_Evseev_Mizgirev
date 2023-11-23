import requests

url_add = 'http://localhost:5000/add'
url_sub = 'http://localhost:5000/subtract'
url_mul = 'http://localhost:5000/multiply'
url_div = 'http://localhost:5000/divide'

while True:
    print('Введите выражение в виде: [число1] [+,-,*,/] [число2]')
    while True:
        num1, op, num2 = input().split()


        if op == '+':
            url = url_add
            break
        elif op == '-':
            url = url_sub
            break
        elif op == '*':
            url = url_mul
            break
        elif op == '/':
            url = url_div
            break
        else:
            print('Операция введена наверно.')
            print('Повторите попытку ввода: [число1] [+,-,*,/] [число2]')

    data = {
        'num1': int(num1),
        'num2': int(num2)
    }

    response = requests.post(url, json=data)
    print(response.json())
    if 'y' != input('Повторить вычисления? [y/n]: '):
        break
