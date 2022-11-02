pierwsze = []
for liczba in range(2,100):
    czy_pierwsza = True
    for i in pierwsze:
        if liczba % i == 0:
            czy_pierwsza = False
    if czy_pierwsza:
        pierwsze.append(liczba)
x = int(input("Podaj dodatnia liczbe naturalna:"))
licznikpierwszych = 0
for pierwsza in pierwsze:
    if pierwsza < x:
        licznikpierwszych = licznikpierwszych + 1
print(licznikpierwszych)