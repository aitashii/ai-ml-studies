# VLAN — Przewodnik Prezentera (5-6 min)

## Zanim zaczniesz

Masz **5-6 minut** na całą prezentację. To nie jest wykład — mów spokojnie, naturalnie, jakbyś tłumaczył znajomemu. Nie musisz czytać slajdów — slajdy są dla widowni, Ty mówisz "co to znaczy". Przy każdym slajdzie podany jest orientacyjny czas.

---

## Slajd 1 — Tytuł (15 sekund)

*"Dzień dobry. Nasz temat to VLAN — Virtual Local Area Network, czyli Wirtualne Sieci Lokalne. To temat numer 25 z listy. Za chwilę wytłumaczę czym jest VLAN, po co się go używa i pokażę jak wygląda konfiguracja w Cisco Packet Tracer."*

---

## Slajd 2 — Czym jest VLAN? (45 sekund)

Wskaż na definicję po lewej stronie i powiedz:

*"VLAN to sposób na podzielenie jednej fizycznej sieci na kilka oddzielnych sieci wirtualnych. Mamy jeden switch, jeden kabel — ale logicznie tworzymy oddzielne 'bańki', które nie widzą się nawzajem."*

Wskaż na diagram z trzema kolorami po prawej:

*"Najlepiej wyobrazić sobie biurowiec. Mamy jeden budynek — jeden switch fizyczny. Ale dział IT, dział HR i Zarząd każdy ma swoją osobną sieć. Pracownik HR nie może 'podsłuchać' ruchu IT-ków, i na odwrót. To właśnie robi VLAN."*

---

## Slajd 3 — Po co VLAN? (40 sekund)

Wskaż kolejno na trzy karty:

*"VLAN daje nam trzy główne korzyści. Po pierwsze bezpieczeństwo — ruch jest izolowany między działami, ataki sieciowe nie rozprzestrzeniają się po całej firmie. Po drugie wydajność — normalnie broadcast, czyli pakiet wysyłany do wszystkich, leci do każdego komputera w sieci. Z VLAN leci tylko do swojego działu — mniej zbędnego ruchu. Po trzecie elastyczność — jeśli przenosimy pracownika z HR do IT, nie przepinamy żadnych kabli, wystarczy zmienić jedną komendę w konfiguracji switcha."*

---

## Slajd 4 — Typy VLAN (40 sekund)

*"Są cztery główne typy VLAN. Data VLAN — to standardowy VLAN dla komputerów i urządzeń użytkowników, każdy dział ma swój. Native VLAN, czyli domyślny VLAN 1 — każdy switch Cisco ma go od razu po włączeniu, najlepiej go zmienić ze względów bezpieczeństwa. Management VLAN — osobna sieć tylko do zarządzania switchami i routerami, żeby nikt postronny nie miał dostępu do konfiguracji. I Voice VLAN — dedykowany dla telefonii VoIP, zapewnia priorytet dla głosu żeby rozmowy były płynne."*

---

## Slajd 5 — Access vs Trunk (50 sekund)

*"W sieci z VLAN mamy dwa rodzaje portów na switchu."*

Wskaż lewą stronę:

*"Access port — to port do którego podłączamy komputer lub inne urządzenie końcowe. Należy do jednego VLAN-u. Urządzenie nie 'wie' że jest w VLAN-ie, po prostu widzi normalną sieć."*

Wskaż prawą stronę:

*"Trunk port — to port który łączy dwa switche ze sobą. Przez jeden kabel przesyła ruch z wielu VLAN-ów jednocześnie. Żeby to działało, każda ramka jest tagowana — ma przyklejoną etykietkę z numerem VLAN-u. Do tego służy standard 802.1Q, który zobaczymy na następnym slajdzie."*

---

## Slajd 6 — IEEE 802.1Q (30 sekund)

*"Standard 802.1Q definiuje jak dokładnie wygląda ten tag. Do normalnej ramki Ethernet dodajemy 4 dodatkowe bajty. W środku tagu mamy między innymi 12-bitowy identyfikator VLAN — to daje nam możliwość stworzenia aż 4094 różnych VLAN-ów w jednej sieci. Taki tag jest dodawany przez switch automatycznie przy wyjściu z portu trunk i usuwany przy wejściu do portu access, więc urządzenie końcowe w ogóle tego nie widzi."*

---

## Slajd 7 — Z VLAN vs bez VLAN (30 sekund)

