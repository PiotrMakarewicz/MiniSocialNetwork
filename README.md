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

- (User) - AUTHOR_OF -> (Post) - określa autorstwo wpisu
- (User) - OBSERVES -> (User) - użytkownik obserwuje innego użytkownika
- (User) - LIKES -> (Post) - użytkownik lubi wpis
- (User) - DISLIKES -> (Post) - użytkownik nie lubi wpisu
- (Post) - REFERS_TO -> (Post) - wpis odnosi się do innego wpisu
- (Post) - TAGGED_AS -> (Tag) - wpis został oznaczony tagiem

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

#### (User) - OBSERVES -> (User) 
 - since

#### (User) - LIKES -> (Post) 
 - datetime

#### (User) - DISLIKES -> (Post)
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
