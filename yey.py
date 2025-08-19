"""
GE 162 - Lab Exercise 1
Part 1.1: Legendre's Polynomials
Author: [Your Name]
"""

import sympy as sp

# Define the variable
t = sp.symbols('t')

# Initialize dictionary for polynomials
P = {}
P[0] = 1      # P0(t) = 1
P[1] = t      # P1(t) = t

# Recurrence formula for n = 2 to 10
for n in range(2, 11):
    P[n] = sp.simplify(
        -((n-1)/n) * P[n-2] + ((2*n-1)/n) * t * P[n-1]
    )

# Print results in nice math form
print("Legendre’s Polynomials Pn(t) from n=2 to n=10:")
for n in range(2, 11):
    print(f"P{n}(t) =", sp.pretty(P[n], use_unicode=True))
