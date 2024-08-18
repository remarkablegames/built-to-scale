label bed:

    scene bg living room night
    with dissolve

    menu:
        "What do you want to do?"

        "Sleep\n(Energy +100)":
            $ energy = 100
            $ days -= 1

            "You had a good night’s rest."

            jump day_end

        "Go back":
            jump activities
