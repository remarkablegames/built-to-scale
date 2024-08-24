label day_02:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg room morning
    with fade

    show friend
    with dissolve

    friend confident "I got an extra book from the library today."

    $ dice_roll = renpy.random.randint(1, 6)

    menu:
        friend "Which one would you like to read?"

        "Book on Intelligence\n{color=#ffbf00}Intelligence +[dice_roll]{/color}":
            $ intelligence += dice_roll

            show friend confident2

            "Your intelligence went up."

        "Book on Charisma\n{color=#ccccff}Charisma +[dice_roll]{/color}":
            $ charisma += dice_roll

            show friend confident3

            "Your charisma went up."

        "Pass":
            "You decided not to read either book."

    return
