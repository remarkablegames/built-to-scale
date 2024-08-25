label day_14:

    stop music fadeout 1
    queue music electro_1 fadein 1

    scene bg office
    with fade

    "As you’re reviewing your sales reports, you notice something strange."

    player "Wait...{w=0.3} these numbers can’t be right."

    show mentor smile2
    with dissolve

    mentor "Surprising, isn’t it?{w=0.3} One of your marketing campaigns went viral overnight.{w=0.3} Your sales have surged!"

    player "That explains it!{w=0.3} I’ve just earned {color=#85bb65}$4,000{/color} in a single day!"

    $ money += 4000

    if equity != 100:
        player "You must be enjoying that [100 - equity]%% equity I gave you."
    else:
        player "You must be enjoying the fruits of our labor."

    mentor giveup "Yes I am,{w=0.1} yes I am."

    hide mentor with dissolve

    "With an extra $4,000 in your account, your confidence is boosted. Onward and upward."

    return
