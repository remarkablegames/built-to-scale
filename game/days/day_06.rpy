label day_06:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    play sound ring

    "Your phone rings unexpectedly."

    player "Hello?"

    mentor "Good day, [player_name].{w=0.3} It’s Jasper."
    mentor "I’ve been watching your progress, and I’m impressed."

    player "Thanks, I appreciate it."
    
    mentor "I’m willing to invest $1,500 into your company immediately."
    
    mentor "However, in return, I request 20%% ownership of your business for the next 10 days."

    player "And what happens after 10 days?"

    mentor "You will regain full control,{w=0.2} but until then, your profits will be reduced by 20%%."

    mentor "The decision is yours.{w=0.3} A small price to pay for such a boost, wouldn’t you agree?"

    menu:
        "Accept the investment.":
            $ money += 1500
            $ equity -= 20
            $ profit_reduction_days = 10
            $ profit_reduction = 0.8

            player "I could use the cash to expand. Let’s do it."
            mentor "The money has been transferred. Remember, your profits will be reduced by 20%% for the next 10 days, and your equity has decreased."

        "Decline the offer.":
            player "I’m not comfortable giving up control of my company, even for a short period. I’ll have to decline."
            mentor "That’s fine. Remember, opportunities like this don’t come often. Best of luck with your venture."

    "The call ends. You’ve made your decision, but what impact will it have on your business?"

    return