*"To porównanie dobrze pokazuje różnicę. Bez VLAN — jeden broadcast domain, brak izolacji, zmiana fizyczna wymaga przepinania kabli, ataki rozchodzą się po całej sieci. Z VLAN — każdy dział to osobna domena, pełna izolacja, zmiany tylko w konfiguracji, ataki zawarte. Różnica jest znacząca szczególnie w większych firmach."*

---

## Slajd 8 — Projekt w Packet Tracer (50 sekund)

Wskaż na schemat:

*"W Cisco Packet Tracer przygotowaliśmy projekt sieci firmy z jednym switchem i sześcioma komputerami w trzech działach. VLAN 10 to dział IT — dwa komputery z adresami 192.168.10.x. VLAN 20 to HR — 192.168.20.x. VLAN 30 to Zarząd — 192.168.30.x."*

*"Każdy komputer jest podłączony do portu access — port należy do jednego VLAN-u. Sprawdziliśmy że ping działa między komputerami w tym samym VLAN-ie, ale nie działa między różnymi VLAN-ami — bo o to właśnie chodzi w segmentacji."*

---

## Slajd 9 — Komendy Cisco IOS (40 sekund)

Wskaż kolejno na cztery bloki kodu:

*"Konfiguracja w Cisco IOS składa się z czterech kroków. Najpierw tworzymy VLAN-y komendą 'vlan' i nadajemy im nazwy. Potem konfigurujemy każdy port access — mówimy do którego VLAN-u należy. Następnie konfigurujemy port trunk między switchami — mówimy jakie VLAN-y mogą przez niego przechodzić. Na końcu weryfikujemy komendą 'show vlan brief' — widzimy listę wszystkich VLAN-ów i portów do nich przypisanych."*

---

## Slajd 10 — Podsumowanie (15 sekund)

*"Podsumowując — VLAN to logiczna segmentacja sieci bez potrzeby dodatkowego sprzętu. Access port dla urządzeń końcowych, trunk między switchami. Daje bezpieczeństwo, wydajność i elastyczność. VLAN ID od 1 do 4094. Tyle ode mnie, dziękuję."*

---

## Co mówić o Packet Tracerze jeśli ktoś zapyta

Jeśli prowadzący lub ktoś z sali zapyta o szczegóły projektu:

*"W Packet Tracerze użyliśmy switcha Cisco Catalyst 2960. Podłączyliśmy sześć komputerów do portów Fa0/1 do Fa0/6. Porty 1 i 2 to VLAN 10, porty 3 i 4 to VLAN 20, porty 5 i 6 to VLAN 30. Każdemu komputerowi ręcznie ustawiliśmy adres IP w odpowiedniej podsieci. Po skonfigurowaniu VLAN-ów w CLI sprawdziliśmy działanie pingiem — w tym samym VLAN ping przechodzi, między różnymi VLAN-ami jest timeout. Dokładnie tak jak powinno działać."*

---

## Szybka ściągawka — co to jest co

Kilka terminów na wypadek pytań:

| Termin | Co to znaczy |
|--------|-------------|
| Switch | Urządzenie sieciowe do którego podłączamy komputery w sieci lokalnej |
| Port Fa0/1 | Konkretne gniazdo fizyczne w switchu (FastEthernet, numer 1) |
| Ping | Komenda testująca czy dwa urządzenia mogą się komunikować |
| 192.168.10.0/24 | Adres sieci — wszystkie komputery zaczynają się od 192.168.10. |
| show vlan brief | Komenda pokazująca listę VLAN-ów i portów — pierwsza rzecz do sprawdzenia gdy coś nie działa |
| Access port | Port dla komputera — należy do jednego VLAN-u |
| Trunk port | Port między switchami — przenosi wiele VLAN-ów naraz |
| 802.1Q | Standard tagowania ramek — te 4 bajty doklejane do każdego pakietu |

---

## Timing — szybkie podsumowanie

| Slajd | Temat | Czas |
|-------|-------|------|
| 1 | Tytuł | 15 sek |
| 2 | Czym jest VLAN | 45 sek |
| 3 | Korzyści | 40 sek |
| 4 | Typy VLAN | 40 sek |
| 5 | Access vs Trunk | 50 sek |
| 6 | 802.1Q | 30 sek |
| 7 | Porównanie | 30 sek |
| 8 | Packet Tracer | 50 sek |
| 9 | Komendy | 40 sek |
| 10 | Podsumowanie | 15 sek |
| **RAZEM** | | **~5:45** |
