# Chat History - AI & ML Studies

This file tracks conversations, learning progress, experiments, and development work related to AI and Machine Learning studies.

## Repository Overview

**Purpose**: Personal repository for AI and ML learning, experiments, and study materials
**Created**: 2025-12-13
**Focus Areas**: To be determined based on study progression

## Session Log

### Session: 2025-12-13

**Repository Initialization:**
- Created new repository `ai-ml-studies` for AI and ML learning
- Separated from previous work repositories (project-octopus, etc.)
- Initialized with git on main branch
- Location: `/Users/ola/Documents/GitHub/ai-ml-studies`

**Purpose:**
- Dedicated space for AI/ML learning materials
- Track experiments and projects
- Document learning journey and insights
- Keep AI/ML work separate from other projects

**Initial Setup:**
- Created CHAT_HISTORY.md for conversation tracking
- Created README.md with repository overview
- Initialized git repository with main branch
- Installed GitHub CLI via Homebrew
- Created repository on GitHub: https://github.com/aitashii/ai-ml-studies
- Configured remote origin using HTTPS (due to SSH key being associated with different account)
- Successfully pushed initial commit to remote

**Technical Details:**
- GitHub Account: aitashii
- Repository URL: https://github.com/aitashii/ai-ml-studies.git
- Local Path: /Users/ola/Documents/GitHub/ai-ml-studies
- Initial Commit: 37f45a9 - "Initial commit: Setup AI & ML studies repository"

**Repository Status:**
- Status: Active and synced with remote
- Branch: main
- Files: README.md, CHAT_HISTORY.md

---

### Session: 2025-12-13 (Continued) - Adding Learning Resources

**Files Added in This Session:**
- README.md - Repository overview and structure
- CHAT_HISTORY.md - This conversation log
- resources/python/wpradzenie_do_pythona.md - Introduction to Python
- resources/python/data_types.md - Python data types guide
- resources/python/operatory.md - Python operators reference
- resources/python/input_output.md - Input/Output in Python
- resources/python/style_guide.md - Python PEP 8 style guide
- resources/tools/vscode_shortcuts.md - VSCode keyboard shortcuts
- resources/networking/Klasy sieci.md - IP address classes and subnetting
- requirements.txt - Python dependencies management file
- resources/wprowadzenie-do-programowania/ - Complete course materials (14 labs, 7 PDFs)

---

### Session: 2026-02-07 - Creating Programming Exercises

**Files Created:**
- Cwiczenia-programowanie/podstawy-programowania.ipynb - 12 programming exercises in 4 sections

---

### Session: 2026-03-28 - Zajecia uniwersyteckie: TI i Ochrona Wlasnosci Intelektualnej + Zaawansowane Sieci

#### Krok 1: Nowe foldery dla przedmiotow

Utworzono strukture folderow dla dwoch nowych przedmiotow semestru 2025/2026:
- `resources/ti-ochrona-wlasnosci-intelektualnej/` (notatki/, laboratoria/, materialy/, README.md)
- `resources/zaawansowane-sieci-komputerowe/` (notatki/, laboratoria/, materialy/, README.md)

---

#### Cwiczenie 1 - TI: Aplikacja workout tracker + analiza prawna zasob0w

**Projekt laboratoryjny: RepLog - Daily Workout Tracker**

Aplikacja webowa (HTML/CSS/JS) do trackowania codziennych treningow silowniowych.

Zasoby uzyte w projekcie i analiza prawna:

| Zasob | Zrodlo | Licencja | Utwor? | Mozna uzyc? |
|-------|--------|----------|--------|-------------|
| Fotografia | Pexels - Anastasia Shuraeva (nr 4944004) | Pexels License | TAK | TAK |
| Czcionki | Google Fonts (Bebas Neue, DM Mono, DM Sans) | OFL 1.1 | TAK | TAK |
| Kod JS/HTML/CSS | Oryginalny | Wlasne prawa autorskie | TAK | TAK |

**Pliki utworzone:**
- `resources/ti-ochrona-wlasnosci-intelektualnej/laboratoria/01-utwory-i-zasoby.md`
- `replog-workout-tracker.html`
- `RepLog-prezentacja-v3.pptx`

---

#### Cwiczenie 2 - TI: Mini analiza "Czy AI zwieksza produktywnosc?"

5 zrodel: GitHub Copilot Study, BCG/Harvard HBS, MIT Writing Study, Stanford/MIT Customer Service, Nielsen Norman Group.

**Pliki utworzone:**
- `AI_Produktywnosc_Analiza.xlsx`
- `AI_Produktywnosc_Slajd_v2.pptx`

---

#### Cwiczenie 4 - TI: Analiza efektywnosci zespolu IT (Sprint #78)

Fibonacci SP Model (finalna metodologia):
- Skala: 1SP<=0.5h | 2SP<=2h | 3SP<=4h | 5SP<=8h | 8SP<=20h
- Capacity: 80h - 20% scrum - 10% przerwy = 56h deep work/sprint

Wyniki finalnej analizy:

