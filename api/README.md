# API

## Przed uruchomieniem

1. Upewnij się, że twoim katalogiem roboczym jest api

2. Stwórz i uruchom wirtualne środowisko dla interpretera Pythona
`virtualenv minisocial network
source minisocialnetwork/bin/activate`

3. Zainstaluj wymagane biblioteki
`pip install -r requirements`

4. W katalogu api stwórz plik o nazwie .env z definicjami zmiennych PORT, NEO4J_URL, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE. Przykładowo:
`PORT=8080
NEO4J_URL=neo4j+s://demo.neo4jlabs.com
NEO4J_USER=user
NEO4J_PASSWORD=password
NEO4J_DATABASE=minisocialnetwork`
