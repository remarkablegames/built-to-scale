label park:

    if time < 14:
        scene bg park day
        with dissolve
    else:
        scene bg park night
        with dissolve

    if time >= time_eod:
        jump go_home

    menu:
        "What do you want to do?"

        "Cardio\n{color=#ccccff}Charisma +1{/color}, {color=#40e0d0}Energy -10{/color}" if energy >= 10:
            $ energy -= 10
            $ charisma += 1
            $ time += 1

            "You upped your appeal."

            jump park

        "Attend a workout class\n{color=#ccccff}Charisma +5{/color}, {color=#40e0d0}Energy -45{/color}" if energy >= 45:
            $ energy -= 45
            $ charisma += 5
            $ time += 2

            "Your charisma increased a lot."

            jump park

        "Hire a private trainer\n{color=#ccccff}Charisma +7, {color=#40e0d0}Energy -35{/color}, {color=#85bb65}Money -$50{/color}" if energy >= 35 and money >= 50:
            $ energy -= 35
            $ money -= 50
            $ charisma += 7
            $ time += 3

            "Your charisma went up significantly."

            jump park

        "Go back":
            jump activities
