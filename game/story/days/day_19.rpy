label day_19:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    play sound ring

    "You’re reviewing your reports when you receive a call."

    player "Hello?"

    company "Good day,{w=.1} [player_name]."
    company "I’m here on behalf of a large corporation that’s taken notice of your success in the scales industry."

    player "What can I do for you?"

    company "We have a promising offer for you."
    company "We’d like to acquire 40%% of your business for a cool $10,000."
    company "It’s a win-win situation.{w=.3} An infusion of capital for you,{w=.1} and a strategic partnership for us."

    player "{alpha=0.7}(thinking){/alpha} {i}40%% of my company?{w=.3} That’s a huge chunk..."

    company "Of course,{w=.2} this is a limited-time offer."
    company "If you accept,{w=.2} we can wire the funds immediately."
    company "But,{w=.1} naturally,{w=.1} you’ll have to relinquish some control over your business."

    show mentor
    with dissolve

    mentor thinking "So,{w=.1} they want equity{w=.1}, but $10,000 is a lot of money."

    menu:
        "What will you do?"

        "Accept the offer ({color=#85bb65}+$10,000{/color}, -40%% equity).":
            $ equity -= 40
            $ money += 10000

            player "It’s a tough decision{w=.1}, but I could use the cash injection."
            player "Ok,{w=.1} I’ll accept the offer."

            company "Excellent decision,{w=.1} [player_name]."
            company "The funds will be transferred right away."
            company "Welcome to a new partnership."

            "You’ve sold 40%% of your company for $10,000."
            "However,{w=.1} with reduced equity,{w=.1} your control over the business has weakened."
            "Keep an eye on this corporation—{w=.3}they might have their sights on more than just a partnership."

        "Decline the offer.":
            player "I appreciate the offer,{w=.1} but I’m not comfortable giving up that much control of my company."

            company "It’s a shame,{w=.1} but I respect your decision."
            company "If you decide to change your mind,{w=.1} feel free to reach out."

            "You’ve decided to keep full control of your company,{w=.1} avoiding the risk of corporate interference."

        "Negotiate for a smaller percentage ({color=#85bb65}+$5,000{/color}, -20%% equity)." if charisma > 25:
            player "How about we compromise?"
            player "I’ll sell you 20%% of my company for $5,000 instead."

            company "Hmm,{w=.2} interesting."
            company "We’ll accept those terms and move forward with the smaller deal."

            $ equity -= 20
            $ money += 5000

            "You’ve successfully negotiated a smaller deal,{w=.1} selling 20%% of your company for $5,000."
            "It’s less risky,{w=.1} but still,{w=.1} you’ve given up a part of your business."

    hide mentor
    with dissolve

    "After the meeting,{w=.1} you reflect on your choice,{w=.1} knowing that the decisions you make now will shape the future of your company."

    return
