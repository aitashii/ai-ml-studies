\- Napisz klasę **Kalkulator**, która ma metody do wykonywania podstawowych działań arytmetycznych (dodawanie, odejmowanie, mnożenie, dzielenie) na dwóch liczbach. Następnie napisz program, który używa tej klasy do obliczania wyników podanych przez użytkownika równań. Na przykład, jeśli użytkownik wpisze `2 + 3`, program powinien wyświetlić `5`.

\- Napisz klasę **Zwierze**, która ma atrybuty `nazwa`, `gatunek` i `wiek`. Następnie napisz kilka podklas, takich jak **Pies**, **Kot** i **Ptak**, które dziedziczą po klasie **Zwierze** i mają dodatkowe atrybuty, takie jak `rasa`, `kolor` i `ulubione jedzenie`. Następnie napisz program, który tworzy obiekty tych podklas i wyświetla informacje o nich. Na przykład, jeśli użytkownik wpisze `pies`, program powinien wyświetlić `Nazwa: Rex, Gatunek: Pies, Wiek: 3, Rasa: Labrador, Kolor: Złoty, Ulubione jedzenie: Kość`.

\- Napisz klasę **Gra**, która ma atrybuty `tytuł`, `gatunek` i `ocena`. Następnie napisz klasę **Biblioteka**, która ma atrybut `lista_gier`, który jest listą obiektów klasy **Gra**. Klasa **Biblioteka** ma również metody do dodawania, usuwania i wyszukiwania gier w liście. Następnie napisz program, który używa klasy **Biblioteka** do zarządzania kolekcją gier użytkownika. Na przykład, jeśli użytkownik wpisze `dodaj Cyberpunk 2077 Akcja 9`, program powinien dodać grę o tym tytule, gatunku i ocenie do listy gier. Jeśli użytkownik wpisze `szukaj Akcja`, program powinien wyświetlić wszystkie gry z gatunku akcji. Jeśli użytkownik wpisze `usuń Cyberpunk 2077`, program powinien usunąć tę grę z listy.

A dalej może nieco większe zadanie. Gra RPG, która wykorzystuje dotychczasowe zadania i funkcje:

\- Napisz klasę **Postać**, która ma atrybuty `imię`, `klasa` (np. Wojownik, Mag, Złodziej), `poziom`, `życie`, `mana`, `siła`, `zręczność` i `inteligencja`. Klasa **Postać** ma również metody do atakowania, broniąc się, leczenia się i używania umiejętności specjalnych. Następnie napisz kilka podklas, które dziedziczą po klasie **Postać** i mają różne wartości atrybutów i umiejętności. Na przykład, klasa **Wojownik** ma wysoką siłę i życie, ale niską manę i inteligencję, a jego umiejętnością specjalną jest **Szał Bojowy**, który zwiększa jego siłę i zręczność na jeden ruch.

\- Napisz klasę **Przeciwnik**, która ma atrybuty `nazwa`, `poziom`, `życie`, `mana`, `atak`, `obrona` i `nagroda`. Klasa **Przeciwnik** ma również metodę do atakowania gracza. Następnie napisz kilka podklas, które dziedziczą po klasie **Przeciwnik** i mają różne wartości atrybutów i sposoby ataku. Na przykład, klasa **Smok** ma wysokie życie i atak, ale niską obronę i manę, a jego sposobem ataku jest **Ogień**, który zadaje duże obrażenia, ale ma niską celność.

\- Napisz klasę **Świat**, która ma atrybut `mapa`, który jest dwuwymiarową listą znaków reprezentujących różne typy terenu (np. `.`, `#`, `~`, *). Klasa* \*Świat\*\* ma również metodę do wyświetlania mapy na ekranie i metodę do sprawdzania, czy dany typ terenu jest możliwy do przejścia. Na przykład, znak `.` oznacza trawę, która jest możliwa do przejścia, a znak `#` oznacza ścianę, która nie jest możliwa do przejścia.

\- Napisz program, który tworzy obiekt klasy **Postać** dla gracza i pozwala mu wybrać jego imię i klasę. Następnie program tworzy obiekt klasy **Świat** i generuje losową mapę. Następnie program umieszcza gracza na losowym miejscu na mapie i pozwala mu się poruszać za pomocą klawiszy `W`, `A`, `S`, `D`. Program również losowo umieszcza na mapie obiekty klas **Przeciwnik** i **Nagroda**. Jeśli gracz napotka przeciwnika, program rozpoczyna walkę, w której gracz i przeciwnik na zmianę wykonują ruchy, aż jeden z nich straci całe życie. Jeśli gracz wygra walkę, program dodaje mu nagrodę przeciwnika do jego ekwipunku i zwiększa jego poziom. Jeśli gracz przegra walkę, program kończy się i wyświetla komunikat o porażce. Jeśli gracz napotka nagrodę, program dodaje ją do jego ekwipunku i wyświetla komunikat o znalezieniu nagrody. Program kończy się, gdy gracz dotrze do wyjścia z mapy i wyświetla komunikat o zwycięstwie.

Podpowiedź - mapę możemy stworzyć za pomocą random. Mapa może być oczywiście w wersji tekstowej - a jej alimenty nogą być znakami, które są w losowych miejscach. 

Samą mapę podpowiadam:

import random

class World:

    def __init__(self, rows, cols):

        \# define the possible terrain types

        self.terrain = \[".", "#", "\~"\]

        \# define the exit symbol

        self.exit = "\*"

        \# create an empty list of the given size

        [self.map](http://self.map) = \[\[None for j in range(cols)\] for i in range(rows)\]

        \# fill the list with random terrain symbols

        for i in range(rows):

            for j in range(cols):

                [self.map](http://self.map)\[i\]\[j\] = random.choice(self.terrain)

        \# place the exit symbol in a random edge position

        \# choose a random edge: 0 for top, 1 for right, 2 for bottom, 3 for left

        edge = random.randint(0, 3)

        if edge == 0: # top edge

            i = 0 # first row

            j = random.randint(0, cols - 1) # random column

        elif edge == 1: # right edge

            i = random.randint(0, rows - 1) # random row

            j = cols - 1 # last column

        elif edge == 2: # bottom edge

            i = rows - 1 # last row

            j = random.randint(0, cols - 1) # random column

        else: # left edge

            i = random.randint(0, rows - 1) # random row

            j = 0 # first column

        \# replace the terrain symbol with the exit symbol

        [self.map](http://self.map)\[i\]\[j\] = self.exit

Trzeba dodać wyświetlanie mapy na ekranie:

def show(self):

    \# iterate over the rows of the map

    for row in [self.map](http://self.map):

        \# join the symbols in the row with spaces

        line = " ".join(row)

        \# print the line

        print(line)

I ewentualnie coś co sprawdza, czy możemy przejść przez teren:

def is_passable(self, terrain):

    \# check if the terrain symbol is a wall or water

    if terrain == "#" or terrain == "\~":

        \# return False, as these are impassable

        return False

    else:

        \# return True, as these are passable

        return True