# Laboratorium 02 — Kolejka (Queue)

**Przedmiot:** Algorytmy i Struktury Danych
**Data:** 2026-03-29

---

## Czym jest Kolejka?

Kolejka to liniowa struktura danych działająca na zasadzie **FIFO** — First In, First Out (pierwszy wchodzi, pierwszy wychodzi). Wyobraź sobie kolejkę w sklepie — pierwsza osoba która staje, pierwsza wychodzi z kasy. Nie możesz "wskoczyć" przed kogoś kto stoi wcześniej.

### Kolejka vs Stos — kluczowa różnica

| | Stos | Kolejka |
|---|---|---|
| Zasada | LIFO — ostatni wchodzi, pierwszy wychodzi | FIFO — pierwszy wchodzi, pierwszy wychodzi |
| Analogia | Stos talerzy | Kolejka w sklepie |
| Dodawanie | `push` — na wierzch | `enqueue` — na tył |
| Zdejmowanie | `pop` — z wierzchu | `dequeue` — z przodu |

---

## Klasa Kolejka — omówienie kodu

Implementacja używa `collections.deque` z biblioteki standardowej Pythona. `deque` (double-ended queue) jest wydajniejszy niż zwykła lista przy operacjach na początku — `popleft()` działa w O(1), podczas gdy `list.pop(0)` to O(n).

### Metody klasy

| Metoda | Co robi | Błąd gdy... |
|--------|---------|-------------|
| `enqueue(wartość)` | Dodaje element na TYŁ kolejki | — |
| `dequeue()` | Zdejmuje i zwraca element z PRZODU | Kolejka pusta (`IndexError`) |
| `przod()` | Podgląda element z przodu bez zdejmowania | Kolejka pusta (`IndexError`) |
| `jest_pusta()` | Zwraca `True` jeśli kolejka nie ma elementów | — |
| `rozmiar()` | Zwraca liczbę elementów w kolejce | — |

### Pełny kod klasy

```python
from collections import deque

class Kolejka:
    def __init__(self):
        self._dane = deque()

    def enqueue(self, wartosc):
        self._dane.append(wartosc)

    def dequeue(self):
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta, nie mozna pobrac elementu")
        return self._dane.popleft()

    def przod(self):
        if self.jest_pusta():
            raise IndexError("Kolejka jest pusta")
        return self._dane[0]

    def jest_pusta(self):
        return len(self._dane) == 0

    def rozmiar(self):
        return len(self._dane)

    def __str__(self):
        return f"Kolejka (przod po lewej): {list(self._dane)}"
```

---

## Zastosowania kolejki w praktyce

Kolejki są wszędzie gdzie coś czeka na przetworzenie w kolejności przybycia: kolejka zadań do drukowania (drukarka przetwarza dokumenty w kolejności wysłania), bufor sieciowy (pakiety przetwarzane w kolejności przybycia), obsługa zdarzeń w grach i aplikacjach (kliknięcia, naciśnięcia klawiszy), system zgłoszeń w help desku (pierwsze zgłoszenie, pierwsze obsłużone) oraz algorytmy przeszukiwania grafów BFS (Breadth-First Search).

---

## Zadanie 3 — Przeplatanie dwóch kolejek

### Opis

Napisz funkcję która łączy dwie kolejki w jedną, biorąc elementy naprzemiennie: jeden z A, jeden z B, jeden z A... Jeśli jedna kolejka jest dłuższa — pozostałe elementy dopisz na koniec.

**Zasada działania:**
1. Utwórz nową, pustą kolejkę wynikową
2. Pętla `while` — dopóki OBIE kolejki mają elementy: `dequeue` z A, `enqueue` do wyniku, potem to samo z B
3. Po pętli — dopisz resztę z tej kolejki która jeszcze nie jest pusta

### Wizualizacja dla A=[1,2,3] i B=[A,B,C]

```
Kolejka A: PRZÓD → [1, 2, 3] ← TYŁ
Kolejka B: PRZÓD → [A, B, C] ← TYŁ

Krok 1: dequeue(A)=1  → wynik: [1]
Krok 2: dequeue(B)=A  → wynik: [1, A]
Krok 3: dequeue(A)=2  → wynik: [1, A, 2]
Krok 4: dequeue(B)=B  → wynik: [1, A, 2, B]
Krok 5: dequeue(A)=3  → wynik: [1, A, 2, B, 3]
Krok 6: dequeue(B)=C  → wynik: [1, A, 2, B, 3, C]

Wynik: PRZÓD → [1, A, 2, B, 3, C] ← TYŁ ✅
```

### Rozwiązanie

