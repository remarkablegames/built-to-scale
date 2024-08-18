label park:

    scene bg park
    with dissolve

    menu:
        "What do you want to do?"

        "Cardio\n{color=#ccccff}Charisma +1{/color}, {color=#40e0d0}Energy -10{/color}" if energy >= 10:
            $ energy -= 10
            $ charisma += 1

            "You increased your charisma."

            jump park

        "Attend a workout class\n{color=#ccccff}Charisma +5{/color}, {color=#40e0d0}Energy -45{/color}" if energy >= 45:
            $ energy -= 45
            $ charisma += 5

            "You greatly increased your charisma."

            jump park

        "Hire a private trainer\n{color=#ccccff}Charisma +7, {color=#40e0d0}Energy -35{/color}, {color=#85bb65}Money -50{/color}" if energy >= 35 and money >= 50:
            $ energy -= 35
            $ money -= 50
            $ charisma += 7

            "You felt your charisma increase by a lot."

            jump park

        "Go back":
            jump activities
