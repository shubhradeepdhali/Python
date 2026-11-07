from user import User
from user_repository import UserRepository

user1 = User("John", 25, "john@gmail.com")
user1.get_user_info
user1_repo = UserRepository("Rey", "reyplaza")

user1.get_user_info()
user1_repo.save_to_database(user1)