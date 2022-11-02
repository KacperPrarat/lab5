import  random

n = 3
m = 3
a = []
for i in range(n):
    a.append([])
for j in a:
    for k in range(m):
        j.append(random.randint(1,21))


for l in a:
    print(l)
licznik = 0
kolumna = 0
rzad = 0
for c in range(n):
  licznik = licznik +  a[rzad][kolumna]
  rzad = rzad + 1
  kolumna = kolumna +1
print("Suma =",licznik)