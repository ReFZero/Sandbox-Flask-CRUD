# Sandbox Flask CRUD 
Podstawowa aplikacja wykorzystujaca framework Flask
## Info:
- Python 3.11
- Flask 3.1
### Biblioteki:
- SQLAlchemy
#### Zmiany w ostatnim commicie:
- Rozdzielono kod na moduły
#### Uruchomienie
Inicjalizacja środowiska
```
$ py -3 -m venv .venv
$ .venv\Scripts\activate
```
Do automatycznej instalacji bibliotek użyjemy PIP. Plik `requirements.txt` zawiera wszystkie niezbedne biblioteki.
```
$ pip install -r requirements.txt
```
Uruchomienie
```
$ flask --app main.py run --debug
```

Aby zaktualizować liste wymaganych bibliotek
```
$ pip freeze > requirements.txt
```

