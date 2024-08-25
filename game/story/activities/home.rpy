label go_home:

    "It’s getting late, I should go home now."

    jump home

label home:

    if time < 10:
        scene bg room morning
        with dissolve
    elif time < 14:
        scene bg room noon
        with dissolve
    elif time < 18:
        scene bg room evening
        with dissolve
    else:
        scene bg room night
        with dissolve

    menu:
        "What do you want to do?"

        "Nap\n{color=#40e0d0}Energy +30{/color}, +3 Hours" if time < 18:
            $ energy += 30
            $ time += 3

            "You took a quick nap."

            jump home

        "Sleep\n{color=#40e0d0}Energy +100{/color}, +1 Day":
            stop music fadeout 3

            scene bg room night light off
            with dissolve

            $ energy = 100
            $ days -= 1

            "You had a good night’s rest."

            jump day_end

        "Go back":
            jump activities
