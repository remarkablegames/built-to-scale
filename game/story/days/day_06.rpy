label day_06:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    play sound ring

    "Your phone rings unexpectedly."

    player "Hello?"

    mentor "Good day, [player_name].{w=.2} It’s [mentor.name]."
    mentor "I’ve been watching your progress,{w=.1} and I’m impressed."

    player "Thanks,{w=.1} I appreciate it."

    mentor "I’m willing to invest $1,500 in your company."

    mentor "However,{w=.1} in return,{w=.1} I request 20%% ownership of your business for the next 10 days."

    player "And what happens after 10 days?"

    mentor "You’ll regain full control,{w=.2} but until then, your profits will be reduced by 20%%."

    mentor "The decision is yours.{w=.3} A small price to pay for such a boost, wouldn’t you agree?"

    menu:
        "What will you do?"

        "Accept the investment ({color=#85bb65}+$1,500{/color}, -20%% equity).":
            play sound kaching

            $ accepted_mentor_investment = True
            $ money += 1500
            $ equity -= 20
            $ profit_reduction_days = 10
            $ profit_reduction = 0.8

            player "I could use the cash to expand."
            player "Let’s do it."
            mentor "The money has been transferred."
            mentor "Remember,{w=.1} your profits will be reduced by 20%% for the next 10 days,{w=.1} and your equity has decreased."

        "Decline the offer.":
            player "I’m not comfortable giving up control of my company,{w=.1} even for a short period."
            player "I’ll have to decline."
            mentor "That’s fine."
            mentor "Remember,{w=.1} opportunities like this don’t come often."
            mentor "Best of luck with your venture."

    "The call ends.{w=.3} You’ve made your decision,{w=.1} but what impact will it have on your business?"

    return
