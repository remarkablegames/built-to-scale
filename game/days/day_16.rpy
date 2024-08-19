label day_16:

    scene bg bus stop morning
    with fade

    "As you’re walking down the street, you spot something on the ground."

    player "Is that... a lotto ticket?"

    "You pick it up and examine it. It’s unscratched, a potential stroke of luck."

    player "Well, I guess there’s only one way to find out if this is my lucky day."

    "You scratch the ticket nervously, anticipation building."

    $ outcome = renpy.random.choice([True, False])

    if outcome:
        $ money += 500
        player "I can't believe it! I just won {color=#85bb65}$500{/color}!"
    else:
        player "No luck this time. It was worth a shot, though."

    "You continue working throughout the day, ready for whatever comes your way."

    return
