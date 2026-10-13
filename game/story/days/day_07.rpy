label day_07:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "You receive a troubling notification{w=.3}—a competitor has started spreading negative rumors about your business."

    player "This has to be [competitor.name].{w=.3} Why is she doing this?"

    "The rumors are quickly spreading,{w=.1} and it’s affecting your brand’s reputation."
    "You need to act fast."

    show mentor
    with dissolve

    mentor "This is bad."
    mentor "You could hire a PR firm to control the damage,{w=.2} but it will cost $500."
    mentor "Or,{w=.1} you could try to weather the storm and hope it blows over."

    menu:
        "Hire a PR firm ({color=#85bb65}-$500{/color}).":
            if money >= 500:
                $ money -= 500
                player "I can’t afford to let this damage my reputation."
                player "Let’s hire the PR firm."
                mentor "Good decision."
                mentor "The PR firm will work quickly to clear your name,{w=.1} and your sales should remain steady."
                "You spend $500, but your reputation remains intact and your sales are unaffected."
            else:
                "You don’t have enough money to hire the PR firm."

        "Ignore the rumors (-30%% profit for 3 days).":
            $ profit_reduction_days = 3
            $ profit_reduction = 0.7
            
            player "I can’t afford the PR firm right now."
            player "I’ll just have to hope the rumors blow over soon."
            mentor "It’s risky,{w=.1} but it might save you some money."
            mentor "Let’s hope the damage isn’t too severe."
            "You decide to ignore the rumors.{w=.3} Unfortunately,{w=.1} this will affect your sales for the next few days."

    return
