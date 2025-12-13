Pule
A: 1.0.0.0 % 127.255.255.255    /8      255.0.0.0
B: 128.0.0.0 % 191.255.255.255  /16     255.255.0.0
C: 192.0.0.0 % 223.255.255.255  /24     255.255.255.0
D: 224.0.0.0 % 239.255.255.255  (Multicast)
E: 240.0.0.0 % 255.255.255.255  (Eksperymentalna/Akademicka)

Pule Prywatne
A: 10.0.0.0 - 10.255.255.255
B: 172.16.0.0 - 172.31.255.255
C: 192.168.0.0 - 192.168.255.255

Zadanie 1.
    192.168.100.14/27
    11000000.10101000.01100100.00001110
    Klasa: C(/24)
    Maska: /27 255.255.255.224
    11111111.11111111.11111111.11100000

    Adres sieci:
    11000000.10101000.01100100.00001110  (IP)
    AND
    11111111.11111111.11111111.11100000  (Maska)
    -----------------------------------------------
    =  11000000.10101000.01100100.00000000
    =  192.168.100.0

Zadanie 2
    150.100.100.100/18
    10010110.01100100.01100100.01100100
    Klasa: B(/16)
    Maska: /18 255.255.192.0
    (Maska /18 oznacza, że pierwsze 18 bitów to jedynki, a pozostałe to zera.
    Binarnie: 11111111.11111111.11000000.00000000
    Dziesiętnie:
    Pierwszy oktet: 11111111 = 255
    Drugi oktet: 11111111 = 255
    Trzeci oktet: 11000000 = 128 + 64 = 192
    Czwarty oktet: 00000000 = 0)
    11111111.11111111.11000000.00000000

    Adres sieci:
    10010110.01100100.01100100.01100100  (IP)
    AND
    11111111.11111111.11000000.00000000  (Maska)
    -----------------------------------------------
    =  10010110.01100100.01000000.00000000
    =  150.100.64.0

Zadanie 3
    12.13.14.15/16
    00001100.00001101.00001110.00001111
    Klasa: A(/8)
    Maska: /16 255.255.0.0
    11111111.11111111.00000000.00000000

    Adres sieci:
    00001100.00001101.00001110.00001111  (IP)
    AND
    11111111.11111111.00000000.00000000  (Maska)
    -----------------------------------------------
    =  00001100.00001101.00000000.00000000
    =  12.13.0.0

    Ilość bitów na hosty: 16 (bo tyle mamy zer w masce podsieci)
    Max ilość hostów: 2^16 - 2
    Ilość bitów na podsieć: 8
    Max ilość podsieci: 2^8
    Broadcast: 12.13.255.255
    Adres ostatniego hosta: 12.13.255.254

Proste wyjaśnienie krok po kroku:

1. Co to jest maska /n:
   - Fragment "/n" mówi ile pierwszych bitów to jedynki.
   - Przykład: /27 oznacza 27 jedynek, czyli maskę 255.255.255.224.

2. Zamiana IP i maski na binarne:
   - Każdy oktet adresu zamieniasz na 8-bitowy zapis binarny.
   - To samo robisz z maską (np. 255 = 11111111, 224 = 11100000).

3. Obliczenie adresu sieci:
   - Dla każdego bitu wykonaj operację AND (IP_bit AND Mask_bit).
   - Wynik to adres sieci (pierwszy adres w podsieci).

4. Ile hostów w podsieci:
   - Policz ile jest zer w masce (to h).
   - Maks hostów = 2^h - 2 (odejmujemy adres sieci i broadcast).

5. Obliczenie broadcastu:
   - Weź adres sieci i ustaw wszystkie bity hosta na 1 — to jest broadcast.

6. Pierwszy i ostatni host:
   - Pierwszy host = adres sieci + 1.
   - Ostatni host = broadcast - 1.

7. Przykład skrócony (192.168.100.14/27):
   - Maska /27 = 255.255.255.224 -> w binarnie: 11111111.11111111.11111111.11100000
   - IP w binarnie: 192.168.100.14 -> ...00001110 (patrz powyżej)
   - AND -> adres sieci = 192.168.100.0
   - Zera w masce = 5 -> hostów = 2^5 - 2 = 30
   - Broadcast = 192.168.100.31
   - Zakres hostów = 192.168.100.1 - 192.168.100.30

