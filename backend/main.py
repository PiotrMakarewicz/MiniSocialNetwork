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


@app.route("/password_check/<username>/<password_hash>")
def get_user_id_if_password_hash_is_correct(username, password_hash):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "MATCH (u:User) "
        "WHERE u.name = \"{}\" "
        "and u.password_hash = \"{}\" "
        "RETURN id(u)"
        .format(username, password_hash)
    )))
    return json.dumps({'id': results[0][0] if len(results) > 0 else None})



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
        #'name': user['name'],
        #'creation_datetime': user['creation_datetime'],
        #'avatar': user['avatar'],
        #'description': user['description'],
        #'role': user['role'],
        'id': user['id'],
    })
    return json.dumps({"users": users})


@app.route("/<userID>")
def get_user(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)"
        "WHERE id(u) = $userID "
        "RETURN u.name as name, "
        "u.creation_datetime as creation_datetime, "
        "u.avatar as avatar, "
        "u.description as description, "
        "u.role as role, "
        "id(u) as id"
        "", {'userID': int(userID)})))
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

@app.route("/post/<postID>")
def get_post(postID):
    db = get_db()
    results  = db.read_transaction(lambda tx: list(tx.run(
        "Match (c:User)-[a:AUTHOR_OF]->(p:Post) "
        "where id(p) = $postID "
        "optional match (:User)-[l:LIKES]->(p) "
        "optional match (:User)-[d:DISLIKES]->(p) "
        "RETURN p.creation_datetime as creation_datetime, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_datetime as update_datetime, "
        "id(c) as authorID, "
        "id(p) as id, "
        "count(l) - count(d) as rating"
        "", {'postID': int(postID)})))
    posts = []
    for post in results:
        posts.append({
            'author': post['authorID'],
            'creation_datetime': post['creation_datetime'],
            'photo_address': post['photo_address'],
            'content': post['content'],
            'update_datetime': post['update_datetime'],
            'rating': post['rating'],
            'id': post['id'],
            })
    return json.dumps({"posts": posts})

@app.route("/post/<postID>/responses")
def get_responses(postID):
    db = get_db()
    results  = db.read_transaction(lambda tx: list(tx.run(
        "Match (w:Post)-[r:REFERS_TO]->(p:Post) "
        "where id(p) = $postID "
        "RETURN id(w) as id"
        "", {'postID': int(postID)})))
    posts = []
    for post in results:
        posts.append({
            'id': post['id'],
            })
    return json.dumps({"posts": posts})

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
        "id(b) as id "
        "", {'userID': int(userID)})))
    observed = []
    for user in results:
        observed.append({
        #'name': user['name'],
        #'creation_datetime': user['creation_datetime'],
        #'avatar': user['avatar'],
        #'description': user['description'],
        #'role': user['role'],
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
        "id(b) as id "
        "", {'userID': int(userID)})))
    observing = []
    for user in results:
        observing.append({
        #'name': user['name'],
        #'creation_datetime': user['creation_datetime'],
        #'avatar': user['avatar'],
        #'description': user['description'],
        #'role': user['role'],
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
        "id(p) as id "
        "ORDER BY creation_datetime DESC"
        "", {'userID': int(userID)})))
    posts = []
    for post in results:
        posts.append({
        #'author': userID,
        #'creation_datetime': post['creation_datetime'],
        #'photo_address': post['photo_address'],
        #'content': post['content'],
        #'update_datetime': post['update_datetime'],
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
        "id(p) as id "
        "ORDER BY creation_datetime DESC"
        "", {'userID': int(userID)})))
    posts = []
    for post in results:
        posts.append({
        #'author': post['author'],
        #'creation_datetime': post['creation_datetime'],
        #'photo_address': post['photo_address'],
        #'content': post['content'],
        #'update_datetime': post['update_datetime'],
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
        "id(p) as id "
        "ORDER BY creation_datetime DESC"
        "", {'userID': int(userID)})))
    posts = []
    for post in results:
        posts.append({
        #'author': post['author'],
        #'creation_datetime': post['creation_datetime'],
        #'photo_address': post['photo_address'],
        #'content': post['content'],
        #'update_datetime': post['update_datetime'],
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
        "id(p) as id "
        "ORDER BY creation_datetime DESC"
        "", {'userID': int(userID)})))
    posts = []
    for post in results:
        posts.append({
        #'author': post['author'],
        #'creation_datetime': post['creation_datetime'],
        #'photo_address': post['photo_address'],
        #'content': post['content'],
        #'update_datetime': post['update_datetime'],
        'id': post['id'],
        })
    return json.dumps({"posts": posts})

