label day_09:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "You receive a proposal from the owner of a struggling scales company."

    company "We’re facing financial difficulties and are willing to sell our company to you for a fair price."
    company "This could be a great opportunity for expansion."

    player "Acquiring a company? This could be a big move, but it comes with risks..."

    show mentor
    with dissolve

    mentor "The acquisition could help you grow your business long-term, but you’ll face some short-term challenges."

    menu:
        "What do you want to do?"

        "Acquire the company ({color=#85bb65}-$2,000{/color}).":
            if money >= 2000:
                $ money -= 2000
                $ profit_reduction_days = 5
                $ profit_reduction = 0.85

                player "I think this acquisition will help my business grow in the long run. Let’s do it."
                "You acquire the company for $2,000. However, the integration process causes some disruptions, reducing your profits by 15%% for the next 5 days."
            else:
                "You don’t have enough money to acquire the company."

        "Decline the offer.":
            player "This is too risky for me right now. I’ll have to pass."
            mentor "Sometimes, it’s better to be cautious. Let’s focus on what you have."

            "You decline the offer and decide to focus on growing your existing business."

    return
