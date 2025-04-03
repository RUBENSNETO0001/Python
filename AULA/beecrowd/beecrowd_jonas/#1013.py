num1 = int(input())
num2 = int(input())
num3 = int(input())

def verificador(a, b, c):
    if a > b and a > c: print(f'{num1} eh o maior')
    elif b > a and b > c: print(f'{num2} eh o maior')
    elif c > a and c > b: print(f'{num3} eh o maior')
verificador(num1, num2, num3)