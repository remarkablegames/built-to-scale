label day_04:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "You receive an urgent email from one of your suppliers."
    "I’m afraid we’ve encountered some issues with the shipment of your scales."
    "There’s a delay, and it’s going to affect your production."

    player "How long will the delay last?"

    "If we expedite the shipment, it will cost an additional $100."
    "Otherwise, it could take a few days to sort out, and you may see a dip in sales."

    menu:
        "Expedite the shipment ({color=#85bb65}-$100{/color}).":
            if money >= 100:
                $ money -= 100

                player "I can’t afford a slowdown in production."
                player "Expedite the shipment."

                "Understood. We’ll ensure your products arrive on time."
            else:
                "You don’t have enough money to cover the expedited shipping cost."

        "Wait for the shipment.":
            $ energy -= 50

            player "I’ll wait it out.{w=0.2} Hopefully, it won’t impact my sales too much."

            "Understood.{w=0.3} We’ll do our best to get things moving as fast as possible."

    "The email leaves you with a difficult decision,{w=0.1} but you’ve made your choice."
    "Now you wait to see what happens."

    return
