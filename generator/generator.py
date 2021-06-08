from neo4j import GraphDatabase, basic_auth, Result
from dotenv import load_dotenv
from faker import Faker
from datetime import date
from datetime import datetime as dt

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
    user['creation_datetime'] = fake.date_time_between('-1y').strftime("%Y-%m-%dT%H:%M:%S")
    user['description'] = fake.paragraph()
    user['role'] = random.choices(['admin', 'none'], [1, 100])[0]
    user['password_hash'] = uuid.uuid4().hex
    user['avatar'] = 'https://via.placeholder.com/300/09f/fff.png'

    return user


def create_fake_post(first_possible_creation_datetime: dt, with_photo: bool) -> dict:
    """
    Returns a dictionary representing a Post node that can be later inserted into the database.
    @param first_possible_creation_datetime: this is the first possible date of this post. It may be used to create a post for a user registered at a certain day
    @param with_photo: if true, adds placeholder photo url as photo_address, if false makes photo_address an empty string
    @return: a dictionary with attributes equivalent to the ones of a Post node in the database.
    """
    global fake

    post = dict()

    post['creation_datetime'] = fake.date_time_between(dt.strptime(first_possible_creation_datetime, "%Y-%m-%dT%H:%M:%S")).strftime("%Y-%m-%dT%H:%M:%S")
    post['update_datetime'] = random.choice([None, fake.date_time_between_dates(dt.strptime(post['creation_datetime'], "%Y-%m-%dT%H:%M:%S"), None)])
    if post['update_datetime'] is not None:
        post['update_datetime'] = post['update_datetime'].strftime("%Y-%m-%dT%H:%M:%S")
    post['content'] = fake.paragraph() 
    post['photo_address'] = 'https://via.placeholder.com/500/02f/a0f.png' if with_photo else ''

    return post

def create_fake_tag() -> dict:
    """
    Returns a dictionary representing a Tag node that can be later inserted into the database.
    @return: a dictionary with attributes equivalent to the ones of a Tag node in the database.
    """
    global fake
    return {'name': fake.word()}



def add_user(user: dict) -> int:
    """
    Adds a new user and returns their ID
    @param user: a dictionary with attributes equivalent to the ones of a User node in the database
    @return: a single number, the ID of a newly added user
    """
    result =  db.run("CREATE (n:User {{name: '{}', creation_datetime: '{}', avatar: '{}', description: '{}', role: '{}', password_hash: '{}'}}) RETURN id(n)"
        .format(user['name'], user['creation_datetime'], user['avatar'], user['description'], user['role'], user['password_hash']))
    return result.data()[0]['id(n)']


def add_post(author_id: int, post: dict) -> int:
    """
    Adds a new post, creates the AUTHOR_OF relationship between author node and post node and returns the ID of a new post
    @param author_id: the ID of an author User node that already exists in the database
    @param post: a dictionary with attributes equivalent to the ones of a Post node in the database
    @return: a single number, the ID of a newly added post
    """
    result = db.run("CREATE (n:Post {{content: '{}', creation_datetime: '{}', update_datetime: '{}', photo_address: '{}'}}) RETURN id(n)"
        .format(post['content'], post['creation_datetime'], post['update_datetime'], post['photo_address']))
    post_id = result.data()[0]['id(n)']
    result = db.run("MATCH (u:User), (p:Post) WHERE id(u) = {} AND id(p) = {} CREATE (u)-[r:AUTHOR_OF]->(p)"
        .format(author_id, post_id))
    return post_id


def add_tag(tag: dict) -> int:
    """
    Adds a new tag to the database
    @param tag: a dictionary with attributes equivalent to the ones of a Tag node in the database.
    @return: a single number, the ID of a newly added tag
    """
    result = db.run("CREATE (t:Tag {{name: '{}'}}) RETURN id(t)".format(tag['name']))
    return result.data()[0]['id(t)']


def add_observes_between(observer_id: int, observed_id: int, since: dt) -> None:
    """
    Creates the OBSERVES relationship between User nodes represented by observer_id and observed_id
    @param observer_id: ID of an observer User node already existing in the database
    @param observed_id: ID of an observed User node already existing in the database
    """
    db.run("MATCH (u:User), (v:User) WHERE id(u) = {} AND id(v) = {} CREATE (u)-[r:OBSERVES {{since: '{}'}}]->(v)"
        .format(observer_id, observed_id, since))


def add_likes_between(user_id: int, post_id: int, datetime: dt) -> None:
    """
    Creates the LIKES relationship between the User node represented by user_id and the Post node represented by post_id
    @param user_id: ID of a User node already existing in the database
    @param post_id: ID of a Post node already exisiting in the database
    """
    db.run("MATCH (u:User), (p:Post) WHERE id(u) = {} AND id(p) = {} CREATE (u)-[r:LIKES {{datetime: '{}'}}]->(p)"
        .format(user_id, post_id, datetime))


def add_dislikes_between(user_id: int, post_id: int, datetime: dt) -> None:
    """
    Creates the DISLIKES relationship between the User node represented by user_id and the Post node represented by post_id
    @param user_id: ID of a User node already existing in the database
    @param post_id: ID of a Post node already existing in the database
    """
    db.run("MATCH (u:User), (p:Post) WHERE id(u) = {} AND id(p) = {} CREATE (u)-[r:DISLIKES {{datetime: '{}'}}]->(p)"
        .format(user_id, post_id, datetime))


