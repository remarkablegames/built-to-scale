default player_name = "Entrepreneur"
default business_name = "Scales, Inc."
default goal = 250000

label start:

    "I’ve always had a dream..."
    "And that dream is to start a company that sells {b}scales{/b}."
    "Why {i}scales{/i}?{w=0.3} Because scales saved my life."
    "But I don’t have much time left..."
    "I’m graduating in {b}30 days{/b}."
    "I have to make {b}$[goal]{/b} for the business to be sustainable."
    "Let’s see how far I go."

    scene bg modern office
    with fade

    show screen info

    show mentor
    with dissolve

    mentor "I’ll be handling your application to start your business."
    mentor "What’s your business called?"

    $ business_name = renpy.input("My business name is...", length=32).strip() or business_name

    mentor smile "“[business_name]”...{w=0.5} It has a nice ring to it!"

    mentor "The paperwork is done,{w=0.2} please sign your name to incorporate your company."

    $ player_name = renpy.input("My first name is...", length=32).strip() or player_name

    mentor smile2 "Congratulations, [player_name]!"
    mentor "Remember that every successful business starts with a dream and a lot of hard work."
    mentor "It’s not just about selling your product,{w=0.3} it’s about solving problems and making people’s lives better."
    mentor "Keep your eyes on the prize and never stop believing in yourself."
    mentor "“[business_name]” could be the start of something big."
    mentor smile "Before you get to work, let’s take a walk."

    jump stats_intro
