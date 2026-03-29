# VLAN w Cisco Packet Tracer — Przewodnik dla Total Noob

## Zanim zaczniesz — jak wygląda okno Packet Tracera

Po otwarciu Packet Tracera zobaczysz 5 stref na ekranie:

- **Górny pasek** — menu (File, Edit, itp.)
- **Szary obszar pośrodku** — workspace, tu budujesz sieć
- **Lewy dolny róg** — kategorie urządzeń (małe ikonki)
- **Prawy dolny róg** — konkretne modele urządzeń (większe obrazki)
- **Prawy górny róg** — tryby: **Realtime** (zegarek) i **Simulation** (stoper)

> Upewnij się że jesteś w trybie **Realtime** — kliknij zegarek jeśli nie jest podświetlony.

---

## KROK 1 — Dodaj switch (przełącznik)

1. W **lewym dolnym rogu** kliknij ikonę wyglądającą jak **pudełko z błyskami** — to `Network Devices`
2. W **prawym dolnym rogu** kliknij ikonę wyglądającą jak **prostokąt z portami** — to `Switches`
3. Znajdź model **2960** (ma napis "2960" pod spodem) i kliknij na niego **raz**
4. Kliknij **raz na środku szarego obszaru roboczego** — switch się pojawi
5. Kliknij **dwukrotnie** na napis "Switch0" pod ikonką, wpisz `SW-GLOWNY` i wciśnij Enter

---

## KROK 2 — Dodaj 6 komputerów (PC)

1. W **lewym dolnym rogu** kliknij ikonę wyglądającą jak **monitor komputera** — to `End Devices`
2. W prawym dolnym rogu kliknij **PC** (prostokąt z ekranem)
3. Kliknij na obszar roboczy — pojawi się komputer. Powtórz **6 razy**
4. Rozstaw komputery tak żeby switch był pośrodku
5. Zmień nazwy klikając dwukrotnie na każdy napis:
   - `PC-IT-1`, `PC-IT-2` — po lewej stronie switcha
   - `PC-HR-1`, `PC-HR-2` — powyżej switcha
   - `PC-MGT`, `PC-MRK` — po prawej stronie switcha

---

## KROK 3 — Połącz komputery kablem ze switchem

1. W **lewym dolnym rogu** kliknij ikonę wyglądającą jak **błyskawica/zygzak** — to `Connections`
2. W prawym dolnym rogu wybierz **Copper Straight-Through** — to **czarna ciągła linia** (nie ta z kreskami!)
3. Kursor zmieni się w krzyżyk — to znaczy że możesz rysować połączenia
4. Kliknij na **PC-IT-1** → w okienku które się pojawi wybierz `FastEthernet0`
5. Kliknij na **SW-GLOWNY** → wybierz `FastEthernet0/1`
6. Kabel zostanie narysowany ✅

Powtórz dla każdego komputera:

| Komputer | Port PC | Port switcha |
|----------|---------|--------------|
| PC-IT-1 | FastEthernet0 | FastEthernet0/1 |
| PC-IT-2 | FastEthernet0 | FastEthernet0/2 |
| PC-HR-1 | FastEthernet0 | FastEthernet0/3 |
| PC-HR-2 | FastEthernet0 | FastEthernet0/4 |
| PC-MGT | FastEthernet0 | FastEthernet0/5 |
| PC-MRK | FastEthernet0 | FastEthernet0/6 |

> Kable mogą być pomarańczowe — to normalne! Poczekaj 20-30 sekund aż zmienią kolor na **zielony**.

---

## KROK 4 — Ustaw adresy IP na komputerach

Dla każdego PC po kolei:

1. Kliknij **dwukrotnie** na ikonkę PC
2. Kliknij zakładkę **Desktop**
3. Kliknij **IP Configuration** (ikona z ekranem i cyferkami)
4. Kliknij kółko przy **Static**
5. Wpisz adres IP i maskę z tabeli poniżej
6. Zamknij okno (X)

