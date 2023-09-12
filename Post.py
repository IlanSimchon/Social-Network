import datetime
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import User
import DateTime.DateTime
import matplotlib.image as mpimg


class Post(ABC):

    def __init__(self, user: User):
        self.author = user
        self.date = datetime.datetime.now()
        self.likes = 0
        self.comments = []

    def like(self, user: User):
        self.likes += 1
        self.author.notify_author("like", user)


    def comment(self, user: User, data: str):
        self.comments += data
        self.author.notify_author("comment", user)
        print(data)


class ImagePost(Post):
    def __init__(self, user: User, path: str):
        super(ImagePost, self).__init__(user)
        self.path = path

    def display(self):
        import matplotlib.image as mpimg
        plt.imshow(mpimg.imread(self.path))
        plt.show()

    def __str__(self):
        return f'\n{self.author.userName} published a Image at {self.date}, to see the image use the diaplay function \n'



class TextPost(Post):
    def __init__(self, user: User, data: str):
        super().__init__(user)
        self.data = data

    def __str__(self):
        return f'\n{self.author.userName} published a post at {self.date}: \n{self.data} \n'