@app.route("/<userID>/like/<postID>")
def like_post(userID, postID):
    db = get_db()
    results = db.write_transaction(lambda tx: list(tx.run(
        "Match (u:User) "
        "Match (p:Post) "
        "where id(u) = $userID AND id(p) = $postID "
        "AND NOT EXISTS { MATCH (u)-[:AUTHOR_OF]->(p)} "
        "optional match (u)-[d:DISLIKES]->(p) "
        "MERGE (u)-[l:LIKES]->(p) "
        "ON CREATE SET l.datetime = datetime() "
        "DELETE d "
        "RETURN id(l) as id"
        "", {'userID': int(userID), 'postID': int(postID)})))
    likes = []
    for like in results:
        likes.append({
            'id': like['id'],
        })
    return json.dumps({"likes": likes})

@app.route("/<userID>/dislike/<postID>")
def dislike_post(userID, postID):
    db = get_db()
    results = db.write_transaction(lambda tx: list(tx.run(
        "Match (u:User) "
        "Match (p:Post) "
        "where id(u) = $userID AND id(p) = $postID "
        "AND NOT EXISTS { MATCH (u)-[:AUTHOR_OF]->(p)} "
        "OPTIONAL MATCH (u)-[l:LIKES]->(p) "
        "MERGE (u)-[d:DISLIKES]->(p) "
        "ON CREATE SET d.datetime = datetime() "
        "DELETE l "
        "RETURN id(d) as id"
        "", {'userID': int(userID), 'postID': int(postID)})))
    dislikes = []
    for dislike in results:
        dislikes.append({
            'id': dislike['id'],
        })
    return json.dumps({"dislikes": dislikes})

@app.route("/<userID>/observe/<observedID>")
def observe_user(userID, observedID):
    db = get_db()
    results = db.write_transaction(lambda tx: list(tx.run(
        "Match (u:User) "
        "Match (o:User) "
        "where id(u) = $userID AND id(o) = $observedID "
        "AND NOT id(u) = $observedID "
        "MERGE (u)-[b:OBSERVES]->(o) "
        "ON CREATE SET b.since = datetime() "
        "RETURN id(b) as id"
        "", {'userID': int(userID), 'observedID': int(observedID)})))
    observations = []
    for obs in results:
        observations.append({
            'id': obs['id']
        })
    return json.dumps({"observations": observations})

@app.route("/<userID>/unobserve/<observedID>")
def unobserve_user(userID, observedID):
    db = get_db()
    results = db.write_transaction(lambda tx: list(tx.run(
        "Match (u:User) "
        "Match (o:User) "
        "where id(u) = $userID AND id(o) = $observedID "
        "MATCH (u)-[b:OBSERVES]->(o) "
        "WITH b, id(b) as identity "
        "DELETE b "
        "RETURN identity as id"
        "", {'userID': int(userID), 'observedID': int(observedID)})))
    observations = []
    for obs in results:
        observations.append({
            'id': obs['id']
        })
    return json.dumps({"observations": observations})

