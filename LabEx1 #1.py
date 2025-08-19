import sympy as sp

t = sp.symbols('t')

P = {}
P[0] = 1      # P0(t) = 1
P[1] = t      # P1(t) = t

for n in range(2, 11):
    P[n] = sp.simplify(
        -((n-1)/n) * P[n-2] + ((2*n-1)/n) * t * P[n-1]
    )

print("Legendre’s Polynomials Pn(t) from n=2 to n=10:")
for n in range(2, 11):
    print(f"P{n}(t) = {P[n]}")

    