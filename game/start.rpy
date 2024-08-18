default player_name = "Entrepreneur"
default business_name = "Scales, Inc."

label start:

    "I’ve always had a dream..."
    "And that dream is to start a company that sells {b}scales{/b}."
    "Why {i}scales{/i}?{w=0.3} Because scales saved my life."
    "But I don’t have much time left..."
    "I’m graduating in {b}30 days{/b}."
    "Let’s see how far I can take this."

    scene bg uni
    with fade

    show screen info

    show angel at scale(0.6), center
    with dissolve

    angel "I’ll be handling your application to start your business."
    angel "What’s your business called?"

    $ business_name = renpy.input("My business name is...", length=32).strip() or business_name

    angel smile "“[business_name]”...{w=0.5} It has a nice ring to it!"

    angel "The paperwork is done,{w=0.2} please sign your name to incorporate your company."

    $ player_name = renpy.input("My first name is...", length=32).strip() or player_name

    angel open smile "Congratulations, [player_name]!"
    angel "Remember that every successful business starts with a dream and a lot of hard work."
    angel "It’s not just about selling your product,{w=0.3} it’s about solving problems and making people’s lives better."
    angel "Keep your eyes on the prize and never stop believing in yourself."
    angel "“[business_name]” could be the start of something big."
    angel smile "Now let’s get to work!"

    jump stats_intro
