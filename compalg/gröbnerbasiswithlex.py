# Define a polynomial ring with lexicographic ordering
R.<x,y,z> = PolynomialRing(QQ, order='lex')

# Define your ideal
I = R.ideal([x^2 + y + z - 1, x + y^2 + z - 1, x + y + z^2 - 1])

# Compute the Gröbner basis (will use lex ordering)
G = I.groebner_basis()
print(G)
