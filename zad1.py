A = [[1,2,3],[4,5,6]]
listaprzejsciowa = []
liczbakolumn = len(A)
liczbawierszy = len(A[0])
for element in A:
    for j in element:
        listaprzejsciowa.append(j)
At = []
for i in range(liczbawierszy):
    At.append([] * liczbawierszy)
licznik = 0
liczba = 0
for element in At:
    liczba = 0
    dodatek = 0
    for i in range(liczbakolumn):
        element.append(listaprzejsciowa[liczba + licznik])
        liczba = liczba + liczbawierszy
    licznik = licznik + 1
for l in At:
    print(l)
