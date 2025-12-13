# Input i Output w Pythonie - Przewodnik

Kompleksowy przewodnik po funkcjach `input()` i `print()` w Pythonie - podstawy, zaawansowane użycie, dobre praktyki i pułapki.

---

## Spis treści

1. [Funkcja print()](#1-funkcja-print)
2. [Funkcja input()](#2-funkcja-input)
3. [Formatowanie output](#3-formatowanie-output)
4. [Walidacja input](#4-walidacja-input)
5. [Dobre praktyki](#5-dobre-praktyki)
6. [Złe praktyki](#6-złe-praktyki)
7. [Pułapki i częste błędy](#7-pułapki-i-częste-błędy)
8. [Zaawansowane techniki](#8-zaawansowane-techniki)

---

## 1. Funkcja print()

### 1.1. Podstawowe użycie

```python
# Najprostsze użycie
print("Hello, World!")

# Wiele argumentów
print("Witaj", "w", "Pythonie")  # Witaj w Pythonie

# Różne typy danych
print(42)
print(3.14)
print(True)
print([1, 2, 3])
```

### 1.2. Parametr `sep` (separator)

```python
# Domyślny separator to spacja
print("a", "b", "c")  # a b c

# Własny separator
print("a", "b", "c", sep="-")  # a-b-c
print("a", "b", "c", sep="")   # abc
print("2024", "01", "15", sep="/")  # 2024/01/15

# Praktyczny przykład - CSV
dane = ["Jan", "Kowalski", "30", "Warszawa"]
print(*dane, sep=",")  # Jan,Kowalski,30,Warszawa
```

### 1.3. Parametr `end` (zakończenie)

```python
# Domyślnie print kończy się znakiem nowej linii \n
print("Linia 1")
print("Linia 2")
# Linia 1
# Linia 2

# Zmiana zakończenia
print("Loading", end="...")
print("Done!")  # Loading...Done!

# Brak nowej linii
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()  # Nowa linia na końcu
```

### 1.4. Parametr `file` (przekierowanie output)

```python
import sys

# Zapis do pliku
with open("output.txt", "w") as f:
    print("To trafi do pliku", file=f)
    print("Również to", file=f)

# Zapis do stderr (błędy)
print("To jest błąd!", file=sys.stderr)

# Zapis do stdout (standardowo)
print("Normalny output", file=sys.stdout)
```

### 1.5. Parametr `flush` (natychmiastowe opróżnienie bufora)

```python
import time

# Bez flush - może czekać na opróżnienie bufora
print("Processing", end="")
time.sleep(2)
print("...Done")

# Z flush - natychmiast wyświetla
print("Processing", end="", flush=True)
time.sleep(2)
print("...Done")

# Przydatne dla pasków postępu
for i in range(10):
    print(".", end="", flush=True)
    time.sleep(0.5)
print()
```

### 1.6. Wyświetlanie specjalnych znaków

```python
# Znaki specjalne
print("Linia 1\nLinia 2")  # Nowa linia
print("Kolumna1\tKolumna2")  # Tab
print("Cytat: \"Python\"")  # Cudzysłów
print("Backslash: \\")  # Backslash
print("Unicode: \u2665")  # ♥

# Raw string - bez interpretacji escape
print(r"C:\Users\nazwa\Documents")  # C:\Users\nazwa\Documents
```

---

## 2. Funkcja input()

### 2.1. Podstawowe użycie

```python
# Proste wczytanie
imie = input("Podaj imię: ")
print(f"Witaj, {imie}!")

# UWAGA: input() ZAWSZE zwraca string!
wiek = input("Podaj wiek: ")
print(type(wiek))  # <class 'str'>
```

### 2.2. Konwersja typów

```python
# Konwersja na int
wiek_str = input("Podaj wiek: ")
wiek = int(wiek_str)
print(f"Za rok będziesz mieć {wiek + 1} lat")

# Krótsza forma
wiek = int(input("Podaj wiek: "))

# Konwersja na float
wzrost = float(input("Podaj wzrost (m): "))
print(f"Twój wzrost: {wzrost}m")

# Lista z wartości rozdzielonych spacją
liczby_str = input("Podaj liczby (oddzielone spacją): ")
liczby = [int(x) for x in liczby_str.split()]
print(f"Suma: {sum(liczby)}")
```

### 2.3. Wieloliniowy input

```python
# Wczytywanie wielu wartości w jednej linii
dane = input("Podaj imię i wiek (oddzielone spacją): ")
imie, wiek = dane.split()
print(f"{imie} ma {wiek} lat")

# Bezpieczniejsza wersja z rozpakowaniem
try:
    imie, wiek = input("Podaj imię i wiek: ").split()
except ValueError:
    print("Błąd: Podaj dokładnie dwie wartości!")

# Wczytywanie do końca inputu (Ctrl+D / Ctrl+Z)
import sys
print("Wpisz tekst (Ctrl+D aby zakończyć):")
wszystkie_linie = sys.stdin.read()
print(f"Wczytano {len(wszystkie_linie)} znaków")
```

### 2.4. Input z domyślną wartością (workaround)

```python
# Python nie ma natywnej domyślnej wartości dla input()
# Workaround:

def input_z_domyslna(prompt, domyslna=""):
    wynik = input(f"{prompt} [{domyslna}]: ")
    return wynik if wynik else domyslna

imie = input_z_domyslna("Podaj imię", "Anonim")
print(f"Witaj, {imie}!")
```

### 2.5. Ukrywanie input (hasła)

```python
import getpass

# Ukrywa wpisywane znaki (dla haseł)
haslo = getpass.getpass("Podaj hasło: ")
print(f"Hasło ma {len(haslo)} znaków")

# Standardowy input dla loginu, ukryty dla hasła
login = input("Login: ")
haslo = getpass.getpass("Hasło: ")
```

---

## 3. Formatowanie output

### 3.1. f-strings (Python 3.6+) - ZALECANE

```python
imie = "Jan"
wiek = 30

# Podstawowe f-string
print(f"Witaj, {imie}!")

# Wyrażenia w f-string
print(f"{imie} ma {wiek} lat i za 5 lat będzie mieć {wiek + 5}")

# Formatowanie liczb
pi = 3.14159265359
print(f"Pi: {pi:.2f}")  # Pi: 3.14
print(f"Pi: {pi:.4f}")  # Pi: 3.1416

# Wyrównywanie
print(f"{'Lewo':<10}|")   # Lewo      |
print(f"{'Prawo':>10}|")  # |     Prawo
print(f"{'Środek':^10}|") # | Środek  |

# Padding zerem
liczba = 42
print(f"{liczba:05}")  # 00042

# Separator tysięcy
suma = 1234567
print(f"{suma:,}")  # 1,234,567
```

### 3.2. format() - Alternatywa

```python
imie = "Jan"
wiek = 30

# Podstawowe użycie
print("Witaj, {}!".format(imie))
print("{} ma {} lat".format(imie, wiek))

# Pozycyjne argumenty
print("{0} ma {1} lat i {0} lubi Pythona".format(imie, wiek))

# Nazwane argumenty
print("{name} ma {age} lat".format(name=imie, age=wiek))

# Formatowanie
print("Pi: {:.2f}".format(3.14159))
```

### 3.3. % operator (stary sposób) - LEGACY

```python
# Nie zalecane w nowym kodzie, ale możesz spotkać w starym
imie = "Jan"
wiek = 30

print("Witaj, %s!" % imie)
print("%s ma %d lat" % (imie, wiek))
print("Pi: %.2f" % 3.14159)
```

### 3.4. Formatowanie tabel

```python
# Proste wyrównanie kolumn
dane = [
    ("Jan", "Kowalski", 30),
    ("Anna", "Nowak", 25),
    ("Piotr", "Wiśniewski", 35)
]

# Nagłówek
print(f"{'Imię':<12} {'Nazwisko':<15} {'Wiek':>5}")
print("-" * 35)

# Dane
for imie, nazwisko, wiek in dane:
    print(f"{imie:<12} {nazwisko:<15} {wiek:>5}")

# Output:
# Imię         Nazwisko        Wiek
# -----------------------------------
# Jan          Kowalski          30
# Anna         Nowak             25
# Piotr        Wiśniewski        35
```

---

## 4. Walidacja input

### 4.1. Podstawowa walidacja

```python
# Sprawdzanie czy input jest liczbą
while True:
    wiek_str = input("Podaj wiek: ")
    if wiek_str.isdigit():
        wiek = int(wiek_str)
        break
    else:
        print("Błąd: Podaj liczbę!")

print(f"Twój wiek: {wiek}")
```

### 4.2. Walidacja z try-except

```python
# Bezpieczna konwersja
while True:
    try:
        wiek = int(input("Podaj wiek: "))
        if wiek < 0:
            print("Wiek nie może być ujemny!")
            continue
        if wiek > 150:
            print("Wiek zbyt duży!")
            continue
        break
    except ValueError:
        print("Błąd: Podaj poprawną liczbę!")

print(f"Twój wiek: {wiek}")
```

### 4.3. Walidacja zakresu

```python
def wczytaj_liczbe(prompt, min_val=None, max_val=None):
    """Wczytuje liczbę z walidacją zakresu"""
    while True:
        try:
            liczba = int(input(prompt))

            if min_val is not None and liczba < min_val:
                print(f"Wartość musi być >= {min_val}")
                continue

            if max_val is not None and liczba > max_val:
                print(f"Wartość musi być <= {max_val}")
                continue

            return liczba
        except ValueError:
            print("Błąd: Podaj poprawną liczbę!")

# Użycie
wiek = wczytaj_liczbe("Podaj wiek (0-150): ", 0, 150)
```

### 4.4. Walidacja wyboru (tak/nie)

```python
def pytaj_tak_nie(prompt):
    """Pyta użytkownika o odpowiedź tak/nie"""
    while True:
        odpowiedz = input(f"{prompt} (t/n): ").lower()
        if odpowiedz in ['t', 'tak', 'yes', 'y']:
            return True
        elif odpowiedz in ['n', 'nie', 'no']:
            return False
        else:
            print("Błąd: Podaj 't' lub 'n'")

# Użycie
czy_kontynuowac = pytaj_tak_nie("Czy chcesz kontynuować?")
if czy_kontynuowac:
    print("Kontynuujemy...")
```

### 4.5. Walidacja email (prosta)

```python
def wczytaj_email():
    """Wczytuje i waliduje email"""
    while True:
        email = input("Podaj email: ").strip()

        if not email:
            print("Email nie może być pusty!")
            continue

        if '@' not in email:
            print("Email musi zawierać @")
            continue

        if '.' not in email.split('@')[1]:
            print("Email musi zawierać domenę z kropką")
            continue

        return email

email = wczytaj_email()
print(f"Email: {email}")
```

---

## 5. Dobre praktyki

### 5.1. Używaj f-strings dla formatowania

```python
# ✅ DOBRZE - f-string (czytelny, szybki)
imie = "Jan"
wiek = 30
print(f"{imie} ma {wiek} lat")

# ❌ UNIKAJ - konkatenacja (nieczytelny)
print(imie + " ma " + str(wiek) + " lat")

# ❌ UNIKAJ - % operator (przestarzały)
print("%s ma %d lat" % (imie, wiek))
```

### 5.2. Zawsze waliduj input użytkownika

```python
# ✅ DOBRZE - walidacja
while True:
    try:
        wiek = int(input("Podaj wiek: "))
        if 0 <= wiek <= 150:
            break
        print("Wiek musi być między 0 a 150")
    except ValueError:
        print("Podaj poprawną liczbę!")

# ❌ ŹLE - brak walidacji
wiek = int(input("Podaj wiek: "))  # Może wyrzucić ValueError!
```

### 5.3. Używaj strip() dla input tekstowego

```python
# ✅ DOBRZE - usuwa białe znaki
imie = input("Podaj imię: ").strip()

# ❌ ŹLE - pozostawia spacje
imie = input("Podaj imię: ")  # "  Jan  " zamiast "Jan"
```

### 5.4. Informuj użytkownika co ma podać

```python
# ✅ DOBRZE - jasny komunikat
wiek = int(input("Podaj swój wiek (liczba całkowita): "))
data = input("Podaj datę urodzenia (RRRR-MM-DD): ")

# ❌ ŹLE - niejasny komunikat
wiek = int(input("Wiek: "))  # Co mam podać?
data = input("Data: ")  # W jakim formacie?
```

### 5.5. Używaj kontekstowych komunikatów błędów

```python
# ✅ DOBRZE - konkretny błąd
try:
    wiek = int(input("Podaj wiek: "))
except ValueError:
    print("Błąd: Wiek musi być liczbą całkowitą!")

# ❌ ŹLE - ogólny błąd
try:
    wiek = int(input("Podaj wiek: "))
except:
    print("Błąd!")  # Jaki błąd?
```

### 5.6. Używaj funkcji pomocniczych dla powtarzalnego kodu

```python
# ✅ DOBRZE - funkcja wielokrotnego użytku
def wczytaj_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            wartosc = int(input(prompt))
            if min_val and wartosc < min_val:
                print(f"Minimum: {min_val}")
                continue
            if max_val and wartosc > max_val:
                print(f"Maksimum: {max_val}")
                continue
            return wartosc
        except ValueError:
            print("Podaj liczbę całkowitą!")

wiek = wczytaj_int("Podaj wiek: ", 0, 150)
ilosc = wczytaj_int("Podaj ilość: ", 1)

# ❌ ŹLE - duplikacja kodu
while True:
    try:
        wiek = int(input("Podaj wiek: "))
        if 0 <= wiek <= 150:
            break
    except ValueError:
        print("Błąd!")

while True:
    try:
        ilosc = int(input("Podaj ilość: "))
        if ilosc >= 1:
            break
    except ValueError:
        print("Błąd!")
```

---

## 6. Złe praktyki

### 6.1. Brak walidacji input

```python
# ❌ ŹLE - założenie że użytkownik zawsze poda poprawne dane
wiek = int(input("Podaj wiek: "))  # Crash gdy użytkownik wpisze "abc"
liczby = [int(x) for x in input("Liczby: ").split()]  # Crash!

# ✅ DOBRZE
try:
    wiek = int(input("Podaj wiek: "))
except ValueError:
    print("Błąd: Podaj liczbę!")
    wiek = 0
```

### 6.2. Używanie eval() na input

```python
# ❌ BARDZO ŹLE - NIEBEZPIECZNE!
wynik = eval(input("Podaj wyrażenie: "))
# Użytkownik może wpisać: __import__('os').system('rm -rf /')

# ✅ DOBRZE - bezpieczne parsowanie
import ast
try:
    wyrazenie = input("Podaj wyrażenie matematyczne: ")
    wynik = ast.literal_eval(wyrazenie)  # Bezpieczniejsze
except:
    print("Niepoprawne wyrażenie")
```

### 6.3. Długie linie print z konkatenacją

```python
# ❌ ŹLE - nieczytelne
print("Użytkownik " + imie + " " + nazwisko + " ma " + str(wiek) + " lat i mieszka w " + miasto)

# ✅ DOBRZE - f-string
print(f"Użytkownik {imie} {nazwisko} ma {wiek} lat i mieszka w {miasto}")
```

### 6.4. Ignorowanie białych znaków

```python
# ❌ ŹLE
haslo = input("Podaj hasło: ")  # "  password  " != "password"

# ✅ DOBRZE
haslo = input("Podaj hasło: ").strip()
```

### 6.5. Złe formatowanie liczb

```python
cena = 1234.5678

# ❌ ŹLE - za dużo miejsc dziesiętnych
print(f"Cena: {cena} PLN")  # Cena: 1234.5678 PLN

# ✅ DOBRZE - odpowiednie formatowanie
print(f"Cena: {cena:.2f} PLN")  # Cena: 1234.57 PLN
print(f"Cena: {cena:,.2f} PLN")  # Cena: 1,234.57 PLN
```

### 6.6. Catch-all exception

```python
# ❌ ŹLE - łapie wszystkie błędy (nawet KeyboardInterrupt)
try:
    wiek = int(input("Wiek: "))
except:
    print("Błąd")

# ✅ DOBRZE - konkretny exception
try:
    wiek = int(input("Wiek: "))
except ValueError:
    print("Błąd: Podaj liczbę")
except KeyboardInterrupt:
    print("\nPrzerwano")
    exit()
```

---

## 7. Pułapki i częste błędy

### 7.1. input() zwraca zawsze string

```python
# ❌ PUŁAPKA
wiek = input("Podaj wiek: ")  # "25" (string!)
if wiek > 18:  # TypeError: '>' not supported between str and int
    print("Pełnoletni")

# ✅ ROZWIĄZANIE
wiek = int(input("Podaj wiek: "))
if wiek > 18:
    print("Pełnoletni")
```

### 7.2. Porównywanie stringów numerycznych

```python
# ❌ PUŁAPKA - porównanie leksykograficzne
liczba1 = input("Liczba 1: ")  # "9"
liczba2 = input("Liczba 2: ")  # "10"
if liczba1 > liczba2:
    print(f"{liczba1} > {liczba2}")  # "9" > "10" leksykograficznie!

# ✅ ROZWIĄZANIE
liczba1 = int(input("Liczba 1: "))
liczba2 = int(input("Liczba 2: "))
if liczba1 > liczba2:
    print(f"{liczba1} > {liczba2}")
```

### 7.3. Puste input

```python
# ❌ PUŁAPKA
imie = input("Podaj imię: ")  # Użytkownik nacisnął tylko Enter
print(f"Witaj, {imie}!")  # Witaj, !

# ✅ ROZWIĄZANIE
while True:
    imie = input("Podaj imię: ").strip()
    if imie:
        break
    print("Imię nie może być puste!")
```

### 7.4. Float precision w output

```python
# ❌ PUŁAPKA
wynik = 0.1 + 0.2
print(f"Wynik: {wynik}")  # Wynik: 0.30000000000000004

# ✅ ROZWIĄZANIE
print(f"Wynik: {wynik:.2f}")  # Wynik: 0.30

# LUB dla finansów - użyj Decimal
from decimal import Decimal
wynik = Decimal('0.1') + Decimal('0.2')
print(f"Wynik: {wynik}")  # Wynik: 0.3
```

### 7.5. Wczytywanie wielu wartości - brak sprawdzenia ilości

```python
# ❌ PUŁAPKA
dane = input("Podaj imię i nazwisko: ").split()
imie = dane[0]
nazwisko = dane[1]  # IndexError gdy użytkownik poda tylko imię!

# ✅ ROZWIĄZANIE 1 - sprawdzenie długości
dane = input("Podaj imię i nazwisko: ").split()
if len(dane) != 2:
    print("Błąd: Podaj dokładnie imię i nazwisko!")
else:
    imie, nazwisko = dane

# ✅ ROZWIĄZANIE 2 - try-except
try:
    imie, nazwisko = input("Podaj imię i nazwisko: ").split()
except ValueError:
    print("Błąd: Podaj dokładnie dwie wartości!")
```

### 7.6. Print z mutable objects

```python
# ❌ PUŁAPKA - modyfikacja po print nie zmienia outputu
lista = [1, 2, 3]
print(f"Lista: {lista}")  # Lista: [1, 2, 3]
lista.append(4)
# Output nie zmienia się - print już wykonany!

# Ale uwaga na to:
lista = [1, 2, 3]
print("Lista:", lista)  # Lista: [1, 2, 3]
lista.append(4)
print("Lista:", lista)  # Lista: [1, 2, 3, 4]
```

### 7.7. Niebezpieczne używanie sep i end

```python
# ❌ PUŁAPKA - zapomnienie o end
for i in range(5):
    print(i, end=" ")
print("Koniec")  # 0 1 2 3 4 Koniec (bez nowej linii przed)

# ✅ ROZWIĄZANIE
for i in range(5):
    print(i, end=" ")
print()  # Nowa linia
print("Koniec")
```

---

## 8. Zaawansowane techniki

### 8.1. Progress bar w konsoli

```python
import time
import sys

def progress_bar(iteracja, total, prefix='', suffix='', length=50):
    """Wyświetla pasek postępu"""
    procent = 100 * (iteracja / float(total))
    filled = int(length * iteracja // total)
    bar = '█' * filled + '-' * (length - filled)
    print(f'\r{prefix} |{bar}| {procent:.1f}% {suffix}', end='', flush=True)
    if iteracja == total:
        print()

# Użycie
items = list(range(100))
for i, item in enumerate(items):
    time.sleep(0.05)
    progress_bar(i + 1, len(items), prefix='Progress:', suffix='Complete')
```

### 8.2. Kolorowy output (ANSI escape codes)

```python
# Kody kolorów ANSI
class Kolory:
    CZERWONY = '\033[91m'
    ZIELONY = '\033[92m'
    ZOLTY = '\033[93m'
    NIEBIESKI = '\033[94m'
    RESET = '\033[0m'

# Użycie
print(f"{Kolory.CZERWONY}To jest czerwone{Kolory.RESET}")
print(f"{Kolory.ZIELONY}To jest zielone{Kolory.RESET}")

# Funkcja pomocnicza
def print_kolor(tekst, kolor):
    print(f"{kolor}{tekst}{Kolory.RESET}")

print_kolor("Sukces!", Kolory.ZIELONY)
print_kolor("Błąd!", Kolory.CZERWONY)
```

### 8.3. Menu interaktywne

```python
def wyswietl_menu():
    """Wyświetla menu i zwraca wybór użytkownika"""
    print("\n=== MENU ===")
    print("1. Opcja 1")
    print("2. Opcja 2")
    print("3. Opcja 3")
    print("0. Wyjście")
    print("============")

    while True:
        try:
            wybor = int(input("Wybierz opcję: "))
            if 0 <= wybor <= 3:
                return wybor
            print("Wybierz opcję 0-3")
        except ValueError:
            print("Podaj liczbę!")

# Użycie
while True:
    wybor = wyswietl_menu()

    if wybor == 0:
        print("Do widzenia!")
        break
    elif wybor == 1:
        print("Wybrano opcję 1")
    elif wybor == 2:
        print("Wybrano opcję 2")
    elif wybor == 3:
        print("Wybrano opcję 3")
```

### 8.4. Wczytywanie do EOF (End of File)

```python
# Wczytywanie wszystkich linii do EOF
print("Wpisz tekst (Ctrl+D lub Ctrl+Z aby zakończyć):")
linie = []
try:
    while True:
        linia = input()
        linie.append(linia)
except EOFError:
    pass

print(f"\nWczytano {len(linie)} linii")
for i, linia in enumerate(linie, 1):
    print(f"{i}: {linia}")
```

### 8.5. Dynamiczne formatowanie tabel

```python
def print_tabela(dane, naglowki):
    """Wyświetla dane w formie tabeli z automatycznym wyrównaniem"""
    # Oblicz szerokości kolumn
    szerokosci = [len(h) for h in naglowki]
    for wiersz in dane:
        for i, komorka in enumerate(wiersz):
            szerokosci[i] = max(szerokosci[i], len(str(komorka)))

    # Separator
    separator = "+" + "+".join(["-" * (s + 2) for s in szerokosci]) + "+"

    # Nagłówek
    print(separator)
    naglowek = "|"
    for h, s in zip(naglowki, szerokosci):
        naglowek += f" {h:<{s}} |"
    print(naglowek)
    print(separator)

    # Dane
    for wiersz in dane:
        linia = "|"
        for komorka, s in zip(wiersz, szerokosci):
            linia += f" {str(komorka):<{s}} |"
        print(linia)
    print(separator)

# Użycie
naglowki = ["Imię", "Nazwisko", "Wiek", "Miasto"]
dane = [
    ["Jan", "Kowalski", 30, "Warszawa"],
    ["Anna", "Nowak", 25, "Kraków"],
    ["Piotr", "Wiśniewski", 35, "Gdańsk"]
]

print_tabela(dane, naglowki)
```

### 8.6. Context manager dla przekierowania output

```python
from contextlib import redirect_stdout
import io

# Przechwytywanie output do zmiennej
f = io.StringIO()
with redirect_stdout(f):
    print("To nie pojawi się na ekranie")
    print("To też nie")

output = f.getvalue()
print(f"Przechwycony output: {output}")

# Przekierowanie do pliku
with open('log.txt', 'w') as f:
    with redirect_stdout(f):
        print("To trafi do pliku")
        print("I to też")
```

---

## 9. Argumenty linii poleceń
### argparse - zalecana metoda

```python
# argparse_example.py
import argparse

parser = argparse.ArgumentParser(description='Prosty przykład argparse')

# Argumenty opcjonalne
parser.add_argument('--name', default='Gość', help='Twoje imię')
parser.add_argument('--age', type=int, help='Twój wiek')

args = parser.parse_args()

print(f"Witaj {args.name}!")
if args.age:
    print(f"Masz {args.age} lat")

# Wywołania:
# python argparse_example.py --name=Adam --age=30
# python argparse_example.py --name Adam --age 30 
# python argparse_example.py --help  # Automatyczna pomoc
```

---

## Podsumowanie - Checklisty

### ✅ Dobre praktyki - DO

- Używaj f-strings do formatowania
- Zawsze waliduj input użytkownika
- Stosuj `.strip()` dla input tekstowego
- Używaj try-except dla konwersji typów
- Podawaj jasne komunikaty (co i jak podać)
- Formatuj liczby odpowiednio (`.2f` dla ceny)
- Twórz funkcje pomocnicze dla powtarzalnego kodu
- Używaj getpass dla haseł
- Informuj o oczekiwanym formacie danych

### ❌ Złe praktyki - DON'T

- Nie używaj eval() na input użytkownika
- Nie zakładaj że input jest poprawny
- Nie używaj konkatenacji stringów zamiast f-strings
- Nie używaj catch-all except
- Nie ignoruj białych znaków w input
- Nie używaj % formatowania w nowym kodzie
- Nie wyświetlaj surowych błędów użytkownikowi
- Nie duplikuj kodu walidacji

### ⚠️ Pułapki - WATCH OUT

- `input()` ZAWSZE zwraca string
- Porównywanie stringów vs liczb ("9" > "10")
- Puste input (tylko Enter)
- Float precision (0.1 + 0.2)
- IndexError przy split() bez sprawdzenia
- Print z end="" bez końcowej nowej linii
- Białe znaki na początku/końcu input
- Konwersja może rzucić ValueError

---



