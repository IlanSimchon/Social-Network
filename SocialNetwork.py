import UserManager
from User import User


class SocialNetwork():
    __instance = None

    def __new__(cls, name: str):
        if cls.__instance is None:
            cls.__instance = super(SocialNetwork, cls).__new__(cls)
            cls.name = name
            cls.users = []
            print("The social network was created!")
        return cls.__instance

    def sign_up(self, userName: str, password: str) -> User or None:
        if not 4 <= len(password) <= 8:
            return None
        for user in self.users:
            if user.userName == userName:
                return None
        user = User(userName, password)
        self.users.append(user)
        return user

    def __str__(self):
        print()
        data = 'Twitter social network:\n'
        for user in self.users:
            data += f'{user.__str__()} \n'
        return data
