label day_16:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg bus stop morning
    with fade

    if accepted_mentor_investment:
        "The 10-day period following [mentor.name]’s investment has ended,{w=.1} and the 20%% equity stake has been reinstated."
        $ equity += 20

    "As you’re walking down the street,{w=.1} you spot something on the ground."

    player "{cps=10}Is that...{/cps}{w=.3} a lotto ticket?"

    "You pick it up and examine it."
    "It’s unscratched,{w=.1} a potential stroke of luck."

    player "Well,{w=.1} I guess there’s only one way to find out if today is my lucky day."

    "You scratch the ticket nervously,{w=.1} anticipation building."

    $ outcome = renpy.random.choice([True, False])

    if outcome:
        $ money += 500
        player "I can’t believe it!"
        player "I just won {color=#85bb65}$500{/color}!"
    else:
        player "No luck this time."
        player "It was worth a shot,{w=.1} though."

    "You continue working through the day,{w=.1} ready for whatever comes your way."

    return
