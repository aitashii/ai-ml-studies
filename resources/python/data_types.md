# Typy Danych w Pythonie - Kompletny Przewodnik

## Spis Treści
1. [Wprowadzenie](#wprowadzenie)
2. [Liczby Całkowite (int)](#liczby-całkowite-int)
3. [Liczby Zmiennoprzecinkowe (float)](#liczby-zmiennoprzecinkowe-float)
4. [Ciągi Znaków (str)](#ciągi-znaków-str)
5. [Wartości Logiczne (bool)](#wartości-logiczne-bool)
6. [Typ None](#typ-none)
7. [Konwersja Typów](#konwersja-typów)
8. [Tabela Podsumowująca](#tabela-podsumowująca)

---

## Wprowadzenie

Python posiada kilka wbudowanych typów danych. Ten przewodnik omawia fundamentalne **podstawowe typy danych**:

- **int** - Liczby całkowite
- **float** - Liczby zmiennoprzecinkowe (dziesiętne)
- **str** - Ciągi znaków (tekst)
- **bool** - Wartości logiczne (True/False)
- **NoneType** - Reprezentuje brak wartości (None)

---

## Liczby Całkowite (int)

### Opis
Liczby całkowite to liczby bez części dziesiętnej. Mogą być dodatnie, ujemne lub zero.

### Przykłady
```python
age = 25
year = 2024
temperature = -5
zero = 0
large_number = 1000000
```

### Kluczowe Właściwości
- **Brak limitu rozmiaru**: Liczby całkowite w Pythonie mogą być dowolnie duże
- **Niezmienne**: Po utworzeniu nie można ich zmienić
- **Typ**: `<class 'int'>`

### Powszechne Operacje
```python
# Arytmetyka
10 + 5      # 15 (dodawanie)
10 - 5      # 5 (odejmowanie)
10 * 5      # 50 (mnożenie)
10 / 5      # 2.0 (dzielenie - zwraca float!)
10 // 3     # 3 (dzielenie całkowite - zwraca int)
10 % 3      # 1 (modulo - reszta z dzielenia)
10 ** 2     # 100 (potęgowanie)

# Porównanie
10 == 10    # True
10 > 5      # True
10 < 20     # True
```

### Przydatne Funkcje
```python
abs(-5)         # 5 (wartość bezwzględna)
pow(2, 3)       # 8 (potęga: 2^3)
int("42")       # 42 (konwersja stringa na int)
```

### Uwagi
- Dzielenie (`/`) zawsze zwraca liczbę zmiennoprzecinkową, nawet jeśli oba operandy są całkowite
- Użyj dzielenia całkowitego (`//`) aby otrzymać wynik całkowity
- Dzielenie całkowite obcina w kierunku ujemnej nieskończoności

---

## Liczby Zmiennoprzecinkowe (float)

### Opis
Liczby zmiennoprzecinkowe reprezentują wartości dziesiętne. Są używane do bardziej precyzyjnych obliczeń.

### Przykłady
```python
pi = 3.14159
price = 19.99
temperature = 98.6
scientific = 2.5e3  # Notacja naukowa: 2500.0
negative = -0.5
```

### Kluczowe Właściwości
- **Precyzja dziesiętna**: Około 15-17 cyfr znaczących
- **Niezmienne**: Po utworzeniu nie można ich zmienić
- **Typ**: `<class 'float'>`
- **Notacja naukowa**: Można używać notacji `e` (np. `1e6` = 1000000.0)

### Powszechne Operacje
```python
# Arytmetyka
3.14 + 2.86     # 6.0
10.5 - 3.2      # 7.3
2.5 * 4         # 10.0
7 / 2           # 3.5

# Zaokrąglanie
round(3.14159, 2)    # 3.14 (zaokrąglenie do 2 miejsc po przecinku)
round(3.7)           # 4 (zaokrąglenie do najbliższej liczby całkowitej)
```

### Przydatne Funkcje
```python
float("3.14")      # 3.14 (konwersja stringa na float)
float(42)          # 42.0 (konwersja int na float)
abs(-3.7)          # 3.7 (wartość bezwzględna)
```

### Ważne Uwagi
- **Problemy z precyzją**: `0.1 + 0.2` może nie być dokładnie równe `0.3` z powodu reprezentacji binarnej
- **Porównywanie**: Używaj zaokrąglania przy porównywaniu floatów: `round(0.1 + 0.2, 10) == 0.3`
- Każda operacja arytmetyczna z float zwraca float

### Formatowanie
```python
value = 3.14159
f"{value:.2f}"     # "3.14" (2 miejsca po przecinku)
f"{value:.4f}"     # "3.1416" (4 miejsca po przecinku)
```

---

## Ciągi Znaków (str)

### Opis
Ciągi znaków reprezentują dane tekstowe. Są to sekwencje znaków ujęte w cudzysłów.

### Przykłady
```python
name = "Alice"
message = 'Witaj, Świecie!'
multiline = """To jest
wieloliniowy
ciąg znaków"""
empty = ""
```

### Kluczowe Właściwości
- **Niezmienne**: Nie można zmieniać znaków w miejscu
- **Indeksowane**: Można uzyskać dostęp do poszczególnych znaków
- **Typ**: `<class 'str'>`
- **Cudzysłowy**: Można używać pojedynczych `'`, podwójnych `"` lub potrójnych `"""` cudzysłowów

### Powszechne Operacje
```python
# Konkatenacja (łączenie)
"Witaj" + " " + "Świecie"    # "Witaj Świecie"

# Powtórzenie
"Ha" * 3                     # "HaHaHa"

# Długość
len("Python")                # 6

# Indeksowanie (od 0)
"Python"[0]                  # "P" (pierwszy znak)
"Python"[-1]                 # "n" (ostatni znak)

# Wycinanie (slicing)
"Python"[0:3]                # "Pyt"
"Python"[2:]                 # "thon"
"Python"[:4]                 # "Pyth"
"Python"[::-1]               # "nohtyP" (odwrócony)
```

### Metody Stringów
```python
text = "  Witaj Świecie  "

text.upper()               # "  WITAJ ŚWIECIE  "
text.lower()               # "  witaj świecie  "
text.strip()               # "Witaj Świecie" (usuwa białe znaki)
text.replace("Świecie", "Python")  # "  Witaj Python  "
text.split()               # ["Witaj", "Świecie"]
"Witaj".startswith("Wi")   # True
"Witaj".endswith("aj")     # True
"123".isdigit()            # True
"abc".isalpha()            # True
```

### Sprawdzanie Stringów
```python
"Witaj" in "Witaj Świecie"   # True (sprawdzanie podciągu)
"xyz" in "Witaj"             # False
"Python".find("th")          # 2 (indeks podciągu, -1 jeśli nie znaleziono)
```

### Formatowanie Stringów
```python
name = "Ala"
age = 25

# F-stringi (Python 3.6+)
f"Mam na imię {name}"                   # "Mam na imię Ala"
f"Mam {age} lat"                        # "Mam 25 lat"
f"{3.14159:.2f}"                        # "3.14"

# Metoda .format()
"Mam na imię {}".format(name)           # "Mam na imię Ala"
"Imię: {}, Wiek: {}".format(name, age)  # "Imię: Ala, Wiek: 25"

# Stary styl (%)
"Mam na imię %s" % name                 # "Mam na imię Ala"
```

### Znaki Specjalne
```python
"Linia 1\nLinia 2"         # Nowa linia
"Tab\ttutaj"               # Tabulator
"Powiedział \"Witaj\""     # Cudzysłów w stringu
"C:\\Users\\nazwa"         # Ukośnik wsteczny (wymaga escape)
```

---

## Wartości Logiczne (bool)

### Opis
Wartości logiczne reprezentują wartości prawdy: `True` lub `False` (wielkość liter ma znaczenie).

### Przykłady
```python
is_active = True
is_logged_in = False
has_permission = True
```

### Kluczowe Właściwości
- **Tylko dwie wartości**: `True` i `False`
- **Typ**: `<class 'bool'>`
- **Podklasa int**: `True` jest równoważne `1`, `False` równoważne `0`

### Operatory Logiczne
```python
# Logiczne AND (I)
True and True      # True
True and False     # False
False and False    # False

# Logiczne OR (LUB)
True or False      # True
False or False     # False

# Logiczne NOT (NIE)
not True           # False
not False          # True

# Złożone wyrażenia
(True and False) or (True and True)    # True
```

### Operatory Porównania (zwracają bool)
```python
10 == 10           # True (równe)
10 != 5            # True (różne)
10 > 5             # True (większe niż)
10 < 20            # True (mniejsze niż)
10 >= 10           # True (większe lub równe)
10 <= 10           # True (mniejsze lub równe)
```

### Prawdziwość i Fałszywość
Wartości, które oceniane są jako `False` (fałszywe):
```python
bool(False)        # False
bool(0)            # False
bool(0.0)          # False
bool("")           # False (pusty string)
bool(None)         # False
```

Wartości, które oceniane są jako `True` (prawdziwe):
```python
bool(True)         # True
bool(1)            # True
bool(42)           # True
bool(-1)           # True
bool("Witaj")      # True
bool(" ")          # True (nawet spacja jest prawdziwa)
```

### Boolean w Arytmetyce
```python
True + True        # 2
True * 10          # 10
False * 100        # 0
int(True)          # 1
int(False)         # 0
```

### Użycie w Warunkach
```python
is_adult = age >= 18
can_vote = is_adult and is_citizen

if is_adult:
    print("Jesteś osobą dorosłą")
```

---

## Typ None

### Opis
`None` to specjalna stała reprezentująca brak wartości lub wartość pustą (null).

### Kluczowe Właściwości
- **Pojedyncza wartość**: Istnieje tylko jeden `None`
- **Typ**: `<class 'NoneType'>`
- **Fałszywy**: Oceniany jako `False` w kontekście logicznym

### Powszechne Zastosowania
```python
# 1. Wartość początkowa/domyślna
result = None
username = None

# 2. Funkcja bez wartości zwracanej
def print_hello():
    print("Witaj")
    # Niejawnie zwraca None

# 3. Opcjonalne parametry funkcji
def greet(name, title=None):
    if title is None:
        return f"Witaj, {name}"
    return f"Witaj, {title} {name}"

# 4. Oznaczanie brakujących/niedostępnych danych
user_profile = {
    "name": "Ala",
    "age": 25,
    "phone": None  # Nie podano
}
```

### Sprawdzanie None
```python
value = None

# POPRAWNY sposób - użyj 'is'
if value is None:
    print("Wartość to None")

# Również poprawne - użyj 'is not'
if value is not None:
    print("Wartość istnieje")

# NIEPOPRAWNE - nie używaj '=='
if value == None:  # Działa, ale nie jest zalecane
    print("Wartość to None")
```

### None vs Inne Fałszywe Wartości
```python
None == False      # False
None == 0          # False
None == ""         # False

None is False      # False
None is 0          # False

bool(None)         # False (None jest fałszywy)
```

### Praktyczny Przykład
```python
def divide(a, b):
    if b == 0:
        return None  # Nie można dzielić przez zero
    return a / b

result = divide(10, 0)
if result is None:
    print("Błąd: Dzielenie przez zero!")
```

---

## Konwersja Typów

### Ogólne Informacje
Konwertowanie między różnymi typami danych jest powszechne w Pythonie.

### Na Liczbę Całkowitą (int)
```python
int(3.7)           # 3 (obcina część dziesiętną)
int("42")          # 42
int(True)          # 1
int(False)         # 0
int("3.14")        # BŁĄD! Użyj int(float("3.14"))
```

### Na Liczbę Zmiennoprzecinkową (float)
```python
float(42)          # 42.0
float("3.14")      # 3.14
float(True)        # 1.0
float(False)       # 0.0
```

### Na String (str)
```python
str(42)            # "42"
str(3.14)          # "3.14"
str(True)          # "True"
str(None)          # "None"
```

### Na Boolean (bool)
```python
bool(1)            # True
bool(0)            # False
bool(42)           # True
bool("")           # False
bool("Witaj")      # True
bool(None)         # False
```

### Sprawdzanie Typu
```python
# Używając type()
type(42)                    # <class 'int'>
type(3.14)                  # <class 'float'>
type("Witaj")               # <class 'str'>
type(True)                  # <class 'bool'>

# Używając isinstance()
isinstance(42, int)         # True
isinstance(3.14, float)     # True
isinstance("Cześć", str)    # True
isinstance(True, bool)      # True
isinstance(True, int)       # True (bool jest podklasą int)
```

### Bezpieczna Konwersja
```python
def safe_int(value):
    """Bezpiecznie konwertuje na int, zwraca None jeśli niemożliwe"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

safe_int("42")        # 42
safe_int("witaj")     # None
safe_int(None)        # None
```

---

## Tabela Podsumowująca

| Typ | Przykład | Zmienny | Powszechne Użycie | Wartość Domyślna |
|-----|----------|---------|-------------------|------------------|
| **int** | `42`, `-10`, `0` | Nie | Liczenie, indeksowanie, liczby całkowite | `0` |
| **float** | `3.14`, `-0.5`, `2.5e3` | Nie | Precyzyjne obliczenia, pomiary | `0.0` |
| **str** | `"Witaj"`, `'Python'` | Nie | Tekst, wiadomości, nazwy | `""` |
| **bool** | `True`, `False` | Nie | Warunki, flagi, logika | `False` |
| **NoneType** | `None` | Nie | Brakujące dane, wartości domyślne | `None` |

### Kluczowe Różnice

#### Integer vs Float
- **int**: Liczby całkowite, bez przecinka dziesiętnego
- **float**: Liczby dziesiętne, ograniczona precyzja
- Dzielenie (`/`) zawsze zwraca float

#### String vs Inne Typy
- Stringi to tekst, muszą być w cudzysłowach
- Można konwertować większość typów na string
- Nie można wykonywać arytmetyki na stringach (oprócz `+` do łączenia)

#### Specjalne Właściwości Boolean
- Tylko dwie wartości: `True`, `False`
- Podklasa int (`True` = 1, `False` = 0)
- Używany w warunkach i logice

#### Specjalne Właściwości None
- Reprezentuje brak/brakującą wartość
- Istnieje tylko jeden `None`
- Sprawdzaj za pomocą `is None`, nie `== None`

---

## Najlepsze Praktyki

### 1. Używaj Odpowiednich Typów
```python
# Dobrze
age = 25                    # int do liczenia
price = 19.99              # float dla pieniędzy
name = "Ala"               # str dla tekstu
is_active = True           # bool dla flag

# Unikaj
age = "25"                 # String kiedy potrzebujesz liczby
price = 19                 # Int kiedy potrzebujesz dziesiętnych
```

### 2. Sprawdzanie Typu
```python
# Dobrze
if isinstance(value, int):
    print("To liczba całkowita")

# Mniej elastyczne
if type(value) == int:
    print("To liczba całkowita")
```

### 3. Sprawdzanie None
```python
# Dobrze
if value is None:
    print("Wartość to None")

# Niezalecane
if value == None:
    print("Wartość istnieje")
```

### 4. Formatowanie Stringów
```python
# Nowoczesne (Python 3.6+)
name = "Ala"
age = 25
message = f"{name} ma {age} lat"

# Alternatywa
message = "{} ma {} lat".format(name, age)
```

### 5. Bezpieczeństwo Konwersji Typów
```python
# Niebezpieczne
user_input = "abc"
number = int(user_input)  # Awaria!

# Bezpieczne
try:
    number = int(user_input)
except ValueError:
    print("Nieprawidłowa liczba")
    number = 0
```

---

## Częste Pułapki

### 1. Precyzja Float
```python
# Problem
0.1 + 0.2 == 0.3          # False! To efekt binarnej reprezentacji liczb zmiennoprzecinkowych: 0.1 i 0.2 nie mają dokładnego zapisu w binarnym float, więc ich suma daje lekko inną wartość niż dokładne 0.3
print(a)                # 0.30000000000000004

# Rozwiązanie
round(0.1 + 0.2, 10) == 0.3   # True

# Dla dokładnych obliczeń dziesiętnych (np. finanse) użyć Decimal:
from decimal import Decimal
Decimal("0.1") + Decimal("0.2") == Decimal("0.3")  # True
```

### 2. Dzielenie Całkowite
```python
# Python 3
10 / 3                    # 3.3333... (float)
10 // 3                   # 3 (int)

# Aby otrzymać wynik całkowity, użyj //
```

### 3. Konwersja Stringa
```python
# Problem
int("3.14")               # BŁĄD!

# Rozwiązanie
int(float("3.14"))        # 3
```

### 4. Porównywanie Boolean
```python
# Unikaj
if is_active == True:     # Zbędne
    pass

# Preferuj
if is_active:             # Czytelne
    pass
```

### 5. None vs False
```python
value = None

# Źle
if not value:             # Pasuje do None, False, 0, "", itp.
    pass

# Poprawnie
if value is None:         # Pasuje tylko do None
    pass
```

---