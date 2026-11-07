# One class should have one responsibility ONLY
# Hence a class should have only one reason to change

class User:
    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
        print(f"User name is {self.name} and user age is {self.age} years")

    def is_adult(self) -> bool:
        return self.age > 18

    def save_to_database(self) -> None:
        print(f"User {self.name} is being saved to DataBase")

    def delete_from_database(self) -> None:
        print(f"User {self.name} is being deleted from database")

user1 = User("Rohan", 34, "rohan@gmail.com")
user1.get_user_info()
print(user1.is_adult())
