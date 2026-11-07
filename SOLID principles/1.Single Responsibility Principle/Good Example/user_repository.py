from user import User

class UserRepository:
    def __init__(self, user_name, password) -> None:
        self.user_name = user_name
        self.password = password

    def save_to_database(self, user: "User"):
        print("saved to database")

    def delete_from_database(self, user: "User"):
        print("deleted from database")