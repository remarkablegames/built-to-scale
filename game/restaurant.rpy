label restaurant:

    scene bg restaurant
    with dissolve

    menu:
        "What do you want to do?"

        "Drink\n(Energy +5, Money -10)":
            $ energy += 5
            $ money -= 10

            "You had an energy drink."

            jump restaurant

        "Eat\n(Energy +10, Money -20)":
            $ energy += 20
            $ money -= 10

            "You had a good meal."

            jump restaurant

        "Go back":
            jump activities
