label park:

    scene bg park
    with dissolve

    menu:
        "What do you want to do?"

        "Cardio\n(Charisma +1, Energy -10)":
            $ energy -= 10
            $ charisma += 1

            "You increased your charisma."

            jump park

        "Attend a workout class\n(Charisma +5, Energy -45)":
            $ energy -= 45
            $ charisma += 5

            "You greatly increased your charisma."

            jump park

        "Hire a private trainer\n(Charisma +7, Energy -35, Money -50)":
            $ energy -= 35
            $ money -= 50
            $ charisma += 7

            "You felt your charisma increase by a lot."

            jump park

        "Go back":
            jump activities
