# Wprowadzenie do Pythona

## Czym jest Python?

Python to wysokopoziomowy, wieloparadygmatowy język programowania stworzony przez Guido van Rossuma w 1991 roku. Charakteryzuje się przejrzystą składnią i filozofią kładącą nacisk na czytelność kodu.

## Język interpretowany czy kompilowany?

### Hybrydowy model wykonywania

Python jest często nazywany językiem **interpretowanym**, ale w rzeczywistości wykorzystuje **hybrydowy model**:

1. **Kompilacja do bytecode'u** - kod źródłowy (`.py`) jest najpierw kompilowany do bytecode'u (`.pyc`)
2. **Interpretacja bytecode'u** - bytecode jest następnie wykonywany przez **Python Virtual Machine (PVM)**

```
kod_zrodlowy.py → [kompilator] → bytecode.pyc → [PVM] → wykonanie
```

### Proces działania

- **Bytecode** to niskopoziomowa, niezależna od platformy reprezentacja kodu źródłowego
- **PVM (Python Virtual Machine)** to środowisko wykonawcze, które interpretuje i wykonuje bytecode
- Pliki `.pyc` są przechowywane w katalogu `__pycache__` aby przyspieszyć kolejne uruchomienia

### Przykład: Bytecode w praktyce

Zobaczmy jak prosty kod Pythona wygląda po kompilacji do bytecode'u:

**Kod źródłowy:**
```python
print("Witaj Swiecie")
```

**Reprezentacja bytecode (używając modułu `dis`):**

```python
import dis

def hello():
    print("Witaj Swiecie")

dis.dis(hello)
```

**Wynik - bytecode:**
```
  2           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('Witaj Swiecie')
              4 CALL_FUNCTION            1
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
```

**Wyjaśnienie instrukcji bytecode:**

| Instrukcja | Znaczenie |
|------------|-----------|
| `LOAD_GLOBAL 0 (print)` | Załaduj funkcję `print` z przestrzeni globalnej |
| `LOAD_CONST 1 ('Witaj Swiecie')` | Załaduj stałą tekstową na stos |
| `CALL_FUNCTION 1` | Wywołaj funkcję z 1 argumentem ze stosu |
| `POP_TOP` | Usuń wynik ze stosu (print zwraca None) |
| `LOAD_CONST 0 (None)` | Załaduj None jako wartość zwracaną |
| `RETURN_VALUE` | Zwróć wartość |

**Numery po lewej stronie** (0, 2, 4, 6, 8, 10) to **offset bytecode** - pozycja instrukcji w bajtach.

**Python używa architektury stack-based** - wszystkie operacje działają na stosie:
1. Załaduj funkcję `print` → stos: `[print]`
2. Załaduj string → stos: `[print, "Witaj Swiecie"]`
3. Wywołaj funkcję → pobiera argumenty ze stosu
4. Wynik (None) → zostaje usunięty

### Sprawdź bytecode samodzielnie

```python
# Zapisz to jako hello.py
print("Witaj Swiecie")

# Uruchom w terminalu
python3 -m dis hello.py

# Lub w kodzie
import dis
dis.dis(compile('print("Witaj Swiecie")', '<string>', 'exec'))
```

**Bytecode to instrukcje dla PVM**, podobnie jak assembly jest instrukcjami dla CPU, ale bytecode jest niezależny od platformy.

## Zalety Pythona

### 1. Czytelność i prostota składni
```python
# Python
def powitanie(imie):
    return f"Witaj, {imie}!"
```

### 2. Bogata biblioteka standardowa
- "Batteries included" - mnóstwo gotowych modułów
- Obszerne ekosystemy bibliotek zewnętrznych (NumPy, Django, Flask, pandas)

### 3. Wieloplatformowość
- Kod działa na Windows, Linux, macOS bez modyfikacji

### 4. Szybkość rozwoju
- Mniej kodu = szybsze prototypowanie
- Idealne do MVP (Minimum Viable Product)

### 5. Wsparcie społeczności
- Ogromna społeczność programistów
- Mnóstwo tutoriali, dokumentacji i bibliotek

### 6. Wszechstronność
- Web development (Django, Flask)
- Data Science i ML (pandas, scikit-learn, TensorFlow)
- Automatyzacja i skrypty
- Desktop apps (PyQt, Tkinter)