@app.route("/tag/<tagName>")
def get_posts_from_tag(tagName):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (p:Post)-[t:TAGGED_AS]->(z:Tag) "
        "WHERE z.name = $tagName "
        "MATCH (u:User)-[a:AUTHOR_OF]->(p) "
        "RETURN p.creation_datetime as creation_datetime, "
        "id(u) as author, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_datetime as update_datetime, "
        "id(p) as id "
        "ORDER BY creation_datetime DESC"
        "", {'tagName': tagName})))
    posts = []
    for post in results:
        posts.append({
        #'author': post['author'],
        #'creation_datetime': post['creation_datetime'],
        #'photo_address': post['photo_address'],
        #'content': post['content'],
        #'update_datetime': post['update_datetime'],
        'id': post['id'],
        })
    return json.dumps({"posts": posts})

@app.route("/post/<postID>/tags")
def get_post_tags(postID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (p:Post)-[t:TAGGED_AS]->(z:Tag) "
        "WHERE id(p) = $postID "
        "MATCH (u:User)-[a:AUTHOR_OF]->(p) "
        "RETURN z.name as name"
        "", {'postID': int(postID)})))
    tags = []
    for tag in results:
        tags.append(tag['name'])
    return json.dumps({"tags": tags})

@app.route("/<userID>/recommended-users")
def recommended_users(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[o:OBSERVES]->(c:User) "
        "WHERE id(u) = $userID "
        "MATCH (c)-[r:OBSERVES]->(b:User) "
        "WHERE NOT EXISTS { MATCH (u)-[:OBSERVES]->(b)} "
        "RETURN DISTINCT b.name as name, "
        "b.creation_datetime as creation_datetime, "
        "b.avatar as avatar, "
        "b.description as description, "
        "b.role as role, "
        "id(b) as id"
        "", {'userID': int(userID)})))
    observed = []
    for user in results:
        observed.append({
        #'name': user['name'],
        #'creation_datetime': user['creation_datetime'],
        #'avatar': user['avatar'],
        #'description': user['description'],
        #'role': user['role'],
        'id': user['id'],
    })
    return json.dumps({"observed": observed})

@app.route("/ranking")
def get_user_ranking():
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "CALL gds.pageRank.stream( "
        "{nodeQuery: 'MATCH (u:User) RETURN id(u) AS id', "
        "relationshipQuery: 'MATCH (b:User)-[:OBSERVES]->(c:User) "
        "RETURN id(b) AS source, id(c) AS target'}"
        ") "
        "YIELD nodeId, score "
        "RETURN gds.util.asNode(nodeId).name as name, score, "
        "nodeId as id "
        "ORDER BY score DESC, name ASC"
        "")))
    ranking = []
    for user in results:
        ranking.append({
        #'name': user['name'],
        'id': user['id'],
        'score': user['score']
    })
    return json.dumps({"ranking": ranking})

@app.route("/<userID>/recommended-posts")
def get_recommended_posts(userID):
    db = get_db()
    results = db.read_transaction(lambda tx: list(tx.run(
        "Match (u:User)-[o:OBSERVES]->(b:User) "
        "Match (b)-[a:LIKES]->(p:Post) "
        "Match (c:User)-[d:AUTHOR_OF]->(p) "
        "where id(u) = $userID "
        "AND duration.inDays(datetime(p.creation_datetime), datetime()).days < 8 "
        "RETURN DISTINCT p.creation_datetime as creation_datetime, "
        "p.photo_address as photo_address, "
        "p.content as content, "
        "p.update_datetime as update_datetime, "
        "id(c) as author, "
        "id(p) as id "
        "ORDER BY creation_datetime DESC"
        "", {'userID': int(userID)})))
    posts = []
    for post in results:
        posts.append({
        #'author': post['author'],
        #'creation_datetime': post['creation_datetime'],
        #'photo_address': post['photo_address'],
        #'content': post['content'],
        #'update_datetime': post['update_datetime'],
        'id': post['id'],
        })
    return json.dumps({"posts": posts})


if __name__ == '__main__':
    app.run(debug=True)