| Komputer | IP Address | Subnet Mask |
|----------|------------|-------------|
| PC-IT-1 | 192.168.10.1 | 255.255.255.0 |
| PC-IT-2 | 192.168.10.2 | 255.255.255.0 |
| PC-HR-1 | 192.168.20.1 | 255.255.255.0 |
| PC-HR-2 | 192.168.20.2 | 255.255.255.0 |
| PC-MGT | 192.168.30.1 | 255.255.255.0 |
| PC-MRK | 192.168.30.2 | 255.255.255.0 |

> Pole `Default Gateway` zostaw puste.

---

## KROK 5 — Otwórz konsolę switcha (CLI)

1. Kliknij **dwukrotnie** na ikonkę **SW-GLOWNY**
2. Kliknij zakładkę **CLI** (czarny ekran tekstowy)
3. Jeśli pojawi się pytanie `Would you like to enter the initial configuration dialog? [yes/no]:` → wpisz `no` i Enter
4. Poczekaj na znak zachęty: `Switch>` lub `Switch#`

> **Zasada:** po każdej linii wciskasz Enter. Wpisuj dokładnie tak jak pokazano — wielkie/małe litery i spacje mają znaczenie!

---

## KROK 6 — Wpisz komendy do switcha

### Część A — Utwórz VLAN-y

```
enable
configure terminal
vlan 10
name IT
vlan 20
name HR
vlan 30
name ZARZAD
exit
```

Po `enable` powinno pojawić się `Switch#` ✅  
Po `configure terminal` powinno pojawić się `Switch(config)#` ✅

### Część B — Przypisz porty do VLAN-ów

```
interface FastEthernet0/1
switchport mode access
switchport access vlan 10
exit
interface FastEthernet0/2
switchport mode access
switchport access vlan 10
exit
interface FastEthernet0/3
switchport mode access
switchport access vlan 20
exit
interface FastEthernet0/4
switchport mode access
switchport access vlan 20
exit
interface FastEthernet0/5
switchport mode access
switchport access vlan 30
exit
interface FastEthernet0/6
switchport mode access
switchport access vlan 30
exit
```

### Część C — Zapisz konfigurację

```
end
write memory
```

Powinieneś zobaczyć: `Building configuration... [OK]` ✅

---

## KROK 7 — Sprawdź czy VLAN-y działają

W CLI switcha wpisz:

```
show vlan brief
```

Powinieneś zobaczyć:

```
VLAN Name         Status    Ports
---- ------------ --------- -------------------
1    default      active    Fa0/7, Fa0/8...
10   IT           active    Fa0/1, Fa0/2
20   HR           active    Fa0/3, Fa0/4
30   ZARZAD       active    Fa0/5, Fa0/6
```

Jeśli VLAN 10, 20 i 30 są widoczne z odpowiednimi portami — sukces! Zamknij okno switcha.

---

## KROK 8 — Przetestuj pingiem

### Test 1 — w obrębie tego samego VLAN-u (powinien DZIAŁAĆ ✅)

1. Kliknij dwukrotnie na **PC-IT-1**
2. Zakładka **Desktop** → **Command Prompt**
3. Wpisz: `ping 192.168.10.2`
4. Wynik: 4 linie `Reply from 192.168.10.2` ✅

### Test 2 — między różnymi VLAN-ami (powinien NIE DZIAŁAĆ ✅)

1. Na tym samym PC-IT-1 wpisz: `ping 192.168.20.1`
2. Wynik: `Request timeout` ✅

> `Request timeout` to **prawidłowy wynik** — VLAN celowo blokuje komunikację między działami!

---

## KROK 9 — Zapisz projekt

**File → Save** (lub Ctrl+S) → wpisz nazwę `VLAN_projekt` → Save.  
Plik zostanie zapisany jako `VLAN_projekt.pkt`

---

## Typowe błędy i rozwiązania

| Problem | Rozwiązanie |
|---------|-------------|
| Kable są czerwone | Poczekaj 20-30 sekund. Jeśli nadal czerwone — sprawdź czy użyłeś Copper Straight-Through |
| `% Invalid input detected` w CLI | Wpisz `end`, potem od nowa `enable` i `configure terminal` |
| `show vlan brief` nie pokazuje VLAN 10/20/30 | Powtórz Krok 6 Część A od początku |
| Ping nie działa w tym samym VLAN-ie | Sprawdź IP adresy (Krok 4) — czy oba PC mają adresy 192.168.10.x |
