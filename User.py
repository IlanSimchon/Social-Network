import SocialNetwork
from Post import *

# Define a mapping from string post categories to the PostCategory enum
PostMap = {
    "Text": PostCategory.TEXT,
    "Image": PostCategory.IMAGE,
    "Sale": PostCategory.SALE
}


class Member(ABC):
    @abstractmethod
    def update(self):
        """
        Abstract method for notifications (Observer design pattern).
        This method should be implemented in subclasses.
        """
        pass


class User(Member):
    def __init__(self, network: SocialNetwork, user_name: str, password: str):
        """
        Initialize a User object with network connection, username, and password.

        Parameters:
        - network (SocialNetwork): The social network instance.
        - user_name (str): The username of the user.
        - password (str): The user's password (consider security implications).
        """
        self.__network = network
        self.__user_name = user_name
        self.__password = password
        self.__followers = set()
        self.__posts = []
        self.__notifications = []

    def get_user_name(self) -> str:
        """
        Get the user's username.

        Returns:
        str: The username of the user.
        """
        return self.__user_name

    def get_password(self) -> str:
        """
        Get the user's password (consider security implications).

        Returns:
        str: The user's password.
        """
        return self.__password

    def get_followers(self) -> set:
        """
        Get the set of users following this user.

        Returns:
        set: A set of User objects representing followers.
        """
        return self.__followers

    def follow(self, user: 'User'):
        """
        Allow this user to follow another user.

        Parameters:
        - user (User): The user to follow.
        """
        if self.is_connected():
            user.__followers.add(self)
            print(f'{self.__user_name} started following {user.__user_name}')
        else:
            raise Exception('Error: you must log in to follow')

    def unfollow(self, user):
        """
        Allow this user to unfollow another user.

        Parameters:
        - user (User): The user to unfollow.
        """
        if self.is_connected():
            if self in user.__followers:
                user.__followers.remove(self)
                print(f'{self.__user_name} unfollowed {user.__user_name}')
            else:
                raise Exception("Error: you need to follow in order to unfollow")
        else:
            raise Exception('Error: you must log in to unfollow')

    def publish_post(self, category: str, *data) -> Post or None:
        """
        Publish a post of the specified category (Text, Image, Sale).

        Parameters:
        - category (str): The category of the post (e.g., "Text", "Image", "Sale").
        - *data: Variable-length arguments depending on the post category.

        Returns:
        Post or None: The created Post object or None if the user not connected.
        """
        if self.is_connected():
            # Use the PostMap to convert the string category to an enum member
            post = PostFactory.create_post(self, PostMap.get(category), *data)
            self.__posts.append(post)
            return post
        raise Exception('Error: you must log in to post')

    def update(self, category: ActionCategory, user: 'User'):
        """
        Notify this user about different activities (e.g., posts, likes, comments) related to other users.

        Parameters:
        - category (str): The category of the notification (e.g., "post", "like", "comment").
        - user (User): The user related to the notification.
        - flag (int): An optional flag for additional information.

        Raises:
        Exception: If the category parameter is invalid.
        """
        if category == ActionCategory.POST:
            self.__notifications.append(f'{user.__user_name} has a new post')
            return
        elif category == ActionCategory.LIKE:
            notification = f'{user.__user_name} liked your post'
            print(f'notification to {self.__user_name}: {notification}')
        elif category == ActionCategory.COMMENT:
            notification = f'{user.__user_name} commented on your post'
            print(f'notification to {self.__user_name}: {notification}: ', end='')
        else:
            raise Exception("Error in category parameter")
        self.__notifications.append(notification)

    def is_connected(self) -> bool:
        """
        Check if this user is connected to the network.

        Returns:
        bool: True if connected, False otherwise.

        Raises:
        Exception: If the user is not found in the network.
        """
        if self in self.__network.get_users().keys():
            return self.__network.get_users()[self]
        raise Exception("Error: User not found!")

    def print_notifications(self):
        """
        Print all notifications for this user.
        """
        print(f"{self.__user_name}'s notifications:")
        for notification in self.__notifications:
            print(notification)

    def __str__(self) -> str:
        """
        Get a string representation of this User object.

        Returns:
        str: A string representation of the User object.
        """
        return f'User name: {self.__user_name}, Number of posts: {len(self.__posts)}, Number of followers: {len(self.__followers)}'