## Wady Pythona

### 1. Wydajność
- Wolniejszy od języków kompilowanych (C, C++, Rust, Go)
- Nie nadaje się do aplikacji wymagających maksymalnej wydajności

### 2. Problemy z wielowątkowością
- **GIL (Global Interpreter Lock)** ogranicza prawdziwe wielowątkowe przetwarzanie
- Lepiej używać wieloprocesowości zamiast wielowątkowości

### 3. Duże zużycie pamięci
- Większe zużycie RAM niż języki niskopoziomowe

### 4. Nie najlepszy dla aplikacji mobilnych
- Ograniczone wsparcie dla iOS/Android

### 5. Błędy wykrywane w runtime
- Brak kompilacji oznacza, że niektóre błędy ujawniają się dopiero podczas działania programu

## Typowanie dynamiczne

### Czym jest typowanie dynamiczne?

W Pythonie **nie deklarujemy typów zmiennych** - typ jest określany automatycznie podczas wykonania programu (runtime).

```python
# Typowanie dynamiczne w Python
x = 10          # x jest int
x = "tekst"     # teraz x jest str
x = [1, 2, 3]   # teraz x jest list
```

### Cechy typowania dynamicznego:

- **Duck typing**: "Jeśli chodzi jak kaczka i kwacze jak kaczka, to jest kaczką"
- Typ zmiennej może się zmieniać podczas działania programu
- Sprawdzanie typów odbywa się w **czasie wykonania (runtime)**
- Większa elastyczność kodu

### Przykład duck typing:

```python
def dodaj_dlugosc(obj):
    return len(obj)

dodaj_dlugosc("Python")    # 6
dodaj_dlugosc([1, 2, 3])   # 3
dodaj_dlugosc({1, 2, 3})   # 3
```

## Typowanie dynamiczne vs statyczne

| Aspekt | Typowanie dynamiczne (Python) | Typowanie statyczne (Java, C++, TypeScript) |
|--------|------------------------------|---------------------------------------------|
| **Deklaracja typów** | Nie wymagana | Wymagana |
| **Sprawdzanie typów** | Runtime (podczas działania) | Compile-time (podczas kompilacji) |
| **Elastyczność** | Wysoka | Niższa |
| **Szybkość pisania** | Szybsza | Wolniejsza |
| **Bezpieczeństwo** | Mniejsze (błędy w runtime) | Większe (błędy przed uruchomieniem) |
| **Refactoring** | Trudniejszy | Łatwiejszy |
| **Performance** | Wolniejszy | Szybszy |
| **Dokumentacja** | Często potrzebna zewnętrzna | Typy są dokumentacją |

### Przykład porównawczy:

```python
# Python (dynamiczne)
def dodaj(a, b):
    return a + b

wynik = dodaj(5, 3)        # OK: 8
wynik = dodaj("A", "B")    # OK: "AB"
wynik = dodaj(5, "text")   # RuntimeError dopiero tutaj!
```

```java
// Java (statyczne)
public int dodaj(int a, int b) {
    return a + b;
}

int wynik = dodaj(5, 3);        // OK: 8
int wynik = dodaj("A", "B");    // Błąd kompilacji!
int wynik = dodaj(5, "text");   // Błąd kompilacji!
```

## Zalety typowania dynamicznego

1. **Szybsze pisanie kodu** - mniej boilerplate'u
2. **Większa elastyczność** - ta sama funkcja działa z różnymi typami
3. **Łatwiejsze prototypowanie** - szybsze testowanie pomysłów
4. **Duck typing** - polimorfizm bez dziedziczenia

## Wady typowania dynamicznego

1. **Błędy typu w runtime** - problemy wykrywane dopiero podczas działania
2. **Trudniejszy refactoring** - IDE nie zawsze wie, jakiego typu jest zmienna
3. **Mniejsza wydajność** - sprawdzanie typów podczas wykonania
4. **Gorsza dokumentacja** - nie wiadomo, jakiego typu parametrów oczekuje funkcja

## Type hints - rozwiązanie hybrydowe

Od Pythona 3.5 dostępne są **type hints** - opcjonalne adnotacje typów:

