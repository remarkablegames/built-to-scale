label day_02:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg room morning light off
    with fade

    show friend
    with dissolve

    friend @ confident "I got an extra book from the library today."

    menu:
        "Which one would you like to read?"

        "Book on Intelligence\n{color=#ffbf00}Intelligence +1{/color}":
            $ intelligence += 1

            "You felt your intelligence go up."

        "Book on Charisma\n{color=#ccccff}Charisma +1{/color}":
            $ charisma += 1

            "You felt your charisma go up."

        "Pass":
            "You decided not to read either book."

    return
