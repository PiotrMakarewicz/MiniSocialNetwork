## Członkowie grupy:
- Gabriel Kępka
- Piotr Makarewicz

## Temat:

Portal społecznościowy będący okrojonym klonem Twittera: użytkownicy posiadają możliwość tworzenia wpisów, obserwowania innych użytkowników, oceniania wpisów.
Informacje dot. użytkowników, postów, obserwowania przechowywane w bazie Neo4j. Frontend napisany w Angularze. Backend w Pythonie i Flasku. 

## Model bazy danych:

### Węzły:
- User - użytkownik
- Post - wpis

### Relacje:
- AUTHOR_OF - określa autorstwo wpisu
- OBSERVES - użytkownik obserwuje innego użytkownika
- LIKES - użytkownik lubi wpis
- DISLIKES - użytkownik nie lubi wpisu
- REFERS_TO - wpis odnosi się do innego wpisu

## Atrybuty węzłów:

### User:
- name
- creation_date
- avatar
- description
- role
- password_hash

### Post:
- creation_date
- update_date
- content
- photo_adress
- tag


## Zapytania do bazy (realizowane przez backend; wstępny plan):
1. tworzenie użytkownika
2. dodawanie wpisu/komentarza
3. edycja wpisu
4. usuwanie wpisu
5. ocenianie wpisu
6. obserwowanie użytkownika
7. usunięcie z obserwowanych użytkownika
8. zmiana atrybutu użytkownika
9. zwrócenie wszystkich wpisów użytkownika
10. zwrócenie wpisów obserwowanych danego użytkownika
11. zwrócenie wpisów z określonego tagu

