label restaurant:

    scene bg restaurant
    with dissolve

    menu:
        "What do you want to do?"

        "Drink\n{color=#40e0d0}Energy +5{/color}, {color=#85bb65}Money -10{/color}":
            $ energy += 5
            $ money -= 10

            "You had an energy drink."

            jump restaurant

        "Eat\n{color=#40e0d0}Energy +10{/color}, {color=#85bb65}Money -20{/color}":
            $ energy += 20
            $ money -= 10

            "You had a good meal."

            jump restaurant

        "Go back":
            jump activities
