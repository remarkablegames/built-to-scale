default time = 0

label activities:

    if time < 12:
        scene bg bus stop morning
        with dissolve
    elif time < 5:
        scene bg bus stop noon
        with dissolve
    elif time < 10:
        scene bg bus stop evening
        with dissolve
    else:
        scene bg bus stop night
        with dissolve

    menu:
        "Where do you want to go?"

        "{color=#ffbf00}Library{/color}":
            jump library

        "{color=#ccccff}Park{/color}":
            jump park

        "{color=#85bb65}Office{/color}":
            jump office

        "{color=#40e0d0}Shop{/color}":
            jump shop

        "Home":
            jump home