def add_refers_to_between(referring_id: int, referred_id: int) -> None:
    """
    Creates the REFERS_TO relationship between the Posts node represented by referring_id and referred_id
    @param referring_id: ID of a Post node already existing in the database
    @param referred_id: ID of a Post node already existing in the database
    """   
    db.run("MATCH (p:Post), (q:Post) WHERE id(p) = {} AND id(q) = {} CREATE (p)-[r:REFERS_TO]->(q)"
        .format(referring_id, referred_id))

def add_tagged_as_between(post_id: int, tag_id: int) -> None:
    """
    Creates the TAGGED_AS relationship between a Post node and a Tag node
    @param post_id: ID of a Post node already existing in the database
    @param tag_id: ID of a Tag node already existing in the database
    """   
    db.run("MATCH (p:Post), (t:Tag) WHERE id(p) = {} AND id(t) = {} CREATE (p)-[r:TAGGED_AS]->(t)"
        .format(post_id, tag_id))


def add_user_for_testing():
    """
    Adds a user that can be later used to test the program
    # username: Userof Minisocialnetwork
    # password: password
    # password_hash: 5f4dcc3b5aa765d61d8327deb882cf99
    """
    global fake

    user = dict()

    user['name'] = "Userof Minisocialnetwork"
    user['creation_datetime'] = fake.date_time_between('-1y').strftime("%Y-%m-%dT%H:%M:%S")
    user['description'] = "A user that can be later used to test the program"
    user['role'] = random.choices(['admin', 'none'], [1, 100])[0]
    user['password_hash'] = "5f4dcc3b5aa765d61d8327deb882cf99"
    user['avatar'] = 'https://via.placeholder.com/300/09f/fff.png'

    add_user(user)



db_params = {
    "users": 200,
    "min user posts": 2,
    "max user posts": 10,
    "min observed by user": 0,
    "max observed by user": 10,
    "min liked posts per user": 0,
    "max liked posts per user": 10,
    "min disliked posts per user": 0,
    "max disliked posts per user": 5,
    "tags": 30,
    "posts with photos freq": 0.1,
    "min tags per post": 0,
    "max tags per post": 5,
    "referring post chance": 0.2
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
            observed = users[observed_id]
            datetime_begin = user['creation_datetime'] if user['creation_datetime'] > observed['creation_datetime'] else observed['creation_datetime']
            since = fake.date_time_between(dt.strptime(datetime_begin,"%Y-%m-%dT%H:%M:%S")).strftime("%Y-%m-%dT%H:%M:%S")
            add_observes_between(user_id, observed_id, since)

    ### Add Post nodes and AUTHOR_OF relationships
    
    for user_id, user in users.items():
        num_posts = random.randint(db_params['min user posts'], db_params['max user posts'])
        for _ in range(num_posts):
            post = create_fake_post(user['creation_datetime'], with_photo=(random.uniform(0, 1) < db_params['posts with photos freq']))
            post_id = add_post(user_id, post)
            posts[post_id] = post
    
    ### Add LIKES and DISLIKES relationships

    for user_id, user in users.items():
        num_liked_posts = random.randint(db_params['min liked posts per user'], db_params['max liked posts per user'])
        num_disliked_posts = random.randint(db_params['min disliked posts per user'], db_params['max disliked posts per user'])
        liked_posts_ids = random.sample(posts.keys(), k=num_liked_posts)
        disliked_posts_ids = random.sample(set(posts.keys()).difference(set(liked_posts_ids)), k=num_disliked_posts)
        for post_id in liked_posts_ids:
            post = posts[post_id]
            datetime_begin = post['creation_datetime'] if post['creation_datetime'] > user['creation_datetime'] else user['creation_datetime']
            datetime = fake.date_time_between(dt.strptime(datetime_begin, "%Y-%m-%dT%H:%M:%S")).strftime("%Y-%m-%dT%H:%M:%S")
            add_likes_between(user_id, post_id, datetime)
        for post_id in disliked_posts_ids:
            post = posts[post_id]
            datetime_begin = post['creation_datetime'] if post['creation_datetime'] > user['creation_datetime'] else user['creation_datetime']
            datetime = fake.date_time_between(dt.strptime(datetime_begin, "%Y-%m-%dT%H:%M:%S")).strftime("%Y-%m-%dT%H:%M:%S")
            post = posts[post_id]
            add_dislikes_between(user_id, post_id, datetime)

    ### Add REFERS_TO relationships

    def get_random_post_created_before(datetime: datetime):
        nonlocal posts

        for _ in range(25):
            post_id, post = random.choice(list(posts.items()))
            if post['creation_datetime'] < datetime:
                return post_id
        
        return None


    for referring_id, referring_post in posts.items():
        if random.uniform(0, 1) < db_params['referring post chance']:
            while True:
                referred_id = get_random_post_created_before(referring_post['creation_datetime'])
                if referred_id != referring_id:
                    break
            if referred_id is not None:
                add_refers_to_between(referring_id, referred_id)
    
    ### Add Tag nodes

    for _ in range(db_params['tags']):
        tag = create_fake_tag()
        tag_id = add_tag(tag)
        tags[tag_id] = tag 
    
    ### Add TAGGED_AS relationships
    
    for post_id, post in posts.items():
        num_tags = random.randint(db_params["min tags per post"], db_params["max tags per post"])
        tag_ids = random.sample(tags.keys(), k=num_tags)
        for tag_id in tag_ids:
            add_tagged_as_between(post_id, tag_id)
    
    add_user_for_testing()


try:
    generate_database()
finally:
    db.close()
