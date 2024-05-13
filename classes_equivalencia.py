import random

def generate_test_cases(min_value, max_value):
    test_cases = []

    # Adiciona um valor menor que o mínimo
    test_cases.append(random.randint(min_value - 10, min_value - 1))

    # Adiciona um valor dentro do intervalo entre o mínimo e o máximo
    test_cases.append(random.randint(min_value, max_value))

    # Adiciona um valor maior que o máximo
    test_cases.append(random.randint(max_value + 1, max_value + 10))

    return test_cases

# Método para imprimir os casos de teste gerados
def print_test_cases(test_cases, min_val, max_val):
    label_test_case = [f"< {min_val}", f"{min_val} a {max_val}", f"> {max_val}"]
    for i in range(3):
        print(f"Test Case {label_test_case[i]}: {test_cases[i]}")

# Solicita os valores mínimo e máximo ao usuário
min_value = int(input("Digite o valor mínimo: "))
max_value = int(input("Digite o valor máximo: "))

# Gera casos de teste e imprime
test_cases = generate_test_cases(min_value, max_value)
print_test_cases(test_cases, min_value, max_value)
