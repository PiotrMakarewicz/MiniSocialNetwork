from neo4j import GraphDatabase, basic_auth
from dotenv import load_dotenv
from faker import Faker
import os

load_dotenv()
url = os.getenv("NEO4J_URL")
username = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PASSWORD")
database = os.getenv("NEO4J_DATABASE")
port = os.getenv("PORT", 8080)

driver = GraphDatabase.driver(url, auth=basic_auth(username, password))
db = driver.session(database=database)

def create_fake_person() -> dict:
    """Returns a dictionary representing a Person node that can be later inserted into the database."""
    pass