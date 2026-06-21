#Interpolação: Splines Linear e cúbico

# DADOS DO PROBLEMA
x = [0.0, 1.0, 2.0, 3.0]
y = [2.5, 4.5, 3.0, 6.0]

xp = 1.5

# SPLINE LINEAR

def spline_linear(x, y, xp):

    n = len(x)

    for i in range(n - 1):

        if x[i] <= xp <= x[i + 1]:

            h = x[i + 1] - x[i]

            s = (y[i] * (x[i + 1] - xp) +
                 y[i + 1] * (xp - x[i])) / h

            return s

    return None



# SPLINE CÚBICA NATURAL
def spline_cubica_natural(x, y, xp):

    n = len(x)

    # Passo 1: calcular h
    h = [0]*(n-1)

    for i in range(n-1):
        h[i] = x[i+1] - x[i]

    # Montar sistema tridiagonal

    a = [0]*n
    b = [0]*n
    c = [0]*n
    d = [0]*n

    # Condições naturais
    b[0] = 1
    b[n-1] = 1

    for i in range(1, n-1):

        a[i] = h[i-1]

        b[i] = 2*(h[i-1] + h[i])

        c[i] = h[i]

        d[i] = 6 * (
            (y[i+1]-y[i])/h[i]
            -
            (y[i]-y[i-1])/h[i-1]
        )

    # Eliminação de Gauss

    for i in range(1, n):

        m = a[i] / b[i-1]

        b[i] = b[i] - m*c[i-1]

        d[i] = d[i] - m*d[i-1]

    # Substituição retroativa

    M = [0]*n

    M[n-1] = d[n-1] / b[n-1]

    for i in range(n-2, -1, -1):

        M[i] = (d[i] - c[i]*M[i+1]) / b[i]

    # Localizar intervalo

    for i in range(n-1):

        if x[i] <= xp <= x[i+1]:

            hi = h[i]

            A = (x[i+1] - xp)/hi
            B = (xp - x[i])/hi

            S = (
                M[i]*(A**3)*hi**2/6
                +
                M[i+1]*(B**3)*hi**2/6
                +
                (y[i] - M[i]*hi**2/6)*A
                +
                (y[i+1] - M[i+1]*hi**2/6)*B
            )

            return S

    return None


linear = spline_linear(x, y, xp)
cubica = spline_cubica_natural(x, y, xp)

print("Spline Linear =", linear)
print("Spline Cúbica Natural =", cubica)