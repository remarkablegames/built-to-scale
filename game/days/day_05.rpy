init python:
    import random

label day_05:

    scene bg office
    with fade

    show mentor at center
    with dissolve

    mentor "Listen, I have an offer from a company. It's risky but promising. Would you like to invest $100?"

    menu:
        "Yes, invest $100.":
            if money >= 100:
                $ money -= 100
                mentor "Great! I'll let you know how it goes."

                $ outcome = random.choice(["success", "failure"])

                if outcome == "success":
                    $ money += 250
                    mentor "Good news! The investment paid off. You earned $250!"
                else:
                    if money >= 50:
                        $ money -= 50
                        mentor "Unfortunately, the investment didn't go as planned, and you lost an additional $50."
                    else:
                        $ money = 0
                        mentor "The investment failed, but you don't have enough money to lose the full $50."

            else:
                mentor "You don't have enough money to invest."

        "No, I'd rather not.":
            mentor "No worries. It's always good to be cautious."

    hide mentor with dissolve
    
    return
