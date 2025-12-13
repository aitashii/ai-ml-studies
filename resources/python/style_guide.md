# Konwencje Nazewnicze w Pythonie (PEP 8)

## Spis treści
- [Ogólne zasady](#ogólne-zasady)
- [Nazwy zmiennych i funkcji](#nazwy-zmiennych-i-funkcji)
- [Nazwy klas](#nazwy-klas)
- [Nazwy stałych](#nazwy-stałych)
- [Nazwy modułów i pakietów](#nazwy-modułów-i-pakietów)
- [Prywatne i chronione elementy](#prywatne-i-chronione-elementy)
- [Unikanie kolizji nazw](#unikanie-kolizji-nazw)
- [Przykłady](#przykłady)

---

## Ogólne zasady

1. **Nazwy powinny być opisowe i zrozumiałe**
   - Unikaj jednoliterowych nazw (z wyjątkiem liczników w pętlach: `i`, `j`, `k`)
   - Używaj pełnych słów zamiast skrótów (chyba że skrót jest powszechnie znany)

2. **Unikaj następujących znaków:**
   - `l` (mała litera L) - łatwo pomylić z `1` lub `I`
   - `O` (duża litera O) - łatwo pomylić z `0`
   - `I` (duża litera I) - łatwo pomylić z `1` lub `l`

3. **Nigdy nie używaj znaków spoza ASCII w identyfikatorach**

---

## Nazwy zmiennych i funkcji

**Konwencja:** `snake_case` (małe litery, słowa oddzielone podkreślnikami)

### Zmienne
```python
# Dobrze
user_name = "Jan"
total_count = 42
is_active = True

# Źle
userName = "Jan"  # camelCase - nie używany w Pythonie
TotalCount = 42   # PascalCase - zarezerwowane dla klas
```

### Funkcje
```python
# Dobrze
def calculate_total():
    pass

def get_user_name():
    pass

def is_valid_email(email):
    pass

# Źle
def CalculateTotal():  # PascalCase
    pass

def getUserName():  # camelCase
    pass
```

---

## Nazwy klas

**Konwencja:** `PascalCase` lub `CapWords` (każde słowo zaczyna się wielką literą, bez podkreślników)

```python
# Dobrze
class User:
    pass

class BankAccount:
    pass

class HTTPResponse:
    pass

class XMLParser:
    pass

# Źle
class user:  # snake_case
    pass

class bank_account:  # snake_case
    pass

class httpResponse:  # camelCase
    pass
```

### Wyjątki (Exceptions)
Wyjątki również używają `PascalCase` i często kończą się sufixem `Error`:

```python
class ValidationError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass

class FileNotFoundError(Exception):  # wbudowany wyjątek
    pass
```

---

## Nazwy stałych

**Konwencja:** `UPPER_CASE_WITH_UNDERSCORES` (wielkie litery, słowa oddzielone podkreślnikami)

```python
# Dobrze
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159
DATABASE_URL = "postgresql://localhost/db"
API_KEY = "secret_key_123"

# Źle
max_connections = 100  # wygląda jak zmienna
MaxConnections = 100   # wygląda jak klasa
```

---

## Nazwy modułów i pakietów

**Konwencja:** `lowercase` lub `lower_case_with_underscores` (małe litery, krótkie nazwy)

```python
# Dobrze
import math
import datetime
import my_module
import user_authentication

# Źle
import MyModule  # PascalCase
import My_Module  # mieszane style
```

### Struktura projektu
```
my_project/
├── __init__.py
├── user_auth.py       # dobrze
├── database.py        # dobrze
├── utils.py          # dobrze
└── UserManagement.py  # źle - PascalCase
```

---

## Prywatne i chronione elementy

### Chronione (protected) - pojedyncze podkreślenie

**Konwencja:** `_single_leading_underscore`

Wskazuje, że element jest do użytku wewnętrznego (konwencja, nie wymuszana przez interpreter).

```python
class User:
    def __init__(self):
        self._internal_value = 42  # chroniona zmienna

    def _helper_method(self):  # chroniona metoda
        pass
```

### Prywatne (private) - podwójne podkreślenie

**Konwencja:** `__double_leading_underscore`

Powoduje name mangling (zmianę nazwy przez interpreter).

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # prywatna zmienna

    def __calculate_interest(self):  # prywatna metoda
        pass
```

### Specjalne metody (magic methods)

**Konwencja:** `__double_leading_and_trailing_underscore__`

```python
class MyClass:
    def __init__(self):  # konstruktor
        pass

    def __str__(self):  # reprezentacja stringowa
        return "MyClass instance"

    def __len__(self):  # długość
        return 0
```

---

## Unikanie kolizji nazw

Jeśli nazwa koliduje ze słowem kluczowym Pythona, dodaj pojedyncze podkreślenie na końcu:

```python
# Dobrze
class_ = "Mathematics"  # unikamy słowa kluczowego 'class'
type_ = "integer"       # unikamy słowa kluczowego 'type'
id_ = 12345            # unikamy funkcji wbudowanej 'id'

# Źle
class = "Mathematics"  # błąd składni
type = "integer"       # zasłania wbudowaną funkcję
```

---

## Przykłady

### Kompletny przykład klasy

```python
# Stałe modułu
MAX_USERS = 1000
DEFAULT_ROLE = "guest"

class UserManager:
    """Klasa do zarządzania użytkownikami."""

    # Zmienna klasowa (publiczna)
    total_users = 0

    def __init__(self, username, email):
        """Konstruktor klasy."""
        # Zmienne instancji (publiczne)
        self.username = username
        self.email = email

        # Chroniona zmienna instancji
        self._created_at = datetime.now()

        # Prywatna zmienna instancji
        self.__password_hash = None

        UserManager.total_users += 1

    def get_user_info(self):
        """Publiczna metoda zwracająca informacje o użytkowniku."""
        return f"{self.username} ({self.email})"

    def _validate_email(self):
        """Chroniona metoda pomocnicza."""
        return "@" in self.email

    def __hash_password(self, password):
        """Prywatna metoda do hashowania hasła."""
        # implementacja
        pass

    @staticmethod
    def is_valid_username(username):
        """Statyczna metoda walidująca nazwę użytkownika."""
        return len(username) >= 3

    @classmethod
    def create_guest_user(cls):
        """Metoda klasowa tworząca użytkownika gościa."""
        return cls("guest", "guest@example.com")
```

### Przykład z funkcjami

```python
# Stałe
MIN_PASSWORD_LENGTH = 8
ALLOWED_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com"]

def validate_user_credentials(username, password):
    """Waliduje dane logowania użytkownika."""
    if not is_valid_username(username):
        return False
    if not is_valid_password(password):
        return False
    return True

def is_valid_username(username):
    """Sprawdza poprawność nazwy użytkownika."""
    return len(username) >= 3 and username.isalnum()

def is_valid_password(password):
    """Sprawdza poprawność hasła."""
    return len(password) >= MIN_PASSWORD_LENGTH

def _internal_helper_function():
    """Funkcja pomocnicza do użytku wewnętrznego modułu."""
    pass
```

---

## Podsumowanie

| Typ | Konwencja | Przykład |
|-----|-----------|----------|
| Zmienna | `snake_case` | `user_name`, `total_count` |
| Funkcja | `snake_case` | `calculate_total()`, `get_data()` |
| Klasa | `PascalCase` | `UserManager`, `BankAccount` |
| Stała | `UPPER_CASE` | `MAX_VALUE`, `API_KEY` |
| Moduł/Pakiet | `lowercase` | `mymodule`, `user_auth` |
| Chronione | `_leading_underscore` | `_internal_value` |
| Prywatne | `__double_leading` | `__private_method` |
| Magic methods | `__dunder__` | `__init__`, `__str__` |

---

## Dodatkowe zasady

1. **Importy** - grupuj w kolejności:
   - Biblioteka standardowa
   - Biblioteki zewnętrzne
   - Moduły lokalne

2. **Długość linii** - maksymalnie 79 znaków (dla kodu), 72 dla komentarzy

3. **Wcięcia** - 4 spacje (nie tabulatory)

4. **Odstępy**:
   - Dwa puste wiersze między definicjami klas najwyższego poziomu
   - Jedna pusta linia między metodami w klasie

5. **Komentarze i docstringi**:
   - Docstringi dla wszystkich modułów, klas i funkcji publicznych
   - Format: `"""Potrójne cudzysłowy."""`

---

## Źródła

- [PEP 8 -- Style Guide for Python Code](https://pep8.org/)
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
