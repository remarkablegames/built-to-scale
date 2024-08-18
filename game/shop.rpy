label shop:

    scene bg shop
    with dissolve

    menu:
        "What do you want to do?"

        "Drink\n{color=#40e0d0}Energy +5{/color}, {color=#85bb65}Money -10{/color}" if money >= 10:
            $ energy += 5
            $ money -= 10

            "You had an energy drink."

            jump shop

        "Eat\n{color=#40e0d0}Energy +10{/color}, {color=#85bb65}Money -20{/color}" if money >= 20:
            $ energy += 20
            $ money -= 10

            "You had a good meal."

            jump shop

        "Go back":
            jump activities
