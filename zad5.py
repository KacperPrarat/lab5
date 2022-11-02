liczbadodatnia = int(input("Podaj liczbe dodatnia"))
pierwsze = []
suma = 0
licznikliczbpierwszych = 0
for liczba in range(2,liczbadodatnia):
    czy_pierwsza = True
    for i in pierwsze:
        if liczba % i == 0:
            czy_pierwsza = False
    if czy_pierwsza:
        pierwsze.append(liczba)
while suma < liczbadodatnia:
    for liczbapierwsza in pierwsze:
        suma = suma + liczbapierwsza
        licznikliczbpierwszych = licznikliczbpierwszych + 1
print(licznikliczbpierwszych)
