label day_14:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "As you’re reviewing your sales reports, you notice something unexpected."

    player "Wait... these numbers can’t be right."

    show mentor smile2
    with dissolve

    mentor "Surprising, isn’t it? One of your marketing campaigns went viral overnight. Your sales have surged!"

    player "That explains it. I’ve just earned {color=#85bb65}$4,000{/color} in a single day!"

    $ money += 4000

    player "You must be enjoying that 20%% equity I gave you."

    mentor giveup "Yes I am, [player_name]. Yes I am."

    hide mentor with dissolve

    "With an extra $4,000 in your account, your confidence is boosted. Onward and upward."

    return
