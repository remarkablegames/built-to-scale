label library:

    scene bg library
    with dissolve

    menu:
        "What do you want to do?"

        "Study\n{color=#ffbf00}Intelligence +1{/color}, {color=#40e0d0}Energy -10{/color}" if energy >= 10:
            play sound writing

            $ energy -= 10
            $ intelligence += 1
            $ time += 1

            "You improved your business smarts."

            jump library

        "Attend a lecture\n{color=#ffbf00}Intelligence +5{/color}, {color=#40e0d0}Energy -45{/color}" if energy >= 45:
            play sound writing

            $ energy -= 45
            $ intelligence += 5
            $ time += 2

            "You greatly increased your business sense."

            jump library

        "Hire a private tutor\n{color=#ffbf00}Intelligence +7{/color}, {color=#40e0d0}Energy -35{/color}, {color=#85bb65}Money -50{/color}" if energy >= 35 and money >= 50:
            play sound writing

            $ energy -= 35
            $ money -= 50
            $ intelligence += 7
            $ time += 3

            "Your acumen went up significantly."

            jump library

        "Go back":
            jump activities