```python
def przeplec_kolejki(kolejka_a: Kolejka, kolejka_b: Kolejka) -> Kolejka:
    wynik = Kolejka()

    while not kolejka_a.jest_pusta() and not kolejka_b.jest_pusta():
        wynik.enqueue(kolejka_a.dequeue())
        wynik.enqueue(kolejka_b.dequeue())

    while not kolejka_a.jest_pusta():
        wynik.enqueue(kolejka_a.dequeue())

    while not kolejka_b.jest_pusta():
        wynik.enqueue(kolejka_b.dequeue())

    return wynik
```

### Dlaczego trzy pętle a nie jedna?

Pierwsza pętla `while` działa tylko gdy obie kolejki mają elementy — warunek `and` sprawia że zatrzymuje się gdy którakolwiek się skończy. Potem dwie osobne pętle dopisują resztę — tylko jedna z nich wykona się (ta której kolejka nie była pusta), druga przeskoczy od razu bo jej kolejka jest już pusta.

### Przykłady

| Kolejka A | Kolejka B | Wynik |
|-----------|-----------|-------|
| `[1, 2, 3]` | `[A, B, C]` | `[1, A, 2, B, 3, C]` |
| `[1, 2]` | `[A, B, C, D]` | `[1, A, 2, B, C, D]` |
| `[1, 2, 3]` | `[]` | `[1, 2, 3]` |
| `[]` | `[]` | `[]` |

### Złożoność (Zadanie 3)

- **Czasowa: O(n + m)** — n i m to rozmiary kolejek, każdy element przetwarzany raz w O(1)
- **Pamięciowa: O(n + m)** — nowa kolejka przechowuje wszystkie elementy

---

## Zadanie 4 — Zliczanie elementów w kolejce (bez niszczenia)

### Opis

Napisz funkcję która zlicza ile razy dany element pojawia się w kolejce. Po zakończeniu kolejka musi wyglądać **dokładnie tak samo** jak przed wywołaniem — nie możesz jej zniszczyć. Masz do dyspozycji TYLKO operacje kolejki: `enqueue`, `dequeue`, `przod`, `jest_pusta`, `rozmiar`.

**Zasada działania:**
1. Zapamiętaj rozmiar kolejki: `n = kolejka.rozmiar()`
2. Utwórz zmienną `licznik = 0`
3. Powtórz dokładnie `n` razy: zdejmij element (`dequeue`), sprawdź czy równy szukanemu, wstaw z powrotem na tył (`enqueue`)
4. Po `n` obrotach kolejka wraca do stanu początkowego

### Wizualizacja dla [3,7,3,1,3,9], szukany=3

```
dequeue()=3, licznik=1, enqueue(3) → [7, 3, 1, 3, 9, 3]
dequeue()=7, licznik=1, enqueue(7) → [3, 1, 3, 9, 3, 7]
dequeue()=3, licznik=2, enqueue(3) → [1, 3, 9, 3, 7, 3]
dequeue()=1, licznik=2, enqueue(1) → [3, 9, 3, 7, 3, 1]
dequeue()=3, licznik=3, enqueue(3) → [9, 3, 7, 3, 1, 3]
dequeue()=9, licznik=3, enqueue(9) → [3, 7, 3, 1, 3, 9] ← jak nowa!

Wynik: 3 ✅
```

### Rozwiązanie

```python
def zlicz_w_kolejce(kolejka: Kolejka, szukany) -> int:
    licznik = 0
    n = kolejka.rozmiar()

    for _ in range(n):
        element = kolejka.dequeue()
        if element == szukany:
            licznik += 1
        kolejka.enqueue(element)

    return licznik
```

### Dlaczego `range(n)` a nie `while not jest_pusta()`?

Gdybyśmy użyli `while not jest_pusta()` — pętla nigdy by się nie skończyła, bo po każdym `dequeue` robimy `enqueue` — kolejka zawsze ma elementy! Dlatego zapamiętujemy rozmiar `n` przed pętlą i obracamy kolejkę **dokładnie n razy** — każdy element wychodzi i wraca raz, a kolejka wraca do stanu pierwotnego.

### Przykłady

| Kolejka | Szukany | Wynik | Kolejka po wywołaniu |
|---------|---------|-------|----------------------|
| `[3, 7, 3, 1, 3, 9]` | `3` | `3` | `[3, 7, 3, 1, 3, 9]` ← bez zmian |
| `[1, 2, 3, 4, 5]` | `6` | `0` | `[1, 2, 3, 4, 5]` ← bez zmian |
| `[5, 5, 5]` | `5` | `3` | `[5, 5, 5]` ← bez zmian |
| `["a", "b", "a"]` | `"a"` | `2` | `["a", "b", "a"]` ← bez zmian |
| `[]` | `1` | `0` | `[]` ← bez zmian |

### Złożoność (Zadanie 4)

- **Czasowa: O(n)** — przeglądamy każdy element dokładnie raz
- **Pamięciowa: O(1)** — tylko zmienna `licznik`, bez żadnych dodatkowych struktur
