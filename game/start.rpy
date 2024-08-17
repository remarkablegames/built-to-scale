label start:

    "I'm going to graduate in 30 days.{w=2.5} I have the choice to either have control of my life or give up my dreams.{w=2.5} Let's take a risk and see how far I get..."

    scene bg uni
    with fade

    show angel at scale(0.6), center
    with dissolve

    angel "Hi there!{w=0.5} So, you want to start your own business...{w=0.5} What’s your name?"

    python:
        player_name = renpy.input("My name is...", length=32)
        player_name = player_name.strip() or "Player"

    angel smile "Nice to meet you, [player_name]!"

    angel "Now tell me, what will you name your business?"

    python:
        business_name = renpy.input("My business name is...", length=32)
        business_name = business_name.strip() or "My Business"

    angel smile "That's a great name... [business_name]! It's got a nice ring to it."

    angel "And what kind of product are you selling?"

    python:
        product_name = renpy.input("My product is...", length=32)
        product_name = product_name.strip() or "Scales"

    angel smile "Great choice! [product_name] are in demand these days."

    angel "Remember, [player_name], every successful business starts with a dream and a lot of hard work."
    angel "It's not just about selling [product_name], it's about solving a problem and making people's lives better."
    angel "Keep your eyes on the goal and never stop believing in yourself. [business_name] could be the start of something amazing."

    angel smile "Now let's get to work!"

    jump stats
