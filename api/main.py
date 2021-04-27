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


if __name__ == '__main__':
    app.run(debug=True)