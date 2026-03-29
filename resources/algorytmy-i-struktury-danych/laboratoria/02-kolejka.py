from collections import deque


# ══════════════════════════════════════════════════════════════
# KLASA KOLEJKA
# ══════════════════════════════════════════════════════════════
#
# Kolejka to struktura danych dzialajaca na zasadzie FIFO —
# First In, First Out (pierwszy wchodzi, pierwszy wychodzi).
# Wyobraz sobie kolejke w sklepie — pierwsza osoba ktora staje,
# pierwsza wychodzi z kasy.
#
# Roznica vs Stos (LIFO):
#   Stos    → ostatni wchodzi, pierwszy wychodzi (talerze)
#   Kolejka → pierwszy wchodzi, pierwszy wychodzi (kolejka w sklepie)
#
# Zastosowania w praktyce:
#   - kolejka zadan do drukowania (drukarka przetwarza w kolejnosci)
#   - bufor sieciowy (pakiety przetwarzane w kolejnosci przybycia)
#   - system zgloszen w help desku (pierwsze zgloszenie, pierwsze obslugiwane)
#   - algorytmy przeszukiwania grafow BFS (Breadth-First Search)
#
# Metody:
#   enqueue(wartosc) — dodaje element na TYL kolejki
#   dequeue()        — zdejmuje element z PRZODU kolejki
#   przod()          — podglada element z przodu bez zdejmowania
#   jest_pusta()     — True jesli kolejka nie ma elementow
#   rozmiar()        — liczba elementow w kolejce
#
# WAZNE: uzywa collections.deque zamiast zwyklej listy!
#   deque.popleft() = O(1)
#   list.pop(0)     = O(n)  ← wolniejsze, przesuwa wszystkie elementy

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


# ══════════════════════════════════════════════════════════════
# ZADANIE 3 — Przeplatanie dwoch kolejek
# ══════════════════════════════════════════════════════════════
#
# OPIS ZADANIA
# ------------
# Napisz funkcje, ktora laczy dwie kolejki w jedna, biorac elementy
# naprzemiennie: jeden z pierwszej, jeden z drugiej, jeden z pierwszej...
#
# Jesli jedna kolejka jest dluzsza — pozostale elementy dopisz na koniec.
#
# WIZUALIZACJA
# ------------
#   Kolejka A: PRZOD → [1, 2, 3] ← TYL
#   Kolejka B: PRZOD → [A, B, C] ← TYL
#
#   Krok 1: dequeue(A) → 1    wynik: [1]
#   Krok 2: dequeue(B) → A    wynik: [1, A]
#   Krok 3: dequeue(A) → 2    wynik: [1, A, 2]
#   Krok 4: dequeue(B) → B    wynik: [1, A, 2, B]
#   Krok 5: dequeue(A) → 3    wynik: [1, A, 2, B, 3]
#   Krok 6: dequeue(B) → C    wynik: [1, A, 2, B, 3, C]
#
#   Wynik: PRZOD → [1, A, 2, B, 3, C] ← TYL  ✅
#
# ZLOZONOSC
# ---------
#   Czasowa:    O(n + m) — n i m to rozmiary kolejek, kazdy element O(1)
#   Pamieciowa: O(n + m) — nowa kolejka przechowuje wszystkie elementy
#
# INPUT
# -----
#   kolejka_a: Kolejka — pierwsza kolejka
#   kolejka_b: Kolejka — druga kolejka
#
# OUTPUT
# ------
#   Kolejka — nowa kolejka z przeplatanymi elementami
#
# PRZYKLADY
# ---------
#   [1, 2, 3] + [A, B, C]   → [1, A, 2, B, 3, C]
#   [1, 2] + [A, B, C, D]   → [1, A, 2, B, C, D]
#   [1, 2, 3] + []          → [1, 2, 3]
#   [] + []                 → []
#
# PODPOWIEDZI
# -----------
#   1. Utworz nowa, pusta kolejke wynikowa
#   2. Petla while — dopoki OBIE kolejki maja elementy:
#      - dequeue z A → enqueue do wyniku
#      - dequeue z B → enqueue do wyniku
#   3. Po petli — dopisz reszte z tej kolejki, ktora jeszcze nie jest pusta
#
# DLACZEGO TRZY PETLE A NIE JEDNA?
#   Pierwsza while dziala tylko gdy obie maja elementy (warunek AND).
#   Zatrzymuje sie gdy ktorakolwiek sie skonczy.
#   Dwie kolejne petle dopisuja reszte — tylko jedna z nich sie wykona
#   (ta ktorej kolejka nie byla pusta), druga przeskoczy od razu.

def przeplec_kolejki(kolejka_a: Kolejka, kolejka_b: Kolejka) -> Kolejka:
    wynik = Kolejka()

    # naprzemiennie dopoki obie maja elementy
    while not kolejka_a.jest_pusta() and not kolejka_b.jest_pusta():
        wynik.enqueue(kolejka_a.dequeue())
        wynik.enqueue(kolejka_b.dequeue())

    # dopisz reszte z A (jesli B skonczyla sie pierwsza)
    while not kolejka_a.jest_pusta():
        wynik.enqueue(kolejka_a.dequeue())

    # dopisz reszte z B (jesli A skonczyla sie pierwsza)
    while not kolejka_b.jest_pusta():
        wynik.enqueue(kolejka_b.dequeue())

    return wynik


