label day_06:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "Your phone rings unexpectedly. The caller ID is blocked."

    player "Hello?"

    "Good day, [player_name]. I'm calling on behalf of a group of investors. We’ve been watching your progress, and we’re impressed."

    player "Who is this?"

    "Who I am is not important. What matters is the opportunity I am offering."
    
    "We’re willing to invest $1,500 into your company immediately. However, in return, we require 20%% ownership of your business for the next 10 days."

    player "And what happens after 10 days?"

    "You will regain full control, but until then, your profits will be reduced by 20%%."
    
    "The decision is yours. A small price to pay for such a boost, wouldn’t you agree?"

    menu:
        "Accept the investment.":
            $ money += 1500
            $ equity -= 20
            $ profit_reduction_days = 10
            $ profit_reduction = 0.8

            player "I could use the cash to expand. Let's do it."
            "The money has been transferred. Remember, your profits will be reduced by 20%% for the next 10 days, and your equity has decreased."  # Fixed the percentage

        "Decline the offer.":
            player "I’m not comfortable giving up control of my company, even for a short period. I’ll have to decline."
            "Suit yourself. Remember, opportunities like this don’t come often. Best of luck with your venture."

    "The call ends. You've made your decision, but what impact will it have on your business?"

    return
