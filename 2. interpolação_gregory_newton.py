def calcular_diferencas_finitas(y):
    n = len(y)
    tabela = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        tabela[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = tabela[i+1][j-1] - tabela[i][j-1]

    return [tabela[0][j] for j in range(n)]

def fatorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def interpolacao_gregory_newton(x, y, x_alvo):

    h = x[1] - x[0]
    n = len(x)

    # u = (x - x0) / h
    u = (x_alvo - x[0]) / h

    diferencas = calcular_diferencas_finitas(y)

    # Fórmula: y0 + u*Δy0 + u(u-1)/2! * Δ^2y0 + ...
    resultado = diferencas[0]
    u_acumulado = 1.0

    for i in range(1, n):
        u_acumulado *= (u - (i - 1))
        termo = (u_acumulado * diferencas[i]) / fatorial(i)
        resultado += termo

    return resultado

if __name__ == "__main__":
    x_minutos = [10.0, 20.0, 30.0, 40.0]
    y_temperatura = [45.0, 52.0, 60.0, 71.0]
    x_alvo = 25.0

    temperatura_estimada = interpolacao_gregory_newton(x_minutos, y_temperatura, x_alvo)

    print(f"--- Interpolação Gregory-Newton ---")
    print(f"Tempo alvo: {x_alvo} minutos")
    print(f"Temperatura estimada: {temperatura_estimada:.2f} ºC")