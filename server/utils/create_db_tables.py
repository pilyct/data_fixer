import sys
import os

# add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app import app
from models.user_model import db

def create_db_tables():
    with app.app_context():
        db.create_all()  # create all tables if they don't exist
        print("Tables created successfully.")

if __name__ == "__main__":
    create_db_tables()