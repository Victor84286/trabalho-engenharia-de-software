def generate_boundary_test_cases(min_value, max_value):
    boundary_test_cases = []

    # Caso mínimo
    boundary_test_cases.append(min_value)

    # Caso máximo
    boundary_test_cases.append(max_value)

    # Caso imediatamente abaixo do mínimo
    boundary_test_cases.append(min_value - 1)

    # Caso imediatamente acima do máximo
    boundary_test_cases.append(max_value + 1)

    return boundary_test_cases

# Método para imprimir os casos de teste gerados
def print_test_cases(test_cases, min_val, max_val):
    label_test_case = [f"= {min_val}", f"= {max_val}", f"{min_val} -1", f"{max_val} +1"]
    for i, test_case in enumerate(test_cases):
        print(f"Test Case {label_test_case[i]}: {test_case}")

# Solicita os valores mínimo e máximo ao usuário
min_value = int(input("Digite o valor mínimo: "))
max_value = int(input("Digite o valor máximo: "))

# Gera casos de teste para valores limite e imprime
boundary_test_cases = generate_boundary_test_cases(min_value, max_value)
print_test_cases(boundary_test_cases, min_value, max_value)
