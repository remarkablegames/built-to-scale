label shop:

    scene bg shop
    with dissolve

    if time >= time_eod:
        jump go_home

    menu:
        "What do you want to do?"

        "Drink\n{color=#40e0d0}Energy +5{/color}, {color=#85bb65}Money -$10{/color}" if money >= 10 and energy < 100:
            $ energy += 5
            $ money -= 10
            $ time += 0.1

            "You drank an energy drink."

            jump shop

        "Snack\n{color=#40e0d0}Energy +10{/color}, {color=#85bb65}Money -$20{/color}" if money >= 20 and energy < 100:
            $ energy += 10
            $ money -= 20
            $ time += 0.2

            "You ate an energy bar."

            jump shop

        "Dine\n{color=#40e0d0}Energy +20{/color}, {color=#85bb65}Money -$40{/color}" if money >= 40 and energy < 100:
            $ energy += 20
            $ money -= 40
            $ time += 0.5

            "You had a hearty meal."

            jump shop

        "Go back":
            jump activities
