# Define a polynomial ring with lexicographic ordering
R.<x,y,z> = PolynomialRing(QQ, order='lex')

# Define your ideal
I = R.ideal([x^2 + y + z - 1, x + y^2 + z - 1, x + y + z^2 - 1])

# Compute the Gröbner basis (will use lex ordering)
G = I.groebner_basis()
print(G)

# # Sheet 13 Q3
# # Define the polynomial ring with lex ordering
# R.<X3, X2, X1> = PolynomialRing(QQ, order='lex')

# # Define the three polynomials
# f1 = 2*X1 + X2 - 2*X2^2 - X3^2
# f2 = X1 - X2^2 + X3^2
# f3 = X1*X2 - X3^2

# # Create the ideal
# I = R.ideal([f1, f2, f3])

# # Compute the Gröbner basis
# G = I.groebner_basis()

# print(G)

