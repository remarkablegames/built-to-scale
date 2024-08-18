label office:

    scene bg office
    with dissolve

    $ sales = 10 + intelligence + charisma
    $ marketing = sales + int((intelligence + charisma) * 1.5)

    menu:
        "What do you want to do?"

        "Sales\n{color=#85bb65}Money +[sales]{/color}, {color=#40e0d0}Energy -10{/color}" if energy >= 10:
            $ energy -= 10
            $ money += sales

            "You made some sales."

            jump office

        "Marketing\n{color=#85bb65}Money +[marketing]{/color}, {color=#40e0d0}Energy -25{/color}" if energy >= 25:
            $ energy -= 25
            $ money += marketing

            "You made more sales."

            jump office

        "Go back":
            jump activities
