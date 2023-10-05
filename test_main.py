from SocialNetwork import SocialNetwork


def main():
    # Creating the network and testing singleton implementation
    network = SocialNetwork("Twitter")
    network2 = SocialNetwork("Facebook")
    print()

    print(f"Is network1 the same instance as network2? {network is network2}")
    print()

    # Creating users with different names
    u1 = network.sign_up("User1", "pass1")
    u2 = network.sign_up("User2", "pass2")
    u3 = network.sign_up("User3", "pass3")
    u4 = network.sign_up("User4", "pass4")
    u5 = network.sign_up("User5", "pass5")

    # Creating followers
    u1.follow(u2)
    u1.follow(u5)
    u2.follow(u5)
    u2.follow(u1)
    u3.follow(u1)
    u3.follow(u2)
    u4.follow(u3)
    u4.follow(u1)
    u5.follow(u2)
    u5.follow(u4)
    print()

    # Creating text post with different content
    p1 = u1.publish_post("Text", "Python is a versatile programming language.")
    p2 = u2.publish_post("Text", "Data science is a fascinating field.")
    p3 = u3.publish_post("Text", "Web development is in high demand.")

    # Creating image post
    p4 = u4.publish_post("Image", 'image1.jpg')

    # Creating sale post with different product details
    p5 = u5.publish_post("Sale", "Used laptop for sale", 500, "New York")

    # Creating likes and comments
    p1.like(u4)
    p1.like(u1)
    p2.like(u1)
    p2.comment(u1, "I totally agree!")
    p3.like(u2)
    p3.comment(u2, "I love building websites!")
    p4.like(u1)
    p5.comment(u3, "Is the laptop still available?")
    p5.comment(u5, "Yes")
    p5.comment(u4, "What's the laptop's brand?")
    print()

    # Price reduction of the product for sale
    p5.discount(50, "pass5")
    print()

    # Additional likes and comments
    p1.like(u2)
    p2.like(u3)
    p4.like(u3)
    p4.comment(u3, "Nice picture!")
    p4.comment(u5, "Where was this taken?")
    print()

    # Defining the product as sold
    p5.sold("pass5")
    print()

    # Displaying the image of the post
    p4.display()

    p4.like(u2)
    p4.comment(u2, "Great photography!")
    print()

    # Using unfollow
    u2.unfollow(u1)
    u3.unfollow(u2)
    print()

    # Using log_in & log_out
    network.log_out("User3")
    network.log_in("User3", "pass3")
    print()

    # User printing
    print(u1)
    print()

    # Post printing
    print(p1)
    print(p5)

    # Printing all notifications received by a certain user
    u4.print_notifications()
    print()

    # Network printing
    print(network)


if __name__ == '__main__':
    main()
