# Define the polynomial ring over F_2
print("Working in F_2[x]")
R.<x> = PolynomialRing(GF(2))

# Define the two polynomials
f = x^6 + x^5 + x^4 + x^3 + x + 1
g = x^5 + x^3 + x^2 + x
print("f(x) =", f)
print("g(x) =", g)
print()

# Calculate GCD
gcd_result = gcd(f, g)
print("gcd(f, g) =", gcd_result)
print()

# Factor the polynomials to see the structure
print("Factorization of f(x):", factor(f))
print("Factorization of g(x):", factor(g))
print("Factorization of gcd:", factor(gcd_result))
print()

# Use extended GCD to find a(x) and b(x) such that gcd = a*f + b*g
gcd_ext, a, b = xgcd(f, g)
print("Extended GCD result:")
print("gcd =", gcd_ext)
print("a(x) =", a)
print("b(x) =", b)
print()

# Verify the extended GCD equation
verification = a*f + b*g
print("Verification: a(x)*f(x) + b(x)*g(x) =", verification)
print("Should equal gcd =", gcd_result)
print("Verification correct:", verification == gcd_result)
print()

# Verify that gcd divides both polynomials
q1, r1 = divmod(f, gcd_result)
q2, r2 = divmod(g, gcd_result)

print("Division check:")
print("f(x) = gcd * (", q1, ") + (", r1, ")")
print("g(x) = gcd * (", q2, ") + (", r2, ")")
print("Remainders should be 0:", r1 == 0 and r2 == 0)
