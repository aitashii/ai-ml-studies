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


def odwroc_napis(napis: str) -> str:
    stos = Stos()

    for znak in napis:
        stos.push(znak)

    wynik = ""
    while not stos.jest_pusty():
        wynik += stos.pop()

    return wynik


if __name__ == "__main__":
    stos = Stos()
    stos.push(10)
    stos.push(20)
    stos.push(30)
    print(stos)
    stos.pop()
    print(stos)
    print(stos.peek())

    print(odwroc_napis("hello"))   # olleh
    print(odwroc_napis("Python"))  # nohtyP
    print(odwroc_napis("12345"))   # 54321
    print(odwroc_napis(""))        # (pusty string)
