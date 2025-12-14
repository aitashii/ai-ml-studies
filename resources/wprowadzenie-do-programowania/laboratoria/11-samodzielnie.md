Witam,

Trochę się rozkręcamy.

### **Część 1 Funkcje** 

1\. Napisz funkcję, która przyjmuje jako argument liczbę i zwraca jej kwadrat.

2\. Napisz funkcję, która przyjmuje jako argument dwa napisy i zwraca napis, który jest połączeniem tych dwóch napisów z separatorem spacją.

3\. Napisz funkcję, która przyjmuje jako argument listę liczb i zwraca największą liczbę z tej listy.

4\. Napisz funkcję, która przyjmuje jako argument listę liczb i zwraca średnią arytmetyczną tych liczb.

5\. Napisz funkcję, która przyjmuje jako argument liczbę i zwraca listę jej dzielników.

6\. Napisz funkcję, która przyjmuje jako argument liczbę i zwraca wartość logiczną True, jeśli liczba jest liczbą pierwszą, lub False, jeśli nie jest.

7\. Napisz funkcję, która przyjmuje jako argument liczbę i zwraca liczbę Fibonacciego o tym indeksie.

8\. Napisz funkcję, która przyjmuje jako argument napis i zwraca liczbę samogłosek w tym napisie.

9\. Napisz funkcję, która przyjmuje jako argument napis i zwraca napis, który jest anagramem tego napisu.

10\. Napisz funkcję, która przyjmuje jako argument napis i zwraca wartość logiczną True, jeśli napis jest pangramem, czyli zawiera wszystkie litery alfabetu, lub False, jeśli nie jest.

Pewnie zadania niby się powtarzają, ale też na tym polega nauka, powtarzaniu.   
Dla pomocy kilka przykładów:

\# Przykład 1: Aplikacja do obliczania pola i obwodu prostokąta

\# Definicja funkcji do obliczania pola prostokąta

def pole_prostokata(a, b):

  return a \* b

\# Definicja funkcji do obliczania obwodu prostokąta

def obwod_prostokata(a, b):

  return 2 \* (a + b)

\# Przykład użycia funkcji

a = 10 # długość boku a

b = 5 # długość boku b

print(f"Pole prostokąta o bokach {a} i {b} wynosi {pole_prostokata(a, b)}")

print(f"Obwód prostokąta o bokach {a} i {b} wynosi {obwod_prostokata(a, b)}")

\# Przykład 2: Aplikacja do generowania liczb losowych z podanego zakresu

\# Importowanie modułu random

import random

\# Definicja funkcji do generowania liczb losowych

def losowa_liczba(min, max):

  return random.randint(min, max)

\# Przykład użycia funkcji

min = 1 # dolna granica zakresu

max = 100 # górna granica zakresu

print(f"Losowa liczba z zakresu od {min} do {max} to {losowa_liczba(min, max)}")

\# Przykład 3: Aplikacja do sprawdzania, czy podane słowo jest palindromem

\# Definicja funkcji do odwracania słowa

def odwroc_slowo(slowo):

  return slowo\[::-1\]

\# Definicja funkcji do sprawdzania, czy słowo jest palindromem

def czy_palindrom(slowo):

  return slowo == odwroc_slowo(slowo)

\# Przykład użycia funkcji

slowo = "kajak" # przykładowe słowo

if czy_palindrom(slowo):

  print(f"Słowo {slowo} jest palindromem")

else:

  print(f"Słowo {slowo} nie jest palindromem")

\# Przykład 4: Aplikacja do obliczania silni podanej liczby

\# Definicja funkcji do obliczania silni

def silnia(n):

  if n == 0 or n == 1:

    return 1

  else:

    return n \* silnia(n - 1)

\# Przykład użycia funkcji

n = 5 # przykładowa liczba

print(f"Silnia liczby {n} wynosi {silnia(n)}")

\# Przykład 5: Aplikacja do konwersji temperatury z stopni Celsjusza na stopnie Fahrenheita i odwrotnie

\# Definicja funkcji do konwersji z Celsjusza na Fahrenheita

def celsjusz_na_fahrenheit(c):

  return c \* 1.8 + 32

\# Definicja funkcji do konwersji z Fahrenheita na Celsjusza

