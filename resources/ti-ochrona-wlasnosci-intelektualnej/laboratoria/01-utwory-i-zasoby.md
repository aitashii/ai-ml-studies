# Laboratorium 01 - Analiza prawna zasobów: RepLog Workout Tracker

**Data:** 2026-03-28  
**Przedmiot:** Technologie Informacyjne i Ochrona Wlasnosci Intelektualnej  
**Projekt:** Aplikacja do trackowania treningów - RepLog

---

## Opis projektu

Jednostronicowa aplikacja webowa (HTML/CSS/JS) do codziennego logowania cwiczen silowniowych.

Struktura strony:
- Naglowek (header) - logo, aktualna data
- Sekcja hero - obraz tla + tytul i opis aplikacji
- Sekcja funkcji - formularz dodawania cwiczen, statystyki, historia

---

## Analiza prawna zasobów

### 1. Obraz tla (fotografia)

| Pole | Tresc |
|------|-------|
| Zasob | Zdjecie silowni - hantle na stojaku |
| Zrodlo | Unsplash, autor: Victor Freitas |
| URL | https://unsplash.com/photos/WvDYdXDzkhs |
| Licencja | Unsplash License |

**Czy jest to utwor?**  
TAK. Fotografia spelnia kryteria utworu w rozumieniu art. 1 ustawy z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych (Dz.U. 1994 nr 24 poz. 83). Jest przejawem dzialalnosci tworczej fotografa (wybor kompozycji, oswietlenia, kadru) o indywidualnym charakterze. Fotografie sa expressis verbis wymienione jako kategoria chronionego utworu (art. 1 ust. 2 pkt 3).

**Czy mozna uzyc?**  
TAK.

**Uzasadnienie:**  
Unsplash License pozwala na bezplatne uzycie fotografii w projektach komercyjnych i niekomercyjnych bez obowiazku atrybucji (choc jest zalecana). Licencja nie ogranicza praw uzytkownika w zakresie modyfikacji i osadzania obrazow na stronach internetowych. Dodalem atrybucje w stopce strony oraz w komentarzu HTML jako dobra praktyke.

Ograniczenia licencji Unsplash, ktore nie dotycza tego projektu:
- zakaz sprzedazy fotografii jako samodzielnego produktu
- zakaz tworzenia konkurencyjnego serwisu ze zdjeciami

---

### 2. Czcionki (typografia)

| Pole | Tresc |
|------|-------|
| Zasob | Bebas Neue, DM Mono, DM Sans |
| Zrodlo | Google Fonts |
| URL | https://fonts.google.com |
| Licencja | SIL Open Font License 1.1 (OFL) |

**Czy jest to utwor?**  
TAK. Czcionki (kroje pisma) sa chronione prawem autorskim jako utwory plastyczne (art. 1 ust. 2 pkt 5 ustawy). Projekt graficzny znakow alfanumerycznych stanowi przejaw indywidualnej tworczosci projektanta.

**Czy mozna uzyc?**  
TAK.

**Uzasadnienie:**  
Licencja OFL (Open Font License) to otwarta licencja pozwalajaca na:
- swobodne uzywanie w projektach komercyjnych i edukacyjnych
- osadzanie via @font-face lub Google Fonts CDN
- modyfikacje pod warunkiem zachowania licencji

Pobranie i renderowanie przez Google Fonts CDN nie wymaga dodatkowych zezwolen.

---

### 3. Kod zrodlowy

| Pole | Tresc |
|------|-------|
| Zasob | JavaScript, HTML, CSS strony |
| Autor | Oryginalny, napisany na potrzeby projektu |
| Zrodlo | Brak zewnetrznych bibliotek z cudzym kodem |

**Czy jest to utwor?**  
TAK. Kod zrodlowy jest chroniony prawem autorskim jako utwor literacki (art. 1 ust. 2 pkt 1 ustawy). Trybunalowi Sprawiedliwosci UE potwierdzil ochrone kodu zrodlowego w sprawie SAS Institute Inc. v. World Programming Ltd (C-406/10). Ochrone zyskuje konkretna ekspresja (zapis kodu), nie sam algorytm ani idea.

**Czy mozna uzyc?**  
TAK - bez ograniczen.

**Uzasadnienie:**  
Kod zostal napisany samodzielnie na potrzeby tego projektu laboratoryjnego. Jako autor przysługuja mi pelne prawa autorskie majatkowe i osobiste (art. 16-17 ustawy). Nie korzystalem z zewnetrznych bibliotek JS (brak jQuery, lodash itp.) - aplikacja uzywa wylacznie natywnego API przegladarki (localStorage, DOM), ktore jest standardem W3C i nie jest objete prawem autorskim.

---

### 4. Tekst / dane w aplikacji

| Pole | Tresc |
|------|-------|
| Zasob | Nazwy kategorii cwiczen, opisy, etykiety UI |
| Autor | Oryginalny |

**Czy jest to utwor?**  
CZESCIOWO. Krotkie etykiety i nazwy kategorii (np. "Klatka", "Plecy", "Serie") to pojedyncze slowa lub minimalne fragmenty - nie spelniaja progu tworczosci indywidualnej i nie sa chronione. Dluzsze teksty opisowe ("Loguj cwiczenia, sledz postepy i buduj konsekwencje...") moga byc traktowane jako miniutworki o malym stopniu oryginalnosci.

**Czy mozna uzyc?**  
TAK - bez ograniczen.

**Uzasadnienie:**  
Wszystkie teksty w aplikacji zostaly napisane oryginalnie. Dane uzytkownika (nazwy cwiczen wpisywane przez uzytkownika) sa tworzone przez uzytkownika i jemu przysługuja.

---

## Podsumowanie

| Zasob | Typ | Utwor? | Legalne? | Podstawa |
|-------|-----|--------|----------|----------|
| Fotografia (Unsplash) | Obraz | TAK | TAK | Unsplash License |
| Czcionki (Google Fonts) | Typografia | TAK | TAK | OFL 1.1 |
| Kod HTML/CSS/JS | Oprogramowanie | TAK | TAK | Wlasne prawa autorskie |
| Etykiety UI | Tekst | CZESCIOWO | TAK | Wlasne prawa autorskie |

---

## Podstawa prawna

- Ustawa z dnia 4 lutego 1994 r. o prawie autorskim i prawach pokrewnych (Dz.U. 1994 nr 24 poz. 83, ze zm.)
- Dyrektywa 2009/24/WE Parlamentu Europejskiego w sprawie ochrony programow komputerowych
- Wyrok TSUE C-406/10, SAS Institute Inc. v. World Programming Ltd (ochrona kodu)
- Unsplash License: https://unsplash.com/license
- SIL Open Font License 1.1: https://scripts.sil.org/OFL