Zadanie 4
    100.110.120.130/18
    Klasa: A
    1) Maska /18 = 255.255.192.0
       binarnie: 11111111.11111111.11000000.00000000

    2) IP w binarnie:
       100  = 01100100
       110  = 01101110
       120  = 01111000
       130  = 10000010
       IP: 01100100.01101110.01111000.10000010

    3) AND IP i maski:
       01100100.01101110.01111000.10000010  (IP)
       11111111.11111111.11000000.00000000  (maska)
       -----------------------------------------------
       01100100.01101110.01000000.00000000  -> 100.110.64.0 (adres sieci)

    4) Liczba bitów hosta = 32 - 18 = 14 (ilosc zer w zapisie binarnym)
       Maks hostów = 2^14 - 2 = 16382

    5) Broadcast:
       trzeci oktet: 01000000 (64) + 00111111 (63) => 01111111 (127)
       broadcast = 100.110.127.255

    6) Zakres hostów:
       pierwszy host = 100.110.64.1
       ostatni host  = 100.110.127.254

Zadanie 5
    130.11.12.200/22
    Klasa: B
    1) Maska /22 = 255.255.252.0
       binarnie: 11111111.11111111.11111100.00000000

    2) IP w binarnie:
       130 = 10000010
       11  = 00001011
       12  = 00001100
       200 = 11001000
       IP: 10000010.00001011.00001100.11001000

    3) AND IP i maski:
       10000010.00001011.00001100.11001000  (IP)
       11111111.11111111.11111100.00000000  (maska)
       -----------------------------------------------
       10000010.00001011.00001100.00000000  -> 130.11.12.0 (adres sieci)

    4) Liczba bitów hosta = 32 - 22 = 10
       Maks hostów = 2^10 - 2 = 1022

       Ilosc bitow na podsiec: /22 - /16 -> 6

    5) Broadcast (obliczamy w ten sposob ze dopisujemy do tego ANDa) ponizej tam gdzie maska ma 0 jedynki a przed przepisujemy to co dostajemy z ANDa)
             11111111.11111111.111111||00.00000000 (maska)
(adres sieci)10000010.00001011.000011||11.11111111 (zera maski zamienione na jedynki)
       Boroadcast: 130.11.15.255

    6) Zakres hostów:
       pierwszy host = 130.11.12.1
       ostatni host  = 130.11.15.254

Zadanie 6
192.168.66.220/25
    Klasa: C
    1) Maska /25 = 255.255.255.128
       binarnie: 11111111.11111111.11111111.10000000

    2) IP w binarnie:
       192 = 11000000
       168 = 10101000
       66  = 01000010
       220 = 11011100
       IP: 11000000.10101000.01000010.11011100

    3) AND IP i maski:
       11000000.10101000.01000010.11011100  (IP)
       11111111.11111111.11111111.10000000  (maska)
       -----------------------------------------------
       11000000.10101000.01000010.10000000  -> 192.168.66.128 (adres sieci)

    4) Liczba bitów hosta = 32 - 25 = 7
       Maks hostów = 2^7 - 2 = 126

       Ilość bitów na podsieć: /25 - /24 -> 1

    5) Broadcast:
       W adresie sieci (binarnie) zamieniamy bity hosta na jedynki:
       11000000.10101000.01000010.11111111
       Broadcast: 192.168.66.255

    6) Zakres hostów:
       pierwszy host = 192.168.66.129
       ostatni host  = 192.168.66.254
    
Zadanie 7 
2.3.4.5/30
    Klasa: A
    1) Maska /30 = 255.255.255.252
       binarnie: 11111111.11111111.11111111.11111100

    2) IP w binarnie:
       2   = 00000010
       3   = 00000011
       4   = 00000100
       5   = 00000101
       IP: 00000010.00000011.00000100.00000101

    3) AND IP i maski:
       00000010.00000011.00000100.00000101  (IP)
       11111111.11111111.11111111.11111100  (maska)
       -----------------------------------------------
       00000010.00000011.00000100.00000100  -> 2.3.4.4 (adres sieci)

    4) Liczba bitów hosta = 32 - 30 = 2
       Maks hostów = 2^2 - 2 = 2

       Ilość bitów na podsieć: /30 - /8 -> 22

    5) Broadcast:
       W adresie sieci (binarnie) zamieniamy bity hosta na jedynki:
       00000010.00000011.00000100.00000111
       Broadcast: 2.3.4.7

    6) Zakres hostów:
       pierwszy host = 2.3.4.5
       ostatni host  = 2.3.4.6