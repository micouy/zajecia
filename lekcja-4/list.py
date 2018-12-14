### LISTY
# lista - dużo danych tego samego rodzaju
a = [1, 3, 3, 4]
pileczki = [
    (10, 5, "czerwony"),
    (11, 5, "czerwony"),
    (12, 5, "czerwony"),
    (13, 5, "czerwony"),
]

pierwsze_liczby_pierwsze = [2, 3, 5, 7, 11]

### TUPLE
# tuple - "zestaw" danych różnych rodzajów dotyczących jednej rzeczy
# każdy element o konkretnym znaczeniu
t = (1, 2.5, "asdfd")
dane_pileczki = (10, 5, "czerwony")

t1 = (3, 4)

# tupla jednoelementowa
# WAŻNY PRZECINEK PO ELEMENCIE
t2 = (3, )

t = (1, )

# zamiana na listę
# NIE NAZYWAĆ LIST "list"
l = list(t)

### FOR LOOP

# range - zakres od 0 do ilosc_razy
ilosc_razy = 10
zakres = range(ilosc_razy)

for zmienna in range(ilosc_razy):
    print(zmienna)

for pileczka in pileczki:
    print(pileczka)

### INDEXOWANIE - wybieranie n_tego + 1 elementu
pileczka_trzecia = pileczki[2]
print("pileczka trzecia: " + str(pileczka_trzecia))

### WHILE
counter = 10

while counter > 0:
    print(counter)
    counter -= 1


counter = 0

# while True:
#     print(counter)
#     counter += 1

### STOPPING AND SKIPPING

skip_n = 6

for i in range(10):
    if i == 6:
        print("skipping 6")

        continue

    print(i)
