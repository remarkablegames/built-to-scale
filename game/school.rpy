label school:

    scene bg library
    with dissolve

    menu:
        "What do you want to do?"

        "Study\n(Intelligence +1, Energy -10)":
            $ energy -= 10
            $ intelligence += 1

            "You increased your understanding of the business."

            jump school

        "Attend a lecture\n(Intelligence +5, Energy -45)":
            $ energy -= 45
            $ intelligence += 5

            "You felt your business acumen increase."

            jump school

        "Hire a private tutor\n(Intelligence +7, Energy -35, Money -50)":
            $ energy -= 35
            $ money -= 50
            $ intelligence += 7

            "You felt your intelligence increase by a lot."

            jump school

        "Go back":
            jump activities
