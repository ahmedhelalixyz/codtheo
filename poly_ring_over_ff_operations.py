# Simple Polynomial Ring Operations over Finite Fields
# Change the field by modifying the GF() parameter below

# Define the field (change GF(2) to GF(p) for other prime fields, or GF(p^k) for extensions)
F = GF(2)  # Change this line to work in different fields
print(f"Working in {F}")

# Define the polynomial ring
R.<x> = PolynomialRing(F)

# Define polynomials here - modify as needed
p1 = (x^2 + 1) * (x^6 + x^5 + x^4 + x^3 +x + 1)
p2 = (x^3 + x^2 + x) * (x^5 + x^3 + x^2 + x) 

print("Polynomial 1:", p1)
print("Polynomial 2:", p2)
print()

# Multiplication
product = p1 * p2
print("Product of p1 & p2 =", product)
print()

# Addition
summation = p1 + p2
print("Sum of p1 & p2 =", summation)
print()

# You can also expand products manually if needed
print("Expanded form:")
expanded = expand(p1 * p2)
print("Expanded =", expanded)
print()
