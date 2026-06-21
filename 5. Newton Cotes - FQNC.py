# Newton-Cotes (FQNC)
def integral_simpson_38_discreto(v, h):
  
    n = len(v) - 1  # Número de intervalos
    
    if n % 3 != 0:
        raise ValueError("O número de intervalos (número de pontos - 1) deve ser múltiplo de 3.")
    
    soma = v[0] + v[-1]
    
    for i in range(1, n):
        if i % 3 == 0:
            soma += 2 * v[i]  # Pontos de junção (múltiplos de 3) multiplicam por 2
        else:
            soma += 3 * v[i]  # Pontos internos multiplicam por 3
            
    # Aplica o coeficiente (3h / 8) no acumulado da soma
    return (3 * h / 8) * soma

# Dados fornecidos pelo monitor de rede:
tempo = [0, 2, 4, 6]
banda_v = [10, 15, 12, 8]
h_constante = 2

# Chamada da função
total_transferido = integral_simpson_38_discreto(banda_v, h_constante)

print("-" * 50)
print(f"O total de dados transferidos foi de: {total_transferido} MB")
print("-" * 50)