# ══════════════════════════════════════════════════════════════
# ZADANIE 4 — Zliczanie elementow w kolejce (bez niszczenia)
# ══════════════════════════════════════════════════════════════
#
# OPIS ZADANIA
# ------------
# Napisz funkcje, ktora zlicza ile razy dany element pojawia sie
# w kolejce. Po zakonczeniu kolejka musi wygladac DOKLADNIE tak samo
# jak przed wywolaniem — nie mozesz jej zniszczyc.
#
# Masz do dyspozycji TYLKO operacje kolejki: enqueue, dequeue,
# przod, jest_pusta, rozmiar.
#
# WIZUALIZACJA
# ------------
#   Kolejka: PRZOD → [3, 7, 3, 1, 3, 9] ← TYL
#   Szukany element: 3
#
#   Krok 1 — przegladaj i odkladaj z powrotem (n = 6 razy):
#     dequeue() = 3, licznik = 1, enqueue(3)  → [7, 3, 1, 3, 9, 3]
#     dequeue() = 7, licznik = 1, enqueue(7)  → [3, 1, 3, 9, 3, 7]
#     dequeue() = 3, licznik = 2, enqueue(3)  → [1, 3, 9, 3, 7, 3]
#     dequeue() = 1, licznik = 2, enqueue(1)  → [3, 9, 3, 7, 3, 1]
#     dequeue() = 3, licznik = 3, enqueue(3)  → [9, 3, 7, 3, 1, 3]
#     dequeue() = 9, licznik = 3, enqueue(9)  → [3, 7, 3, 1, 3, 9]
#                                                ↑ kolejka jak nowa!
#
#   Wynik: 3 (trojka wystepuje 3 razy) ✅
#
# ZLOZONOSC
# ---------
#   Czasowa:    O(n) — przegladamy kazdy element dokladnie raz
#   Pamieciowa: O(1) — uzywamy tylko zmiennej licznik (bez dodatkowych struktur)
#
# INPUT
# -----
#   kolejka: Kolejka — kolejka z elementami
#   szukany: dowolny — element do zliczenia
#
# OUTPUT
# ------
#   int — ile razy szukany element wystepuje w kolejce
#
# PRZYKLADY
# ---------
#   [3, 7, 3, 1, 3, 9], szukany=3  → 3
#   [1, 2, 3, 4, 5], szukany=6     → 0
#   [5, 5, 5], szukany=5           → 3
#   ["a", "b", "a"], szukany="a"   → 2
#   [], szukany=1                  → 0
#
# PODPOWIEDZI
# -----------
#   1. Zapamietaj rozmiar kolejki: n = kolejka.rozmiar()
#   2. Utworz zmienna licznik = 0
#   3. Powtorz n razy:
#      - zdejmij element z przodu (dequeue)
#      - jesli element == szukany → zwieksz licznik
#      - wstaw element z powrotem na koniec (enqueue)
#   4. Po n obrotach kolejka wraca do stanu poczatkowego
#
# DLACZEGO range(n) A NIE while not jest_pusta()?
#   Gdybysmy uzyly while not jest_pusta() — petla nigdy by sie nie skonczyla!
#   Po kazdym dequeue robimy enqueue — kolejka zawsze ma elementy.
#   Dlatego zapamiętujemy n przed petla i obracamy kolejke DOKLADNIE n razy.

def zlicz_w_kolejce(kolejka: Kolejka, szukany) -> int:
    licznik = 0
    n = kolejka.rozmiar()

    for _ in range(n):
        element = kolejka.dequeue()
        if element == szukany:
            licznik += 1
        kolejka.enqueue(element)

    return licznik


# ══════════════════════════════════════════════════════════════
# TESTY
# ══════════════════════════════════════════════════════════════

def zbuduj_kolejke(*elementy) -> Kolejka:
    """pomocnicza funkcja — tworzy kolejke z listy elementow"""
    k = Kolejka()
    for e in elementy:
        k.enqueue(e)
    return k


if __name__ == "__main__":

    # --- test klasy Kolejka ---
    print("=== Test klasy Kolejka ===")
    k = Kolejka()
    k.enqueue(10)
    k.enqueue(20)
    k.enqueue(30)
    print(k)              # Kolejka (przod po lewej): [10, 20, 30]
    print(k.dequeue())    # 10  ← FIFO, wychodzi pierwszy
    print(k)              # Kolejka (przod po lewej): [20, 30]
    print(k.przod())      # 20

    # --- testy Zadanie 3 ---
    print("\n=== Zadanie 3 — Przeplatanie kolejek ===")
    testy_z3 = [
        ([1, 2, 3],    ["A", "B", "C"],    [1,"A",2,"B",3,"C"]),
        ([1, 2],       ["A","B","C","D"],   [1,"A",2,"B","C","D"]),
        ([1, 2, 3],    [],                  [1, 2, 3]),
        ([],           [],                  []),
    ]
    for dane_a, dane_b, oczekiwany in testy_z3:
        a = zbuduj_kolejke(*dane_a)
        b = zbuduj_kolejke(*dane_b)
        wynik = przeplec_kolejki(a, b)
        lista_wyniku = list(wynik._dane)
        status = "OK" if lista_wyniku == oczekiwany else "FAIL"
        print(f" [{status}] {dane_a} + {dane_b} → {lista_wyniku}")

    # --- testy Zadanie 4 ---
    print("\n=== Zadanie 4 — Zliczanie elementow w kolejce ===")
    testy_z4 = [
        ([3, 7, 3, 1, 3, 9], 3,    3),
        ([1, 2, 3, 4, 5],    6,    0),
        ([5, 5, 5],          5,    3),
        (["a", "b", "a"],   "a",   2),
        ([],                 1,    0),
    ]
    for dane, szukany, oczekiwany in testy_z4:
        k = zbuduj_kolejke(*dane)
        wynik = zlicz_w_kolejce(k, szukany)
        status = "OK" if wynik == oczekiwany else "FAIL"
        print(f" [{status}] {dane}, szukany={szukany!r} → {wynik}")
        print(f"        kolejka po wywolaniu: {k}")
