from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from datetime import datetime
from enum import Enum
import User


class PostCategory(Enum):
    """
    Enum representing the category of a post.
    """
    TEXT = "Text"
    IMAGE = "Image"
    SALE = "Sale"


class ActionCategory(Enum):
    """
    Enum representing the category of a post action (e.g., POST, LIKE, COMMENT).
    """
    POST = "post"
    LIKE = "like"
    COMMENT = "comment"


class PostFactory:
    @staticmethod
    def create_post(author: User, category: PostCategory, *data):
        """
        Create a post based on the given category.

        Parameters:
        - author (User): The user creating the post.
        - category (PostCategory): The category of the post (TEXT, IMAGE, SALE).
        - *data: Variable-length arguments depending on the post category.

        Returns:
        Post: The created Post object.
        """
        if category == PostCategory.TEXT:
            post = TextPost(author, data[0])
        elif category == PostCategory.IMAGE:
            post = ImagePost(author, data[0])
        elif category == PostCategory.SALE:
            post = SalePost(author, data[0], data[1], data[2])
        else:
            raise Exception("Error: category parameter not correct")
        return post


class Sender:
    @abstractmethod
    def update(self):
        pass


class Post(ABC, Sender):
    def __init__(self, user: User):
        """
        Initialize a Post object.

        Parameters:
        - user (User): The user creating the post.
        """
        self._author = user
        self._date = datetime.now()
        self._likes = []
        self._comments = []
        self.update(ActionCategory.POST, user)

    def like(self, user: User):
        """
        Allow a user to like this post.

        Parameters:
        - user (User): The user liking the post.
        """
        if user.is_connected():
            self.update(ActionCategory.LIKE, user)
            self._likes.append(user)
        else:
            raise Exception('Error: you must log in to like')

    def comment(self, user: User, data: str):
        """
        Allow a user to comment on this post.

        Parameters:
        - user (User): The user commenting on the post.
        - data (str): The comment text.
        """
        if user.is_connected():
            self.update(ActionCategory.COMMENT, user)
            print(data)
            self._comments.append((user, data))
        else:
            raise Exception('Error: you must log in to comment')

    def update(self, category: ActionCategory, user: User):
        """
        Notify users about post-related activities.

        Parameters:
        - category (ActionCategory): The category of the activity (POST, LIKE, COMMENT).
        - user (User): The user involved in the activity.
        """
        if category == ActionCategory.POST:
            for user in self._author.get_followers():
                user.notify(category, self._author)
        elif category in (ActionCategory.LIKE, ActionCategory.COMMENT):
            if self._author.get_user_name() != user.get_user_name():
                self._author.notify(category, user)
            for u in set(self._likes + [t[0] for t in self._comments]):
                if self._author.get_user_name() != u.get_user_name():
                    u.notify_participant(category, user, self._author)

    @abstractmethod
    def __str__(self):
        pass


class ImagePost(Post):
    def __init__(self, user: User, path: str):
        super(ImagePost, self).__init__(user)
        self.__path = path
        print(self)

    def display(self):
        """
        Display the image associated with the post.
        """
        print("Shows picture")
        plt.imshow(mpimg.imread(self.__path))
        plt.show()

    def __str__(self):
        return f'{self._author.get_user_name()} published an Image at {self._date}, to see the image, use the display function\n'


class TextPost(Post):
    def __init__(self, user: User, data: str):
        super().__init__(user)
        self.__data = data
        print(self)

    def __str__(self):
        return f'{self._author.get_user_name()} published a post at {self._date}:\n"{self.__data}"\n'


class SalePost(Post):
    def __init__(self, user: User, description: str, price: int, location: str):
        super().__init__(user)
        self.__description = description
        self.__price = price
        self.__location = location
        self.__available = True
        print(self)

    def sold(self, password: str):
        """
        Mark the product as sold.

        Parameters:
        - password (str): The seller's password for verification.
        """
        if password == self._author.get_password():
            self.__available = False
            print(f"{self._author.get_user_name()}'s product is sold")
        else:
            raise Exception('Error: only a seller can announce that the product is sold')

    def discount(self, discount: int, password: str):
        """
        Apply a discount to the product's price.

        Parameters:
        - discount (int): The discount percentage.
        - password (str): The seller's password for verification.
        """
        if password == self._author.get_password():
            self.__price = self.__price * (1 - discount / 100)
            print(f'Discount on {self._author.get_user_name()} product! the new price is: {self.__price}')
        else:
            raise Exception('Error: only a seller can change the price of the product')

    def __str__(self):
        """
        Generate a string representation of the SalePost.

        Returns:
        str: A string containing details of the SalePost.
        """
        s = f'{self._author.get_user_name()} published a product for sale at {self._date}:\n'
        s += 'Sold! ' if not self.__available else 'For sale! '
        return s + f'{self.__description}, price: {self.__price}, pickup from: {self.__location}\n'

