label day_19:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    play sound ring

    "You’re reviewing your reports when you receive a call."

    player "Hello?"

    company "Good day, [player_name].{w=0.3} I’m here on behalf of a large corporation that’s taken notice of your success in the scales industry."

    player "What can I do for you?"

    company "We have a promising offer for you."
    company "We’d like to acquire 40%% of your business for a cool $10,000."
    company "It’s a win-win situation.{w=0.3} An infusion of capital for you, and a strategic partnership for us."

    player "{alpha=0.7}(thinking){/alpha} {i}40%% of my company?{w=0.3} That’s a huge chunk...{/i}"

    company "Of course, this is a limited-time offer."
    company "If you accept, we can wire the funds immediately."
    company "But, naturally, you’ll have to relinquish some control over your business."

    show mentor
    with dissolve

    mentor thinking "So, they want equity, but $10,000 is a lot of money."

    menu:
        "What will you do?"

        "Accept the offer ({color=#85bb65}+$10,000{/color}, -40%% equity).":
            $ equity -= 40
            $ money += 10000

            player "It’s a tough decision, but I could use the cash injection. I’ll accept the offer."

            company "Excellent decision, [player_name]."
            company "The funds will be transferred right away. Welcome to a new partnership."

            "You’ve sold 40%% of your company for $10,000."
            "However, with reduced equity, your control over the business has weakened."
            "Keep an eye on this corporation—they might have their sights on more than just a partnership."

        "Decline the offer.":
            player "I appreciate the offer, but I’m not comfortable giving up that much control of my company."

            company "It’s a shame, but I respect your decision."
            company "If you decide to change your mind, feel free to reach out."

            "You’ve decided to keep full control of your company, avoiding the risk of corporate interference."

        "Negotiate for a smaller percentage ({color=#85bb65}+$5,000{/color}, -20%% equity)." if charisma > 25:
            player "How about we compromise? I’ll sell you 20%% of my company for $5,000 instead."

            company "Hmm, interesting. That’s acceptable. We’ll move forward with the smaller deal."

            $ equity -= 20
            $ money += 5000

            "You’ve successfully negotiated a smaller deal, selling 20%% of your company for $5,000."
            "It’s less risky, but still, you’ve given up a part of your business."

    hide mentor
    with dissolve

    "After the meeting, you reflect on your choice, knowing that the decisions you make now will shape the future of your company."

    return