```python
def powitanie(imie: str) -> str:
    return f"Witaj, {imie}!"

def dodaj(a: int, b: int) -> int:
    return a + b

liczby: list[int] = [1, 2, 3, 4]
```

Zalety type hints:
- Lepsza dokumentacja kodu
- Wsparcie IDE (autocomplete, podpowiedzi)
- Narzędzia do statycznej analizy (mypy, pyright)
- **Nie wymuszają** typów w runtime (tylko podpowiedzi)

## Alternatywy do tradycyjnych plików źródłowych

### REPL (Read-Eval-Print Loop)

**REPL** to interaktywny interpreter Pythona dostępny bezpośrednio z terminala.

#### Jak uruchomić REPL?

```bash
$ python3
Python 3.11.0
>>> print("Hello, World!")
Hello, World!
>>> x = 10
>>> x * 2
20
>>> exit()
```

#### Zalety REPL:

1. **Natychmiastowa ewaluacja** - widzisz wyniki od razu
2. **Eksperymentowanie** - idealne do testowania fragmentów kodu
3. **Nauka** - świetne do poznawania nowych bibliotek i funkcji
4. **Debugging** - szybkie sprawdzanie wartości i typów
5. **Prototypowanie** - testowanie pomysłów przed zapisem do pliku
6. **Dostęp do dokumentacji** - `help(funkcja)` bezpośrednio w REPL

```python
>>> help(len)
>>> dir(str)  # Lista metod obiektu
>>> type(42)  # Sprawdzenie typu
<class 'int'>
```

#### Wady REPL:

1. **Brak trwałości** - kod ginie po zamknięciu sesji
2. **Trudne w użyciu dla większych programów** - tylko dla małych fragmentów
3. **Brak zarządzania wersjami** - nie można śledzić historii zmian
4. **Ograniczone edytowanie** - trudniejsze poprawianie błędów w długich liniach
5. **Brak współdzielenia** - trudno pokazać kod innym

#### Kiedy używać REPL?

- Szybkie obliczenia matematyczne
- Testowanie składni i funkcji
- Eksploracja nowych bibliotek
- Sprawdzanie dokumentacji (`help()`, `dir()`)
- Debugowanie małych problemów

### Jupyter Notebooks

**Jupyter Notebook** to interaktywne środowisko łączące kod, tekst, wizualizacje i wyniki w jednym dokumencie.

#### Czym są Jupyter Notebooks?

```python
# Komórka 1: Import bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Komórka 2: Obliczenia
dane = np.random.randn(1000)

# Komórka 3: Wizualizacja
plt.hist(dane, bins=30)
plt.show()  # Wykres wyświetla się bezpośrednio w notebooku
```

#### Jak uruchomić Jupyter Notebook?

```bash
# Instalacja
pip install jupyter

# Uruchomienie
jupyter notebook

# Lub Jupyter Lab (nowsza wersja)
pip install jupyterlab
jupyter lab
```

#### Zalety Jupyter Notebooks:

1. **Interaktywność** - wykonywanie kodu komórka po komórce
2. **Wizualizacja inline** - wykresy i obrazy bezpośrednio w dokumencie
3. **Dokumentacja + kod** - Markdown + kod w jednym miejscu
4. **Eksploracja danych** - idealne do data science i analizy
5. **Współdzielenie** - łatwe udostępnianie (.ipynb) lub eksport do HTML/PDF
6. **Edukacja** - świetne do tutoriali i prezentacji
7. **Reproducibility** - krok po kroku analizy danych
8. **Zachowanie stanu** - zmienne pozostają w pamięci między komórkami
9. **Rich output** - HTML, LaTeX, audio, wideo

```markdown
# Analiza danych sprzedaży

## Import danych
```

```python
import pandas as pd
df = pd.read_csv('sprzedaz.csv')
df.head()
```

```markdown
## Wizualizacja
```

```python
df.plot(kind='bar')
```

#### Wady Jupyter Notebooks:

1. **Trudne w kontroli wersji (Git)** - format JSON, dużo metadanych
2. **Niebezpieczny stan globalny** - komórki można uruchamiać w dowolnej kolejności
3. **Nie dla aplikacji produkcyjnych** - tylko do eksploracji i prototypowania
4. **Ukryte zależności** - kolejność wykonania komórek ma znaczenie
5. **Gorsze refaktoryzowanie** - brak pełnego wsparcia IDE
6. **Trudniejsze testowanie** - unit testy nie są naturalne w notebookach
7. **Wydajność** - większe zużycie zasobów niż zwykły Python

