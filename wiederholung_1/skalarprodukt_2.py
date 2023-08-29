a = [1, 2, 3]
b = [4, 5, 6]

ergebnis = 0
for index in range(0, len(a)):
    ergebnis = ergebnis + a[index] * b[index]
print(ergebnis)
