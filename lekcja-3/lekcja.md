# Instrukcje warunkowe - cz. 1.
Instrukcje warunkowe służą do dynamicznego podejmowania decyzji przez program.
Używamy ich, gdy jego zachowanie nie może być określone podczas pisania kodu i
jest uzależnione danych wejściowych, np. od tekstu wpisanego przez użytkownika
czy informacji pobranych z internetu.

## If, else, elif
Instrukcje warunkowe w Pythonie wyglądają następująco:
```python
if warunek:
    # kod, który wykona się, jeśli warunek jest prawdziwy

if warunek:
    # kod...
else:
    # kod, który wykona się, jeśli warunek jest fałszywy

if warunek1:
    # kod, który wykona się, jeśli warunek1 jest prawdziwy
elif warunek2:
    # kod, który wykona się, jeśli warunek1 JEST NIEPRAWDZIWY i warunek2 jest prawdziwy
else:
    # kod, który wykona się, jeśli żaden z warunków nie jest prawdziwy

# kod niezależny od instrukcji warunkowych
```

## Porównywanie zmiennych
Zmienne w Python mogą być porównane przez następujące znaki:
* `>`
* `>=` - większe lub równe
* `<`
* `<=` - mniejsze lub równe
* `==` - równe (nie mylić z `=`)
* `!=` - nierówne

```python
x = 10
y = 5

if x == y:
    print("Liczby są równe.")
else:
    print("Liczby są nierówne")

str1 = "napis 1"
str2 = "napis 2"

if str1 != str2:
    print("Napisy są różne.")
    print(str1)
    print(str2)
```