| Miejsce | Developer | SP Total | Earned Rate |
|---------|-----------|----------|-------------|
| 1 | Piotr | 36 | 102.9% |
| 2 | Bartek | 35 | 100.0% |
| 3 | Kuba | 24 | 85.7% |
| 7 | Marta | 28 | 80.0% |

**Pliki utworzone:**
- `Analiza_Fibonacci_Sprint78.xlsx`
- `Analiza_Fibonacci_Slajd.pptx`

---

#### Zaawansowane Sieci - Temat 25: VLAN

Wybrany temat: VLAN (prosty projekt - 1 switch, 6 PC, bez routera).

Topologia (SWITCH-GLOWNY, Cisco Catalyst 2960):

| PC | VLAN | IP | Port switcha |
|----|------|----|--------------|
| PC-IT-1 | 10 | 192.168.10.1 | Fa0/5 |
| PC-IT-2 | 10 | 192.168.10.2 | Fa0/6 |
| PC-HR-1 | 20 | 192.168.20.1 | Fa0/3 |
| PC-HR-2 | 20 | 192.168.20.2 | Fa0/4 |
| PC-ZARZAD-1 | 30 | 192.168.30.1 | Fa0/1 |
| PC-ZARZAD-2 | 30 | 192.168.30.2 | Fa0/2 |

Uwagi:
- Nazwy zmienione: PC-MGT/MRK → PC-ZARZAD-1/PC-ZARZAD-2
- Default Gateway: puste (nie potrzebne bez routera)
- Izolacja dziala w switchu, nie w adresach IP
- X-y w Simulation mode = normalne zachowanie STP, nie blad konfiguracji

Wynik show vlan brief (potwierdzony):
```
10  IT      active  Fa0/5, Fa0/6
20  HR      active  Fa0/3, Fa0/4
30  ZARZAD  active  Fa0/1, Fa0/2
```

**Pliki utworzone:**
- `resources/zaawansowane-sieci-komputerowe/laboratoria/01-VLAN-packet-tracer-guide.md`
- `resources/zaawansowane-sieci-komputerowe/laboratoria/01-VLAN-przewodnik-prezentera.md`
- `resources/zaawansowane-sieci-komputerowe/laboratoria/01-VLAN-legenda-tracer.md`
- `resources/zaawansowane-sieci-komputerowe/laboratoria/01-VLAN-zrodla.md`
- `VLAN_Prezentacja_v2.pptx` (10 slajdow, paleta Space Indigo)

---

### Session: 2026-03-29 - Algorytmy i Struktury Danych + Pytanie o Slack

#### Krotka rozmowa o Slacku

W trakcie sesji padlo pytanie czy Claude ma dostep do Slacka Kaiko i moze czytac wiadomosci. Odpowiedz: tak, przez polaczone narzedzie Slack. Claude sprawdzil DM z Hannesem Hase (Product, hannes.hase@kaiko.ai) i potwierdzil ze ostatnia wiadomosc w konwersacji byla od Oli (2026-03-27 16:45): "I'm glad you at least feel relieved, I'm sure you will find something better for you which will help you utilize all your skills". Konwersacja dotyczyla odejscia Hannesa z Kaiko.

---

#### Algorytmy i Struktury Danych - Stos i Kolejka

**Nowy folder:** `resources/algorytmy-i-struktury-danych/laboratoria/`

**Temat: Stos (Stack) - LIFO**

Klasa Stos z metodami: push, pop, peek, jest_pusty, rozmiar.

Zadanie 1 - Odwracanie napisu:
- Wersja 1 (nasze): petla while + operator +=
- Wersja 2 (wykladowcy, pastebin.com/K9tzXmtB): testy jako lista krotek z walidacja [OK]/[FAIL], alternatywa z list comprehension

Zadanie 2 - Palindrom:
- Kluczowa linia: `oczyszczony = napis.lower().replace(" ", "")`
- Wszystkie 7 testow [OK]

**Temat: Kolejka (Queue) - FIFO**

Klasa Kolejka uzywajaca collections.deque (popleft() = O(1) vs list.pop(0) = O(n)).

Zadanie 3 - Przeplatanie dwoch kolejek:
- Trzy petle: pierwsza while (obie niepuste), potem dwie dopisujace reszte
- Wszystkie 4 testy [OK]

Zadanie 4 - Zliczanie elementow w kolejce (bez niszczenia):
- Klucz: range(n) zapewnia dokladnie n obrotow, kolejka wraca do stanu poczatkowego
- Zlozonosc: O(n) czasowa, O(1) pamieciowa
- Wszystkie 5 testow [OK]

**Pliki utworzone:**
- `resources/algorytmy-i-struktury-danych/laboratoria/01-stos.py`
- `resources/algorytmy-i-struktury-danych/laboratoria/01-stos-notatki.md`
- `resources/algorytmy-i-struktury-danych/laboratoria/02-kolejka.py`
- `resources/algorytmy-i-struktury-danych/laboratoria/02-kolejka-notatki.md`

---

## Study Notes

(Add your study notes, experiments, and learnings here as you progress)

---

## Project Ideas

(Track AI/ML project ideas and experiments here)

---

## Resources

(Add useful resources, papers, tutorials, courses, etc.)
