def quadratura_gauss(funcao, a, b, n_pontos):
    
    # Mapeamento do intervalo [a,b] para o intervalo padrão [-1, 1] de Gauss
    jacobiano = (b - a) / 2.0
    meio = (b + a) / 2.0
    
    # Definindo as raízes (t) e pesos (w) dependendo do número de pontos
    if n_pontos == 2:
        # Raízes = ±1/√3
        t = [-(1/3)**0.5, (1/3)**0.5]
        w = [1.0, 1.0]
    elif n_pontos == 3:
        # Raízes = ±√(3/5) e 0
        t = [-(3/5)**0.5, 0.0, (3/5)**0.5]
        w = [5/9, 8/9, 5/9]
    else:
        raise ValueError("Esta implementação só suporta n_pontos 2 ou 3.")
        
    soma = 0.0
    
    
    for i in range(n_pontos):
        # Calcula o 'x' real correspondente ao 't' da tabela
        x = jacobiano * t[i] + meio
        
        # Acumula o valor na soma
        soma += w[i] * funcao(x)
        
    # Retorna o valor final ajustado pelo Jacobiano
    return jacobiano * soma

# Função do torque do motor: f(x) = 5x³ + x² - 12x + 4
def torque(x):
    return 5*(x**3) + (x**2) - 12*x + 4

# Parâmetros
limite_inferior = -1.0
limite_superior = 1.0
pontos = 2

# Calcula o trabalho total
trabalho_total = quadratura_gauss(torque, limite_inferior, limite_superior, pontos)

print("-" * 50)
print("CÁLCULO DE TRABALHO (QUADRATURA DE GAUSS)")
print("-" * 50)
print(f"Trabalho total calculado (n=2): {trabalho_total:.4f}")
print("-" * 50)