#### Kiedy używać Jupyter Notebooks?

- **Data Science i Machine Learning** - analiza, wizualizacja, modelowanie
- **Eksploracja danych** - EDA (Exploratory Data Analysis)
- **Prototypowanie algorytmów** - szybkie testowanie pomysłów
- **Edukacja** - tutoriale, kursy, prezentacje
- **Dokumentacja techniczna** - runnable documentation
- **Raporty** - łączenie analizy z narracją

**Nie używać Jupyter do:**
- Aplikacji produkcyjnych
- Web API i serwisów
- Bibliotek Pythona
- Długoterminowych projektów wymagających CI/CD

### Porównanie: Pliki .py vs REPL vs Jupyter

| Aspekt | Pliki `.py` | REPL | Jupyter Notebooks |
|--------|-------------|------|-------------------|
| **Trwałość** | Tak | Nie | Tak |
| **Kontrola wersji** | Doskonała | Brak | Problematyczna |
| **Interaktywność** | Nie | Tak | Tak |
| **Wizualizacje** | Zewnętrzne | Zewnętrzne | Inline |
| **Dokumentacja** | Komentarze/docstring | Brak | Markdown + kod |
| **Produkcja** | Tak | Nie | Nie |
| **Nauka** | Dobra | Świetna | Świetna |
| **Data Science** | Możliwa | Słaba | Doskonała |
| **Testing** | Łatwe | Trudne | Trudne |
| **IDE Support** | Pełne | Podstawowe | Średnie |

### Google Colab - Jupyter w chmurze

**Google Colab** to darmowa platforma do uruchamiania Jupyter Notebooks w chmurze:

- Darmowe GPU i TPU
- Nie wymaga instalacji
- Integracja z Google Drive
- Idealne do nauki ML/AI

```python
# W Google Colab
from google.colab import drive
drive.mount('/content/drive')
```

## Dodatkowe koncepcje Pythona

### Context Managers

Context managery pozwalają na eleganckie zarządzanie zasobami (pliki, połączenia):

```python
# Automatyczne zamknięcie pliku
with open('plik.txt', 'r') as f:
    zawartosc = f.read()
# Plik jest automatycznie zamknięty po wyjściu z bloku

# Własny context manager
class MojManager:
    def __enter__(self):
        print("Wejście do kontekstu")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Wyjście z kontekstu")

with MojManager() as m:
    print("W środku kontekstu")
```

### Python Virtual Machine (PVM)

- **PVM** to serce Pythona - interpreter bytecode'u
- Różne implementacje: CPython (standardowa), PyPy (szybsza), Jython (Java), IronPython (.NET)
- **CPython** kompiluje do bytecode'u i wykonuje w PVM
- PVM jest przenośny - ten sam bytecode działa na różnych platformach

### Memory Management

- **Automatyczne zarządzanie pamięcią** - garbage collection
- **Reference counting** - zliczanie referencji do obiektów
- **Cyclic garbage collector** - usuwanie cyklicznych referencji

```python
import sys

a = []
sys.getrefcount(a)  # Liczba referencji do obiektu
```

## Podsumowanie

Python to wszechstronny język idealny do:
- Nauki programowania (przejrzysta składnia)
- Szybkiego prototypowania
- Data Science i Machine Learning
- Automatyzacji i skryptów
- Web development

Jednak nie jest najlepszym wyborem do:
- Aplikacji wymagających maksymalnej wydajności
- Aplikacji mobilnych
- Niskopoziomowego programowania systemowego

**Kluczowa zasada Pythona**: "Czytelność ma znaczenie" (Readability counts) - z The Zen of Python

```python
import this  # Wypróbuj w interpreterze Pythona!
```

## Workflow dla różnych scenariuszy

1. **Nauka podstaw** → REPL
2. **Eksploracja danych** → Jupyter Notebook
3. **Prototyp algorytmu** → Jupyter Notebook → refaktor do .py
4. **Aplikacja produkcyjna** → pliki .py + testy + Git
5. **Tutorial/prezentacja** → Jupyter Notebook
6. **Biblioteka** → pliki .py + dokumentacja

