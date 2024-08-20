label office:

    scene bg office
    with dissolve

    $ base_sales = 10 + intelligence + charisma
    $ base_marketing = base_sales + int((intelligence + charisma) * 2)

    if profit_reduction_days > 0:
        $ sales = int(base_sales * profit_reduction)
        $ marketing = int(base_marketing * profit_reduction)
    else:
        $ sales = base_sales
        $ marketing = base_marketing

    if profit_boost_days > 0:
        $ sales = int(base_sales * profit_boost)
        $ marketing = int(base_marketing * profit_boost)
    else:
        $ sales = base_sales
        $ marketing = base_marketing

    menu:
        "What do you want to do?"

        "Sales\n{color=#85bb65}Money +[sales]{/color}, {color=#40e0d0}Energy -10{/color}" if energy >= 10:
            $ energy -= 15
            $ money += sales
            $ time += 1

            "You made some sales."

            jump office

        "Marketing\n{color=#85bb65}Money +[marketing]{/color}, {color=#40e0d0}Energy -25{/color}" if energy >= 25:
            $ energy -= 25
            $ money += marketing
            $ time += 2

            "You made more sales."

            jump office

        "Go back":
            jump activities
