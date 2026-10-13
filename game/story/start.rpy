label start:

    play music electro_1 fadein 1

    "I’ve always had a dream..."
    "And that dream is to start a company that sells {b}scales{/b}."
    "Why {i}scales{/i}?{w=.3} Because scales saved my life."
    "But I don’t have much time left..."
    "I’m graduating in {b}[days_total] days{/b}."
    "I have to make {b}$[goal:,]{/b} for the business to be sustainable."
    "Let’s see how far I go."

    stop music fadeout 1
    queue music electro_2a
    queue music electro_2b

    scene bg modern office
    with fade

    show screen info

    show mentor
    with dissolve

    mentor "I’ll be handling your application to start your business."
    mentor "What’s your business called?"

    $ business_name = renpy.input("My business name is...", default="Scales, Inc.", length=32).strip() or business_name

    mentor smile "{cps=10}“[business_name]”...{/cps}{w=.5} It has a nice ring to it!"

    mentor "The paperwork’s done,{w=.2} please sign your name to incorporate your company."

    $ player_name = renpy.input("My name is...", default="Entrepreneur", length=32).strip() or player_name

    mentor smile2 "Congratulations,{w=.1} [player_name]!"
    mentor "Remember that every successful business starts with a dream and a lot of hard work."
    mentor "It’s not just about selling your product,{w=.2} but about solving problems to make people’s lives better."
    mentor "“[business_name]” could be the next big thing."
    mentor smile "Before you get to work,{w=.2} let’s take a quick detour."

    jump stats_intro