---

## Słowa kluczowe w Pythonie (Keywords)

### Czym są słowa kluczowe?

**Słowa kluczowe (keywords)** to **zarezerwowane słowa** w Pythonie, które mają specjalne znaczenie dla interpretera. **Nie można** używać ich jako nazw zmiennych, funkcji, klas czy innych identyfikatorów.

### Lista wszystkich słów kluczowych

Python 3.11+ ma **35 słów kluczowych**. 

```python
import keyword
print(keyword.kwlist)
print(f"Liczba słów kluczowych: {len(keyword.kwlist)}")
```

### Pełna lista słów kluczowych z wyjaśnieniami

#### 1. **Kontrola przepływu programu**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `if` | Instrukcja warunkowa | `if x > 0: print("Dodatnie")` |
| `elif` | Alternatywny warunek (else if) | `elif x == 0: print("Zero")` |
| `else` | Domyślna gałąź warunku | `else: print("Ujemne")` |
| `while` | Pętla z warunkiem | `while x < 10: x += 1` |
| `for` | Pętla iteracyjna | `for i in range(5): print(i)` |
| `break` | Przerwanie pętli | `if x == 5: break` |
| `continue` | Przejście do następnej iteracji | `if x % 2 == 0: continue` |
| `pass` | Pusta instrukcja (placeholder) | `if x > 0: pass` |

**Przykłady:**

```python
# if-elif-else
wiek = 18
if wiek < 18:
    print("Niepełnoletni")
elif wiek == 18:
    print("Właśnie pełnoletni")
else:
    print("Pełnoletni")

# while z break
licznik = 0
while True:
    licznik += 1
    if licznik == 5:
        break
    print(licznik)

# for z continue
for i in range(10):
    if i % 2 == 0:
        continue  # Pomiń parzyste liczby
    print(i)  # Wyświetl tylko nieparzyste

# pass jako placeholder
def funkcja_do_implementacji():
    pass  # Napiszę później
```

#### 2. **Definiowanie struktur**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `def` | Definicja funkcji | `def powitanie(): print("Cześć")` |
| `class` | Definicja klasy | `class Pies: pass` |
| `return` | Zwrócenie wartości z funkcji | `return wynik` |
| `yield` | Zwrócenie wartości z generatora | `yield element` |
| `lambda` | Funkcja anonimowa (jednolinijkowa) | `lambda x: x * 2` |

**Przykłady:**

```python
# def - zwykła funkcja
def dodaj(a, b):
    return a + b

# class - definicja klasy
class Samochod:
    def __init__(self, marka):
        self.marka = marka

# lambda - funkcja anonimowa
pomnoz = lambda x, y: x * y
print(pomnoz(3, 4))  # 12

# yield - generator
def liczby():
    for i in range(5):
        yield i

for n in liczby():
    print(n)  # 0, 1, 2, 3, 4
```

#### 3. **Obsługa wyjątków**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `try` | Początek bloku obsługi wyjątków | `try: plik = open('test.txt')` |
| `except` | Przechwycenie wyjątku | `except FileNotFoundError: print("Brak pliku")` |
| `finally` | Kod wykonywany zawsze (nawet przy wyjątku) | `finally: plik.close()` |
| `raise` | Wywołanie wyjątku | `raise ValueError("Błędna wartość")` |
| `assert` | Sprawdzenie warunku (debugging) | `assert x > 0, "x musi być dodatnie"` |

**Przykłady:**

```python
# try-except-finally
try:
    wynik = 10 / 0
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")
finally:
    print("Ten kod wykona się zawsze")

# raise - wywołanie własnego wyjątku
def sprawdz_wiek(wiek):
    if wiek < 0:
        raise ValueError("Wiek nie może być ujemny")
    return wiek

# assert - sprawdzenie założenia
def pierwiastek(x):
    assert x >= 0, "Liczba musi być nieujemna"
    return x ** 0.5
```

#### 4. **Wartości logiczne i specjalne**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `True` | Wartość logiczna prawda | `is_active = True` |
| `False` | Wartość logiczna fałsz | `is_empty = False` |
| `None` | Brak wartości (null) | `wynik = None` |

