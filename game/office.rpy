label office:

    scene bg club
    with dissolve

    $ sales = 10 + intelligence + charisma
    $ marketing = sales + int((intelligence + charisma) * 1.5)

    menu:
        "What do you want to do?"

        "Sales\n(Money +[sales], Energy -10)":
            $ energy -= 10
            $ money += amount

            "You made some sales."

            jump office

        "Marketing\n(Money +[marketing], Energy -25)":
            $ energy -= 25
            $ money += marketing

            "You made more sales."

            jump office

        "Go back":
            jump activities
