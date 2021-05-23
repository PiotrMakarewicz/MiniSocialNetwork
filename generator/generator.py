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
    """
    Returns a dictionary representing a User node that can be later inserted into the database.
    @return: a dictionary with attributes equivalent to the ones of a User node in the database.
    """
    global fake

    user = dict()

    user['name'] = fake.name()
    user['creation_date'] = fake.date_between('-5y')
    user['description'] = fake.paragraph()
    user['role'] = random.choices(['admin', 'none'], [1, 100])[0]
    user['password_hash'] = uuid.uuid4().hex
    user['avatar'] = 'https://via.placeholder.com/300/09f/fff.png'

    return user


def create_fake_post(first_possible_creation_date) -> dict:
    """
    Returns a dictionary representing a Post node that can be later inserted into the database.
    @param first_possible_creation_date: this is the first possible date of this post. It may be used to create a post for a user registered at a certain day
    @return: a dictionary with attributes equivalent to the ones of a Post node in the database.
    """
    global fake

    post = dict()

    #post['creation_date'] = fake.date_between(first_possible_creation_date)
    post['creation_date'] = fake.date_between(first_possible_creation_date)
    
    post['update_date'] = random.choice([None, fake.date_between_dates(post['creation_date'], None)])
    post['content'] = fake.paragraph() 
    post['photo_address'] = random.choices(['', 'https://via.placeholder.com/500/02f/a0f.png'], [10, 3])[0]

    return post


def add_user(user: dict) -> int:
    """
    Adds a new user and returns their ID
    @param user: a dictionary with attributes equivalent to the ones of a User node in the database
    @return: a single number, the ID of a newly added user
    """
    result =  db.run("CREATE (n:User {{name: '{}', creation_date: '{}', avatar: '{}', description: '{}', role: '{}', password_hash: '{}'}}) RETURN id(n)"
        .format(user['name'], user['creation_date'], user['avatar'], user['description'], user['role'], user['password_hash']))
    return result.data()[0]['id(n)']


def add_post(author_id: int, post: dict) -> int:
    """
    Adds a new post, creates the AUTHOR_OF relationship between author node and post node and returns the ID of a new post
    @param author_id: the ID of an author User node that already exists in the database
    @param post: a dictionary with attributes equivalent to the ones of a Post node in the database
    @return: a single number, the ID of a newly added post
    """
    result = db.run("CREATE (n:Post {{creation_date: '{}', update_date: '{}', content: '{}', photo_address: '{}'}}) RETURN id(n)"
        .format(post['creation_date'], post['update_date'], post['content'], post['photo_address']))
    post_id = result.data()[0]['id(n)']
    result = db.run("MATCH (u:User), (p:Post) WHERE id(u) = {} AND id(p) = {} CREATE (u)-[r:AUTHOR_OF]->(p)"
        .format(author_id, post_id))
    return post_id


def add_observes_between(observer_id: int, observed_id: int) -> None:
    """
    Creates the OBSERVES relationship between User nodes represented by observer_id and observed_id
    @param observer_id: ID of an observer User node already existing in the database
    @param observed_id: ID of an observed User node already existing in the database
    """
    db.run("MATCH (u:User), (v:User) WHERE id(u) = {} AND id(v) = {} CREATE (u)-[r:OBSERVES]->(v)"
        .format(observer_id, observed_id))


db_params = {
    "users": 30,
    "min user posts": 2,
    "max user posts": 6,
    "min observed by user": 0,
    "max observed by user": 6,
    "min liked posts per user": 0,
    "max liked posts per user": 6,
    "min disliked posts per user": 0,
    "max disliked posts per user": 6,
    "tags": 10,
    "posts with photos freq": 0.3,
    "min tags per post": 0,
    "max tags per post": 5,
    "referring post chance": 0.5
}


def generate_database():

    # All entries in a form: "id: node-representing-dictionary"
    users = dict()
    posts = dict()
    tags = dict()

    ### Add User nodes

    for _ in range(db_params['users']):
        user = create_fake_user()
        user_id = add_user(user)
        users[user_id] = user

    ### Add OBSERVES relationships
    
    for user_id, user in users.items():
        other_user_ids = list(set(users.keys()).difference({user_id}))
        num_observed = random.randint(db_params['min observed by user'], db_params['max observed by user'])
        observed_ids = random.sample(other_user_ids, k=num_observed)
        for observed_id in observed_ids:
            add_observes_between(user_id, observed_id)

    ### Add Post nodes and AUTHOR_OF relationships
    
    for user_id, user in users.items():
        num_posts = random.randint(db_params['min user posts'], db_params['max user posts'])
        
        for _ in range(num_posts):
            add_post(user_id, create_fake_post(user['creation_date']))





generate_database()

db.close()