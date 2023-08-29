import random

zahlen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for index in range(10):
    zahlen[index] = random.randrange(1, 101)

summe = 0
for zahl in zahlen:
    summe = summe + zahl
print(zahlen)
print(summe)
# sum-Funktion verwenden
print(sum(zahlen))
