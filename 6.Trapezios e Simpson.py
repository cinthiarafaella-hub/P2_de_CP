def integral_trapezio_discreto(v, h):

    # Inicia com a soma dos extremos
    soma = v[0] + v[-1]
    
    # Laço pelos pontos intermediários (multiplicados por 2)
    for i in range(1, len(v) - 1):
        soma += 2 * v[i]
        
    return (h / 2) * soma


def integral_simpson_13_discreto(v, h):
    
    n = len(v) - 1  # Número de intervalos
    
    if n % 2 != 0:
        raise ValueError("Para Simpson 1/3, o número de intervalos precisa ser par.")
        
    soma = v[0] + v[-1]
    
    # Laço pelos pontos intermediários
    for i in range(1, n):
        if i % 2 == 0:
            soma += 2 * v[i] # Índices pares: multiplicam por 2
        else:
            soma += 4 * v[i] # Índices ímpares: multiplicam por 4
            
    return (h / 3) * soma

# Dados do carro elétrico
t = [0.0, 0.5, 1.0, 1.5, 2.0]
v = [0, 40, 65, 80, 90]


h = 0.5 

# Chamando as funções e guardando os resultados
distancia_trapezio = integral_trapezio_discreto(v, h)
distancia_simpson = integral_simpson_13_discreto(v, h)

print("-" * 50)
print("DISTÂNCIA TOTAL PERCORRIDA PELO CARRO ELÉTRICO")
print("-" * 50)
print(f"Método dos Trapézios: {distancia_trapezio:.2f} km")
print(f"Método de Simpson:    {distancia_simpson:.2f} km")
print("-" * 50)