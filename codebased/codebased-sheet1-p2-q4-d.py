# Checking if my calculations are correct for a queston in the sheet

#Define the finite field F_4 = F_2[a]/(a^2 + a + 1)
K.<a> = GF(2**2, name='a', modulus=x^2 + x +  1)

# Display all elements of the field
print("Elements of F_4:")
for i, elem in enumerate(K):
    print("{}: {}".format(i, elem))
print()


# Checking my calculations
print("="*50)
print("My calculations should be...")
print("="*50)
G = matrix(K, 2, 4, [
    [1, 0, a, a+1],
    [0, 1, 1, a]
])
G_T = G.transpose() 
result = G * G_T
print(result)
print()
