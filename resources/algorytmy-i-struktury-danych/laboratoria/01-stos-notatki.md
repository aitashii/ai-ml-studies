# Laboratorium 01 — Stos (Stack)

**Przedmiot:** Algorytmy i Struktury Danych
**Data:** 2026-03-29

---

## Czym jest Stos?

Stos to liniowa struktura danych działająca na zasadzie **LIFO** — Last In, First Out (ostatni wchodzi, pierwszy wychodzi). Wyobraź sobie stos talerzy — kładziesz talerze jeden na drugi i zdejmujesz zawsze z wierzchu. Nie możesz wyciągnąć talerza ze środka bez zdejmowania tych powyżej.

---

## Klasa Stos — omówienie kodu

```python
class Stos:
    def __init__(self, pojemnosc: int | None = None):
        self._dane = []
        self._pojemnosc = pojemnosc
```

`_dane` to lista Pythona przechowująca elementy stosu. `_pojemnosc` to opcjonalne ograniczenie rozmiaru — jeśli `None`, stos jest nieograniczony.

### Metody klasy

| Metoda | Co robi | Błąd gdy... |
|--------|---------|-------------|
| `push(wartość)` | Wkłada element na wierzch stosu | Stos pełny (`OverflowError`) |
| `pop()` | Zdejmuje i zwraca element z wierzchu | Stos pusty (`OverflowError`) |
| `peek()` | Podgląda wierzchni element bez zdejmowania | Stos pusty (`IndexError`) |
| `jest_pusty()` | Zwraca `True` jeśli stos nie ma elementów | — |
| `rozmiar()` | Zwraca liczbę elementów na stosie | — |

### Pełny kod klasy

```python
class Stos:
    def __init__(self, pojemnosc: int | None = None):
        self._dane = []
        self._pojemnosc = pojemnosc

    def push(self, wartosc):
        if self._pojemnosc is not None and len(self._dane) >= self._pojemnosc:
            raise OverflowError("Stos jest pelny, nie mozna dodac elementu")
        self._dane.append(wartosc)

    def pop(self):
        if self.jest_pusty():
            raise OverflowError("Stos jest pusty, nie mozna zdjac elementu")
        return self._dane.pop()

    def peek(self):
        if self.jest_pusty():
            raise IndexError("Stos jest pusty")
        return self._dane[-1]

    def jest_pusty(self):
        return len(self._dane) == 0

    def rozmiar(self):
        return len(self._dane)

    def __str__(self):
        return f"Stos (wierzcholek po prawej): {self._dane}"


if __name__ == "__main__":
    stos = Stos()
    stos.push(10)
    stos.push(20)
    stos.push(30)
    print(stos)          # Stos (wierzcholek po prawej): [10, 20, 30]
    stos.pop()
    print(stos)          # Stos (wierzcholek po prawej): [10, 20]
    print(stos.peek())   # 20
```

---

## Zastosowania stosu w praktyce

Stosy są wszędzie w programowaniu:

- **Historia cofania (Ctrl+Z)** — każda akcja jest wrzucana na stos, cofanie zdejmuje ostatnią
- **Nawigacja "wstecz" w przeglądarce** — stos odwiedzonych stron
- **Call stack** — wywołania funkcji w każdym języku programowania są zarządzane przez stos wywołań
- **Sprawdzanie nawiasów** — czy nawiasy `({[]})` są poprawnie zagnieżdżone to klasyczny algorytm na stosie
- **Odwracanie danych** — Zadanie 1 poniżej
- **Sprawdzanie palindromów** — Zadanie 2 poniżej

---

## Zadanie 1 — Odwracanie napisu za pomocą stosu

### Opis

Napisz funkcję która odwraca podany napis (string) używając stosu.

**Zasada działania:**
1. Włóż każdy znak napisu na stos (`push`)
2. Zdejmuj znaki ze stosu (`pop`) i buduj nowy napis
3. Dzięki LIFO — ostatni włożony znak zostanie zdjęty pierwszy, co naturalnie odwraca kolejność

### Wizualizacja dla napisu "ABC"

```
Krok 1 — push wszystkich znaków:
  push('A') → stos: [A]
  push('B') → stos: [A, B]
  push('C') → stos: [A, B, C]  ← C na wierzchołku

Krok 2 — pop wszystkich znaków:
  pop() → 'C'  → wynik: "C"
  pop() → 'B'  → wynik: "CB"
  pop() → 'A'  → wynik: "CBA"

Wynik: "CBA" ✅
```

### Rozwiązanie (wersja 1 — nasze)

```python
def odwroc_napis(napis: str) -> str:
    stos = Stos()

    for znak in napis:
        stos.push(znak)

    wynik = ""
    while not stos.jest_pusty():
        wynik += stos.pop()

    return wynik
```

