label day_20:

    stop music fadeout 1

    scene bg office
    with fade

    "As you sit in your office,{w=.1} lost in thought about your business and the future,{w=.1} [mentor.name] enters with a serious expression on his face."

    queue music orchestral_waltz

    show mentor thinking
    with dissolve

    mentor thinking "Hey,{w=.1} [player_name],{w=.1} I’ve been thinking a lot about your situation."
    mentor thinking "You’ve come far,{w=.1} but I think there’s one final move we can make."

    player "What do you mean,{w=.1} [mentor.name]?"

    if equity < 100:
        show mentor

        mentor "I know you’ve lost some equity along the way." 
        mentor "I made some calls and used my connections." 
        player "I’m all ears..."
        mentor "I can get your lost equity back to 100%%,{w=.1} but there’s a catch."
        mentor "You’ll need to pay me $10,000."
        mentor "It’s steep,{w=.1} but this could give you back full control of your business."

    else:
        show mentor

        mentor "You’ve done well to maintain full control of your company so far,{w=.1} but here’s what I’m offering..."
        mentor "I’m willing to buy 51%% of the company from you right now."
        mentor "In exchange, I’ll give you $25,000."
        mentor "You’ll have the cash to secure your future,{w=.1} but you’ll be giving up majority control of the business."
        mentor "What do you say?"

    menu:
        "What will you do?"

        "Accept [mentor.name]’s offer." if equity < 100 and money >= 10000:
            $ money -= 10000
            $ equity = 100

            player "Alright,{w=.1} [mentor.name] I’ll pay the $10,000."
            player "Getting full control of the company is worth it."

            show mentor smile

            mentor "Good choice,{w=.1} [player_name]."
            mentor "You’ve regained full control.{w=3} Now, let’s push forward and secure your future."

            "You’ve paid [mentor.name] $10,000,{w=.1} but you’ve regained 100%% equity in your business."
            "It’s a relief to have full control again."

        "Sell 51%% equity to [mentor.name] for $25,000." if equity >= 51:
            $ money += 25000
            $ equity -= 51

            player "I could use the money.{w=.2} Let’s do it."

            show mentor smile

            mentor "You’ve made the right decision.{w=.3} I’ll transfer the funds immediately."
            mentor "Just remember,{w=.2} you’re no longer the sole owner of the company."

            "[mentor.name] has purchased 51%% of your business for $25,000."
            "You’ve gained a significant amount of cash, but lost majority control."

        "Decline [mentor.name]’s offer.":
            player "I can’t afford to lose control of the company,{w=.2} and I don’t have the funds for the equity."
            player "I’ll have to pass, [mentor.name]."

            show mentor thinking

            mentor "I understand,{w=.1} [player_name]."
            mentor "It’s a tough decision,{w=.1} but I respect your choice."
            mentor "Just remember,{w=.1} the road ahead won’t be easy."

            "You’ve decided to retain control of the company,{w=.1} but you know that the future will be difficult without [mentor.name]’s additional support."

    hide mentor 
    with dissolve

    "The conversation with [mentor.name] leaves you deep in thought." 
    "Whatever choice you made,{w=.1} the future of your business hangs in the balance."

    return
