label library:

    scene bg library
    with dissolve

    menu:
        "What do you want to do?"

        "Study\n{color=#ffbf00}Intelligence +1{/color}, {color=#40e0d0}Energy -10{/color}" if energy >= 10:
            $ energy -= 10
            $ intelligence += 1

            "You increased your understanding of the business."

            jump library

        "Attend a lecture\n{color=#ffbf00}Intelligence +5{/color}, {color=#40e0d0}Energy -45{/color}" if energy >= 45:
            $ energy -= 45
            $ intelligence += 5

            "You felt your business acumen increase."

            jump library

        "Hire a private tutor\n{color=#ffbf00}Intelligence +7{/color}, {color=#40e0d0}Energy -35{/color}, {color=#85bb65}Money -50{/color}" if energy >= 35 and money >= 50:
            $ energy -= 35
            $ money -= 50
            $ intelligence += 7

            "You felt your intelligence increase by a lot."

            jump library

        "Go back":
            jump activities
