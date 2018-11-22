# Operacje na zmiennych i ich typy
## Typy zmiennych
Zmienne mogą przechowywać różne typy danych, m. in.:
* `int` - liczba całkowita
* `float` - ułamek dziesiętny
* `string` - napis

## Operacje na zmiennych
Działania matematyczne - `+-*/`:

```python
x = 5
y = 10
z = x + y
print(x * z)

# itp.
```

Połączenie działań i przypisania wartości:

```python
x = 5

# te dwie linijki oznaczają to samo
x = x + 10
x += 10

x -= 5
x *= 5
x /= 5

# podchwytliwe pytanie: co robi kod poniżej?
x =+ 5
```

Łączenie stringów:

```python
str1 = "napis1"
str2 = "napis2"
str3 = str1 + " " + str2

print(str3)
# wypisuje: napis1 napis2

str1 += " "
str1 += str2
print(str1)
# wypisuje: napis1 napis2
```
