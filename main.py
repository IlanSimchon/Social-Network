# import SocialNetwork as sn
#
#
# if __name__ == '__main__':
#
#     social_network = sn.SocialNetwork("Twitter")
#
#     u1 = social_network.sign_up("Gal123@fake.com", '123456')
#     u2 = social_network.sign_up("Meir123@fake.com", '123456')
#     u3 = social_network.sign_up("Ron123@fake.com", '123456')
#     u4 = social_network.sign_up("Amir123@fake.com", '123456')
#     u5 = social_network.sign_up("Eitan123@fake.com", '123456')
#
#     u1.follow(u4)
#     u1.follow(u5)
#     u2.follow(u2)
#     u3.follow(u1)
#     u4.follow(u1)
#     u4.follow(u2)
#     u4.follow(u3)
#     u4.follow(u4)
#     u5.follow(u1)
#
#     u1.Publish_post("Text", "This is my first Post!")
#
#     u2.Publish_post("Image", 'image 1.png')
#
#     u1.posts[0].like(u2)
#     u1.posts[0].like(u2)
#
#     u1.posts[0].comment(u5, "Nice!")
#
#
#
#
#     print(social_network)
import SocialNetwork as sn
import random

if __name__ == '__main__':
    social_network = sn.SocialNetwork("MySocialNetwork")

    # Create 30 users
    users = []
    user_data = [
        ("Alice", "pass1"),
        ("Bob", "pass2"),
        ("Charlie", "pass3"),
        ("David", "pass4"),
        ("Eve", "pass5"),
        ("Frank", "pass6"),
        ("Grace", "pass7"),
        ("Hank", "pass8"),
        ("Ivy", "pass9"),
        ("Jack", "pass10"),
        ("Kate", "pass11"),
        ("Liam", "pass12"),
        ("Mia", "pass13"),
        ("Noah", "pass14"),
        ("Olivia", "pass15"),
        ("Parker", "pass16"),
        ("Quinn", "pass17"),
        ("Ryan", "pass18"),
        ("Sophia", "pass19"),
        ("Tyler", "pass20"),
        ("Uma", "pass21"),
        ("Victor", "pass22"),
        ("Wendy", "pass23"),
        ("Xander", "pass24"),
        ("Yara", "pass25"),
        ("Zane", "pass26"),
        ("Nina", "pass27"),
        ("Oscar", "pass28"),
        ("Penny", "pass29"),
        ("Riley", "pass30")
    ]

    for name, password in user_data:
        user = social_network.sign_up(name, password)
        users.append(user)

    # Randomly make users follow each other
    for user in users:
        num_followings = random.randint(5, 15)
        for _ in range(num_followings):
            random_user = random.choice(users)
            if random_user != user:
                user.follow(random_user)

    # Each user makes a post
    post_comments = [
        "Great post!",
        "Interesting!",
        "Well said!",
        "I agree with you.",
        "Can't believe it!",
        "Thanks for sharing!",
        "I learned something new.",
        "This is awesome!",
        "You're so talented.",
        "Impressive!",
    ]

    for user in users:
        post_type = random.choice(["Text", "Image"])
        if post_type == "text":
            post_content = "This is a random text post."
        else:
            post_content = f'image_{user.userName}.png'
        user.Publish_post(post_type, post_content)

        # Randomly add comments and likes to posts
        num_likes = random.randint(0, len(users) // 2)
        for _ in range(num_likes):
            random_user = random.choice(users)
            if random_user != user:
                user.posts[-1].like(random_user)

        num_comments = random.randint(0, len(users) // 2)
        for _ in range(num_comments):
            random_user = random.choice(users)
            if random_user != user:
                random_comment = random.choice(post_comments)
                user.posts[-1].comment(random_user, random_comment)

    print(social_network)
