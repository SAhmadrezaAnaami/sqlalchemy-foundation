from db import db
from model.user import User

def add_user(name: str, email: str):
    with db.get_session() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()

if __name__ == "__main__":
    add_user("John Doe", "john@example.com")
