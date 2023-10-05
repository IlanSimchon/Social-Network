from User import User


class SocialNetwork:
    __instance = None

    def __new__(cls, name: str):
        """
        Create a new instance of SocialNetwork if it doesn't exist.

        Parameters:
        - name (str): The name of the social network.

        Returns:
        SocialNetwork: The existing or newly created instance of SocialNetwork.
        """
        if cls.__instance is None:
            cls.__instance = super(SocialNetwork, cls).__new__(cls)
            cls.__name = name
            cls.__users_connection = {}
            print(f'The social network {name} was created!')
        return cls.__instance

    def sign_up(self, userName: str, password: str) -> User:
        """
        Register a new user in the social network.

        Parameters:
        - userName (str): The username of the new user.
        - password (str): The password for the new user.

        Returns:
        User or None: The created User object if registration is successful, or None if registration fails.
        """
        if not 4 <= len(password) <= 8:
            raise Exception("Error: password must be 4 to 8 characters long")
        for user in self.__users_connection:
            if user.get_user_name() == userName:
                raise Exception("Error: username already exists")
        user = User(self, userName, password)
        self.__users_connection[user] = True
        return user

    def log_in(self, user_name: str, password: str) -> User:
        """
        Log in a user to the social network.

        Parameters:
        - user_name (str): The username of the user.
        - password (str): The password for the user.

        Returns:
        User: The User object of the logged-in user.

        Raises:
        Exception: If the user is not found or the login credentials are incorrect.
        """
        for user in self.__users_connection.keys():
            if user.get_user_name() == user_name and user.get_password() == password:
                self.__users_connection[user] = True
                print(f'{user.get_user_name()} connected')
                return user
        raise Exception("User not found!")

    def log_out(self, user_name: str):
        """
        Log out a user from the social network.

        Parameters:
        - user_name (str): The username of the user to log out.
        """
        for user in self.__users_connection.keys():
            if user.get_user_name() == user_name:
                self.__users_connection[user] = False
                print(f'{user.get_user_name()} disconnected')

    def get_users(self) -> dict:
        """
        Get the dictionary of users in the social network.

        Returns:
        dict: A dictionary where keys are User objects and values indicate their connection status (True or False).
        """
        return self.__users_connection

    def __str__(self) -> str:
        """
        Generate a string representation of the social network and its users.

        Returns:
        str: A string containing details of the social network and its users.
        """
        data = f'{self.__name} social network:'
        for user in self.__users_connection:
            data += f'\n{user}'
        return data
