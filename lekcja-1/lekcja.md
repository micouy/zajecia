# Lekcja 1 - VS Code, wiersz poleceń i Hello World

## VS Code
VS Code to program służący do **edytowania kodu** naszego programu. Za jego pomocą możemy tworzyć nowe pliki, otwierać istniejące i zapisywać je na komputerze. Działa on **podobnie do Word'a**, ale ma wiele funkcji przydatnych podczas programowania.

Przed uruchomieniem napisanego kodu należy pamiętać o zapisaniu go (w odpowiednim miejscu, jeżeli zapisujemy plik po raz pierwszy). Do zapisywania plików służy skrót `Ctrl + S`, za to żeby "Zapisać plik jako", używamy `Ctrl + Shift + S`. Skróty klawiszowe przyspieszają programowanie i najlepiej jest wyrobić nawyk ich używania już na początku.

## Wiersz poleceń
Wiersz poleceń to program, w którym możemy **wywoływać komendy**, które zostaną wykonane przez komputer. Te komendy są różne dla różnych systemów operacyjnych, ale skupię się na tych, których używa się w systemie Windows. Sam wiersz poleceń możemy uruchomić poprzez naciśnięcie klawisza `Windows`, a następnie wpisanie "cmd".

Każde kolejne polecenie wyprzedza informacja o folderze, w którym znajduje się użytkownik (należy o tym myśleć podobnie, jak gdybyśmy otwierali folder normalnie - możemy wykonać polecenia **"w kontekście" danego folderu**, np. wejść w jeden z **jego** podfolderów, wypisać **jego** zawartość lub uruchomić plik znajdujący się w **nim**). Przykładowy widok po uruchomienia wiersza poleceń:
```
C:\Users\Mikolaj>
```

Kolejne komendy możemy pisać pojedynczo, za każdym razem naciskając `Enter`. Jeżeli zrobimy jakiś błąd, nie możemy go już zmienić i musimy napisać polecenie poprawnie w następnej linijce. W przypadku komend, których będziemy używać, nie ma ryzyka wywołania komend, które spowodują niechciane zmiany na komputerze, jednak podczas pracy z wierszem poleceń zawsze należy być uważnym.

Jeżeli chcemy wywołać komendę kolejny raz, możemy do niej wrócić za pomocą strzałek w górę i w dół, za to jeżeli chcemy podpowiedzi podczas pisania komendy, należy naciskać `Tab` i `Shift + Tab` - w ten sposób możemy pokazać następną i poprzednią podpowiedź.

Komendy wypisane poniżej będę pokazywał na przykładowym dysku.
Do opisania jego struktury użyję takiego zapisu:
```
prywatne\                   <-- folder
├── dokumenty\              <-- folder `dokumenty` jest wewnątrz (jest podfolderem) folderu `prywatne`
│   ├── pusty-folder\
│   ├── dokument1.docx      <-- plik `dokument1.docx` znajduje się wewnątrz folderu `dokumenty`, obok folderu `pusty-folder`
│   └── dokument2.docx
└── haslo.txt
```

Jego struktura jest następująca:
```
C:\
├── zdjecia\
│   ├── ja.png
│   ├── pies.png
│   └── rodzina.png
└── prywatne\
    ├── dokumenty\
    │   ├── pusty-folder\
    │   ├── dokument1.docx
    │   └── dokument2.docx
    └── haslo.txt
```

Polecenia, których będziemy używać często podczas programowania:
* `cd <ścieżka_do_folderu>`, np:
```
C:\prywatne>cd dokumenty
C:\prywatne\dokumenty>
```

```
C:\prywatne>cd dokumenty\pusty-folder
C:\prywatne\dokumenty\pusty-folder>
```

```
C:\prywatne>cd \zdjecia
C:\zdjecia>
```

* `cd ..`, czyli "cofnij się do folderu-rodzica", np:
```
C:\prywatne\dokumenty>cd ..
C:\prywatne>
```

* `dir`, czyli "wypisz pliki z obecnego folderu", np (zapis poglądowy, w rzeczywistości informacje wyglądają nieco inaczej):
```
C:\prywatne\dokumenty>dir

15-11-2018 18:22 <DIR> .
15-11-2018 18:22 <DIR> ..
15-11-2018 18:22 <DIR> pusty-folder
15-11-2018 18:23       dokument1.docx
15-11-2018 18:23       dokument2.docx
```

## Python - Hello World
Aby napisać pierwszy program w Pythonie, należy otworzyć VS, następnie stworzyć nowy plik (poprzez `Plik -> Nowy` lub `Stwórz nowy plik` w menu po otworzeniu VS. Po wprowadzeniu każdej zmiany w pliku należy go zapisać, żeby Python mógł uruchomić kod, który właśnie napisaliśmy.

Nasz pierwszy program będzie wypisywał "Hello world!", a następnie kończył pracę. Żeby to zrobić, musimy napisać następującą rzecz:
```python
print("Hello world!")
```

Należy zwrócić uwagę na cudzysłowy wokół "Hello world!" - informują one, że tekst między nimi nie należy traktować jak kod, lecz jako sekwencję znaków. Później musimy go zapisać - ja użyję nazwy `hello-world.py`.

Aby go uruchomić, należy owtorzyć wiersz poleceń, przejść do folderu, w którym zapisany jest plik, a następnie wywołać następującą komendę:
```
C:\folder-w-ktorym-jest-kod>python hello-world.py
```

W wierszu poleceń pojawi się "Hello world!", a następnie powróci on do zwykłej pracy (wyświetli się linijka `C:\...`).
