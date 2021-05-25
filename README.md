# MiniSocialNetwork

Portal społecznościowy będący okrojonym klonem Twittera: użytkownicy posiadają możliwość tworzenia wpisów, obserwowania innych użytkowników, oceniania wpisów.
Informacje dot. użytkowników, postów, obserwowania przechowywane w bazie Neo4j. Frontend napisany w Angularze. Backend w Pythonie i Flasku.

## Członkowie grupy

- Gabriel Kępka
- Piotr Makarewicz

## Model bazy danych

### Węzły

- User - użytkownik
- Post - wpis
- Tag - hasztag

### Relacje

- AUTHOR_OF - określa autorstwo wpisu
- OBSERVES - użytkownik obserwuje innego użytkownika
- LIKES - użytkownik lubi wpis
- DISLIKES - użytkownik nie lubi wpisu
- REFERS_TO - wpis odnosi się do innego wpisu
- TAGGED_AS - wpis został oznaczony tagiem

### Atrybuty węzłów

#### User

- name
- creation_datetime
- avatar
- description
- role
- password_hash

#### Post

- creation_datetime
- update_datetime
- content
- photo_adress

#### Tag

- name

### Atrybuty relacji

#### OBSERVES
 - since_datetime

#### LIKES
 - datetime

#### DISLIKES
 - datetime

### Zapytania do bazy (realizowane przez backend; wstępny plan)

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
12. zwrócenie wpisów polubionych przez obserwowanych
13. pokazanie polecanych postów
14. pokazanie polecanych znajomych
15. zwrócenie rankingu popularności użytkowników (np. przez PageRank)

### Wprowadzenie przykładowych danych do bazy

```cypher
CREATE (n:User {name: 'Andy', creation_date: '2021-01-10', avatar: 'https://via.placeholder.com/300/09f/fff.png', description: 'the first user!',role: 'none', password_hash: 'none'})
CREATE (n:User {name: 'Johnny', creation_date: '2021-03-12', avatar: 'https://via.placeholder.com/300/09f/fff.png', description: 'the first user!',role: 'none', password_hash: 'none'})
CREATE (n:User {name: 'Robert', creation_date: '2020-12-12', avatar: 'https://via.placeholder.com/300/09f/fff.png', description: 'the first user!',role: 'none', password_hash: 'none'})
```
