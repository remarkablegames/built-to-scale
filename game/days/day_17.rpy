label day_17:

    scene bg office
    with fade

    "As you’re winding down for the day, your phone rings. It’s an unfamiliar number."

    player "Hello?"

    "Hi, [player_name]. My name is Jordan. I’m a representative of one of the largest retail chains in the country."

    player "{i}The biggest chain? What do they want with me?{/i}"

    "We’ve been monitoring your progress in the scales industry, and we think your product has potential to hit the mainstream market."

    player "Go on..."

    "We’d like to offer you a distribution deal. We’ll carry your scales in our stores across the country. But there’s a catch—once we take on your product, you’ll need to cut your prices by 30%%. We can start moving your product as soon as you agree."

    show mentor smile2 at right
    with dissolve

    mentor "This is interesting! So, what will you do?"

    menu:
        "Accept the offer (Profits reduced by 30%% for the next 4 days).":
            $ profit_reduction_days = 4
            $ profit_reduction = 0.7
            player "This could open up a massive new market. Let’s do it."
            "Great choice, [player_name]. I’ll have the contract sent over. Welcome to the big leagues."
            "You sign the distribution deal, hoping the volume makes up for the reduced profit margins."

        "Decline the offer.":
            player "I can’t afford to cut my prices that much, even for a big chain. I’ll have to pass."
            "That’s unfortunate, but I understand. Best of luck with your business."
            "You hang up the phone, wondering if you’ve passed up a huge opportunity—or dodged a bullet."
    
    hide competitor with dissolve

    "The day ends. You're surprised at the amount of attention your business is gaining."

    return
