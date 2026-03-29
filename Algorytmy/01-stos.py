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


# ══════════════════════════════════════════════════════════════
# ZADANIE 1 — Odwracanie napisu za pomocą stosu
# ══════════════════════════════════════════════════════════════
#
# Zasada: wrzuc kazdy znak na stos (push),
# potem zdejmuj (pop) i buduj nowy napis.
# LIFO sprawia ze znaki wychodza w odwrotnej kolejnosci.
#
# Wizualizacja dla "ABC":
#   push: stos = [A, B, C]  ← C na wierzcholku
#   pop:  C → B → A         ← wynik = "CBA"


# ── WERSJA 1: nasze rozwiazanie ──────────────────────────────
def odwroc_napis(napis: str) -> str:
    stos = Stos()

    # krok 1 — wrzuc kazdy znak na stos
    for znak in napis:
        stos.push(znak)

    # krok 2 — zdejmuj znaki i buduj wynik przez +=
    wynik = ""
    while not stos.jest_pusty():
        wynik += stos.pop()

    return wynik


# ── WERSJA 2: rozwiazanie wykladowcy ─────────────────────────
# Zrodlo: https://pastebin.com/K9tzXmtB
#
# Roznica vs Wersja 1:
#   - testy sa zorganizowane jako lista krotek (napis, oczekiwany)
#   - wynik porownywany z oczekiwanym — drukuje [OK] lub [FAIL]
#   - zakomentowana alternatywna linia z list comprehension:
#       znaki = [stos.pop() for _ in range(stos.rozmiar())]
#       wynik = "".join(znaki)
#     Jest rownowaznie z petla while, ale bardziej "pythonowa"
#
def odwroc_napis_v2(napis: str) -> str:
    stos = Stos()

    for znak in napis:
        stos.push(znak)

    wynik = ""
    while not stos.jest_pusty():
        wynik += stos.pop()
    # alternatywa z list comprehension (zakomentowana przez wykladowce):
    # znaki = [stos.pop() for _ in range(stos.rozmiar())]
    # wynik = "".join(znaki)

    return wynik


# ══════════════════════════════════════════════════════════════
# ZADANIE 2 — Sprawdzanie palindromu za pomocą stosu
# ══════════════════════════════════════════════════════════════
#
# Palindrom to slowo/zdanie ktore czytane od tylu brzmi tak samo
# jak od przodu (ignorujemy wielkosc liter i spacje).
#
# Zasada:
#   1. Zamien napis na male litery i usun spacje (.lower(), .replace())
#   2. Wrzuc kazdy znak oczyszczonego napisu na stos
#   3. Zdejmuj znaki ze stosu i porownuj z oczyszczonym napisem znak po znaku
#   4. Jesli wszystkie znaki sie zgadzaja — to palindrom
#
# Dlaczego to dziala?
#   Stos odwraca kolejnosc znakow (LIFO).
#   Jesli odwrocony napis == oryginalny napis — to palindrom.
#
# Wizualizacja dla "kajak":
#   oczyszczony: "kajak"
#   push: stos = [k, a, j, a, k]  ← k na wierzcholku
#   porownanie:
#     oryginał[0]='k'  vs  pop()='k'  → OK
#     oryginał[1]='a'  vs  pop()='a'  → OK
#     oryginał[2]='j'  vs  pop()='j'  → OK
#     oryginał[3]='a'  vs  pop()='a'  → OK
#     oryginał[4]='k'  vs  pop()='k'  → OK
#   Wynik: True ✅
#
# Przyklady:
#   czy_palindrom("kajak")              → True
#   czy_palindrom("racecar")            → True
#   czy_palindrom("Ala ma kota")        → False
#   czy_palindrom("Kobyla ma maly bok") → True  (spacje i wielkosc ignorowane)
#   czy_palindrom("hello")              → False
#   czy_palindrom("")                   → True  (pusty napis to palindrom)
#   czy_palindrom("a")                  → True


def czy_palindrom(napis: str) -> bool:
    # krok 1 — oczyszczenie: male litery, bez spacji
    oczyszczony = napis.lower().replace(" ", "")

    # krok 2 — wrzuc kazdy znak na stos
    stos = Stos()
    for znak in oczyszczony:
        stos.push(znak)

    # krok 3 — zdejmuj i porownuj z oczyszczonym napisem znak po znaku
    for znak in oczyszczony:
        if stos.pop() != znak:
            return False

    return True


# ══════════════════════════════════════════════════════════════
# TESTY
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # --- test klasy Stos ---
    print("=== Test klasy Stos ===")
    stos = Stos()
    stos.push(10)
    stos.push(20)
    stos.push(30)
    print(stos)         # Stos (wierzcholek po prawej): [10, 20, 30]
    stos.pop()
    print(stos)         # Stos (wierzcholek po prawej): [10, 20]
    print(stos.peek())  # 20

    # --- testy Zadanie 1 Wersja 1 (nasze) ---
    print("\n=== Zadanie 1 — Wersja 1 (nasze) ===")
    print(odwroc_napis("hello"))   # olleh
    print(odwroc_napis("Python"))  # nohtyP
    print(odwroc_napis("12345"))   # 54321
    print(odwroc_napis("a"))       # a
    print(odwroc_napis(""))        # (pusty string)

    # --- testy Zadanie 1 Wersja 2 (wykladowcy) ---
    print("\n=== Zadanie 1 — Wersja 2 (wykladowcy) ===")
    testy_z1 = [
        ("hello",        "olleh"),
        ("Python",       "nohtyP"),
        ("ala ma kota",  "atok am ala"),
    ]
    for napis, oczekiwany in testy_z1:
        wynik = odwroc_napis_v2(napis)
        status = "OK" if wynik == oczekiwany else "FAIL"
        print(f' [{status}] odwroc_napis("{napis}") = "{wynik}"')

    # --- testy Zadanie 2 — palindrom ---
    print("\n=== Zadanie 2 — Palindrom ===")
    testy_z2 = [
        ("kajak",                True),
        ("racecar",              True),
        ("Ala ma kota",          False),
        ("Kobyla ma maly bok",   True),
        ("hello",                False),
        ("",                     True),
        ("a",                    True),
    ]
    for napis, oczekiwany in testy_z2:
        wynik = czy_palindrom(napis)
        status = "OK" if wynik == oczekiwany else "FAIL"
        print(f' [{status}] czy_palindrom("{napis}") = {wynik}')
