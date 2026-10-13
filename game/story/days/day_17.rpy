label day_17:

    stop music fadeout 1

    scene bg office
    with fade

    play sound ring

    "Your phone rings as soon as you get in."
    "It’s an unfamiliar number."

    queue music orchestral_waltz

    player "Hello?"

    company "Hi,{w=.1} [player_name].{w=.3} My name is Jordan."
    company "I’m a representative of one of the largest retail chains in the country."

    player "{alpha=0.7}(thinking){/alpha} {i}The biggest chain?{w=.3} What do they want with me?"

    company "We’ve been monitoring your progress in the scales industry."
    company "And we believe your product has the potential to make it in the mainstream market."

    player "Go on..."

    company "We’d like to offer you a distribution deal."

    player "What does it entail?"

    company "We’ll carry your scales in our stores across the country."
    company "But there’s a catch..."

    player "I’m listening..."

    company "Once we take on your product, you’ll need to cut your prices by 30%%."
    company "We can start moving your product as soon as you agree."

    show mentor
    with dissolve

    mentor smile2 "This is interesting!{w=.3} So, what will you do?"

    menu:
        "I will..."

        "Accept the offer (-30%% profits for the next 4 days).":
            $ profit_reduction_days = 4
            $ profit_reduction = 0.7

            player "This could open up a massive new market."
            player "Let’s do it."

            company "Great choice, [player_name]."
            company "I’ll have the contract sent over."
            company "Welcome to the big leagues."

            "You sign the distribution deal,{w=.2} hoping the volume makes up for the reduced profit margins."

        "Decline the offer.":
            player "I can’t afford to cut my prices that much,{w=.1} even for a big chain."
            player "I’ll have to pass."

            company "That’s unfortunate,{w=.1} but I understand."
            company "Best of luck with your business."

            "You hang up the phone,{w=.1} wondering if you’ve passed up a huge opportunity—{w=.2}or dodged a bullet."

    hide competitor with dissolve

    "You’re surprised at the amount of attention your business is gaining."

    return
