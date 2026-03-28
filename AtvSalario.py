# Recebe o bruto anual e devolve no final um cenário deduzido de alíquotas de imposto de renda simplificado.
try:
    salarioB = int(input("Digite o seu salário bruto: "))
    if salarioB <= 2000:
        salarioL = salarioB - (salarioB * 0.10)
        res = (f"O salário líquido deste salário é de: {salarioL:.2f}")
    elif salarioB > 2000:
        salarioL = salarioB - (salarioB * 0.15)
        res = (f"O salário líquido deste salário é de: {salarioL:.2f}")
    print(res)
except ValueError:
    print("O valor tem que ser numérico, Tente novamente!")