**Przykłady:**

```python
# True/False
jest_pelnoletni = True
ma_prawo_jazdy = False

if jest_pelnoletni and not ma_prawo_jazdy:
    print("Może zdawać na prawo jazdy")

# None - brak wartości
def znajdz_uzytkownika(id):
    if id == 1:
        return {"imie": "Jan"}
    return None

uzytkownik = znajdz_uzytkownika(5)
if uzytkownik is None:
    print("Nie znaleziono użytkownika")
```

#### 5. **Operatory logiczne**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `and` | Logiczne AND (i) | `if x > 0 and x < 10:` |
| `or` | Logiczne OR (lub) | `if x == 0 or x == 1:` |
| `not` | Logiczne NOT (negacja) | `if not is_empty:` |

**Przykłady:**

```python
# and - oba warunki muszą być True
wiek = 25
ma_dowod = True
if wiek >= 18 and ma_dowod:
    print("Może wejść do klubu")

# or - przynajmniej jeden warunek True
dzien = "sobota"
if dzien == "sobota" or dzien == "niedziela":
    print("Weekend!")

# not - negacja
jest_pada = False
if not jest_pada:
    print("Można wyjść bez parasola")
```

#### 6. **Przynależność i tożsamość**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `in` | Sprawdzenie czy element jest w kolekcji | `if "a" in lista:` |
| `is` | Sprawdzenie tożsamości obiektów | `if x is None:` |
| `not in` | Sprawdzenie czy elementu NIE MA w kolekcji | `if "x" not in tekst:` |
| `is not` | Sprawdzenie braku tożsamości | `if x is not None:` |

**Przykłady:**

```python
# in - przynależność do kolekcji
owoce = ["jabłko", "banan", "gruszka"]
if "banan" in owoce:
    print("Mamy banany!")

tekst = "Python jest super"
if "Java" not in tekst:
    print("To nie jest o Javie")

# is - tożsamość obiektów (ten sam obiekt w pamięci)
a = [1, 2, 3]
b = a  # b wskazuje na ten sam obiekt co a
c = [1, 2, 3]  # c to nowy obiekt

print(a is b)  # True - ten sam obiekt
print(a is c)  # False - różne obiekty
print(a == c)  # True - ale mają tę samą wartość

# Zawsze używaj 'is' do porównania z None
wynik = None
if wynik is None:
    print("Brak wyniku")
```

#### 7. **Import modułów**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `import` | Import modułu | `import math` |
| `from` | Import konkretnych elementów | `from math import sqrt` |
| `as` | Alias dla modułu/funkcji | `import numpy as np` |

**Przykłady:**

```python
# import - import całego modułu
import math
print(math.pi)
print(math.sqrt(16))

# from - import konkretnych funkcji
from math import pi, sqrt
print(pi)
print(sqrt(25))

# as - alias
import numpy as np  # Skrót np zamiast numpy
import pandas as pd
import matplotlib.pyplot as plt

# Kombinacja from-import-as
from datetime import datetime as dt
teraz = dt.now()
```

#### 8. **Zakresy i zmienne**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `global` | Deklaracja zmiennej globalnej | `global licznik` |
| `nonlocal` | Dostęp do zmiennej z zewnętrznego zakresu | `nonlocal x` |
| `del` | Usunięcie zmiennej/elementu | `del lista[0]` |

**Przykłady:**

```python
# global - modyfikacja zmiennej globalnej
licznik = 0

def zwieksz():
    global licznik  # Bez tego utworzyłoby lokalną zmienną
    licznik += 1

zwieksz()
print(licznik)  # 1

# nonlocal - dostęp do zmiennej z funkcji zewnętrznej
def zewnetrzna():
    x = 10

    def wewnetrzna():
        nonlocal x  # Odniesienie do x z zewnetrzna()
        x += 5

    wewnetrzna()
    print(x)  # 15

zewnetrzna()

# del - usuwanie zmiennych i elementów
lista = [1, 2, 3, 4, 5]
del lista[0]  # Usuwa pierwszy element
print(lista)  # [2, 3, 4, 5]

slownik = {"a": 1, "b": 2}
del slownik["a"]  # Usuwa klucz "a"
```