def fahrenheit_na_celsjusz(f):

  return (f - 32) / 1.8

\# Przykład użycia funkcji

c = 25 # temperatura w stopniach Celsjusza

f = 77 # temperatura w stopniach Fahrenheita

print(f"{c} stopni Celsjusza to {celsjusz_na_fahrenheit(c)} stopni Fahrenheita")

print(f"{f} stopni Fahrenheita to {fahrenheit_na_celsjusz(f)} stopni Celsjusza")

Pomoce dydaktyczne:

(1) Funkcje - Definicja i wywołanie funkcji, przekazywanie argumentów .... <https://chyla.org/artykuly/python/python-tutorial/funkcje.html>.

(2) Funkcje - Learn Python - Free Interactive Python Tutorial. <https://www.learnpython.org/pl/Funkcje>.

(3) Funkcje w Python - [Analityk.edu.pl](http://Analityk.edu.pl). <https://analityk.edu.pl/funkcje-w-python/>.

(4) Tworzenie funkcji w Pythonie. <https://www.algorytm.edu.pl/funkcje-w-python>.

### **Część 2 - Klasy i obiekty:**

Obiety są połączeniem zmiennych i funkcji w jedną strukturalną całość. Obiekty biorą swoje zmienne i funkcje z klas. Klasy są podstawowym schematem, według których tworzone są obiekty.

Poniżej znajduje się bardzo prosty przykład klasy:

```
 class MojaKlasa:
      zmienna = "blah"
      def funkcja(self):
           print "To jest wiadomość wewnątrz klasy."
```

Przykład z [learnpython.org](http://learnpython.org)  
Inaczej można opisać klasy i obiekty jako szablony, które definiują atrybuty i metody wspólne dla pewnej grupy obiektów.  
 są po raz pierwszy a więc zadania są z przykładami. Ale też opisem o co chodzi w tym wszystkim:

Zadanie 1: Zdefiniuj klasę o nazwie `Osoba`, która ma dwa atrybuty: `imie` i `wiek`. Następnie utwórz dwie instancje tej klasy: `osoba1` o imieniu "Anna" i wieku 25 lat oraz `osoba2` o imieniu "Tomasz" i wieku 30 lat. Wypisz na ekranie imię i wiek każdej osoby.

\# Zdefiniuj klasę Osoba

class Osoba:

    \# Zdefiniuj konstruktor klasy, który przyjmuje dwa argumenty: imie i wiek

    def __init__(self, imie, wiek):

        \# Przypisz argumenty do atrybutów klasy

        self.imie = imie

        self.wiek = wiek

\# Utwórz instancję klasy Osoba o imieniu "Anna" i wieku 25 lat

osoba1 = Osoba("Anna", 25)

\# Utwórz instancję klasy Osoba o imieniu "Tomasz" i wieku 30 lat

osoba2 = Osoba("Tomasz", 30)

\# Wypisz na ekranie imię i wiek każdej osoby

print(f"Osoba 1: {osoba1.imie}, {osoba1.wiek} lat")

print(f"Osoba 2: {osoba2.imie}, {osoba2.wiek} lat"

Wyjaśnienie: Aby zdefiniować klasę w Pythonie, używamy słowa kluczowego `class` i nadajemy klasie nazwę. W tym przypadku nazwaliśmy klasę `Osoba`. Następnie zdefiniowaliśmy specjalną metodę o nazwie `__init__`, która jest wywoływana automatycznie, gdy tworzymy nową instancję klasy. Metoda ta przyjmuje argument `self`, który odnosi się do samej instancji, oraz dwa argumenty `imie` i `wiek`, które przekazujemy podczas tworzenia instancji. W ciele metody `__init__` przypisujemy argumenty `imie` i `wiek` do atrybutów klasy, które możemy później odwoływać się za pomocą kropki. Na przykład, `osoba1.imie` zwraca imię pierwszej osoby, a `osoba2.wiek` zwraca wiek drugiej osoby. Aby utworzyć instancję klasy, używamy nazwy klasy i podajemy argumenty w nawiasach. Na przykład, `Osoba("Anna", 25)` tworzy instancję klasy `Osoba` o imieniu "Anna" i wieku 25 lat. Aby wypisać na ekranie imię i wiek każdej osoby, używamy funkcji `print` i łączymy tekst i zmienne za pomocą znaku `f` przed nawiasami i klamr {} wewnątrz nawiasów. Na przykład, `print(f"Osoba 1: {osoba1.imie}, {osoba1.wiek} lat")` wypisuje na ekranie "Osoba 1: Anna, 25 lat".

Zadanie 2: Zmodyfikuj klasę `Osoba` z poprzedniego zadania, dodając do niej metodę `przedstaw_sie`, która wypisuje na ekranie wiadomość w formacie "Cześć, jestem {imie} i mam {wiek} lat". Następnie wywołaj tę metodę dla każdej instancji klasy `Osoba`.

\# Zdefiniuj klasę Osoba

class Osoba:

    \# Zdefiniuj konstruktor klasy, który przyjmuje dwa argumenty: imie i wiek

    def __init__(self, imie, wiek):

        \# Przypisz argumenty do atrybutów klasy

        self.imie = imie

        self.wiek = wiek

    \# Zdefiniuj metodę przedstaw_sie, która wypisuje na ekranie wiadomość w formacie "Cześć, jestem {imie} i mam {wiek} lat"

    def przedstaw_sie(self):

        print(f"Cześć, jestem {self.imie} i mam {self.wiek} lat")

\# Utwórz instancję klasy Osoba o imieniu "Anna" i wieku 25 lat

osoba1 = Osoba("Anna", 25)

\# Utwórz instancję klasy Osoba o imieniu "Tomasz" i wieku 30 lat

osoba2 = Osoba("Tomasz", 30)

\# Wywołaj metodę przedstaw_sie dla każdej osoby

osoba1.przedstaw_sie()

osoba2.przedstaw_sie()

Wyjaśnienie: Aby dodać metodę do klasy, używamy takiej samej składni jak przy definiowaniu funkcji, ale wcięcie metody pod nazwą klasy. W tym przypadku zdefiniowaliśmy metodę `przedstaw_sie`, która przyjmuje argument `self`, który odnosi się do samej instancji, i używa atrybutów `imie` i `wiek` tej instancji, aby wypisać na ekranie wiadomość w formacie "Cześć, jestem {imie} i mam {wiek} lat". Aby wywołać metodę dla instancji klasy, używamy kropki i nazwy metody z nawiasami. Na przykład, `osoba1.przedstaw_sie()` wywołuje metodę `przedstaw_sie` dla instancji `osoba1` i wypisuje na ekranie "Cześć, jestem Anna i mam 25 lat".

Zadanie 3: Zdefiniuj klasę o nazwie `Punkt`, która reprezentuje punkt na płaszczyźnie dwuwymiarowej. Klasa ta ma dwa atrybuty: `x` i `y`, które oznaczają współrzędne punktu. Następnie zdefiniuj metodę `odleglosc_od_zera`, która zwraca odległość punktu od początku układu współrzędnych (0, 0). Użyj twierdzenia Pitagorasa, aby obliczyć odległość: 𝑥2+𝑦2‾‾‾‾‾‾‾√ Następnie utwórz dwie instancje tej klasy: `punkt1` o współrzędnych (3, 4) i `punkt2` o współrzędnych (-5, -12). Wypisz na ekranie odległość każdego punktu od zera.

\# Zaimportuj moduł math, aby użyć funkcji pierwiastka kwadratowego

import math

\# Zdefiniuj klasę Punkt

class Punkt:

    \# Zdefiniuj konstruktor klasy, który przyjmuje dwa argumenty: x i y

    def __init__(self, x, y):

        \# Przypisz argumenty do atrybutów klasy

        self.x = x

        self.y = y

\# Zdefiniuj metodę odleglosc_od_zera, która zwraca odległość punktu od początku układu współrz

Źródła:

- Podstawy języka Python | Przykłady i zadania z rozwiązaniami. <https://zadaniezinformatyki.pl/python-podstawy/>.
- 300+ Ćwiczeń - Programowanie w języku Python - od A do Z. <https://www.udemy.com/course/programowanie-w-jezyku-python-od-a-do-z-cwiczenia/>.
- 1000+ zadań w Pythonie (i każdym innym języku) - ćwiczenia dla .... <https://www.flynerd.pl/2018/06/500-zadan-w-pythonie-i-kazdym-innym-jezyku.html>.