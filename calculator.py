# Calculadora

num1 = int(input('Digite um número: '))
num2 = int(input("DIgite outro número: "))
operator = int(input("Digite uma operação: "))

def calculator(num1, num2, operator):
    if operator == 1:
        return num1 + num2

    elif operator == 2:
        return num1 - num2

    elif operator == 3:
        return num1 * num2

    elif operator == 4:
        return num1 / num2

    else:
        print("Nenhuma operação foi escolhida. Tente novamente")

result = calculator(num1, num2, operator)

print(f'O resultado da operação é: {result}')


