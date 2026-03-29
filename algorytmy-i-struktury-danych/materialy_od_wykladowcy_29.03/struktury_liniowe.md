# Struktury Liniowe w Pythonie — Kompletny Przewodnik

## Spis treści

1. [Wprowadzenie — czym sa struktury liniowe?](#wprowadzenie--czym-sa-struktury-liniowe)
2. [Stos (Stack)](#1-stos-stack)
   - [Czym jest stos?](#11-czym-jest-stos)
   - [Zasada LIFO](#12-zasada-lifo)
   - [Stos wywolan w Pythonie (call stack)](#13-stos-wywolan-w-pythonie-call-stack)
   - [Implementacja na liscie Pythona](#14-implementacja-na-liscie-pythona)
   - [Implementacja na liscie jednokierunkowej](#15-implementacja-na-liscie-jednokierunkowej)
   - [Zlozonosc obliczeniowa](#16-zlozonosc-obliczeniowa)
   - [Ograniczenia stosu](#17-ograniczenia-stosu--czego-nie-mozna-robic)
   - [Zle praktyki](#18-zle-praktyki)
   - [Dobre praktyki](#19-dobre-praktyki)
   - [Algorytmy z uzyciem stosu](#110-algorytmy-z-uzyciem-stosu)
3. [Kolejka (Queue)](#2-kolejka-queue)
   - [Czym jest kolejka?](#21-czym-jest-kolejka)
   - [Zasada FIFO](#22-zasada-fifo)
   - [Implementacja naiwna (antyprzyklad)](#23-implementacja-naiwna-antyprzyklad)
   - [Implementacja na collections.deque](#24-implementacja-na-collectionsdeque)
   - [Implementacja na liscie jednokierunkowej](#25-implementacja-na-liscie-jednokierunkowej-z-ogonem)
   - [Kolejka cykliczna (Circular Buffer)](#26-kolejka-cykliczna-circular-buffer)
   - [Zlozonosc obliczeniowa](#27-zlozonosc-obliczeniowa-1)
   - [Ograniczenia kolejki](#28-ograniczenia-kolejki--czego-nie-mozna-robic)
   - [Zle praktyki](#29-zle-praktyki)
   - [Dobre praktyki](#210-dobre-praktyki)
   - [Algorytmy z uzyciem kolejki](#211-algorytmy-z-uzyciem-kolejki)
4. [Lista jednokierunkowa (Singly Linked List)](#3-lista-jednokierunkowa-singly-linked-list)
   - [Czym jest lista jednokierunkowa?](#31-czym-jest-lista-jednokierunkowa)
   - [Tablica vs lista — roznica w pamieci](#32-tablica-vs-lista--roznica-w-pamieci)
   - [Implementacja wezla i listy](#33-implementacja-wezla-i-listy)
   - [Operacje krok po kroku](#34-operacje-krok-po-kroku)
   - [Zlozonosc obliczeniowa](#35-zlozonosc-obliczeniowa-2)
   - [Ograniczenia listy](#36-ograniczenia--czego-nie-mozna-robic)
   - [Zle praktyki](#37-zle-praktyki)
   - [Dobre praktyki](#38-dobre-praktyki)
   - [Algorytmy na listach](#39-algorytmy-na-listach)
5. [Porownanie struktur](#4-porownanie-struktur)
   - [Tabela zlozonosci](#41-tabela-zlozonosci--wszystkie-struktury-obok-siebie)
   - [Tabela pamieciowa](#42-tabela-pamieciowa)
   - [Kiedy uzywac ktorej struktury?](#43-kiedy-uzywac-ktorej-struktury)
6. [Typowe bledy i pulapki](#5-typowe-bledy-i-pulapki)
7. [Gotowe implementacje w Pythonie](#6-gotowe-implementacje-w-pythonie)
   - [Stos](#61-stos-list-deque-lifoqueue)
   - [Kolejka](#62-kolejka-deque-queue-simplequeue-priorityqueue-asyncioqueue-multiprocessingqueue)
   - [Lista jednokierunkowa](#63-lista-jednokierunkowa-brak-wbudowanej-llist)
   - [Kopiec — heapq](#64-kopiec--heapq)
   - [Zestawienie](#65-zestawienie-wlasna-implementacja-vs-biblioteka)
8. [Zadania do samodzielnego rozwiazania](#7-zadania-do-samodzielnego-rozwiazania)

---

## Wprowadzenie — czym sa struktury liniowe?
Struktura danych to sposób organizacji danych w pamięci komputera.

Struktury danych pozwalają na przechowywanie obiektów w pamięci oraz wykonywanie na nich pewnych operacji, takich jak: umieszczanie w strukturze nowych obiektów lub usuwanie ich; sprawdzanie, czy obiekt jest elementem struktury; iteracja po obiektach w strukturze; indeksowanie (czyli wybieranie obiektu spod danego indeksu bądź klucza); etc.

Znanymi już, wbudowanymi w Pythona strukturami danych są listy, zbiory, słowniki i krotki.
 Struktury różnią się dostępnymi operacjami, oraz czasami ich działania. Nie istnieje "uniwersalna" struktura danych pozwalająca na wszystkie możliwe operacje i jednocześnie gwarantująca najlepsze czasy działania tych operacji. Zamiast tego, każda struktura jest efektem pewnych kompromisów między czasami konkretnych operacji, rozmiarem pamięci jaki struktura zajmuje, etc. Wady i zalety struktury determinują jej przydatność w konkretnych algorytmach.

Przykładowo: lista może zostać użyta w zastępstwie zbioru, jednak czas operacji x in s dla list jest liniowy, a nie stały jak w przypadku zbioru. Z drugiej strony, lista pozwala na utrzymywanie obiektów w żądanej kolejności.

**Struktura liniowa** to taka struktura danych, w ktorej elementy sa ulozone jeden za drugim — kazdy element (poza pierwszym i ostatnim) ma dokladnie jednego **poprzednika** i jednego **nastepnika**.

```
Struktura liniowa:
  [A] --> [B] --> [C] --> [D] --> [E]
  Kazdy element "widzi" co najwyzej jednego sasiada z przodu i z tylu.

Struktura nieliniowa (drzewo):
           [A]
          /   \
        [B]   [C]
       / \      \
     [D] [E]    [F]
  Element moze miec wielu "nastepnikow" (dzieci).
```

W tym przewodniku omowimy trzy podstawowe struktury liniowe:

| Struktura | Zasada dostepu | Analogia z zycia |
|-----------|---------------|-------------------|
| **Stos** | LIFO — ostatni wchodzi, pierwszy wychodzi | Stos talerzy |
| **Kolejka** | FIFO — pierwszy wchodzi, pierwszy wychodzi | Kolejka w sklepie |
| **Lista jednokierunkowa** | Sekwencyjny — od poczatku do konca | Pociag — wagony polaczone w jednym kierunku |

Dlaczego to wazne? Bo kazdy program, ktory piszesz, korzysta z tych struktur — jawnie lub niejawnie. Stos wywolan funkcji, kolejka zadan systemu operacyjnego, lista elementow na stronie — to wszystko struktury liniowe.

---

## 1. Stos (Stack)

### 1.1. Czym jest stos?

Stos to struktura danych, w ktorej elementy mozna dodawac i usuwac **tylko z jednego konca** — z wierzcholka (ang. *top*).

**Analogie z zycia codziennego:**

- **Stos talerzy** — bierzesz talerz z gory, dokladasz tez na gore. Nie wyciagasz talerza ze srodka (bo reszta sie przewroci).
- **Ctrl+Z (cofanie)** — kazda akcja jest "odkladana na stos". Cofanie zdejmuje ostatnia akcje.
- **Przegladarka internetowa** — przycisk "Wstecz" zdejmuje ostatnia strone ze stosu historii.
- **Stos wywolan funkcji** — kazde wywolanie funkcji tworzy nowa "ramke" na stosie. Gdy funkcja konczy prace, ramka jest zdejmowana.

```
     Analogia: stos talerzy

        ___________
       |  talerz 3 |  <-- mozesz wziac TYLKO ten (wierzcholek)
       |___________|
       |  talerz 2 |  <-- ten jest "uwieziony" pod spodem
       |___________|
       |  talerz 1 |  <-- do tego nie masz dostepu
       |___________|
       |___________| <-- dno
```

### 1.2. Zasada LIFO

LIFO = **Last In, First Out** (ostatni wchodzi, pierwszy wychodzi).

Element, ktory zostal dodany najpozniej, zostanie usuniety jako pierwszy.

```
Etap 1: push(10)    Etap 2: push(20)    Etap 3: push(30)    Etap 4: pop() = 30
     TOP                  TOP                  TOP                  TOP
  |-------|           |-------|            |-------|            |-------|
  |  10   |           |  20   |            |  30   | <-- pop    |  20   | <-- teraz tu
  |-------|           |-------|            |-------|            |-------|
  | BOTTOM|           |  10   |            |  20   |            |  10   |
  |_______|           |-------|            |-------|            |-------|
                      | BOTTOM|            |  10   |            | BOTTOM|
                      |_______|            |-------|            |_______|
                                           | BOTTOM|
                                           |_______|
```

Podstawowe operacje stosu:
- **`push(x)`** — dodaje element na wierzcholek stosu,
- **`pop()`** — zdejmuje i zwraca element z wierzcholka,
- **`peek()`** — zwraca element z wierzcholka **bez usuwania**,
- **`jest_pusty()`** — sprawdza, czy stos jest pusty.

### 1.3. Stos wywolan w Pythonie (call stack)

Kazde wywolanie funkcji w Pythonie tworzy nowa **ramke** (*frame*) na stosie wywolan. Gdy funkcja konczy prace, ramka jest zdejmowana. Rekurencja to doslownie budowanie stosu wywolan.

```python
def silnia(n):
    # Kazde wywolanie tworzy nowa ramke na stosie
    if n == 0:
        return 1
    return n * silnia(n - 1)

# silnia(3) wywoluje silnia(2), ktora wywoluje silnia(1), ktora wywoluje silnia(0)
# Stos wywolan w szczytowym momencie:
#   [silnia(0)]  <-- wierzcholek (wykonuje sie teraz)
#   [silnia(1)]
#   [silnia(2)]
#   [silnia(3)]  <-- dno (czeka na wynik)

# Wynik 1 "pnie sie" w gore: 1*1*2*3 = 6
```

```
Wizualizacja stosu wywolan dla silnia(3):

  Faza "zanurzania"              Faza "wynurzania"
  (budowanie stosu):             (zdejmowanie ramek):

  silnia(3) woła silnia(2)       silnia(0) zwraca 1
  silnia(2) woła silnia(1)       silnia(1) zwraca 1*1 = 1
  silnia(1) woła silnia(0)       silnia(2) zwraca 2*1 = 2
  silnia(0) -> przypadek bazowy  silnia(3) zwraca 3*2 = 6
```

Przekroczenie maksymalnej glebokosci stosu wywolan powoduje blad `RecursionError` (Python domyslnie: 1000 poziomow).

```python
import sys
print(sys.getrecursionlimit())   # 1000

sys.setrecursionlimit(10_000)    # mozna zwiekszyc (ostroznie!)
# Zbyt duza wartosc moze spowodowac crash interpretera (przepelnienie
# prawdziwego stosu systemowego, nie tylko Pythonowego limitu).
```

> **Wazne:** Jesli algorytm wymaga glebokosci rekurencji wiekszej niz ~1000, rozważ zamiane na wersje iteracyjna z jawnym stosem (patrz sekcja 1.10).

### 1.4. Implementacja na liscie Pythona

Pythonowa lista (`list`) moze sluzyc jako stos — operacje `append` i `pop` dzialaja na koncu listy w czasie O(1) amortyzowanym (dynamiczne powiekszanie tablicy).

```python
class Stos:
    """Stos zaimplementowany na wbudowanej liscie Pythona.

    Wewnetrznie uzywa list(), ktora jest tablica dynamiczna.
    Operacje push/pop dzialaja na KONCU listy (indeks -1),
    dzieki czemu sa O(1) amortyzowane.
    """

    def __init__(self, pojemnosc: int = None):
        self._dane = []
        self._pojemnosc = pojemnosc  # None = nieograniczony

    def push(self, wartosc):
        """O(1) amortyzowane — dodaje element na wierzcholek."""
        if self._pojemnosc and len(self._dane) >= self._pojemnosc:
            raise OverflowError("Stos jest pelny (overflow).")
        self._dane.append(wartosc)

    def pop(self):
        """O(1) — zdejmuje i zwraca element z wierzcholka."""
        if self.jest_pusty():
            raise IndexError("Stos jest pusty (underflow).")
        return self._dane.pop()

    def peek(self):
        """O(1) — zwraca wierzcholek bez usuwania."""
        if self.jest_pusty():
            raise IndexError("Stos jest pusty.")
        return self._dane[-1]

    def jest_pusty(self):
        """O(1) — sprawdza, czy stos jest pusty."""
        return len(self._dane) == 0

    def rozmiar(self):
        """O(1) — zwraca liczbe elementow."""
        return len(self._dane)

    def __str__(self):
        if self.jest_pusty():
            return "Stos: [] (pusty)"
        return "Stos (wierzch po prawej): " + str(self._dane)

    def __repr__(self):
        return f"Stos({self._dane})"
```

### 1.5. Implementacja na liscie jednokierunkowej

Wstawianie i zdejmowanie zawsze od **glowy** — dzieki temu obie operacje to O(1) bez amortyzacji i bez potrzeby znania ogona.

```python
class StosNaLiscie:
    """Stos zaimplementowany na liscie jednokierunkowej.

    Wierzcholek stosu = glowa listy. Kazdy push/pop operuje
    na glowie, wiec nie trzeba przechodzic calej listy.
    """

    def __init__(self):
        self._glowa = None  # wierzcholek stosu
        self._rozmiar = 0

    def push(self, wartosc):
        """O(1) — dodaje nowy wezel jako nowa glowe."""
        nowy = Wezel(wartosc)
        nowy.nastepny = self._glowa
        self._glowa = nowy
        self._rozmiar += 1

    def pop(self):
        """O(1) — usuwa i zwraca wezel z glowy."""
        if self.jest_pusty():
            raise IndexError("Stos jest pusty (underflow).")
        wartosc = self._glowa.dane
        self._glowa = self._glowa.nastepny
        self._rozmiar -= 1
        return wartosc

    def peek(self):
        """O(1) — zwraca wartosc glowy bez usuwania."""
        if self.jest_pusty():
            raise IndexError("Stos jest pusty.")
        return self._glowa.dane

    def jest_pusty(self):
        """O(1)"""
        return self._glowa is None

    def rozmiar(self):
        """O(1)"""
        return self._rozmiar

    def __str__(self):
        elementy = []
        aktualny = self._glowa
        while aktualny:
            elementy.append(str(aktualny.dane))
            aktualny = aktualny.nastepny
        return "TOP -> " + " -> ".join(elementy) + " -> BOTTOM"
```

```
Wizualizacja stosu na liscie jednokierunkowej:

Po push(10), push(20), push(30):

  _glowa (wierzcholek)
    |
   [30] --> [20] --> [10] --> None
    TOP                        BOTTOM

pop() -> zwraca 30, przesuwa _glowa:

  _glowa
    |
   [20] --> [10] --> None
    TOP      BOTTOM
```

### 1.6. Zlozonosc obliczeniowa

| Operacja | Stos na `list` | Stos na liscie jednokierunkowej |
|----------|---------------|--------------------------------|
| `push(x)` | O(1) amortyzowane | O(1) |
| `pop()` | O(1) | O(1) |
| `peek()` | O(1) | O(1) |
| `jest_pusty()` | O(1) | O(1) |
| `rozmiar()` | O(1) | O(1) |
| Dostep do i-tego elementu | O(1)* | O(n) |
| Wyszukiwanie wartosci | O(n) | O(n) |
| Pamiec na n elementow | O(n) | O(n) + narzut wskaznikow |

\* Dostep po indeksie w `list` to O(1), ale **to NIE jest operacja stosu** — stos z definicji nie oferuje dostepu do srodka.

> **Amortyzowane O(1)** — zwykle operacja trwa O(1), ale co jakis czas tablica musi sie powiekszy (realokacja), co kosztuje O(n). Sredni koszt na operacje jest jednak O(1).

### 1.7. Ograniczenia stosu — czego NIE MOZNA robic

Stos to **struktura z ograniczonym dostepem** — to jest jego sila, ale i ograniczenie.

**1. Brak dostepu do srodka**

Nie mozna odczytac ani zmodyfikowac elementu w srodku stosu bez zdejmowania wszystkich elementow nad nim.

```
Chcesz odczytac element "B"?

  TOP -> [D] -> [C] -> [B] -> [A] -> BOTTOM

  Musisz zdjac D, potem C, dopiero wtedy widzisz B.
  A potem musisz odlozyc C i D z powrotem!
```

**Dlaczego?** Bo stos z definicji udostepnia TYLKO wierzcholek. To nie jest blad implementacji — to fundamentalna wlasciwosc struktury. Gdyby stos udostepnial dostep do srodka, bylby tablica, a nie stosem.

**2. Brak iteracji bez destrukcji**

Przejrzenie wszystkich elementow stosu wymaga ich zdejmowania. Po zakonczeniu iteracji stos jest pusty (chyba ze elementy sa odkladane na stos pomocniczy).

**3. Brak wyszukiwania w O(1)**

Nie mozna sprawdzic, czy dany element jest na stosie, bez przejrzenia calego stosu (O(n)).

**4. Brak sortowania w sensownym czasie**

Sortowanie stosu wymaga operacji ktore sa nienaturalne dla tej struktury.

> **Wniosek:** Jesli potrzebujesz dostepu do elementow w srodku, wyszukiwania, lub iteracji — stos nie jest wlasciwa struktura. Uzyj listy, tablicy lub innej struktury.

### 1.8. Zle praktyki

#### Uzycie stosu zamiast listy gdy potrzebujesz dostepu do srodka

```python
# ZLE — uzywanie stosu do przechowywania danych, do ktorych potrzebny
# jest losowy dostep
stos = Stos()
for i in range(100):
    stos.push(i)

# Chcemy odczytac 50-ty element — musimy zdjac 50 elementow!
pomocniczy = Stos()
for _ in range(50):
    pomocniczy.push(stos.pop())
wartosc = stos.peek()  # dopiero teraz mamy dostep
# ... i musimy odlozyc z powrotem
while not pomocniczy.jest_pusty():
    stos.push(pomocniczy.pop())

# DOBRZE — jesli potrzebujesz dostepu po indeksie, uzyj listy
dane = list(range(100))
wartosc = dane[50]  # O(1)
```

#### Brak sprawdzenia pustosci przed pop/peek

```python
# ZLE — brak sprawdzenia pustosci
def zle_pop(stos):
    return stos._dane.pop()   # IndexError gdy stos jest pusty!

# DOBRZE — zawsze sprawdzaj
def dobre_pop(stos):
    if stos.jest_pusty():
        raise IndexError("Stos jest pusty.")
    return stos._dane.pop()
```

#### Bezposredni dostep do wewnetrznej listy

```python
# ZLE — lamie enkapsulacje, omija kontrole
stos = Stos()
stos.push(10)
stos.push(20)
stos._dane.insert(0, 5)  # wstawianie na dno stosu — to nie jest operacja stosu!
stos._dane[1] = 99       # modyfikacja srodka — stos tego nie powinien umozliwiac

# DOBRZE — uzywaj TYLKO push/pop/peek
stos = Stos()
stos.push(10)
stos.push(20)
wartosc = stos.pop()  # 20
```

#### Rekurencja bez ograniczenia glebokosci

```python
# ZLE — moze spowodowac RecursionError dla duzych danych
def suma_listy(glowa):
    if glowa is None:
        return 0
    return glowa.dane + suma_listy(glowa.nastepny)

# DOBRZE — wersja iteracyjna (dla duzych danych)
def suma_listy_iteracyjna(glowa):
    suma = 0
    aktualny = glowa
    while aktualny:
        suma += aktualny.dane
        aktualny = aktualny.nastepny
    return suma
```

### 1.9. Dobre praktyki

#### Uzywaj wyjatkow zamiast zwracania None

```python
# DOBRZE — jasny komunikat bledu
def pop(self):
    if self.jest_pusty():
        raise IndexError("Stos jest pusty (underflow).")
    return self._dane.pop()

# ZLE — cichy blad, trudny do debugowania
def pop(self):
    if self.jest_pusty():
        return None  # klient nie wie, czy None to wartosc czy blad
    return self._dane.pop()
```

#### Dodaj ograniczenie pojemnosci gdy to potrzebne

```python
# DOBRZE — stos z limitem zapobiega niekontrolowanemu zuzyciu pamieci
stos = Stos(pojemnosc=1000)
try:
    stos.push(wartosc)
except OverflowError:
    print("Stos pelny — nie mozna dodac elementu")
```

#### Implementuj protokol Pythona (`__len__`, `__bool__`)

```python
class Stos:
    # ... reszta implementacji ...

    def __len__(self):
        """Pozwala uzyc len(stos)."""
        return len(self._dane)

    def __bool__(self):
        """Pozwala uzyc: if stos: ..."""
        return len(self._dane) > 0

# Teraz mozna pisac idiomatyczny Python:
stos = Stos()
stos.push(10)

if stos:                    # zamiast: if not stos.jest_pusty()
    print(f"Rozmiar: {len(stos)}")  # zamiast: stos.rozmiar()
```

#### Rozdzielaj logike od wyswietlania

```python
# DOBRZE — metoda __str__ do wyswietlania, osobna logika
class Stos:
    def __str__(self):
        return "Stos: " + str(self._dane)

    def __repr__(self):
        return f"Stos({self._dane})"

# W kodzie:
print(stos)     # uzywa __str__  — ladny format dla uzytkownika
print(repr(stos))  # uzywa __repr__ — format dla programisty
```

### 1.10. Algorytmy z uzyciem stosu

#### Sprawdzanie poprawnosci nawiasow

Klasyczne zastosowanie — weryfikacja zagniezdzen nawiasow w kodzie zrodlowym.

```python
def nawiasy_poprawne(wyrazenie: str) -> bool:
    """Sprawdza, czy nawiasy w wyrazeniu sa poprawnie domkniete.

    Idea: otwierajace nawiasy odkladamy na stos.
    Gdy natrafiamy na zamykajacy, sprawdzamy, czy pasuje do wierzcholka.
    Na koncu stos musi byc pusty (wszystkie otwarte zostaly zamkniete).
    """
    stos = Stos()
    pary = {')': '(', ']': '[', '}': '{'}

    for i, znak in enumerate(wyrazenie):
        if znak in '([{':
            stos.push(znak)
        elif znak in ')]}':
            if stos.jest_pusty():
                print(f"Blad na pozycji {i}: '{znak}' bez otwierajacego.")
                return False
            if stos.pop() != pary[znak]:
                print(f"Blad na pozycji {i}: niezgodnosc nawiasow.")
                return False

    if not stos.jest_pusty():
        print("Blad: niezamkniete nawiasy otwierajace.")
        return False
    return True


print(nawiasy_poprawne("({[]})"))    # True
print(nawiasy_poprawne("({[})"))     # False — niezgodnosc
print(nawiasy_poprawne("((())"))     # False — niezamkniete
print(nawiasy_poprawne(""))          # True — puste wyrazenie jest poprawne
```

#### Ewaluacja wyrazen w Odwrotnej Notacji Polskiej (ONP/RPN)

ONP eliminuje potrzebe nawiasow. Operandy odkladamy na stos, operator pobiera dwa operandy i odklada wynik.

```
Przyklad: "3 4 + 2 * 7 /"  odpowiada  (3 + 4) * 2 / 7

Krok 1: push(3)  --> stos: [3]
Krok 2: push(4)  --> stos: [3, 4]
Krok 3: '+'  --> pop() = 4, pop() = 3, push(3+4=7)  --> stos: [7]
Krok 4: push(2)  --> stos: [7, 2]
Krok 5: '*'  --> pop() = 2, pop() = 7, push(7*2=14) --> stos: [14]
Krok 6: push(7)  --> stos: [14, 7]
Krok 7: '/'  --> pop() = 7, pop() = 14, push(14/7=2) --> stos: [2]

Wynik: 2.0
```

```python
def oblicz_onp(wyrazenie: str) -> float:
    """Oblicza wartosc wyrazenia w Odwrotnej Notacji Polskiej.

    Argumenty:
        wyrazenie: tokeny oddzielone spacjami, np. "3 4 + 2 *"
    """
    stos = Stos()
    operatory = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    for token in wyrazenie.split():
        if token in operatory:
            if stos.rozmiar() < 2:
                raise ValueError(f"Za malo operandow dla operatora '{token}'.")
            b = stos.pop()  # drugi operand (zdejmowany pierwszy)
            a = stos.pop()  # pierwszy operand
            stos.push(operatory[token](a, b))
        else:
            stos.push(float(token))

    if stos.rozmiar() != 1:
        raise ValueError("Niepoprawne wyrazenie ONP.")
    return stos.pop()


print(oblicz_onp("3 4 +"))          # 7.0
print(oblicz_onp("3 4 + 2 * 7 /"))  # 2.0
print(oblicz_onp("5 1 2 + 4 * + 3 -"))  # 14.0
```

#### Zamiana dziesietnej na inna podstawe

```python
def zmien_podstawe(liczba: int, podstawa: int) -> str:
    """Konwertuje nieujemna liczbe calkowita na podany system liczbowy.

    Obsluguje podstawy 2-16.
    Idea: dzielimy przez podstawe i odkladamy reszty na stos.
    Na koncu zdejmujemy reszty — sa w odwroconej kolejnosci (wlasciwej).
    """
    if liczba == 0:
        return "0"
    if not 2 <= podstawa <= 16:
        raise ValueError("Podstawa musi byc z zakresu 2-16.")

    cyfry = "0123456789ABCDEF"
    stos = Stos()

    while liczba > 0:
        stos.push(cyfry[liczba % podstawa])
        liczba //= podstawa

    wynik = []
    while not stos.jest_pusty():
        wynik.append(stos.pop())
    return "".join(wynik)


print(zmien_podstawe(42, 2))    # 101010  (binarny)
print(zmien_podstawe(42, 8))    # 52      (oktalny)
print(zmien_podstawe(255, 16))  # FF      (szesnastkowy)
```

#### Iteracyjny DFS (przeszukiwanie w glab)

```python
def dfs_iteracyjny(graf: dict, start) -> list:
    """Przeszukuje graf w glab (DFS) iteracyjnie, uzywajac stosu.

    Iteracyjne DFS za pomoca stosu jest odpowiednikiem rekurencyjnego DFS
    (ktory niejawnie korzysta ze stosu wywolan).
    """
    odwiedzone = set()
    stos = Stos()
    stos.push(start)
    wynik = []

    while not stos.jest_pusty():
        wezel = stos.pop()
        if wezel not in odwiedzone:
            odwiedzone.add(wezel)
            wynik.append(wezel)
            # Sasiadow dodajemy w odwroconej kolejnosci,
            # by zachowac porzadek alfabetyczny/naturalny odwiedzania
            for sasiad in reversed(graf.get(wezel, [])):
                if sasiad not in odwiedzone:
                    stos.push(sasiad)

    return wynik


graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
print(dfs_iteracyjny(graf, 'A'))  # ['A', 'B', 'D', 'E', 'C', 'F']
```

#### Symulowanie rekurencji iteracyjnie

Zamiana algorytmu rekurencyjnego na iteracyjny eliminuje ryzyko przepelnienia stosu wywolan.

```python
def silnia_iteracyjna(n: int) -> int:
    """Oblicza n! iteracyjnie, symulujac stos wywolan."""
    stos = Stos()
    wynik = 1

    # Faza "zanurzania" — odkladamy wywolania na stos
    while n > 0:
        stos.push(n)
        n -= 1

    # Faza "wynurzania" — zdejmujemy i obliczamy
    while not stos.jest_pusty():
        wynik *= stos.pop()

    return wynik


print(silnia_iteracyjna(10))  # 3628800
```

---

## 2. Kolejka (Queue)

### 2.1. Czym jest kolejka?

Kolejka to struktura danych, w ktorej elementy sa dodawane na **koniec** i usuwane z **poczatku**.

**Analogie z zycia codziennego:**

- **Kolejka w sklepie** — kto przyszedl pierwszy, ten jest obslugiwany pierwszy. Nowi klienci ustawiaja sie na koncu.
- **Drukarka** — dokumenty sa drukowane w kolejnosci wyslania. Pierwszy wyslany = pierwszy wydrukowany.
- **Scheduler systemu operacyjnego** — procesy czekaja w kolejce na dostep do procesora.
- **Buforowanie filmow na YouTube** — klatki sa pobierane i umieszczane w kolejce, a odtwarzacz pobiera je z poczatku.

```
     Analogia: kolejka w sklepie

     WEJSCIE (enqueue)                KASA (dequeue)
         |                                |
         v                                v
     [Ewa] [Dawid] [Celina] [Bob] --> [Anna]
      rear                             front
      (koniec)                        (poczatek)

     Anna jest obslugiwana pierwsza (FIFO).
     Ewa dolaczyala ostatnia — bedzie obslugiwana na koncu.
```

### 2.2. Zasada FIFO

FIFO = **First In, First Out** (pierwszy wchodzi, pierwszy wychodzi).

Element, ktory zostal dodany najwczesniej, zostanie usuniety jako pierwszy.

```
ENQUEUE -->  [E | D | C | B | A]  --> DEQUEUE
              rear              front

Etap 1: enqueue(A)   front=[A] rear=[A]
Etap 2: enqueue(B)   front=[A] rear=[B]
Etap 3: enqueue(C)   front=[A] rear=[C]
Etap 4: dequeue()=A  front=[B] rear=[C]
Etap 5: enqueue(D)   front=[B] rear=[D]
```

Podstawowe operacje:
- **`enqueue(x)`** — dodaje element na koniec kolejki,
- **`dequeue()`** — usuwa i zwraca element z przodu kolejki,
- **`front()`** — podglad elementu z przodu bez usuwania,
- **`jest_pusta()`** — sprawdza, czy kolejka jest pusta.

### 2.3. Implementacja naiwna (antyprzyklad)

Ta implementacja jest **niepoprawna wydajnosciowo** — pokazujemy ja jako przestroge.

```python
# UWAGA: TO JEST ANTYPRZYKLAD — NIE UZYWAJ TEJ IMPLEMENTACJI!
class KolejkaNaiwna:
    """Kolejka na liscie Pythona — NIEEFEKTYWNA.

    Problem: pop(0) przesuwa WSZYSTKIE elementy o jedno miejsce w lewo.
    Dla n elementow to O(n) na kazde dequeue!
    """

    def __init__(self):
        self._dane = []

    def enqueue(self, wartosc):
        self._dane.append(wartosc)   # O(1) amortyzowane — OK

    def dequeue(self):
        if not self._dane:
            raise IndexError("Kolejka jest pusta.")
        return self._dane.pop(0)
        # pop(0) jest O(n) — Python musi przesunac WSZYSTKIE pozostale
        # elementy o jedno miejsce w lewo!

# Dla n operacji dequeue: O(n^2) lacznie — bardzo wolne!
```

```
Dlaczego pop(0) jest O(n)?

PRZED pop(0):
  indeks:  [0]  [1]  [2]  [3]  [4]
  wartosc: [A]  [B]  [C]  [D]  [E]

PO pop(0) = A:
  Trzeba przesunac B, C, D, E o jedno miejsce w lewo:
  indeks:  [0]  [1]  [2]  [3]
  wartosc: [B]  [C]  [D]  [E]
           <--  <--  <--  <--   4 przesuniecia!

  Dla 1 000 000 elementow = 999 999 przesuniec na KAZDYM dequeue!
```

### 2.4. Implementacja na collections.deque

`deque` (*double-ended queue*) to zoptymalizowana struktura z biblioteki standardowej. Wewnetrznie zaimplementowana jako lista dwukierunkowa blokow — operacje na obu koncach to O(1).

```python
from collections import deque


class Kolejka:
    """Kolejka FIFO zaimplementowana na collections.deque.

    deque jest optymalna — popleft() i append() sa O(1).
    """

    def __init__(self, maxlen: int = None):
        # maxlen ogranicza rozmiar — nowe elementy wypychaja stare
        self._dane = deque(maxlen=maxlen)

    def enqueue(self, wartosc):
        """O(1) — dodaje element na koniec kolejki."""
        self._dane.append(wartosc)

    def dequeue(self):
        """O(1) — usuwa i zwraca element z przodu kolejki."""
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta (underflow).")
        return self._dane.popleft()

    def front(self):
        """O(1) — zwraca element z przodu bez usuwania."""
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta.")
        return self._dane[0]

    def jest_pusta(self):
        """O(1) — sprawdza, czy kolejka jest pusta."""
        return len(self._dane) == 0

    def rozmiar(self):
        """O(1) — zwraca liczbe elementow."""
        return len(self._dane)

    def __iter__(self):
        return iter(self._dane)

    def __str__(self):
        return "FRONT -> " + " -> ".join(str(x) for x in self._dane) + " -> REAR"
```

### 2.5. Implementacja na liscie jednokierunkowej (z ogonem)

Przechowujemy wskazniki na glowe (*front*) i ogon (*rear*), dzieki czemu obie operacje sa O(1).

```python
class KolejkaNaLiscie:
    """Kolejka FIFO zaimplementowana na liscie jednokierunkowej.

    Kluczowe: wskaznik _ogon eliminuje potrzebe przechodzenia calej listy
    przy enqueue. Bez niego enqueue byloby O(n).
    """

    def __init__(self):
        self._glowa = None  # przod kolejki (dequeue stad)
        self._ogon = None   # koniec kolejki (enqueue tutaj)
        self._rozmiar = 0

    def enqueue(self, wartosc):
        """O(1) — dodaje nowy wezel na ogon."""
        nowy = Wezel(wartosc)
        if self._ogon is not None:
            self._ogon.nastepny = nowy
        self._ogon = nowy
        if self._glowa is None:
            self._glowa = nowy  # pierwsza enqueue: glowa = ogon
        self._rozmiar += 1

    def dequeue(self):
        """O(1) — usuwa i zwraca wartosc z glowy."""
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta (underflow).")
        wartosc = self._glowa.dane
        self._glowa = self._glowa.nastepny
        if self._glowa is None:
            self._ogon = None  # kolejka opustoszala — resetujemy ogon
        self._rozmiar -= 1
        return wartosc

    def front(self):
        """O(1) — zwraca wartosc z przodu bez usuwania."""
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta.")
        return self._glowa.dane

    def jest_pusta(self):
        """O(1)"""
        return self._glowa is None

    def rozmiar(self):
        """O(1)"""
        return self._rozmiar

    def __str__(self):
        elementy = []
        aktualny = self._glowa
        while aktualny:
            elementy.append(str(aktualny.dane))
            aktualny = aktualny.nastepny
        return "FRONT -> " + " -> ".join(elementy) + " -> REAR"
```

```
Wizualizacja stanu wskaznikow kolejki na liscie:

Po enqueue(A), enqueue(B), enqueue(C):

 glowa                    ogon
   |                        |
  [A] -------> [B] -------> [C] -> None

dequeue() -> zwraca A, przesuwa glowe:

          glowa            ogon
            |                |
           [B] ----------> [C] -> None

enqueue(D):

          glowa                    ogon
            |                        |
           [B] -------> [C] -------> [D] -> None
```

### 2.6. Kolejka cykliczna (Circular Buffer)

Kolejka cykliczna (ang. *circular queue* lub *ring buffer*) to wydajna implementacja kolejki o stalym rozmiarze na tablicy. Unika problemu "przesuwania" elementow dzieki zawijaniu indeksow modulo.

```
Idea kolejki cyklicznej:

Zwykla tablica — po kilku dequeue marnujemy miejsce z przodu:
  [_] [_] [C] [D] [E]         <-- 2 zmarnowane miejsca!
            ^front    ^rear

Kolejka cykliczna — indeksy "zawijaja sie" (modulo):
  [F] [_] [C] [D] [E]         <-- F jest na pozycji 0 (zawiniety rear)
   ^rear   ^front

  Logicznie: FRONT -> C -> D -> E -> F -> REAR
  Fizycznie tablica wyglada jak pierscien.
```

```python
class KolejkaCykliczna:
    """Kolejka o stalym rozmiarze oparta na tablicy cyklicznej.

    Wskazniki front i rear "obiegaja" tablice po okregu:
    gdy dotra do konca tablicy, wracaja na poczatek (operacja % pojemnosc).
    """

    def __init__(self, pojemnosc: int):
        if pojemnosc <= 0:
            raise ValueError("Pojemnosc musi byc dodatnia.")
        self._pojemnosc = pojemnosc
        self._dane = [None] * pojemnosc
        self._front = 0   # indeks pierwszego elementu
        self._rear = 0    # indeks nastepnego wolnego miejsca
        self._rozmiar = 0

    def enqueue(self, wartosc):
        """O(1) — dodaje element do kolejki."""
        if self.jest_pelna():
            raise OverflowError("Kolejka jest pelna (overflow).")
        self._dane[self._rear] = wartosc
        self._rear = (self._rear + 1) % self._pojemnosc  # zawijanie!
        self._rozmiar += 1

    def dequeue(self):
        """O(1) — usuwa i zwraca element z przodu."""
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta (underflow).")
        wartosc = self._dane[self._front]
        self._dane[self._front] = None   # opcjonalne czyszczenie
        self._front = (self._front + 1) % self._pojemnosc  # zawijanie!
        self._rozmiar -= 1
        return wartosc

    def front(self):
        """O(1) — zwraca przod kolejki bez usuwania."""
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta.")
        return self._dane[self._front]

    def jest_pusta(self):
        """O(1)"""
        return self._rozmiar == 0

    def jest_pelna(self):
        """O(1)"""
        return self._rozmiar == self._pojemnosc

    def rozmiar(self):
        """O(1)"""
        return self._rozmiar

    def __str__(self):
        if self.jest_pusta():
            return "KolejkaCykliczna: [] (pusta)"
        elementy = []
        for i in range(self._rozmiar):
            idx = (self._front + i) % self._pojemnosc
            elementy.append(str(self._dane[idx]))
        return f"KolejkaCykliczna [{self._pojemnosc}]: FRONT -> " + " -> ".join(elementy) + " -> REAR"


# Przyklad:
kc = KolejkaCykliczna(3)
kc.enqueue(1)
kc.enqueue(2)
kc.enqueue(3)
print(kc)             # FRONT -> 1 -> 2 -> 3 -> REAR
print(kc.dequeue())   # 1
kc.enqueue(4)         # miejsce po 1 jest znowu dostepne!
print(kc)             # FRONT -> 2 -> 3 -> 4 -> REAR
```

### 2.7. Zlozonosc obliczeniowa

| Operacja | Naiwna (list) | deque | Lista z ogonem | Cykliczna |
|----------|--------------|-------|----------------|-----------|
| `enqueue(x)` | O(1) amort. | O(1) | O(1) | O(1) |
| `dequeue()` | **O(n)** | O(1) | O(1) | O(1) |
| `front()` | O(1) | O(1) | O(1) | O(1) |
| `jest_pusta()` | O(1) | O(1) | O(1) | O(1) |
| `rozmiar()` | O(1) | O(1) | O(1) | O(1) |
| Dostep do i-tego | O(1) | O(n)* | O(n) | O(1) |
| Wyszukiwanie | O(n) | O(n) | O(n) | O(n) |
| Pamiec | O(n) | O(n) | O(n) + wskazniki | O(pojemnosc) |

\* `deque` ma O(1) dostep do obu koncow, ale O(n) do srodka.

### 2.8. Ograniczenia kolejki — czego NIE MOZNA robic

**1. Brak dostepu do konca (ani do srodka)**

Kolejka udostepnia TYLKO element z przodu (`front`). Nie mozna podejrzec ostatniego elementu ani elementu w srodku bez dekolejkowania.

```
Chcesz zobaczyc element D?

  FRONT -> [A] -> [B] -> [C] -> [D] -> REAR

  Musisz zdjac A, B, C — dopiero wtedy D jest na froncie.
  Jesli chcesz zachowac A, B, C — musisz je zapisac i z powrotem wlozyc.
```

**Dlaczego?** Kolejka z definicji gwarantuje kolejnosc FIFO. Gdyby mozna bylo "przeskakiwac" do srodka, kolejnosc bylaby naruszona — a to fundamentalna wlasciwosc kolejki.

**2. Brak usuwania z dowolnej pozycji**

Nie mozna usunac elementu ze srodka kolejki. Trzeba dekolejkowac wszystkie elementy przed nim.

**3. Kolejka cykliczna ma staly rozmiar**

Nie mozna jej powiekszac dynamicznie (bez kopiowania do nowej, wiekszej tablicy).

**4. Brak sortowania w sensownym czasie**

Sortowanie kolejki wymaga wyciagniecia wszystkich elementow, posortowania i ponownego wlozenia.

> **Wniosek:** Jesli potrzebujesz dostepu do dowolnego elementu lub usuwania ze srodka, kolejka nie jest wlasciwa struktura.

### 2.9. Zle praktyki

#### Uzywanie `list.pop(0)` zamiast `deque.popleft()`

```python
# ZLE — O(n) na kazde dequeue, lacznie O(n^2)
kolejka = []
for i in range(100_000):
    kolejka.append(i)
while kolejka:
    kolejka.pop(0)  # WOLNE!  ~sekundy

# DOBRZE — O(1) na kazde dequeue, lacznie O(n)
from collections import deque
kolejka = deque()
for i in range(100_000):
    kolejka.append(i)
while kolejka:
    kolejka.popleft()  # SZYBKIE!  ~milisekundy
```

#### Zapomnienie o resetowaniu ogona przy dequeue

```python
# ZLE — klasyczny blad w implementacji na liscie
def zle_dequeue(self):
    wartosc = self._glowa.dane
    self._glowa = self._glowa.nastepny
    # BRAK: if self._glowa is None: self._ogon = None
    # Ogon nadal wskazuje na usuniety wezel!
    # Nastepne enqueue uszkodzi strukture.
    return wartosc

# DOBRZE
def dobre_dequeue(self):
    wartosc = self._glowa.dane
    self._glowa = self._glowa.nastepny
    if self._glowa is None:
        self._ogon = None  # kolejka pusta — resetujemy ogon!
    self._rozmiar -= 1
    return wartosc
```

#### Uzywanie kolejki do problemu wymagajacego stosu

```python
# ZLE — cofanie akcji (undo) za pomoca kolejki
# Kolejka daje FIFO — cofniecie usunie NAJSTARSZA akcje, nie ostatnia!
kolejka_akcji = Kolejka()
kolejka_akcji.enqueue("wpisz A")
kolejka_akcji.enqueue("wpisz B")
kolejka_akcji.enqueue("wpisz C")
cofnieta = kolejka_akcji.dequeue()  # "wpisz A" — to NIE jest ostatnia akcja!

# DOBRZE — uzyj stosu (LIFO)
stos_akcji = Stos()
stos_akcji.push("wpisz A")
stos_akcji.push("wpisz B")
stos_akcji.push("wpisz C")
cofnieta = stos_akcji.pop()  # "wpisz C" — poprawnie, ostatnia akcja
```

### 2.10. Dobre praktyki

#### Uzywaj `deque` zamiast `list` dla kolejek

```python
# DOBRZE — zawsze uzywaj deque dla operacji kolejkowych
from collections import deque

kolejka = deque()
kolejka.append("zadanie_1")   # enqueue
kolejka.append("zadanie_2")
print(kolejka.popleft())      # dequeue -> "zadanie_1"
```

#### Uzywaj `maxlen` dla buforow o stalym rozmiarze

```python
# DOBRZE — deque z maxlen automatycznie usuwa stare elementy
from collections import deque

# Bufor ostatnich 5 logów
logi = deque(maxlen=5)
for i in range(10):
    logi.append(f"log_{i}")

print(list(logi))  # ['log_5', 'log_6', 'log_7', 'log_8', 'log_9']
# Stare logi (0-4) zostaly automatycznie usuniete!
```

#### Sprawdzaj pustosc przed dequeue

```python
# DOBRZE — zawsze sprawdzaj przed dekolejkowaniem
if not kolejka.jest_pusta():
    element = kolejka.dequeue()
else:
    print("Kolejka pusta — nic do przetworzenia")
```

#### Kolejka priorytetowa zamiast sortowania

```python
# ZLE — sortowanie calej listy zadan za kazdym razem
import heapq

# DOBRZE — uzyj kolejki priorytetowej
zadania = []
heapq.heappush(zadania, (3, "mniej wazne"))
heapq.heappush(zadania, (1, "pilne!"))
heapq.heappush(zadania, (2, "normalne"))

while zadania:
    priorytet, zadanie = heapq.heappop(zadania)
    print(f"[{priorytet}] {zadanie}")
# [1] pilne!
# [2] normalne
# [3] mniej wazne
```

### 2.11. Algorytmy z uzyciem kolejki

#### BFS — przeszukiwanie wszerz

Kolejka jest fundamentem algorytmu BFS, ktory odwiedza wezly grafu poziomami (najpierw wszyscy sasiedzi, potem sasiedzi sasiadow itd.).

```python
def bfs(graf: dict, start) -> list:
    """Przeszukuje graf wszerz (BFS) i zwraca liste odwiedzonych wezlow.

    Kolejka gwarantuje przetwarzanie wezlow w kolejnosci odkrywania —
    najpierw najblizsi sasiedzi, potem dalsi (poziom po poziomie).
    """
    odwiedzone = {start}
    kolejka = Kolejka()
    kolejka.enqueue(start)
    wynik = []

    while not kolejka.jest_pusta():
        wezel = kolejka.dequeue()
        wynik.append(wezel)
        for sasiad in graf.get(wezel, []):
            if sasiad not in odwiedzone:
                odwiedzone.add(sasiad)
                kolejka.enqueue(sasiad)

    return wynik


graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
print(bfs(graf, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
#                             poziom 0  poziom 1    poziom 2
```

#### BFS — najkrotsza sciezka w grafie niewazonym

```python
def najkrotsza_sciezka(graf: dict, start, cel) -> list:
    """Zwraca najkrotsza sciezke od start do cel (liczba krawedzi).

    BFS gwarantuje znalezienie najkrotszej sciezki w grafach niewazonych,
    bo odwiedza wezly rosnaco wedlug odleglosci od startu.
    """
    if start == cel:
        return [start]

    odwiedzone = {start}
    kolejka = Kolejka()
    kolejka.enqueue([start])  # przechowujemy cala sciezke, nie tylko wezel

    while not kolejka.jest_pusta():
        sciezka = kolejka.dequeue()
        wezel = sciezka[-1]
        for sasiad in graf.get(wezel, []):
            if sasiad not in odwiedzone:
                nowa_sciezka = sciezka + [sasiad]
                if sasiad == cel:
                    return nowa_sciezka
                odwiedzone.add(sasiad)
                kolejka.enqueue(nowa_sciezka)

    return []  # brak sciezki


graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': ['F'], 'F': []
}
print(najkrotsza_sciezka(graf, 'A', 'F'))  # ['A', 'C', 'F']
```

#### Symulacja kolejki obslugi (Hot Potato)

Klasyczna symulacja gry "goracy ziemniak" — element jest przekazywany n razy, a osoba trzymajaca go odpada.

```python
def hot_potato(osoby: list, liczba: int) -> str:
    """Symuluje gre Hot Potato (goracy ziemniak).

    Kolejka symuluje krag: dequeue pobiera osobe z przodu,
    enqueue dodaje ja z powrotem — n razy. Przy n-tym podaniu osoba odpada.
    """
    kolejka = Kolejka()
    for osoba in osoby:
        kolejka.enqueue(osoba)

    while kolejka.rozmiar() > 1:
        # Przekazuj ziemniak n razy
        for _ in range(liczba):
            kolejka.enqueue(kolejka.dequeue())
        # Osoba trzymajaca ziemniak po n przekazaniach odpada
        wypadla = kolejka.dequeue()
        print(f"Odpada: {wypadla}")

    return kolejka.dequeue()


zwyciezca = hot_potato(["Anna", "Bob", "Celina", "Dawid", "Ewa"], 7)
print(f"Zwyciezca: {zwyciezca}")
```

#### Drukowanie binarnych liczb od 1 do n

```python
def binarne_od_1_do_n(n: int) -> list:
    """Generuje binarne reprezentacje liczb 1..n uzywajac kolejki.

    Idea: zaczynamy od "1". Dla kazdej liczby generujemy dwie kolejne
    przez dolaczenie "0" i "1". Kolejka zachowuje wlasciwa kolejnosc.
    """
    wynik = []
    kolejka = Kolejka()
    kolejka.enqueue("1")

    for _ in range(n):
        przod = kolejka.dequeue()
        wynik.append(przod)
        kolejka.enqueue(przod + "0")
        kolejka.enqueue(przod + "1")

    return wynik


print(binarne_od_1_do_n(7))
# ['1', '10', '11', '100', '101', '110', '111']
#   1    2     3     4      5      6      7
```

---

## 3. Lista jednokierunkowa (Singly Linked List)

### 3.1. Czym jest lista jednokierunkowa?

Lista jednokierunkowa (ang. *singly linked list*) to dynamiczna struktura danych zlozona z **wezlow** (ang. *nodes*). Kazdy wezel przechowuje:
- **dane** — wartosc elementu,
- **wskaznik** — referencje do nastepnego wezla w liscie.

Ostatni wezel wskazuje na `None`, co sygnalizuje koniec listy.

**Analogie z zycia codziennego:**

- **Pociag** — wagony (wezly) polaczone hakami (wskaznikami) w jednym kierunku. Mozesz isc od lokomotywy do ostatniego wagonu, ale nie mozesz sie cofnac.
- **Lancuch** — kazde ogniwo jest polaczone z nastepnym. Mozesz dodac nowe ogniwo w dowolnym miejscu, rozlaczajac i laczac ogniwa.
- **Poscig policyjny** — swiadek mowi "uciekl w te strone" (wskaznik), idziesz do nastepnego swiadka, ktory mowi to samo. Nie mozesz sie cofnac, bo nikt nie wskazuje wstecz.

```
Lista jednokierunkowa:

  glowa
    |
   [10] ---> [20] ---> [30] ---> [40] ---> None
   dane: 10  dane: 20  dane: 30  dane: 40
   nast: *   nast: *   nast: *   nast: None
```

### 3.2. Tablica vs lista — roznica w pamieci

To fundamentalna roznica, ktora wplywna na wydajnosc WSZYSTKICH operacji.

```
TABLICA (ciagly blok pamieci):
Adres:  1000  1004  1008  1012
        [ 10 ][ 20 ][ 30 ][ 40 ]
         [0]   [1]   [2]   [3]
Dostep do arr[i]: adres = 1000 + i * 4  --> O(1)
Wstawienie w srodku: trzeba przesunac elementy --> O(n)

LISTA JEDNOKIERUNKOWA (wezly rozrzucone w pamieci):
Adres:  1000         2048         3512         5001
        [10 | 2048]-->[20 | 3512]-->[30 | 5001]-->[40 | None]
         glowa
Dostep do i-tego elementu: trzeba przejsc od glowy --> O(n)
Wstawienie (gdy mamy wskaznik): przepiecie wskaznikow --> O(1)
```

**Kluczowe konsekwencje:**
- Tablice maja O(1) dostep po indeksie, ale O(n) wstawianie/usuwanie w srodku (przesuwanie elementow).
- Listy maja O(n) dostep, ale O(1) wstawianie/usuwanie, gdy mamy wskaznik do wezla poprzedzajacego.
- Lista nie wymaga z gory rezerwowania ciaglego bloku pamieci — rosnie dynamicznie.

```
Wstawianie w srodku — porownanie:

TABLICA — wstaw 25 na indeks 2:
  PRZED:  [10] [20] [30] [40] [__]
  Krok 1: przesun 30 i 40 w prawo: [10] [20] [__] [30] [40]
  Krok 2: wstaw: [10] [20] [25] [30] [40]
  Koszt: O(n) — przesuwanie elementow

LISTA — wstaw 25 po wezle z wartoscia 20:
  PRZED:  [10]->[20]->[30]->[40]->None
  Krok 1: nowy = [25]
  Krok 2: nowy.nast = [30]     (nowy wskazuje na nastepnik [20])
  Krok 3: [20].nast = [25]     (przepinamy wskaznik)
  PO:     [10]->[20]->[25]->[30]->[40]->None
  Koszt: O(1) — tylko przepiecie wskaznikow (jesli juz mamy wskaznik do [20])
```

### 3.3. Implementacja wezla i listy

```python
class Wezel:
    """Pojedynczy wezel listy jednokierunkowej."""

    def __init__(self, dane):
        self.dane = dane
        self.nastepny = None  # wskaznik na kolejny wezel


class ListaJednokierunkowa:
    """Lista jednokierunkowa z podstawowymi operacjami."""

    def __init__(self):
        self.glowa = None  # wskaznik na pierwszy wezel (head)
        self._rozmiar = 0  # przechowujemy rozmiar, by dlugosc() bylo O(1)

    # ------------------------------------------------------------------ #
    # Wstawianie                                                           #
    # ------------------------------------------------------------------ #

    def dodaj_na_poczatek(self, dane):
        """O(1) — wstawia nowy wezel przed aktualna glowa."""
        nowy = Wezel(dane)
        nowy.nastepny = self.glowa
        self.glowa = nowy
        self._rozmiar += 1

    def dodaj_na_koniec(self, dane):
        """O(n) — wstawia nowy wezel na koncu listy.

        Wymaga przejscia calej listy, by znalezc ostatni wezel.
        Mozna zoptymalizowac do O(1) przechowujac wskaznik na ogon.
        """
        nowy = Wezel(dane)
        if self.glowa is None:
            self.glowa = nowy
        else:
            aktualny = self.glowa
            while aktualny.nastepny is not None:
                aktualny = aktualny.nastepny
            aktualny.nastepny = nowy
        self._rozmiar += 1

    def dodaj_po(self, wezel, dane):
        """O(1) — wstawia nowy wezel bezposrednio po podanym wezle."""
        if wezel is None:
            raise ValueError("Podany wezel nie moze byc None.")
        nowy = Wezel(dane)
        nowy.nastepny = wezel.nastepny
        wezel.nastepny = nowy
        self._rozmiar += 1

    # ------------------------------------------------------------------ #
    # Usuwanie                                                             #
    # ------------------------------------------------------------------ #

    def usun_pierwszy(self):
        """O(1) — usuwa i zwraca dane z pierwszego wezla."""
        if self.glowa is None:
            raise IndexError("Lista jest pusta.")
        dane = self.glowa.dane
        self.glowa = self.glowa.nastepny
        self._rozmiar -= 1
        return dane

    def usun_wartosc(self, dane):
        """O(n) — usuwa pierwsze wystapienie podanej wartosci."""
        if self.glowa is None:
            raise ValueError("Lista jest pusta.")

        # Szczegolny przypadek: usuwamy glowe
        if self.glowa.dane == dane:
            self.glowa = self.glowa.nastepny
            self._rozmiar -= 1
            return

        aktualny = self.glowa
        while aktualny.nastepny is not None:
            if aktualny.nastepny.dane == dane:
                aktualny.nastepny = aktualny.nastepny.nastepny
                self._rozmiar -= 1
                return
            aktualny = aktualny.nastepny

        raise ValueError(f"Wartosc {dane} nie istnieje w liscie.")

    # ------------------------------------------------------------------ #
    # Wyszukiwanie i dostep                                                #
    # ------------------------------------------------------------------ #

    def szukaj(self, dane):
        """O(n) — zwraca wezel z podana wartoscia lub None."""
        aktualny = self.glowa
        while aktualny is not None:
            if aktualny.dane == dane:
                return aktualny
            aktualny = aktualny.nastepny
        return None

    def pobierz(self, indeks: int):
        """O(n) — zwraca wartosc elementu o podanym indeksie."""
        if indeks < 0 or indeks >= self._rozmiar:
            raise IndexError(f"Indeks {indeks} poza zakresem.")
        aktualny = self.glowa
        for _ in range(indeks):
            aktualny = aktualny.nastepny
        return aktualny.dane

    def dlugosc(self):
        """O(1) — zwraca liczbe wezlow."""
        return self._rozmiar

    # ------------------------------------------------------------------ #
    # Pomocnicze                                                           #
    # ------------------------------------------------------------------ #

    def odwroc(self):
        """O(n) — odwraca liste w miejscu (in-place)."""
        poprzedni = None
        aktualny = self.glowa
        while aktualny is not None:
            nastepny = aktualny.nastepny  # zapamietaj kolejny
            aktualny.nastepny = poprzedni  # odwroc wskaznik
            poprzedni = aktualny           # przesun poprzedni
            aktualny = nastepny            # przesun aktualny
        self.glowa = poprzedni

    def __len__(self):
        return self._rozmiar

    def __iter__(self):
        aktualny = self.glowa
        while aktualny is not None:
            yield aktualny.dane
            aktualny = aktualny.nastepny

    def __str__(self):
        return " -> ".join(str(x) for x in self) + " -> None"
```

### 3.4. Operacje krok po kroku

#### Wstawianie na poczatku — `dodaj_na_poczatek(5)`

```
PRZED:  glowa
          |
         [10] -> [20] -> [30] -> None

KROK 1: Tworzysz nowy wezel: nowy = Wezel(5)
        nowy: [5 | None]

KROK 2: nowy.nastepny = glowa  (nowy wskazuje na stary pierwszy wezel)
        nowy: [5 | *]-->[10]->[20]->[30]->None

KROK 3: glowa = nowy  (przestawiamy glowe)
         glowa
           |
          [5] -> [10] -> [20] -> [30] -> None
```

#### Wstawianie na koncu — `dodaj_na_koniec(40)`

```
PRZED:  glowa
          |
         [10] -> [20] -> [30] -> None

KROK 1: Tworzysz nowy wezel: nowy = Wezel(40)
        nowy: [40 | None]

KROK 2: Przechodzisz od glowy do ostatniego wezla:
        aktualny = [10] -> [20] -> [30]  (stop, bo [30].nastepny == None)

KROK 3: aktualny.nastepny = nowy
         glowa
           |
          [10] -> [20] -> [30] -> [40] -> None
```

#### Wstawianie w srodku — `dodaj_po(wezel_20, 25)`

```
PRZED:  glowa
          |
         [10] -> [20] -> [30] -> None
                   ^
                   wezel_20

KROK 1: nowy = Wezel(25)
KROK 2: nowy.nastepny = wezel_20.nastepny  (nowy wskazuje na [30])
KROK 3: wezel_20.nastepny = nowy           (wezel_20 wskazuje na nowy)

PO:     glowa
          |
         [10] -> [20] -> [25] -> [30] -> None
```

#### Usuwanie wezla ze srodka — `usun_wartosc(20)`

```
PRZED:  glowa
          |
         [10] -> [20] -> [30] -> None

KROK 1: Idziemy do wezla POPRZEDZAJACEGO usuwany:
        aktualny = wezel z wartoscia 10

KROK 2: aktualny.nastepny = aktualny.nastepny.nastepny
        [10].nastepny = [20].nastepny = wezel [30]

PO:    glowa
         |
        [10] -> [30] -> None
        (wezel [20] zostaje odlaczony i usuniety przez garbage collector)
```

> **Dlaczego potrzebujemy wezla poprzedzajacego?**
> Lista jest jednokierunkowa — nie mozna cofnac wskaznika. Musimy znac wezel przed usuwanym, by przepiac jego wskaznik `nastepny`.

#### Odwracanie listy — `odwroc()`

Odwracanie in-place uzywa trzech zmiennych: `poprzedni`, `aktualny`, `nastepny`.

```
PRZED: None <- poprzedni    aktualny    nastepny
                              |
               None <- [10] -> [20] -> [30] -> None

KROK 1 (aktualny = 10):
  nastepny = [20]
  [10].nastepny = None   (odwrocono!)
  poprzedni = [10]
  aktualny = [20]

KROK 2 (aktualny = 20):
  nastepny = [30]
  [20].nastepny = [10]   (odwrocono!)
  poprzedni = [20]
  aktualny = [30]

KROK 3 (aktualny = 30):
  nastepny = None
  [30].nastepny = [20]   (odwrocono!)
  poprzedni = [30]
  aktualny = None  --> koniec petli

glowa = poprzedni = [30]
PO: [30] -> [20] -> [10] -> None
```

### 3.5. Zlozonosc obliczeniowa

| Operacja | Zlozonosc czasowa | Zlozonosc pamieciowa |
|----------|-------------------|----------------------|
| Dostep po indeksie (`pobierz`) | O(n) | O(1) |
| Wstawienie na poczatku (`dodaj_na_poczatek`) | O(1) | O(1) |
| Wstawienie na koncu (`dodaj_na_koniec`) | O(n)* | O(1) |
| Wstawienie po wezle (`dodaj_po`) | O(1) | O(1) |
| Usuniecie z poczatku (`usun_pierwszy`) | O(1) | O(1) |
| Usuniecie ze srodka/konca (`usun_wartosc`) | O(n) | O(1) |
| Wyszukiwanie (`szukaj`) | O(n) | O(1) |
| Odwracanie (`odwroc`) | O(n) | O(1) |
| Wykrywanie cyklu (Floyd) | O(n) | O(1) |
| Dlugosc (`dlugosc`) | O(1)** | O(1) |

\* Mozna zoptymalizowac do O(1) przechowujac wskaznik na ogon (jak w `KolejkaNaLiscie`).

\*\* Dzieki przechowywaniu `_rozmiar` jako pola. Bez tego bylaby O(n) (trzeba przejsc cala liste).

### 3.6. Ograniczenia — czego NIE MOZNA robic

**1. Brak dostepu losowego (random access) w O(1)**

Nie mozna odczytac i-tego elementu bez przejscia od glowy. To O(n), a nie O(1) jak w tablicy.

```
Chcesz element o indeksie 3?

  [10] -> [20] -> [30] -> [40] -> [50] -> None
   ^       ^       ^       ^
   i=0     i=1     i=2     i=3   <-- musisz przejsc 4 wezly!

W tablicy: arr[3] -> O(1) (jeden skok do adresu w pamieci)
W liscie: musisz przejsc 3 -> O(n) (sekwencyjne przechodzenie)
```

**Dlaczego?** Wezly listy sa rozrzucone w pamieci — nie ma wzoru "adres = baza + i * rozmiar". Jedyny sposob dotarcia do wezla to podazanie za wskaznikami od poczatku.

**2. Brak cofania (traversal wsteczny)**

Lista jednokierunkowa nie ma wskaznikow wstecz. Nie mozna przejsc od konca do poczatku.

```
  [10] -> [20] -> [30] -> None
                    ^
                    Jestes tutaj. Chcesz wrocic do [20]?
                    NIE MOZESZ — brak wskaznika wstecznego!
                    Musisz zaczac od glowy i przejsc od nowa.
```

**Dlaczego?** Kazdy wezel ma TYLKO wskaznik `nastepny`. Gdyby mial tez `poprzedni`, bylaby to lista **dwukierunkowa** (doubly linked list) — inna struktura.

**3. Brak wyszukiwania binarnego**

Nawet jesli lista jest posortowana, binary search nie dziala — bo nie masz dostepu O(1) do srodkowego elementu.

**4. Narzut pamieci na wskazniki**

Kazdy wezel przechowuje dodatkowy wskaznik (`nastepny`), co zuzywa wiecej pamieci niz tablica z tymi samymi danymi.

```
Tablica 4 intow:  [10, 20, 30, 40]  -> 4 * 8 bajtow = 32 bajty
Lista 4 wezlow:   kazdy wezel = dane (8B) + wskaznik (8B) = 16B
                  4 * 16 = 64 bajty -> PODWOJNY koszt pamieci!
```

> **Wniosek:** Lista jednokierunkowa jest dobra, gdy czesto wstawiasz/usuwasz z poczatku lub srodka (majac wskaznik), ale zla jesli potrzebujesz szybkiego dostepu po indeksie lub wyszukiwania binarnego.

### 3.7. Zle praktyki

#### Brak obslugi przypadku pustej listy

```python
# ZLE — zapomnielismy o pustej liscie
def dodaj_na_koniec(self, dane):
    nowy = Wezel(dane)
    aktualny = self.glowa
    while aktualny.nastepny is not None:  # BLAD: AttributeError jesli glowa is None!
        aktualny = aktualny.nastepny
    aktualny.nastepny = nowy

# DOBRZE — sprawdzamy czy lista jest pusta
def dodaj_na_koniec(self, dane):
    nowy = Wezel(dane)
    if self.glowa is None:
        self.glowa = nowy
        return
    aktualny = self.glowa
    while aktualny.nastepny is not None:
        aktualny = aktualny.nastepny
    aktualny.nastepny = nowy
```

#### Modyfikacja listy podczas iteracji

```python
# ZLE — usuwamy elementy podczas przechodzenia przez liste
aktualny = lista.glowa
while aktualny:
    if aktualny.dane % 2 == 0:
        lista.usun_wartosc(aktualny.dane)  # niszczymy strukture!
    aktualny = aktualny.nastepny  # aktualny.nastepny moze byc juz None!

# DOBRZE — zbieramy wartosci do usuniecia, potem usuwamy
do_usuniecia = [x for x in lista if x % 2 == 0]
for wartosc in do_usuniecia:
    lista.usun_wartosc(wartosc)
```

#### Utrata referencji do reszty listy

```python
# ZLE — utracilismy cala reszte listy!
def zle_wstaw_po(wezel, nowy_wezel):
    wezel.nastepny = nowy_wezel  # BLAD: nowy_wezel.nastepny jest None!
    # Wszystko co bylo po wezel jest stracone.

# DOBRZE — najpierw polacz nowy wezel z reszta, potem z poprzednikiem
def dobrze_wstaw_po(wezel, nowy_wezel):
    nowy_wezel.nastepny = wezel.nastepny  # NAJPIERW polacz z reszta
    wezel.nastepny = nowy_wezel           # POTEM przepnij poprzednika
```

> **Zasada:** Przy wstawianiu/usuwaniu zawsze NAJPIERW podlacz nowy wezel do reszty listy, a POTEM przepnij wskaznik z poprzedniego wezla. W odwrotnej kolejnosci stracisz referencje.

#### Uzywanie listy jednokierunkowej zamiast tablicy gdy potrzebujesz dostepu po indeksie

```python
# ZLE — czesty dostep po indeksie w liscie jednokierunkowej
lista = ListaJednokierunkowa()
for i in range(1000):
    lista.dodaj_na_koniec(i)

# 1000 razy pobieramy element po indeksie — kazde pobierz to O(n)!
for i in range(1000):
    wartosc = lista.pobierz(i)  # lacznie O(n^2)!

# DOBRZE — uzyj zwyklej listy Pythona (tablicy dynamicznej)
dane = list(range(1000))
for i in range(1000):
    wartosc = dane[i]  # O(1) — lacznie O(n)
```

### 3.8. Dobre praktyki

#### Przechowuj rozmiar jako pole

```python
# DOBRZE — rozmiar w O(1) dzieki osobnemu polu
class ListaJednokierunkowa:
    def __init__(self):
        self.glowa = None
        self._rozmiar = 0  # aktualizuj przy kazdym dodaj/usun

    def dlugosc(self):
        return self._rozmiar  # O(1)!

# ZLE — liczenie dlugosci za kazdym razem
def dlugosc(self):
    licznik = 0
    aktualny = self.glowa
    while aktualny:
        licznik += 1
        aktualny = aktualny.nastepny
    return licznik  # O(n) za kazdym razem!
```

#### Uzywaj wezla-straznika (sentinel) do uproszczenia kodu

```python
# DOBRZE — wezel-straznik eliminuje przypadki brzegowe
class ListaZeStraznikiem:
    def __init__(self):
        self._straznik = Wezel(None)  # "sztuczna" glowa — nigdy nie jest usuwana
        self._rozmiar = 0

    def dodaj_na_poczatek(self, dane):
        """Nie trzeba sprawdzac, czy lista jest pusta!"""
        nowy = Wezel(dane)
        nowy.nastepny = self._straznik.nastepny
        self._straznik.nastepny = nowy
        self._rozmiar += 1

    def usun_wartosc(self, dane):
        """Nie trzeba osobno obslugiwac usuwania glowy!"""
        aktualny = self._straznik  # zaczynamy od straznika
        while aktualny.nastepny is not None:
            if aktualny.nastepny.dane == dane:
                aktualny.nastepny = aktualny.nastepny.nastepny
                self._rozmiar -= 1
                return
            aktualny = aktualny.nastepny
        raise ValueError(f"Wartosc {dane} nie istnieje w liscie.")
```

#### Implementuj `__iter__` do wygodnego przechodzenia

```python
# DOBRZE — protokol iteratora pozwala uzywac for/in
class ListaJednokierunkowa:
    def __iter__(self):
        aktualny = self.glowa
        while aktualny is not None:
            yield aktualny.dane
            aktualny = aktualny.nastepny

# Teraz mozna:
for wartosc in lista:
    print(wartosc)

# Albo:
wartosci = list(lista)  # konwersja do listy Pythona
suma = sum(lista)       # suma elementow
```

#### Przechowuj wskaznik na ogon dla czestych operacji na koncu

```python
# DOBRZE — dodaj_na_koniec w O(1) dzieki wskaznikowi na ogon
class ListaZOgonem:
    def __init__(self):
        self.glowa = None
        self._ogon = None
        self._rozmiar = 0

    def dodaj_na_koniec(self, dane):
        """O(1) — dzieki wskaznikowi na ogon."""
        nowy = Wezel(dane)
        if self._ogon is not None:
            self._ogon.nastepny = nowy
        else:
            self.glowa = nowy
        self._ogon = nowy
        self._rozmiar += 1
```

### 3.9. Algorytmy na listach

#### Znajdowanie srodkowego elementu — algorytm dwoch wskaznikow

Klasyczna technika: jeden wskaznik (`wolny`) przesuwa sie o 1 wezel, drugi (`szybki`) o 2. Gdy szybki dotrze do konca, wolny jest w polowie.

```python
def znajdz_srodek(glowa: Wezel) -> Wezel:
    """O(n) czas, O(1) pamiec — zwraca wezel srodkowy listy.

    Dla parzystej liczby wezlow zwraca drugi z dwoch srodkowych.
    """
    if glowa is None:
        return None
    wolny = glowa
    szybki = glowa
    while szybki is not None and szybki.nastepny is not None:
        wolny = wolny.nastepny
        szybki = szybki.nastepny.nastepny
    return wolny


# Przyklad:
# Lista: [1] -> [2] -> [3] -> [4] -> [5] -> None
# Wynik: wezel z wartoscia 3
#
# Lista: [1] -> [2] -> [3] -> [4] -> None
# Wynik: wezel z wartoscia 3 (drugi srodkowy)
```

```
Wizualizacja algorytmu dwoch wskaznikow:

Lista: [1] -> [2] -> [3] -> [4] -> [5] -> None

Krok 0: wolny=[1], szybki=[1]
Krok 1: wolny=[2], szybki=[3]
Krok 2: wolny=[3], szybki=[5]
Krok 3: szybki.nastepny == None -> STOP

wolny wskazuje na [3] = srodek!
```

#### Wykrywanie cyklu — algorytm Floyda (zolw i zajac)

```python
def ma_cykl(glowa: Wezel) -> bool:
    """O(n) czas, O(1) pamiec — wykrywa cykl w liscie (algorytm Floyda).

    Idea: jesli lista ma cykl, szybki wskaznik w koncu dogoni wolny
    wewnatrz tego cyklu, jak biegacz na torze okreznym.
    """
    if glowa is None:
        return False
    wolny = glowa
    szybki = glowa
    while szybki is not None and szybki.nastepny is not None:
        wolny = wolny.nastepny
        szybki = szybki.nastepny.nastepny
        if wolny is szybki:   # te same obiekty w pamieci
            return True
    return False


# Dlaczego dziala?
# Bez cyklu: szybki dotrze do None i petla sie skonczy.
# Z cyklem: obaj wskaznicy wchodza do cyklu. Szybki "goni" wolnego
# i musi go dogonic, bo odleglosc miedzy nimi maleje o 1 w kazdym kroku.
```

```
Wizualizacja cyklu:

  [1] -> [2] -> [3] -> [4] -> [5]
                  ^                |
                  |________________|    <-- cykl! [5].nastepny = [3]

  Bez algorytmu Floyda musielibysmy zapamietywac odwiedzone wezly (O(n) pamieci).
  Z Floydem: O(1) pamieci (tylko dwa wskazniki).
```

#### Scalanie dwoch posortowanych list

```python
def scal_posortowane(l1: Wezel, l2: Wezel) -> Wezel:
    """O(n + m) — scala dwie posortowane listy w jedna posortowana liste.

    Technika: wezel-straznik (sentinel) eliminuje szczegolny przypadek
    pustej listy wynikowej na poczatku algorytmu.
    """
    straznik = Wezel(0)   # wezel pomocniczy — jego dane nas nie interesuja
    aktualny = straznik

    while l1 is not None and l2 is not None:
        if l1.dane <= l2.dane:
            aktualny.nastepny = l1
            l1 = l1.nastepny
        else:
            aktualny.nastepny = l2
            l2 = l2.nastepny
        aktualny = aktualny.nastepny

    # Dolacz pozostale wezly (co najwyzej jedna z list jest niepusta)
    aktualny.nastepny = l1 if l1 is not None else l2

    return straznik.nastepny  # pomijamy wezel-straznik


# Przyklad:
# L1: [1] -> [3] -> [5] -> None
# L2: [2] -> [4] -> [6] -> None
# Wynik: [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> None
```

#### Usuwanie n-tego elementu od konca

```python
def usun_nth_od_konca(glowa: Wezel, n: int) -> Wezel:
    """O(L) czas, O(1) pamiec — usuwa n-ty wezel od konca listy.

    Technika dwoch wskaznikow z odstepem n wezlow:
    gdy szybki dotrze do konca, wolny jest dokladnie przy wezle do usuniecia.
    """
    straznik = Wezel(0)
    straznik.nastepny = glowa
    wolny = straznik
    szybki = straznik

    # Przesun szybki o n+1 krokow do przodu
    for _ in range(n + 1):
        szybki = szybki.nastepny

    # Przesun oba wskazniki az szybki dotrze do konca
    while szybki is not None:
        wolny = wolny.nastepny
        szybki = szybki.nastepny

    # wolny wskazuje teraz na wezel PRZED usuwanym
    wolny.nastepny = wolny.nastepny.nastepny
    return straznik.nastepny
```

```
Wizualizacja usuwania 2. elementu od konca:

  straznik -> [1] -> [2] -> [3] -> [4] -> [5] -> None
  ^wolny                                           ^szybki (po 3 krokach)

  Przesuwamy oba:
  straznik -> [1] -> [2] -> [3] -> [4] -> [5] -> None
                      ^wolny                       ^szybki

  Jeszcze raz:
  straznik -> [1] -> [2] -> [3] -> [4] -> [5] -> None
                              ^wolny               ^szybki (= None po przesunieciu)

  wolny.nastepny = wolny.nastepny.nastepny
  = [3].nastepny = [5]

  Wynik: [1] -> [2] -> [3] -> [5] -> None  (usuniety [4])
```

---

## 4. Porownanie struktur

### 4.1. Tabela zlozonosci — wszystkie struktury obok siebie

| Operacja | Tablica (`list`) | Lista jednokierunkowa | Stos | Kolejka (deque) |
|----------|-----------------|----------------------|------|----------------|
| Dostep po indeksie | **O(1)** | O(n) | O(n)* | O(n)* |
| Wstawienie na poczatku | O(n) | **O(1)** | **O(1)** | **O(1)** |
| Wstawienie na koncu | **O(1)** amort. | O(n)** | **O(1)** amort. | **O(1)** |
| Wstawienie w srodku | O(n) | **O(1)***  | N/A | N/A |
| Usuniecie z poczatku | O(n) | **O(1)** | N/A | **O(1)** |
| Usuniecie z konca | **O(1)** | O(n) | **O(1)** | **O(1)** |
| Usuniecie ze srodka | O(n) | O(n) | N/A | N/A |
| Wyszukiwanie | O(n) | O(n) | O(n) | O(n) |

\* Stos i kolejka z definicji nie oferuja dostepu po indeksie — to nie jest ich przeznaczenie.

\*\* O(1) jesli przechowujemy wskaznik na ogon.

\*\*\* O(1) jesli juz mamy wskaznik do wezla poprzedzajacego (znalezienie go to O(n)).

### 4.2. Tabela pamieciowa

| Struktura | Pamiec na n elementow | Narzut | Uwagi |
|-----------|----------------------|--------|-------|
| Tablica (`list`) | O(n) | Nadmiar przy realokacji (~12.5%) | Ciagly blok pamieci |
| Lista jednokierunkowa | O(n) | +1 wskaznik na wezel (8B) | Wezly rozrzucone w pamieci |
| Stos na `list` | O(n) | Jak tablica | — |
| Stos na liscie | O(n) | +1 wskaznik na wezel | — |
| Kolejka na `deque` | O(n) | Bloki po 64 elementy | Wewnetrznie lista blokow |
| Kolejka cykliczna | O(pojemnosc) | Staly rozmiar | Bez realokacji |

> **Uwaga o cache:** Tablice sa szybsze w praktyce niz listy wskaznikowe (nawet jesli zlozonosc jest taka sama), bo elementy sa obok siebie w pamieci — procesor moze je efektywnie cachowac. Wezly listy sa rozrzucone — kazdy dostep to potencjalne "cache miss".

### 4.3. Kiedy uzywac ktorej struktury?

| Mam problem... | Uzyj struktury | Dlaczego |
|----------------|---------------|----------|
| Cofanie akcji (undo/redo) | **Stos** | LIFO — ostatnia akcja cofana pierwsza |
| Przechodzenie grafu w glab (DFS) | **Stos** | DFS = LIFO |
| Ewaluacja wyrazen (ONP) | **Stos** | Operandy na stos, operator zdejmuje dwa |
| Sprawdzanie nawiasow | **Stos** | Otwierajacy na stos, zamykajacy sprawdza |
| Kolejkowanie zadan (scheduler) | **Kolejka** | FIFO — kto pierwszy, ten obsluzony |
| Przechodzenie grafu wszerz (BFS) | **Kolejka** | BFS = FIFO |
| Buforowanie danych (producer-consumer) | **Kolejka** | Producent enqueue, konsument dequeue |
| Czeste wstawianie/usuwanie na poczatku | **Lista jednokierunkowa** | O(1) wstawianie na poczatek |
| Potrzebujesz szybkiego dostepu po indeksie | **Tablica (`list`)** | O(1) random access |
| Operacje na obu koncach | **`deque`** | O(1) na obu koncach |
| Kolejka o stalym rozmiarze, bez alokacji | **Kolejka cykliczna** | Staly rozmiar, brak realokacji |
| Przetwarzanie wg priorytetu | **Kolejka priorytetowa (`heapq`)** | Zawsze pobiera element o najwyzszym priorytecie |
| Wielowatkowe producer-consumer | **`queue.Queue`** | Thread-safe z blokadami |

---

## 5. Typowe bledy i pulapki

### 1. Zapomnienie o przypadku brzegowym pustej struktury

```python
# ZLE — brak sprawdzenia pustosci
def zle_pop(stos):
    return stos._dane.pop()   # IndexError gdy stos jest pusty

# DOBRZE
def dobre_pop(stos):
    if stos.jest_pusty():
        raise IndexError("Stos jest pusty.")
    return stos._dane.pop()
```

### 2. Gubienie ogona kolejki przy dequeue

```python
# ZLE — klasyczny blad: nie zerujemy _ogon gdy kolejka sie oproznia
def zle_dequeue(self):
    wartosc = self._glowa.dane
    self._glowa = self._glowa.nastepny
    # BRAK: if self._glowa is None: self._ogon = None
    # Ogon nadal wskazuje na usuniety wezel! Nastepne enqueue uszkodzi strukture.
    return wartosc
```

### 3. Uzywanie `list.pop(0)` jako kolejki

```python
# Pulapka wydajnosciowa:
import time

n = 100_000
dane = list(range(n))

# Naiwna "kolejka" na liscie — O(n^2)
start = time.time()
q = list(range(n))
while q:
    q.pop(0)
print(f"list.pop(0): {time.time() - start:.3f}s")  # ~sekundy

# Wlasciwa kolejka — O(n)
from collections import deque
start = time.time()
q = deque(range(n))
while q:
    q.popleft()
print(f"deque.popleft(): {time.time() - start:.3f}s")  # milisekundy
```

### 4. Modyfikacja listy podczas iteracji

```python
lista = ListaJednokierunkowa()
for i in range(5):
    lista.dodaj_na_koniec(i)

# ZLE — usuwamy elementy podczas przechodzenia przez liste
aktualny = lista.glowa
while aktualny:
    if aktualny.dane % 2 == 0:
        lista.usun_wartosc(aktualny.dane)  # niszczymy strukture podczas iteracji!
    aktualny = aktualny.nastepny  # aktualny.nastepny moze byc juz niepoprawny!

# DOBRZE — zbieramy wartosci do usuniecia, potem usuwamy
do_usuniecia = [x for x in lista if x % 2 == 0]
for wartosc in do_usuniecia:
    lista.usun_wartosc(wartosc)
```

### 5. Przepelnienie stosu przy glebokiej rekurencji

```python
# ZLE — moze wywolac RecursionError dla duzych n:
def suma_rekurencyjna(n):
    if n == 0:
        return 0
    return n + suma_rekurencyjna(n - 1)

# BEZPIECZNA wersja iteracyjna:
def suma_iteracyjna(n):
    return n * (n + 1) // 2   # wzor matematyczny, O(1)

# Lub z jawnym stosem, gdy nie ma prostego wzoru:
def suma_ze_stosem(n):
    stos = Stos()
    while n > 0:
        stos.push(n)
        n -= 1
    wynik = 0
    while not stos.jest_pusty():
        wynik += stos.pop()
    return wynik
```

### 6. Utrata wskaznikow przy wstawianiu do listy

```python
# ZLE — kolejnosc operacji jest kluczowa!
def zle_wstaw(wezel, nowy):
    wezel.nastepny = nowy         # utracilismy wskaznik na reszte listy!
    nowy.nastepny = ???           # za pozno — nie wiemy, co bylo dalej

# DOBRZE — najpierw polacz nowy z reszta, potem przepnij
def dobrze_wstaw(wezel, nowy):
    nowy.nastepny = wezel.nastepny  # nowy wskazuje na reszte
    wezel.nastepny = nowy           # teraz mozemy bezpiecznie przepiac
```

### 7. Porownywanie wezlow przez wartosc zamiast przez referencje

```python
# ZLE — porownanie wartosci moze dac falszywe trafienie
if wezel_a.dane == wezel_b.dane:  # dwa rozne wezly z ta sama wartoscia!
    print("Ten sam wezel")

# DOBRZE — porownanie referencji (tozsamosci obiektow)
if wezel_a is wezel_b:  # ten sam obiekt w pamieci
    print("Ten sam wezel")
```

---

## 6. Gotowe implementacje w Pythonie

Python dostarcza kilka wbudowanych i standardowych narzedzi, ktore zastepuja lub uzupelniaja wlasnorecznie implementacje. Warto je znac, zeby nie wynajdywac kola na nowo w produkcyjnym kodzie.

### 6.1. Stos (`list`, `deque`, `LifoQueue`)

#### `list` — najprostsza opcja

Wbudowana lista jest domyslnym wyborem dla stosu w Pythonie. Operacje `append` i `pop` dzialaja na koncu listy w czasie **O(1) amortyzowanym**.

```python
stos = []

stos.append(10)   # push
stos.append(20)
stos.append(30)

print(stos[-1])   # peek  -> 30
print(stos.pop()) # pop   -> 30
print(stos.pop()) # pop   -> 20
print(stos)       # [10]
```

> **Uwaga:** `list` nie jest thread-safe. W programach wielowatkowych uzyj `queue.LifoQueue`.

#### `collections.deque` — alternatywa dla stosu

`deque` mozna uzywac jak stosu — operacje na prawym koncu sa identyczne z `list`, ale `deque` ma stala wydajnosc i nie przeprowadza kosztownych realokacji przy duzych rozmiarach.

```python
from collections import deque

stos = deque()
stos.append(10)    # push
stos.append(20)
print(stos[-1])    # peek  -> 20
print(stos.pop())  # pop   -> 20
```

#### `queue.LifoQueue` — stos thread-safe

Modul `queue` z biblioteki standardowej oferuje struktury przystosowane do wspolpracy wielu watkow. `LifoQueue` to stos z wbudowana synchronizacja (blokadami).

```python
from queue import LifoQueue

stos = LifoQueue(maxsize=0)  # maxsize=0 oznacza brak limitu

stos.put(10)    # push — odpowiednik put()
stos.put(20)
stos.put(30)

print(stos.get())  # pop  -> 30  (blokuje watek, jesli stos jest pusty)
print(stos.qsize()) # 2

# Wersja nieblokujaca:
try:
    wartosc = stos.get_nowait()   # rzuca queue.Empty jesli pusty
except Exception as e:
    print(e)
```

**Kiedy uzywac `LifoQueue`:** w programach wielowatkowych, gdzie kilka watkow produkuje i konsumuje dane jednoczesnie.

---

### 6.2. Kolejka (`deque`, `Queue`, `SimpleQueue`, `PriorityQueue`, `asyncio.Queue`, `multiprocessing.Queue`)

#### `collections.deque` — zalecana kolejka ogolnego uzytku

Najwydajniejsza kolejka w standardowej bibliotece. Wewnetrznie zaimplementowana jako **lista dwukierunkowa blokow** — operacje na obu koncach sa O(1).

```python
from collections import deque

q = deque()
q.append("A")      # enqueue — dodaj z prawej
q.append("B")
q.append("C")

print(q[0])          # front  -> A (bez usuwania)
print(q.popleft())   # dequeue -> A
print(q)             # deque(['B', 'C'])

# Bonus: deque obsluguje tez operacje na lewym koncu
q.appendleft("Z")    # dodaj z lewej — O(1)
q.pop()              # usun z prawej — O(1)

# Ograniczenie rozmiaru (ring buffer):
bufor = deque(maxlen=3)
for i in range(5):
    bufor.append(i)
print(bufor)         # deque([2, 3, 4], maxlen=3) — stare elementy wypadaja
```

#### `queue.Queue` — kolejka FIFO thread-safe

Analogicznie do `LifoQueue`, ale z kolejnoscia FIFO. Przeznaczona do wzorca producent-konsument w watkach.

```python
from queue import Queue
import threading

q = Queue(maxsize=5)  # maxsize=0 oznacza brak limitu

def producent():
    for i in range(5):
        q.put(i)               # blokuje jesli kolejka pelna
        print(f"Wyprodukowano: {i}")

def konsument():
    for _ in range(5):
        wartosc = q.get()      # blokuje jesli kolejka pusta
        print(f"Skonsumowano: {wartosc}")
        q.task_done()          # sygnalizuje zakonczenie przetwarzania

t1 = threading.Thread(target=producent)
t2 = threading.Thread(target=konsument)
t1.start(); t2.start()
t1.join(); t2.join()

q.join()  # czeka az wszystkie task_done() zostana wywolane
```

#### `queue.SimpleQueue` — uproszczona kolejka thread-safe (Python 3.7+)

Lejsza wersja `Queue` bez limitu rozmiaru, `task_done()` i `join()`. Preferowana gdy nie potrzebujesz tych funkcji.

```python
from queue import SimpleQueue

q = SimpleQueue()
q.put("zadanie_1")
q.put("zadanie_2")

print(q.get())         # zadanie_1
print(q.empty())       # False
```

#### `queue.PriorityQueue` — kolejka priorytetowa thread-safe

Elementy sa pobierane w kolejnosci rosnacej priorytetu (najmniejsza wartosc = najwyzszy priorytet). Wewnetrznie uzywa kopca (*heap*).

```python
from queue import PriorityQueue

pq = PriorityQueue()

# Wstawiamy tuple (priorytet, dane)
pq.put((3, "zadanie niskopriorytowe"))
pq.put((1, "zadanie krytyczne"))
pq.put((2, "zadanie normalne"))

while not pq.empty():
    priorytet, zadanie = pq.get()
    print(f"[{priorytet}] {zadanie}")

# [1] zadanie krytyczne
# [2] zadanie normalne
# [3] zadanie niskopriorytowe
```

#### `asyncio.Queue` — kolejka dla kodu asynchronicznego

Odpowiednik `queue.Queue` dla programowania asynchronicznego (`async`/`await`). Nie jest thread-safe, ale jest *coroutine-safe*.

```python
import asyncio

async def producent(q: asyncio.Queue):
    for i in range(3):
        await q.put(i)
        print(f"Wyprodukowano: {i}")
        await asyncio.sleep(0.1)

async def konsument(q: asyncio.Queue):
    while True:
        wartosc = await q.get()   # czeka na element (nie blokuje event loop)
        print(f"Skonsumowano: {wartosc}")
        q.task_done()

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producent(q), konsument(q))

asyncio.run(main())
```

#### `multiprocessing.Queue` — kolejka miedzy procesami

Gdy watki nie wystarczaja (GIL w CPython), `multiprocessing.Queue` pozwala na komunikacje miedzy osobnymi procesami przez mechanizm *pipe* i *socket*.

```python
from multiprocessing import Process, Queue

def pracownik(q: Queue, id: int):
    q.put(f"Wynik od procesu {id}")

if __name__ == "__main__":
    q = Queue()
    procesy = [Process(target=pracownik, args=(q, i)) for i in range(3)]
    for p in procesy:
        p.start()
    for p in procesy:
        p.join()
    while not q.empty():
        print(q.get())
```

---

### 6.3. Lista jednokierunkowa (brak wbudowanej, `llist`)

Python **nie posiada wbudowanej listy jednokierunkowej** jako osobnego typu. Wbudowana `list` to tablica dynamiczna (*dynamic array*), nie lista wskaznikowa.

Jednak `collections.deque` jest wewnetrznie zaimplementowane jako **dwukierunkowa lista wskaznikowa blokow** — daje O(1) na obu koncach, ale nie udostepnia dostepu do wezlow wewnetrznych.

#### `llist` — zewnetrzna biblioteka

Biblioteka `llist` (instalacja: `pip install llist`) dostarcza listy jednokierunkowe i dwukierunkowe jako typy w C, co daje wydajnosc porownywalna z kodem natywnym.

```python
# pip install llist
from llist import sllist, sllistnode

lista = sllist([1, 2, 3, 4])

lista.appendright(5)    # O(1) — dodaj na koniec
lista.appendleft(0)     # O(1) — dodaj na poczatek
print(lista)            # sllist([0, 1, 2, 3, 4, 5])

lista.remove(lista.nodeat(2))  # O(1) — usun wezel po referencji
print(list(lista))             # [0, 1, 3, 4, 5]

# Dostep do wezlow:
wezel = lista.first          # pierwszy wezel
print(wezel.value)           # 0
print(wezel.next.value)      # 1
```

W praktyce dydaktycznej i algorytmicznej **wlasna implementacja wezlow jest preferowana** — pozwala zrozumiec mechanizm, a `llist` zostawic na kod produkcyjny.

---

### 6.4. Kopiec — `heapq`

Modul `heapq` implementuje **kopiec minimalny** (*min-heap*) bezposrednio na zwyklej liscie Pythona. To najszybsza kolejka priorytetowa w standardowej bibliotece (bez synchronizacji watkow).

```python
import heapq

# heapq operuje bezposrednio na liscie
kopiec = []

heapq.heappush(kopiec, 5)    # O(log n) — wstaw
heapq.heappush(kopiec, 1)
heapq.heappush(kopiec, 3)

print(kopiec[0])             # peek minimum -> 1 (bez usuwania)
print(heapq.heappop(kopiec)) # O(log n) -> 1
print(heapq.heappop(kopiec)) # -> 3

# Tworzenie kopca z istniejacej listy:
dane = [5, 2, 8, 1, 9]
heapq.heapify(dane)           # O(n) — przeksztalca in-place
print(dane[0])                # 1

# n najmniejszych/najwiekszych elementow:
print(heapq.nsmallest(3, dane))  # [1, 2, 5]
print(heapq.nlargest(3, dane))   # [9, 8, 5]
```

> **Uwaga:** `heapq` implementuje **kopiec minimalny**. Aby uzyskac kopiec maksymalny, przechowuj wartosci z odwroconym znakiem: `heappush(h, -wartosc)`, `val = -heappop(h)`.

---

### 6.5. Zestawienie: wlasna implementacja vs biblioteka

| Struktura | Wlasna implementacja | Biblioteka standardowa | Kiedy uzyc biblioteki |
|-----------|--------------------|----------------------|----------------------|
| Stos | `class Stos` na `list` | `list`, `deque`, `queue.LifoQueue` | Wielowatkowosc -> `LifoQueue` |
| Kolejka FIFO | `class Kolejka` na `deque` | `deque`, `queue.Queue`, `queue.SimpleQueue` | Wielowatkowosc -> `Queue` |
| Kolejka priorytetowa | Wlasny kopiec | `heapq`, `queue.PriorityQueue` | Zawsze — `heapq` jest optymalne |
| Lista jednokierunkowa | `class ListaJednokierunkowa` | brak wbudowanej / `llist` (pip) | Kod produkcyjny -> `llist` |
| Kolejka async | — | `asyncio.Queue` | Kod async — zawsze |
| Kolejka IPC | — | `multiprocessing.Queue` | Wiele procesow — zawsze |

> **Zasada:** Na zajeciach implementujemy od zera (zeby zrozumiec mechanizm). W kodzie produkcyjnym uzywamy gotowych bibliotek (szybsze, przetestowane, thread-safe).

---

## 7. Zadania do samodzielnego rozwiazania

### Lista jednokierunkowa

1. **(Latwe)** Zaimplementuj metode `zawiera(wartosc)`, ktora zwraca `True` jesli lista zawiera podana wartosc.
2. **(Latwe)** Zaimplementuj metode `zamien(w1, w2)`, ktora zamienia miejscami wartosci dwoch wezlow o podanych danych.
3. **(Srednie)** Napisz funkcje `usun_duplikaty(glowa)`, ktora usuwa zduplikowane wezly z nieposortowanej listy. Jakie jest minimalne uzycie pamieci dodatkowej?
4. **(Srednie)** Sprawdz, czy lista jest palindromem (czyta sie tak samo od przodu i tylu). Wskazowka: znajdz srodek, odwroc druga polowe, porownaj.
5. **(Trudne)** Zaimplementuj liste z wezlem-wartownikiem (*sentinel node*), ktory upraszcza obsluge pustej listy i skrajnych przypadkow.

### Stos

1. **(Latwe)** Zaimplementuj stos z minimalna wartoscia: `push`, `pop`, `min()` — wszystkie w O(1). Wskazowka: trzymaj drugi stos pomocniczy.
2. **(Srednie)** Zaimplementuj kolejke uzywajac **dwoch stosow**. Kiedy dequeue amortyzuje sie do O(1)?
3. **(Srednie)** Napisz funkcje zamieniajaca wyrazenie infiksowe (np. `"3 + 4 * 2"`) na ONP. Wskazowka: algorytm stacji rozrzadowej (*shunting-yard*).
4. **(Trudne)** Zaimplementuj algorytm sortowania przez stos: posortuj stos tak, by najmniejszy element byl na wierzchu. Uzywaj tylko operacji na stosach.

### Kolejka

1. **(Latwe)** Odwroc kolejke uzywajac tylko jednego stosu pomocniczego.
2. **(Srednie)** Zaimplementuj kolejke priorytetowa (*priority queue*) jako opakowanie na `heapq`. Co zmienia sie w porownaniu do zwyklej kolejki FIFO?
3. **(Srednie)** Zaimplementuj algorytm generowania pierwszych n liczb Fibonacciego z uzyciem kolejki — bez rekurencji i bez tablicy wynikow.
4. **(Trudne)** Znajdz maximum w kazdym oknie rozmiaru k w tablicy liczb (problem *sliding window maximum*). Uzyj deque dla rozwiazania O(n).
