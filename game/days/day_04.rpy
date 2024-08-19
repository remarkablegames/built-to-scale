label day_04:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "You receive an urgent email from one of your suppliers."

    "I'm afraid we've encountered some issues with the shipment of your scales. There's a delay, and it's going to affect your production."

    player "How long will the delay be?"

    "If we expedite the shipment, it will cost an additional $100. Otherwise, it could take a few days to sort out, and you may see a dip in sales."

    menu:
        "Pay $100 to expedite the shipment.":
            if money >= 100:
                $ money -= 100
                player "I can't afford a slowdown in production. Expedite the shipment."
                "Understood. We’ll ensure your products arrive on time."
            else:
                "You don't have enough money to cover the expedited shipping cost."

        "Wait for the shipment.":
            $ energy -= 50
            player "I'll wait it out. Hopefully, it won't impact my sales too much."
            "Understood. We'll do our best to get things moving as soon as possible."

    "The email leaves you with a difficult decision, but you've made your choice. Now you wait to see what happens."

    return
