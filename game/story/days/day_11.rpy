label day_11:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "You receive an email from one of your key suppliers."

    supplier "We’re offering a limited-time discount on bulk materials,{w=.1} but you’ll need to make a large upfront purchase."

    player "A discount?{w=.2} This could help reduce my costs in the short term,{w=.1} but it’s a big investment."

    show mentor
    with dissolve

    mentor "If you purchase the materials now,{w=.1} you’ll secure a lower price,{w=.1} which could boost your profits."
    mentor "However,{w=.1} if you pass on this,{w=.1} the prices might go up and your margins could shrink."

    menu:
        "What do you want to do?"

        "Purchase bulk materials ({color=#85bb65}-$2,000{/color}).":
            if money >= 2000:
                $ money -= 2000
                $ profit_boost_days = 5
                $ profit_boost = 1.2

                player "I’ll take the gamble."
                player "Let’s buy the materials in bulk and hope it pays off."
                mentor "Good call.{w=.3} With lower material costs,{w=.1} your profits will see a boost over the next few days."
                "You spend $2,000 on bulk materials."
                "Your profits will increase by 20%% for the next 5 days due to reduced costs."

            else:
                "You don’t have enough money to make the bulk purchase."

        "Pass on the deal.":
            player "I can’t take the risk right now."
            player "I’ll hold off on the bulk purchase."
            mentor "Fair enough,{w=.1} but be prepared for potential price increases later."

            "You decide to pass on the deal,{w=.1} opting to avoid the upfront cost but potentially facing higher prices in the future."

    return
