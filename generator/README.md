# API

## Przed uruchomieniem

Upewnij się, że twoim katalogiem roboczym jest generator

Stwórz i uruchom wirtualne środowisko dla interpretera Pythona

```bash
virtualenv venv
source venv/bin/activate
```

Zainstaluj wymagane biblioteki

```bash
pip install -r requirements
```

W katalogu generator na tym samym poziomie, co generator.py stwórz plik o nazwie .env z definicjami zmiennych PORT, NEO4J_URL, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE. Przykładowo:

```dotenv
PORT = '8080'
NEO4J_URL = 'bolt://localhost:7687'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'password'
NEO4J_DATABASE = 'neo4j'
```
