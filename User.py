from datetime import datetime
from abc import ABC, abstractmethod

import SocialNetwork
from Post import TextPost, ImagePost, Post


class User:

    def __init__(self, userName: str, password: str):
        self.userName = userName
        self.password = password
        self.followers = set()
        # self.follows_them = set()
        self.posts = []
        self.notification = []

    def follow(self, user: 'User'):
        # self.follows_them.add(user)
        user.followers.add(self)

    def unFollow(self, user):
        # self.follows_them.remove(user)
        user.followers.remove(self)

    def Publish_post(self, type: str, data: str) -> Post or None:
        if type == "Text":
            post = TextPost(self, data)
        elif type == "Image":
            post = ImagePost(self, data)
        else:
            raise Exception
        self.posts.append(post)
        print(post)
        self.update()
        return post

    def update(self):
        for follower in self.followers:
            follower.notify(self)

    def notify(self, user:'User'):
        self.notification.append(f'{user.userName} has a new post')

    def notify_author(self, type: str, user:'User'):
        if type == "like":
            notification = f'{user.userName} liked your post'
            print('notification to ',self.userName, ': ', notification)
            self.notification.append(notification)
        elif type == 'comment':
            notification = f'{user.userName} commented on your post: '
            print('notification to ',self.userName, ': ', notification, end='')
            self.notification.append(notification)
        else:
            raise Exception

    def __str__(self):
            return f'user name: {self.userName}, number of posts: {len(self.posts)} ' \
                                                      f', number of followers: {len(self.followers)}'

# class Person:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.__id = args[0]
#             self.__name = args[1]
#             self.__year = args[2]
#         elif len(args) == 1 and isinstance(args[0], Person):
#             self.__id = args[0].__id
#             self.__name = args[0].__name
#             self.__year = args[0].__year
#         else:
#             raise Exception
#
#     def get_id(self) -> int:
#         return self.__id
#
#     def get_name(self) -> str:
#         return self.__name
#
#     def get_age(self) -> int:
#         return int(datetime.now().year) - self.__year
#
#     def __set_name__(self, new_name: str):
#         self.__name = new_name
#
#     def __eq__(self, other: 'Person'):
#         return self.__id == other.__id
#
#     def __str__(self):
#         return f'ID: {self.__id}, Name: {self.__name}, Age: {self.get_age()}'
#
#
# class observer(ABC):
#     @abstractmethod
#     def update(self, ):
#         pass
#
#
# class User(Person, observer):
#
#     def __init__(self, person: 'Person', mail: str, password: str):
#         super().__init__(person)
#         self.userName = mail
#         self.password = password
#         self.posts = []
#         self.followers = set()
#         self.follows_them = ()
#         self.notification = []
#
#     def follow(self, user:'User'):
#         self.follows_them.add(user)
#         user.followers.add(1)
#
#     def unFollow(self, user):
#         self.follows_them.remove(user)
#         user.followers.remove(self)
#
#     def Publish_post(self, data: str):
#         post = Post(data)
#         self.posts.append(post)
#         self.update()
#
#     def update(self):
#         for follower in self.followers:
#             follower.notify("post", self)
#
#     def notify(self, type: str, user: 'User'):
#         if type == "post":
#             self.notification.append(f'{user.userName} has a new post')
#         elif type == "like":
#             self.notification.append(f'{user.userName} liked your post')
#         elif type == 'comment':
#             self.notification.append(f'{user.userName} commented on your post')
#         else:
#             raise Exception
#
#     def __str__(self):
#         return super(User, self).__str__(), ' ' + f'Mail: {self.userName}, number of posts: {len(self.posts)} ' \
#                                                   f', number of followers: {len(self.followers)}'