### Rozwiązanie (wersja 2 — wykładowcy)

Źródło: https://pastebin.com/K9tzXmtB

Różnice vs wersja 1: testy jako lista krotek `(napis, oczekiwany)` z automatyczną walidacją `[OK]`/`[FAIL]`. Wykładowca pokazał też alternatywę z list comprehension (zakomentowaną):

```python
def odwroc_napis_v2(napis: str) -> str:
    stos = Stos()

    for znak in napis:
        stos.push(znak)

    wynik = ""
    while not stos.jest_pusty():
        wynik += stos.pop()
    # alternatywa (bardziej pythonowa):
    # znaki = [stos.pop() for _ in range(stos.rozmiar())]
    # wynik = "".join(znaki)

    return wynik

if __name__ == "__main__":
    testy = [
        ("hello",        "olleh"),
        ("Python",       "nohtyP"),
        ("ala ma kota",  "atok am ala"),
    ]
    for napis, oczekiwany in testy:
        wynik = odwroc_napis_v2(napis)
        status = "OK" if wynik == oczekiwany else "FAIL"
        print(f' [{status}] odwroc_napis("{napis}") = "{wynik}"')
```

### Złożoność (Zadanie 1)

- **Czasowa: O(n)** — przechodzimy przez napis dwa razy (raz push, raz pop)
- **Pamięciowa: O(n)** — przechowujemy n znaków na stosie

---

## Zadanie 2 — Sprawdzanie palindromu za pomocą stosu

### Opis

Napisz funkcję która sprawdza czy podany napis jest palindromem, używając stosu.

**Palindrom** to słowo lub zdanie które czytane od tyłu brzmi tak samo jak od przodu. Ignorujemy wielkość liter i spacje.

**Zasada działania:**
1. Zamień napis na małe litery i usuń spacje (`.lower()`, `.replace()`)
2. Włóż każdy znak oczyszczonego napisu na stos
3. Zdejmuj znaki ze stosu i porównuj z oczyszczonym napisem znak po znaku
4. Jeśli wszystkie znaki się zgadzają — to palindrom

### Dlaczego to działa?

Stos odwraca kolejność znaków (LIFO). Zdejmując znaki ze stosu dostajemy napis czytany od tyłu. Jeśli ten odwrócony napis jest identyczny z oryginałem — to palindrom.

### Wizualizacja dla "kajak"

```
Oczyszczony: "kajak"

Push: stos = [k, a, j, a, k]  ← k na wierzchołku

Porównanie:
  oryginał[0]='k'  vs  pop()='k'  → OK ✅
  oryginał[1]='a'  vs  pop()='a'  → OK ✅
  oryginał[2]='j'  vs  pop()='j'  → OK ✅
  oryginał[3]='a'  vs  pop()='a'  → OK ✅
  oryginał[4]='k'  vs  pop()='k'  → OK ✅

Wynik: True — "kajak" jest palindromem ✅
```

### Wizualizacja dla "hello" (NIE palindrom)

```
Oczyszczony: "hello"

Push: stos = [h, e, l, l, o]  ← o na wierzchołku

Porównanie:
  oryginał[0]='h'  vs  pop()='o'  → RÓŻNE ❌

Wynik: False — "hello" nie jest palindromem ✅
```

### Rozwiązanie

```python
def czy_palindrom(napis: str) -> bool:
    # krok 1 — oczyszczenie: male litery, bez spacji
    oczyszczony = napis.lower().replace(" ", "")

    # krok 2 — wrzuc kazdy znak na stos
    stos = Stos()
    for znak in oczyszczony:
        stos.push(znak)

    # krok 3 — zdejmuj i porownuj znak po znaku
    for znak in oczyszczony:
        if stos.pop() != znak:
            return False

    return True
```

### Przykłady

| Napis | Wynik | Dlaczego |
|-------|-------|----------|
| `"kajak"` | `True` | czytany od tyłu = "kajak" |
| `"racecar"` | `True` | czytany od tyłu = "racecar" |
| `"Ala ma kota"` | `False` | od tyłu = "atok am ala" |
| `"Kobyła ma mały bok"` | `True` | po oczyszczeniu = palindrom |
| `"hello"` | `False` | od tyłu = "olleh" |
| `""` | `True` | pusty napis — brak znaków do porównania |
| `"a"` | `True` | jeden znak zawsze palindrom |

### Złożoność (Zadanie 2)

- **Czasowa: O(n)** — trzy przejścia przez napis: oczyszczenie, push, pop+porównanie
- **Pamięciowa: O(n)** — przechowujemy n znaków na stosie
