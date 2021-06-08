import os
import logging
import json

from flask import Flask, g, Response, request
from flask_cors import CORS
from neo4j import GraphDatabase, basic_auth
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()
url = os.getenv("NEO4J_URL")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")
database = os.getenv("NEO4J_DATABASE")
port = os.getenv("PORT", 8080)

driver = GraphDatabase.driver(url, auth=basic_auth(username, password))


def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session(database=database)
    return g.neo4j_db
    

@app.route("/")
def get_all_users():
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "MATCH (u:User)"
        "RETURN u.name as name, "
        "u.creation_datetime as creation_datetime, "
        "u.avatar as avatar, "
        "u.description as description, "
        "u.role as role, "
        "id(u) as id"
        "")))
    users = []
    for user in results:
        users.append({
        'name': user['name'],
        'creation_datetime': user['creation_datetime'],
        'avatar': user['avatar'],
        'description': user['description'],
        'role': user['role'],
        'id': user['id'],
    })
    return json.dumps({"users": users})


@app.route("/<userID>")
def get_user(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User {id: $userID})"
        "RETURN u.name as name, "
        "u.creation_datetime as creation_datetime, "
        "u.avatar as avatar, "
        "u.description as description, "
        "u.role as role, "
        "id(u) as id"
        "", {'userID': userID})))
    users = []
    for result in results:
        users.append({
            'name': result['name'],
            'creation_datetime': result['creation_datetime'],
            'avatar': result['avatar'],
            'description': result['description'],
            'role': result['role'],
            'id': result['id'],
        })
    return json.dumps({"users": users})


@app.route("/<userID>/observed")
def get_observed_by_user(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[o:OBSERVES]->(b:User) "
        "WHERE id(u) = $userID "
        "RETURN b.name as name, "
        "b.creation_datetime as creation_datetime, "
        "b.avatar as avatar, "
        "b.description as description, "
        "b.role as role, "
        "id(b) as id"
        "", {'userID': userID})))
    observed = []
    for user in results:
        observed.append({
        'name': user['name'],
        'creation_datetime': user['creation_datetime'],
        'avatar': user['avatar'],
        'description': user['description'],
        'role': user['role'],
        'id': user['id'],
    })
    return json.dumps({"observed": observed})


@app.route("/<userID>/observing")
def get_observing_user(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)<-[o:OBSERVES]-(b:User) "
        "WHERE id(u) = $userID "
        "RETURN b.name as name, "
        "b.creation_datetime as creation_datetime, "
        "b.avatar as avatar, "
        "b.description as description, "
        "b.role as role, "
        "id(b) as id"
        "", {'userID': userID})))
    observing = []
    for user in results:
        observing.append({
        'name': user['name'],
        'creation_datetime': user['creation_datetime'],
        'avatar': user['avatar'],
        'description': user['description'],
        'role': user['role'],
        'id': user['id'],
    })
    return json.dumps({"observing": observing})


@app.route("/<userID>/posts")
def get_posts_by_user(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[a:AUTHOR_OF]->(p:Post) "
        "WHERE id(u) = $userID "
        "RETURN p.creation_datetime as creation_datetime, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_datetime as update_datetime, "
        "id(p) as id"
        "", {'userID': userID})))
    posts = []
    for post in results:
        posts.append({
        'author': userID,
        'creation_datetime': post['creation_datetime'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_datetime': post['update_datetime'],
        'id': post['id'],
        })
    return json.dumps({"posts": posts})


@app.route("/<userID>/liked")
def get_liked_by_user(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[l:LIKES]->(p:Post) "
        "Match (c:User)-[a:AUTHOR_OF]->(p) "
        "where id(u) = $userID "
        "RETURN p.creation_datetime as creation_datetime, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_datetime as update_datetime, "
        "c.name as author, "
        "id(p) as id"
        "", {'userID': userID})))
    posts = []
    for post in results:
        posts.append({
        'author': post['author'],
        'creation_datetime': post['creation_datetime'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_datetime': post['update_datetime'],
        'id': post['id'],
        })
    return json.dumps({"posts": posts})


@app.route("/<userID>/disliked")
def get_disliked_by_user(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[l:DISLIKES]->(p:Post) "
        "Match (c:User)-[a:AUTHOR_OF]->(p) "
        "where id(u) = $userID "
        "RETURN p.creation_datetime as creation_datetime, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_datetime as update_datetime, "
        "c.name as author, "
        "id(p) as id"
        "", {'userID': userID})))
    posts = []
    for post in results:
        posts.append({
        'author': post['author'],
        'creation_datetime': post['creation_datetime'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_datetime': post['update_datetime'],
        'id': post['id'],
        })
    return json.dumps({"posts": posts})


@app.route("/<userID>/observed/posts")
def get_posts_by_observed(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[o:OBSERVES]->(b:User) "
        "Match (b)-[a:AUTHOR_OF]->(p:Post) "
        "where id(u) = $userID "
        "RETURN p.creation_datetime as creation_datetime, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_datetime as update_datetime, "
        "b.name as author"
        "id(p) as id"
        "", {'userID': userID})))
    posts = []
    for post in results:
        posts.append({
        'author': post['author'],
        'creation_datetime': post['creation_datetime'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_datetime': post['update_datetime'],
        'id': post['id'],
        })
    return json.dumps({"posts": posts})

# @app.route("/<userID>/like/<postID>")
# def like_post(userID, postID):
#     db = get_db()
#     results = db.read_transaction(lambda tx: list(tx.run(
#         "Match (u:User) "
#         "Match (p:Post) "
#         "where id(u) = $userID AND id(p) = $postID "
#         "CREATE (u)-[l:LIKES {datetime: datetime()}]->(p)"
#         "", {'userID': userID})))


if __name__ == '__main__':
    app.run(debug=True)
