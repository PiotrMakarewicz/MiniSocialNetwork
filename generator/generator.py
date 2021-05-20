from neo4j import GraphDatabase, basic_auth, Result
from dotenv import load_dotenv
from faker import Faker
import os
import random
import uuid


load_dotenv()
url = os.getenv("NEO4J_URL")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")
database = os.getenv("NEO4J_DATABASE")
port = os.getenv("PORT", 8080)

driver = GraphDatabase.driver(url, auth=basic_auth(username, password))
db = driver.session(database=database)

fake = Faker()


def create_fake_user() -> dict:
    """Returns a dictionary representing a User node that can be later inserted into the database."""
    global fake

    user = dict()

    user['name'] = fake.name()
    user['creation_date'] = fake.date_between('-5y')
    user['description'] = fake.paragraph()
    user['role'] = random.choices(['admin', 'none'], [1, 100])[0]
    user['password_hash'] = uuid.uuid4().hex
    user['avatar'] = 'https://via.placeholder.com/300/09f/fff.png'

    return user


def create_fake_post() -> dict:
    """Returns a dictionary representing a Post node that can be later inserted into the database. """
    global fake

    post = dict()

    post['creation_date'] = fake.date_between('-5y')
    post['update_date'] = fake.date_between_dates(post['creation_date'], None)
    post['content'] = fake.paragraph() 
    post['photo_address'] = random.choices(['', 'https://via.placeholder.com/500/02f/a0f.png'], [10, 3])[0]

    return post


def add_user(user: dict) -> Result:
    return db.run("CREATE (n:User {{name: '{}', creation_date: '{}', avatar: '{}', description: '{}', role: '{}', password_hash: '{}'}})"
        .format(user['name'], user['creation_date'], user['avatar'], user['description'], user['role'], user['password_hash']))


def add_post(post: dict) -> Result:
    return db.run("CREATE (n:Post {{creation_date: '{}', update_date: '{}', content: '{}', photo_address: '{}'}})"
        .format(post['creation_date'], post['update_date'], post['content'], post['photo_address']))


for _ in range(25):
    add_user(create_fake_user())

for _ in range(25):
    add_post(create_fake_post())

db.close()