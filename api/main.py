import os
import logging
import json

from flask import Flask, g, Response, request
from neo4j import GraphDatabase, basic_auth
from dotenv import load_dotenv

app = Flask(__name__)

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
        "u.creation_date as creation_date, "
        "u.avatar as avatar, "
        "u.description as description, "
        "u.role as role, "
        "u.password_hash as password_hash"
        "")))
    users = []
    for user in results:
        users.append({
        'name': user['name'],
        'creation_date': user['creation_date'],
        'avatar': user['avatar'],
        'description': user['description'],
        'role': user['role'],
        'password_hash': user['password_hash']
    })
    return Response(json.dumps({"users": users}), mimetype="application/json")


@app.route("/<username>/observed")
def get_observed_by_user(username):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[o:OBSERVES]->(b:User) "
        "WHERE u.name = $username "
        "RETURN b.name as name, "
        "b.creation_date as creation_date, "
        "b.avatar as avatar, "
        "b.description as description, "
        "b.role as role, "
        "b.password_hash as password_hash"
        "", {'username': username})))
    observed = []
    for user in results:
        observed.append({
        'name': user['name'],
        'creation_date': user['creation_date'],
        'avatar': user['avatar'],
        'description': user['description'],
        'role': user['role'],
        'password_hash': user['password_hash']
    })
    return Response(json.dumps({"observed": observed}), mimetype="application/json")


@app.route("/<username>/observing")
def get_observing_user(username):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)<-[o:OBSERVES]-(b:User) "
        "WHERE u.name = $username "
        "RETURN b.name as name, "
        "b.creation_date as creation_date, "
        "b.avatar as avatar, "
        "b.description as description, "
        "b.role as role, "
        "b.password_hash as password_hash"
        "", {'username': username})))
    observing = []
    for user in results:
        observing.append({
        'name': user['name'],
        'creation_date': user['creation_date'],
        'avatar': user['avatar'],
        'description': user['description'],
        'role': user['role'],
        'password_hash': user['password_hash']
    })
    return Response(json.dumps({"observing": observing}), mimetype="application/json")


@app.route("/<username>/posts")
def get_posts_by_user(username):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[a:AUTHOR_OF]->(p:Post) "
        "WHERE u.name = $username "
        "RETURN p.creation_date as creation_date, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_date as update_date"
        "", {'username': username})))
    posts = []
    for post in results:
        posts.append({
        'author': username,
        'creation_date': post['creation_date'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_date': post['update_date']
        })
    return Response(json.dumps({"posts": posts}), mimetype="application/json")


@app.route("/<username>/liked")
def get_liked_by_user(username):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[l:LIKES]->(p:Post) "
        "Match (c:User)-[a:AUTHOR_OF]->(p) "
        "where u.name = $username "
        "RETURN p.creation_date as creation_date, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_date as update_date, "
        "c.name as author"
        "", {'username': username})))
    posts = []
    for post in results:
        posts.append({
        'author': post['author'],
        'creation_date': post['creation_date'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_date': post['update_date']
        })
    return Response(json.dumps({"posts": posts}), mimetype="application/json")


@app.route("/<username>/disliked")
def get_disliked_by_user(username):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[l:DISLIKES]->(p:Post) "
        "Match (c:User)-[a:AUTHOR_OF]->(p) "
        "where u.name = $username "
        "RETURN p.creation_date as creation_date, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_date as update_date, "
        "c.name as author"
        "", {'username': username})))
    posts = []
    for post in results:
        posts.append({
        'author': post['author'],
        'creation_date': post['creation_date'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_date': post['update_date']
        })
    return Response(json.dumps({"posts": posts}), mimetype="application/json")


@app.route("/<username>/observed/posts")
def get_posts_by_observed(username):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[o:OBSERVES]->(b:User) "
        "Match (b)-[a:AUTHOR_OF]->(p:Post) "
        "where u.name = $username "
        "RETURN p.creation_date as creation_date, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_date as update_date, "
        "b.name as author"
        "", {'username': username})))
    posts = []
    for post in results:
        posts.append({
        'author': post['author'],
        'creation_date': post['creation_date'],
        'photo_address': post['photo_address'],
        'content': post['content'],
        'update_date': post['update_date']
        })
    return Response(json.dumps({"posts": posts}), mimetype="application/json")


if __name__ == '__main__':
    app.run(debug=True)
