class User:
    """Takes in an id, username, and password."""
    # Constructor function

    def __init__(self, id, username, password) -> None:
        self.user_id = id
        self.username = username
        self.password = password
        self.followers = 0
        self.following = []

    def get_user_info(self):
        return f"User ID: {self.user_id}, Username: {self.username}. Password: {self.password}."

    def increase_follower_count(self):
        self.followers += 1

    def decrease_follower_count(self):
        self.followers -= 1

    def follow_user(self, user):
        self.following.append(user)

    def show_followed_users(self):
        for user in self.following:
            print(user.get_user_info())


user_1 = User(id="01", username="John", password="Blepbelp")
user_2 = User(id="02", username="JAMES", password="Blepbelp")
user_3 = User(id="03", username="JONES", password="Blepbelp")
user_1.increase_follower_count()
user_1.increase_follower_count()
user_1.follow_user(user_2)
user_1.follow_user(user_3)
user_1.show_followed_users()
