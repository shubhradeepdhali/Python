# One class should have one responsibility ONLY
# Hence a class should have only one reason to change

class User:
    def __init__(self, name: str, age: int, email: str) -> None:
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
            print(f"User name is {self.name} and user age is {self.age} years") 