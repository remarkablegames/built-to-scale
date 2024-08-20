label day_05:

    stop music fadeout 1

    scene bg office
    with fade

    play sound knock
    "You hear a knock on the door."

    queue music orchestral_waltz

    show mentor
    with dissolve

    mentor "Listen, I have an offer from a company. It’s risky but promising. Would you like to invest $100?"

    menu:
        "Yes, invest $100.":
            if money >= 100:
                $ money -= 100
                mentor "Great! I’ll let you know how it goes."

                hide mentor
                with dissolve

                pause 1.0

                show mentor
                with dissolve

                $ outcome = renpy.random.choice([True, False])

                if outcome:
                    $ money += 250
                    mentor "Good news! The investment paid off. You earned $250!"
                else:
                    if money >= 50:
                        $ money -= 50
                        mentor "Unfortunately, the investment didn’t go as planned, and you lost an additional $50."
                    else:
                        $ money = 0
                        mentor "The investment failed, but you don’t have enough money to lose the full $50."

            else:
                mentor "You don’t have enough money to invest."

        "No, I’d rather not.":
            mentor "No worries. It’s always good to be cautious."

    hide mentor with dissolve
    
    return
