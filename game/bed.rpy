label bed:

    scene bg living room night
    with dissolve

    menu:
        "What do you want to do?"

        "Sleep\n{color=#40e0d0}Energy +100{/color}":
            $ energy = 100
            $ days -= 1

            scene black
            with fade

            "You had a good night’s rest."

            jump day_end

        "Go back":
            jump activities
