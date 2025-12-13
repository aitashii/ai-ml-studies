# Operatory w Pythonie - Przewodnik

Kompletny przewodnik po operatorach w Pythonie - od podstaw do zaawansowanych technik, z przykładami, dobrymi praktykami i pułapkami.

---

## Spis treści

1. [Operatory arytmetyczne](#1-operatory-arytmetyczne)
2. [Operatory porównania](#2-operatory-porównania)
3. [Operatory logiczne](#3-operatory-logiczne)
4. [Operatory przypisania](#4-operatory-przypisania)
5. [Operatory tożsamości](#5-operatory-tożsamości)
6. [Operatory przynależności](#6-operatory-przynależności)
7. [Operatory bitowe](#7-operatory-bitowe)
8. [Pierwszeństwo operatorów](#8-pierwszeństwo-operatorów)
9. [Dobre praktyki](#9-dobre-praktyki)
10. [Złe praktyki](#10-złe-praktyki)
11. [Pułapki i częste błędy](#11-pułapki-i-częste-błędy)

---

## 1. Operatory arytmetyczne

Służą do wykonywania operacji matematycznych.

### 1.1. Dodawanie (+)

```python
# Liczby
x = 10 + 5
print(x)  # 15

y = 3.14 + 2.86
print(y)  # 6.0

# Łączenie stringów
tekst = "Python" + " " + "3"
print(tekst)  # Python 3

# Mieszanie typów - int i float
wynik = 10 + 5.5
print(wynik)  # 15.5
print(type(wynik))  # <class 'float'>
```

### 1.2. Odejmowanie (-)

```python
# Podstawowe odejmowanie
x = 20 - 7
print(x)  # 13

# Liczby ujemne
y = 5 - 10
print(y)  # -5

# Float
z = 10.5 - 3.2
print(z)  # 7.3
```

### 1.3. Mnożenie (*)

```python
# Liczby
x = 6 * 7
print(x)  # 42

# Float
y = 2.5 * 4
print(y)  # 10.0

# Powtarzanie stringa
tekst = "Ha" * 3
print(tekst)  # HaHaHa

powitanie = "Python! " * 5
print(powitanie)  # Python! Python! Python! Python! Python!
```

### 1.4. Dzielenie (/)

```python
# Dzielenie zawsze zwraca float
x = 10 / 2
print(x)  # 5.0
print(type(x))  # <class 'float'>

y = 7 / 2
print(y)  # 3.5

# Dzielenie przez 1
z = 10 / 1
print(z)  # 10.0 (float!)
```

### 1.5. Dzielenie całkowite (//)

```python
# Dzielenie całkowite - obcina część dziesiętną
x = 7 // 2
print(x)  # 3 (nie 3.5)

y = 10 // 3
print(y)  # 3

# Z liczbami ujemnymi - zaokrągla w dół
z = -7 // 2
print(z)  # -4 (nie -3!)

# Z float
a = 7.5 // 2
print(a)  # 3.0 (float, ale bez części dziesiętnej)
```

### 1.6. Modulo - reszta z dzielenia (%)

```python
# Reszta z dzielenia
x = 10 % 3
print(x)  # 1 (10 = 3*3 + 1)

y = 17 % 5
print(y)  # 2

# Sprawdzanie parzystości
liczba = 8
if liczba % 2 == 0:
    print("Parzysta")
else:
    print("Nieparzysta")

# Cykl wartości
for i in range(10):
    dzien = i % 7  # Zawsze 0-6
    print(f"{i} -> dzień {dzien}")
```

### 1.7. Potęgowanie (**)

```python
# Potęga
x = 2 ** 3
print(x)  # 8 (2^3)

y = 5 ** 2
print(y)  # 25

# Pierwiastek (potęga ułamkowa)
pierwiastek = 16 ** 0.5
print(pierwiastek)  # 4.0

# Pierwiastek trzeciego stopnia
pierwiastek3 = 27 ** (1/3)
print(pierwiastek3)  # 3.0

# Potęga ujemna (1/x^n)
z = 2 ** -2
print(z)  # 0.25 (1/4)
```

### 1.8. Negacja (-)

```python
# Zmiana znaku
x = 10
y = -x
print(y)  # -10

# Podwójna negacja
z = --10
print(z)  # 10

liczba = 5
przeciwna = -liczba
print(przeciwna)  # -5
```

---

## 2. Operatory porównania

Zwracają wartości logiczne: `True` lub `False`.

### 2.1. Równość (==)

```python
# Porównanie liczb
print(5 == 5)  # True
print(5 == 3)  # False

# Porównanie stringów
print("Python" == "Python")  # True
print("Python" == "python")  # False (wielkość liter ma znaczenie!)

# Porównanie float i int
print(5.0 == 5)  # True (wartości równe)
print(type(5.0) == type(5))  # False (różne typy!)
```

### 2.2. Nierówność (!=)

```python
# Różne od
print(5 != 3)  # True
print(5 != 5)  # False

# Stringi
print("Python" != "Java")  # True

# Typy
x = 10
y = 10.0
print(x != y)  # False (wartości równe)
```

### 2.3. Większe (>)

```python
print(10 > 5)  # True
print(5 > 10)  # False
print(5 > 5)  # False

# Float
print(3.14 > 3)  # True

# Stringi - porównanie leksykograficzne
print("b" > "a")  # True
print("Python" > "Java")  # True (P > J w alfabecie)
```

### 2.4. Mniejsze (<)

```python
print(5 < 10)  # True
print(10 < 5)  # False
print(5 < 5)  # False

# Liczby ujemne
print(-5 < -3)  # True
print(-10 < 0)  # True
```

### 2.5. Większe lub równe (>=)

```python
print(10 >= 5)  # True
print(5 >= 5)  # True
print(3 >= 5)  # False

# Sprawdzanie zakresu
wiek = 18
if wiek >= 18:
    print("Pełnoletni")
```

### 2.6. Mniejsze lub równe (<=)

```python
print(5 <= 10)  # True
print(5 <= 5)  # True
print(10 <= 5)  # False

# Sprawdzanie przedziału
temperatura = 25
if temperatura <= 30:
    print("Temperatura w normie")
```

### 2.7. Porównania łańcuchowe

```python
# Można łączyć porównania
x = 15
print(10 < x < 20)  # True (x jest między 10 a 20)
print(10 <= x <= 20)  # True

# Zamiast
print(x > 10 and x < 20)  # To samo, ale mniej czytelne

# Więcej porównań
y = 50
print(10 < y < 100 < 1000)  # True
```

---

## 3. Operatory logiczne

Łączą warunki logiczne.

### 3.1. AND (and)

Zwraca `True` tylko gdy OBA warunki są prawdziwe.

```python
# Tabela prawdy AND
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Przykład praktyczny
wiek = 25
ma_prawo_jazdy = True

if wiek >= 18 and ma_prawo_jazdy:
    print("Może prowadzić samochód")

# Wiele warunków
temperatura = 22
wilgotnosc = 60

if temperatura > 20 and temperatura < 30 and wilgotnosc < 70:
    print("Idealne warunki")
```

### 3.2. OR (or)

Zwraca `True` gdy PRZYNAJMNIEJ JEDEN warunek jest prawdziwy.

```python
# Tabela prawdy OR
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# Przykład praktyczny
jest_weekend = False
jest_urlop = True

if jest_weekend or jest_urlop:
    print("Można odpocząć!")

# Sprawdzanie wielu możliwości
dzien = "sobota"
if dzien == "sobota" or dzien == "niedziela":
    print("Weekend!")
```

### 3.3. NOT (not)

Odwraca wartość logiczną.

```python
# Negacja
print(not True)   # False
print(not False)  # True

# Przykład praktyczny
jest_deszcz = False

if not jest_deszcz:
    print("Można iść na spacer")

# Podwójna negacja
x = True
print(not not x)  # True (ale bez sensu, lepiej samo x)
```

### 3.4. Łączenie operatorów logicznych

```python
# AND ma wyższy priorytet niż OR
a = True
b = False
c = True

print(a or b and c)  # True (interpretowane jako: a or (b and c))
print((a or b) and c)  # True (wymuszamy kolejność nawiasami)

# Złożone warunki
wiek = 20
student = True
ma_znizke = False

if (wiek < 26 and student) or ma_znizke:
    print("Przysługuje zniżka")
```

### 3.5. Short-circuit evaluation

```python
# AND - jeśli pierwszy False, drugi nie jest sprawdzany
def funkcja1():
    print("Funkcja 1 wywołana")
    return False

def funkcja2():
    print("Funkcja 2 wywołana")
    return True

print("=== AND ===")
wynik = funkcja1() and funkcja2()
# Wypisze tylko: Funkcja 1 wywołana
# funkcja2() nie zostanie wywołana bo funkcja1() zwróciła False

print("\n=== OR ===")
wynik = funkcja2() or funkcja1()
# Wypisze tylko: Funkcja 2 wywołana
# funkcja1() nie zostanie wywołana bo funkcja2() zwróciła True
```

---

## 4. Operatory przypisania

Przypisują wartości do zmiennych.

### 4.1. Podstawowe przypisanie (=)

```python
# Proste przypisanie
x = 10
imie = "Jan"
czy_aktywny = True

# Wielokrotne przypisanie
a = b = c = 0
print(a, b, c)  # 0 0 0

# Przypisanie wielu wartości (rozpakowanie)
x, y = 5, 10
print(x)  # 5
print(y)  # 10

# Zamiana wartości
a = 3
b = 7
a, b = b, a  # Zamiana bez zmiennej tymczasowej
print(a, b)  # 7 3
```

### 4.2. Dodaj i przypisz (+=)

```python
# Zamiast x = x + 5
x = 10
x += 5
print(x)  # 15

# Równoważne
y = 10
y = y + 5
print(y)  # 15

# Ze stringiem
tekst = "Python"
tekst += " 3"
print(tekst)  # Python 3

# Licznik w pętli
suma = 0
for i in range(5):
    suma += i
print(suma)  # 0+1+2+3+4 = 10
```

### 4.3. Odejmij i przypisz (-=)

```python
x = 20
x -= 7
print(x)  # 13

# Odliczanie
licznik = 10
while licznik > 0:
    print(licznik)
    licznik -= 1
# 10, 9, 8, ..., 1
```

### 4.4. Pomnóż i przypisz (*=)

```python
x = 5
x *= 3
print(x)  # 15

# Podwajanie
liczba = 2
liczba *= 2
print(liczba)  # 4

# String
tekst = "Ha"
tekst *= 3
print(tekst)  # HaHaHa
```

### 4.5. Podziel i przypisz (/=)

```python
x = 20
x /= 4
print(x)  # 5.0 (float!)

# Zawsze zwraca float
y = 10
y /= 2
print(y)  # 5.0 (nie 5)
print(type(y))  # <class 'float'>
```

### 4.6. Dzielenie całkowite i przypisz (//=)

```python
x = 17
x //= 5
print(x)  # 3

# Zmniejszanie o połowę (całkowitą)
liczba = 100
liczba //= 2
print(liczba)  # 50
```

### 4.7. Modulo i przypisz (%=)

```python
x = 17
x %= 5
print(x)  # 2

# Ograniczanie do zakresu
liczba = 25
liczba %= 10
print(liczba)  # 5 (zawsze 0-9)
```

### 4.8. Potęgowanie i przypisz (**=)

```python
x = 2
x **= 3
print(x)  # 8 (2^3)

# Podwójna wartość przez potęgę
podstawa = 3
podstawa **= 2
print(podstawa)  # 9
```

---

## 5. Operatory tożsamości

Sprawdzają czy obiekty są TYM SAMYM obiektem w pamięci.

### 5.1. is

```python
# is sprawdza tożsamość (ten sam obiekt), nie wartość
a = 10
b = 10
print(a is b)  # True (małe liczby są cache'owane)

# Większe liczby
x = 1000
y = 1000
print(x is y)  # False (różne obiekty)
print(x == y)  # True (ale wartości równe!)

# None - zawsze używaj 'is'
wartosc = None
print(wartosc is None)  # True - POPRAWNIE

# Stringi
s1 = "Python"
s2 = "Python"
print(s1 is s2)  # True (stringi są internowane)
```

### 5.2. is not

```python
x = 10
y = 20
print(x is not y)  # True (różne obiekty)

# Z None
wartosc = 5
if wartosc is not None:
    print("Wartość istnieje")

# Różnica is vs ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True (te same wartości)
print(a is b)   # False (różne obiekty w pamięci)
```

### 5.3. Kiedy używać is vs ==

```python
# ✅ DOBRZE - is dla None
x = None
if x is None:
    print("x to None")

# ❌ ŹLE - == dla None (działa, ale nieidiomatyczne)
if x == None:
    print("x to None")

# ✅ DOBRZE - == dla wartości
a = 10
b = 10
if a == b:
    print("Wartości równe")

# ❌ ŹLE - is dla wartości (może nie działać)
x = 1000
y = 1000
if x is y:  # Może być False mimo równych wartości!
    print("To może nie zadziałać")
```

---

## 6. Operatory przynależności

Sprawdzają czy element należy do sekwencji.

### 6.1. in

```python
# W stringu
print("Py" in "Python")  # True
print("Java" in "Python")  # False

# Sprawdzanie podciągu
email = "user@example.com"
if "@" in email:
    print("Email zawiera @")

# Sprawdzanie wielu znaków
tekst = "Hello World"
if "World" in tekst:
    print("Znaleziono 'World'")

# Liczby w stringu
numer = "12345"
if "3" in numer:
    print("Zawiera cyfrę 3")
```

### 6.2. not in

```python
# Brak w stringu
print("x" not in "Python")  # True
print("y" not in "Python")  # False

# Walidacja
haslo = "secret123"
if " " not in haslo:
    print("Hasło nie zawiera spacji - OK")

# Sprawdzanie zakazanych znaków
nazwa_pliku = "dokument.txt"
zakazane = "/*?<>|"
jest_poprawny = True

for znak in zakazane:
    if znak in nazwa_pliku:
        jest_poprawny = False
        break

if jest_poprawny:
    print("Nazwa pliku poprawna")
```

---

## 7. Operatory bitowe

Operacje na bitach liczb całkowitych.

### 7.1. AND bitowe (&)

```python
# Iloczyn bitowy
a = 12  # 1100 w binarnym
b = 10  # 1010 w binarnym
print(a & b)  # 8 (1000 w binarnym)

# Sprawdzanie parzystości (szybsze niż %)
liczba = 7
if liczba & 1:
    print("Nieparzysta")
else:
    print("Parzysta")
```

### 7.2. OR bitowe (|)

```python
# Suma bitowa
a = 12  # 1100
b = 10  # 1010
print(a | b)  # 14 (1110)

# Ustawianie bitów
flagi = 0
flagi = flagi | 1  # Ustaw bit 0
flagi = flagi | 2  # Ustaw bit 1
print(flagi)  # 3 (0011)
```

### 7.3. XOR bitowe (^)

```python
# XOR - różne bity dają 1
a = 12  # 1100
b = 10  # 1010
print(a ^ b)  # 6 (0110)

# Zamiana wartości bez trzeciej zmiennej
x = 5
y = 10
x = x ^ y
y = x ^ y
x = x ^ y
print(x, y)  # 10 5
```

### 7.4. NOT bitowe (~)

```python
# Negacja bitowa (zwraca -(n+1))
a = 5
print(~a)  # -6

# 5 = 0101
# ~5 = 1010 (w reprezentacji U2 to -6)
```

### 7.5. Przesunięcie w lewo (<<)

```python
# Przesunięcie bitowe w lewo (mnożenie przez 2^n)
a = 5  # 0101
print(a << 1)  # 10 (1010) - mnożenie przez 2
print(a << 2)  # 20 (10100) - mnożenie przez 4

# Szybkie mnożenie przez potęgi 2
liczba = 3
wynik = liczba << 3  # 3 * 2^3 = 3 * 8 = 24
print(wynik)  # 24
```

### 7.6. Przesunięcie w prawo (>>)

```python
# Przesunięcie bitowe w prawo (dzielenie przez 2^n)
a = 20  # 10100
print(a >> 1)  # 10 (01010) - dzielenie przez 2
print(a >> 2)  # 5 (00101) - dzielenie przez 4

# Szybkie dzielenie całkowite przez potęgi 2
liczba = 32
wynik = liczba >> 3  # 32 / 2^3 = 32 / 8 = 4
print(wynik)  # 4
```

---

## 8. Pierwszeństwo operatorów

Kolejność wykonywania operacji (od najwyższego do najniższego).

### 8.1. Tabela pierwszeństwa

```
1. ()                   - Nawiasy
2. **                   - Potęgowanie
3. +x, -x, ~x          - Plus jednoargumentowy, minus, NOT bitowe
4. *, /, //, %         - Mnożenie, dzielenie
5. +, -                - Dodawanie, odejmowanie
6. <<, >>              - Przesunięcia bitowe
7. &                   - AND bitowe
8. ^                   - XOR bitowe
9. |                   - OR bitowe
10. ==, !=, <, >, <=, >=, is, is not, in, not in  - Porównania
11. not                - NOT logiczne
12. and                - AND logiczne
13. or                 - OR logiczne
14. =, +=, -=, etc.    - Przypisania
```

### 8.2. Przykłady pierwszeństwa

```python
# Potęgowanie przed mnożeniem
wynik = 2 + 3 * 4
print(wynik)  # 14 (nie 20!) - najpierw 3*4, potem +2

# Potęgowanie
wynik = 2 ** 3 ** 2
print(wynik)  # 512 (nie 64!) - od prawej: 3^2=9, potem 2^9=512

# Nawiasy zmieniają kolejność
wynik = (2 + 3) * 4
print(wynik)  # 20

# Porównania i logiczne
wynik = 5 > 3 and 10 < 20
print(wynik)  # True - najpierw porównania, potem and

# Złożone wyrażenie
a = 10
b = 5
c = 2
wynik = a + b * c
print(wynik)  # 20 (nie 30!) - 5*2=10, potem 10+10=20
```

### 8.3. Używanie nawiasów dla czytelności

```python
# ❌ Niejasne
wynik = a + b * c / d - e

# ✅ Jasne
wynik = a + ((b * c) / d) - e

# Nawet gdy nawiasy nie są potrzebne, pomagają w czytelności
if (wiek >= 18) and (ma_dowod or ma_paszport):
    print("Może wejść")
```

---

## 9. Dobre praktyki

### 9.1. Używaj nawiasów dla czytelności

```python
# ❌ ŹLE - niejasne
if a and b or c and d:
    pass

# ✅ DOBRZE - jasne intencje
if (a and b) or (c and d):
    pass
```

### 9.2. Porównania z None używaj 'is'

```python
x = None

# ❌ ŹLE
if x == None:
    pass

# ✅ DOBRZE
if x is None:
    pass
```

### 9.3. Używaj operatorów przypisania

```python
# ❌ ŹLE - rozwlekłe
licznik = licznik + 1
suma = suma + wartość

# ✅ DOBRZE - zwięzłe
licznik += 1
suma += wartość
```

### 9.4. Porównania łańcuchowe

```python
x = 15

# ❌ ŹLE
if x > 10 and x < 20:
    pass

# ✅ DOBRZE - czytelniejsze
if 10 < x < 20:
    pass
```

### 9.5. Unikaj zbędnych porównań do True/False

```python
jest_aktywny = True

# ❌ ŹLE
if jest_aktywny == True:
    pass

# ✅ DOBRZE
if jest_aktywny:
    pass

# ❌ ŹLE
if jest_aktywny == False:
    pass

# ✅ DOBRZE
if not jest_aktywny:
    pass
```

### 9.6. Używaj `/` dla dzielenia rzeczywistego, `//` dla całkowitego

```python
# ✅ DOBRZE - jasne intencje
srednia = suma / ilosc  # Dzielenie rzeczywiste
polowa = liczba // 2    # Dzielenie całkowite

# ❌ ŹLE - niejasne
wynik = int(suma / ilosc)  # Lepiej użyć //
```

### 9.7. Formatowanie dla czytelności

```python
# ❌ ŹLE - gęsto
wynik=a+b*c-d/e

# ✅ DOBRZE - spacje wokół operatorów
wynik = a + b * c - d / e

# ✅ DOBRZE - grupowanie
wynik = (a + b) * (c - d) / e
```

---

## 10. Złe praktyki

### 10.1. Wielokrotne przypisanie dla różnych wartości

```python
# ❌ ŹLE - mylące
x = y = 0
x += 5
print(x, y)  # 5 0 - y nie zmienione!

# ✅ DOBRZE - osobno
x = 0
y = 0
x += 5
```

### 10.2. Porównywanie float bezpośrednio

```python
# ❌ ŹLE - problemy z precyzją
wynik = 0.1 + 0.2
if wynik == 0.3:  # False!
    print("Równe")

# ✅ DOBRZE - tolerancja
import math
if math.isclose(wynik, 0.3):
    print("Równe")

# LUB
if abs(wynik - 0.3) < 1e-9:
    print("Równe")
```

### 10.3. Używanie is do porównywania wartości

```python
# ❌ ŹLE
a = 1000
b = 1000
if a is b:  # Może być False!
    print("Równe")

# ✅ DOBRZE
if a == b:
    print("Równe")
```

### 10.4. Modyfikacja zmiennej w złożonym wyrażeniu

```python
# ❌ ŹLE - nieczytelne i ryzykowne
x = 5
y = (x := x + 1) + x
print(y)  # ?

# ✅ DOBRZE - jasne kroki
x = 5
x = x + 1
y = x + x
print(y)  # 12
```

### 10.5. Łączenie zbyt wielu operatorów

```python
# ❌ ŹLE - nieczytelne
if a and b or c and not d or e and f:
    pass

# ✅ DOBRZE - rozdzielone na zmienne
warunek1 = a and b
warunek2 = c and not d
warunek3 = e and f

if warunek1 or warunek2 or warunek3:
    pass
```

### 10.6. Nadużywanie operatorów bitowych

```python
# ❌ ŹLE - niejasne dla większości
if x & 1:  # Sprawdzanie parzystości
    pass

# ✅ DOBRZE - jasne
if x % 2 == 1:  # Nieparzysta
    pass

# Operatory bitowe tylko gdy faktycznie są potrzebne! (np. impl protokolow sieciowych, dane binarne RGB, kompresje , praca z niskopoziomowych API, optymalizacja wydajnosci (jezeli potrzebna) itd itd) 
# W 90% przypadkow nie sa potrzebne
```

---

## 11. Pułapki i częste błędy

### 11.1. Dzielenie przez zero

```python
# ❌ PUŁAPKA
# print(10 / 0)  # ZeroDivisionError!

# ✅ ROZWIĄZANIE
dzielnik = 0
if dzielnik != 0:
    wynik = 10 / dzielnik
else:
    print("Nie można dzielić przez zero!")
```

### 11.2. Kolejność operatorów

```python
# ❌ PUŁAPKA
wynik = 2 + 3 * 4
print(wynik)  # 14 (może się spodziewać 20)

# ✅ ROZWIĄZANIE - nawiasy
wynik = (2 + 3) * 4
print(wynik)  # 20
```

### 11.3. Float precision

```python
# ❌ PUŁAPKA
print(0.1 + 0.2 == 0.3)  # False!
print(0.1 + 0.2)  # 0.30000000000000004

# ✅ ROZWIĄZANIE
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

### 11.4. Operator modulo z liczbami ujemnymi

```python
# Wynik ma znak dzielnika, nie dzielnej
print(7 % 3)    # 2
print(-7 % 3)   # 2 (nie -2!)
print(7 % -3)   # -2
print(-7 % -3)  # -2

# Python: a % b ma zawsze znak b
```

### 11.5. Dzielenie całkowite z liczbami ujemnymi

```python
# Zaokrągla w dół (w kierunku -∞)
print(7 // 2)   # 3
print(-7 // 2)  # -4 (nie -3!)

# Uwaga na różnicę z int(7/2)
print(int(-7 / 2))  # -3
print(-7 // 2)      # -4
```

### 11.6. Walrus operator (przypisuje i zwraca wartość) (:=) w złych miejscach

```python
= to statement (instrukcja) — tylko przypisuje
:= to expression (wyrażenie) — przypisuje i zwraca wartość

tekst = input("Wpisz tekst: ")
if (n := len(tekst)) > 10:
    print(f"Tekst ma {n} znaków")

# ❌ PUŁAPKA - trudne do debugowania
if (n := len(tekst)) > 10 and (s := tekst.upper()) != "":
    print(n, s)

# ✅ LEPIEJ - jasne kroki
n = len(tekst)
s = tekst.upper()
if n > 10 and s != "":
    print(n, s)
```

### 11.7. Priorytet and vs or

```python
# ❌ PUŁAPKA
a = True
b = False
c = True

# Co to zwróci?
print(a or b and c)  # True (a or (b and c))

# ✅ ROZWIĄZANIE - nawiasy
print((a or b) and c)  # True
print(a or (b and c))  # True
```

### 11.8. Przypisanie vs porównanie

```python
# ❌ BŁĄD w Pythonie (w C to działa!)
x = 10
if x = 5:  # SyntaxError: invalid syntax
    print("...")

# Python chroni przed tym błędem
# W C/C++ to by przypisało 5 do x i zwróciło True

# ✅ POPRAWNIE
if x == 5:
    print("x równe 5")
```

### 11.9. is vs == dla małych liczb

```python
# PUŁAPKA - działa dla małych liczb, nie dla dużych
a = 256
b = 256
print(a is b)  # True (Python cache'uje -5 do 256)

a = 257
b = 257
print(a is b)  # False (większe liczby nie są cache'owane)
print(a == b)  # True

# ZAWSZE używaj == do porównywania wartości!
```

### 11.10. Stringi i + vs +=

```python
# ❌ NIEEFEKTYWNE - tworzy nowe stringi
s = ""
for i in range(1000):
    s = s + str(i)  # Wolne!

# ✅ LEPIEJ - += jest zoptymalizowane
s = ""
for i in range(1000):
    s += str(i)  # Szybsze

# ✅ NAJLEPIEJ - join
s = "".join(str(i) for i in range(1000))  # Najszybsze
```

---

## Podsumowanie - Checklisty

### ✅ Dobre praktyki - DO

- Używaj spacji wokół operatorów dla czytelności
- Stosuj `is` i `is not` dla porównań z `None`
- Używaj operatorów przypisania (`+=`, `-=`, etc.)
- Stosuj porównania łańcuchowe: `10 < x < 20`
- Używaj nawiasów dla czytelności, nawet gdy nie są wymagane
- Stosuj `//` dla dzielenia całkowitego, `/` dla rzeczywistego
- Używaj `math.isclose()` do porównywania float
- Unikaj porównań do `True`/`False` - sprawdzaj wartość bezpośrednio

### ❌ Złe praktyki - DON'T

- Nie używaj `is` do porównywania wartości (tylko dla `None`)
- Nie porównuj float używając `==`
- Nie nadużywaj walrus operator (`:=`)
- Nie łącz zbyt wielu operatorów w jednym wyrażeniu
- Nie używaj operatorów bitowych gdy niepotrzebne
- Nie zapominaj o nawiasach w złożonych wyrażeniach
- Nie używaj wielokrotnego przypisania dla różnych wartości
- Nie modyfikuj zmiennej w złożonym wyrażeniu

### ⚠️ Pułapki - WATCH OUT

- Dzielenie przez zero: `10 / 0` → ZeroDivisionError
- Float precision: `0.1 + 0.2 != 0.3`
- Kolejność operatorów: `2 + 3 * 4 = 14` (nie 20)
- Modulo z ujemnymi: `-7 % 3 = 2` (nie -2)
- `//` z ujemnymi: `-7 // 2 = -4` (nie -3)
- `and` ma wyższy priorytet niż `or`
- `is` vs `==` dla liczb > 256
- Potęgowanie od prawej: `2**3**2 = 512` (nie 64)
- Stringi: `+` nieefektywne w pętli
- Przypisanie (`=`) vs porównanie (`==`)

---

## Tabela operatorów - szybkie odniesienie

| Kategoria | Operatory | Przykład | Wynik |
|-----------|-----------|----------|-------|
| **Arytmetyczne** | `+`, `-`, `*`, `/`, `//`, `%`, `**` | `10 // 3` | `3` |
| **Porównania** | `==`, `!=`, `>`, `<`, `>=`, `<=` | `5 > 3` | `True` |
| **Logiczne** | `and`, `or`, `not` | `True and False` | `False` |
| **Przypisania** | `=`, `+=`, `-=`, `*=`, `/=`, etc. | `x += 5` | - |
| **Tożsamości** | `is`, `is not` | `x is None` | `True/False` |
| **Przynależności** | `in`, `not in` | `'a' in 'abc'` | `True` |
| **Bitowe** | `&`, `|`, `^`, `~`, `<<`, `>>` | `5 & 3` | `1` |

---

**Pamiętaj:** W razie wątpliwości użyj nawiasów - czytelność kodu jest ważniejsza niż zwięzłość!
