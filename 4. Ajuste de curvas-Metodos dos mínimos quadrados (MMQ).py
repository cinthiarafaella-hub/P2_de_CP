#Ajuste de curvas-Metodos dos mínimos quadrados(MMQ)

# DADOS

x = [8, 9, 10, 11, 12]
y = [2.1, 2.8, 3.1, 4.0, 4.8]

n = len(x)

# SOMATÓRIOS

soma_x = 0
soma_y = 0
soma_x2 = 0
soma_xy = 0

for i in range(n):

    soma_x += x[i]
    soma_y += y[i]
    soma_x2 += x[i]**2
    soma_xy += x[i]*y[i]

# MMQ - RETA y = ax + b

a = (n*soma_xy - soma_x*soma_y) / \
    (n*soma_x2 - soma_x**2)

b = (soma_y - a*soma_x) / n

# PREVISÃO PARA x = 13
x_prev = 13

y_prev = a*x_prev + b

# RESULTADOS

print("Coeficiente angular (a) =", a)
print("Coeficiente linear (b) =", b)

print("\nEquação ajustada:")
print(f"P1(x) = {a:.4f}x + {b:.4f}")

print(f"\nPrevisão para x=13:")
print(f"P1(13) = {y_prev:.4f}")