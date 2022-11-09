b = int(input("Podaj liczbe dodatnia:"))
a = 1
c = 0
licznikliczb = 0
if b > 0:
    while (a + c) <= b:
        a = a + c
        c = c +1
        a = a + 1
        licznikliczb = licznikliczb + 1
print("Liczba liczb których suma jest mniejsza niż",b,"to",licznikliczb)