#### 9. **Context managers**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `with` | Context manager (automatyczne zarządzanie zasobami) | `with open('file.txt') as f:` |

**Przykłady:**

```python
# with - automatyczne zamknięcie pliku
with open('dane.txt', 'r') as plik:
    zawartosc = plik.read()
# Plik jest automatycznie zamknięty po wyjściu z bloku

# Wiele zasobów jednocześnie
with open('in.txt', 'r') as f_in, open('out.txt', 'w') as f_out:
    dane = f_in.read()
    f_out.write(dane.upper())

# Własny context manager
class MojManager:
    def __enter__(self):
        print("Otwarcie zasobu")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Zamknięcie zasobu")

with MojManager() as m:
    print("Używanie zasobu")
```

#### 10. **Funkcje asynchroniczne (async/await)**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `async` | Definicja funkcji asynchronicznej | `async def pobierz_dane():` |
| `await` | Oczekiwanie na wynik operacji asynchronicznej | `wynik = await pobierz()` |

**Przykłady:**

```python
import asyncio

# async/await - programowanie asynchroniczne
async def pobierz_dane(id):
    print(f"Pobieram dane {id}...")
    await asyncio.sleep(1)  # Symulacja operacji I/O
    return f"Dane {id}"

async def main():
    # Równoległe wykonanie
    zadania = [pobierz_dane(i) for i in range(3)]
    wyniki = await asyncio.gather(*zadania)
    print(wyniki)

# Uruchomienie
asyncio.run(main())
```

#### 11. **Soft keywords (Python 3.10+)**

| Słowo kluczowe | Opis | Przykład |
|----------------|------|----------|
| `match` | Pattern matching (switch-case) | `match value:` |
| `case` | Przypadek w pattern matching | `case 1: print("Jeden")` |

**Przykłady:**

```python
# match-case - pattern matching (Python 3.10+)
def opisz_liczbe(n):
    match n:
        case 0:
            return "Zero"
        case 1:
            return "Jeden"
        case -1:
            return "Minus jeden"
        case _:  # Wildcard (default)
            return "Inna liczba"

print(opisz_liczbe(1))  # "Jeden"

# Zaawansowane pattern matching
def opisz_punkt(punkt):
    match punkt:
        case (0, 0):
            return "Początek układu współrzędnych"
        case (0, y):
            return f"Na osi Y: {y}"
        case (x, 0):
            return f"Na osi X: {x}"
        case (x, y):
            return f"Punkt ({x}, {y})"

print(opisz_punkt((0, 5)))  # "Na osi Y: 5"
```

### Sprawdzanie czy słowo jest słowem kluczowym

```python
import keyword

# Sprawdź czy słowo jest słowem kluczowym
print(keyword.iskeyword("for"))    # True
print(keyword.iskeyword("print"))  # False - print to funkcja, nie keyword!

# Lista wszystkich słów kluczowych
print(keyword.kwlist)

# Soft keywords (Python 3.10+)
print(keyword.softkwlist)  # ['match', 'case', '_']
```

### Ważne: Nie używaj słów kluczowych jako nazw!

```python
# ❌ ZŁE - błąd składni
def = 5  # SyntaxError: invalid syntax
class = "Python"  # SyntaxError: invalid syntax
for = [1, 2, 3]  # SyntaxError: invalid syntax

# ✅ DOBRE
def_value = 5
class_name = "Python"
for_loop = [1, 2, 3]
```

### Ewolucja słów kluczowych

Python dodaje nowe słowa kluczowe w nowych wersjach:

| Wersja | Nowe słowa kluczowe |
|--------|---------------------|
| Python 2.6 | `with`, `as` |
| Python 3.0 | `True`, `False`, `None` (stały się słowami kluczowymi) |
| Python 3.5 | `async`, `await` |
| Python 3.10 | `match`, `case` (soft keywords) |

### Podsumowanie

- Python ma **35 słów kluczowych** (Python 3.11+)
- **Nie można** używać ich jako nazw zmiennych, funkcji, klas
- Dzielą się na kategorie: kontrola przepływu, definicje, wyjątki, logika, import, async
- Sprawdź listę: `import keyword; print(keyword.kwlist)`
- Niektóre funkcje wbudowane (jak `print`, `len`, `range`) **NIE SĄ** słowami kluczowymi!
