label home:

    if time < 12:
        scene bg room morning
        with dissolve
    elif time < 4:
        scene bg room noon
        with dissolve
    elif time < 8:
        scene bg room evening
        with dissolve
    else:
        scene bg room night
        with dissolve

    menu:
        "What do you want to do?"

        "Sleep\n{color=#40e0d0}Energy +100{/color}":
            $ energy = 100
            $ days -= 1

            scene bg room night light off
            with fade

            "You had a good night’s rest."

            jump day_end

        "Go back":
            jump activities
