label start:
    "I’ve always had a dream..."
    "And that dream is to start a company that sells {b}scales{/b}."
    "Why {i}scales{/i}?{w=0.3} Because scales saved my life."
    "But I don’t have much time left..."
    "I’m graduating in {b}30 days{/b}."
    "So let’s see how far I can go."

    scene bg uni
    with fade

    show angel at scale(0.6), center
    with dissolve

    angel "Your application to start a business that sells scales looks good."
    angel "Just confirming,{w=0.2} what’s your business called again?"

    python:
        business_name = renpy.input("My business name is...", length=32)
        business_name = business_name.strip() or "Scales, Inc."

    angel smile "“[business_name]”...{w=0.5} It has a nice ring to it!"

    angel "Everything’s in place,{w=0.3} please sign your first name so you can officially incorporate your business."

    python:
        player_name = renpy.input("My first name is...", length=32)
        player_name = player_name.strip() or "Entrepreneur"

    angel "Congratulations, [player_name]!"
    angel "Remember that every successful business starts with a dream and a lot of hard work."
    angel "It’s not just about selling your product,{w=0.3} it’s about solving problems and making people’s lives better."
    angel "Keep your eyes on the prize and never stop believing in yourself."
    angel "“[business_name]” could be the start of something amazing."
    angel smile "Now let’s get to work!"

    jump stats_intro
