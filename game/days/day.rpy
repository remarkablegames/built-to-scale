label day_start:

    $ today = 30 - days + 1

    if today == 1:
        call day_01
    elif today == 2:
        call day_02
    elif today == 3:
        call day_03
    elif today == 4:
        call day_04
    elif today == 5:
        call day_05
    elif today == 6:
        call day_06
    elif today == 7:
        call day_07
    elif today == 8:
        call day_08
    elif today == 9:
        call day_09
    elif today == 10:
        call day_10
    elif today == 11:
        call day_11
    elif today == 12:
        call day_12
    elif today == 13:
        call day_13
    elif today == 14:
        call day_14
    elif today == 15:
        call day_15
    elif today == 16:
        call day_16
    elif today == 17:
        call day_17
    elif today == 18:
        call day_18
    elif today == 19:
        call day_19
    elif today == 20:
        call day_20
    elif today == 21:
        call day_21
    elif today == 22:
        call day_22
    elif today == 23:
        call day_23
    elif today == 24:
        call day_24
    elif today == 25:
        call day_25
    elif today == 26:
        call day_26
    elif today == 27:
        call day_27
    elif today == 28:
        call day_28
    elif today == 29:
        call day_29
    elif today == 30:
        call day_30

    stop music fadeout 1
    queue music electro_2c fadein 1
    queue music electro_2d
    queue music [electro_2e, electro_2f]

    jump activities

label day_end:

    if profit_reduction_days > 0:
        $ profit_reduction_days -= 1

        if profit_reduction_days == 0:
            $ profit_reduction = 1.0
            "Your temporary ownership deal has expired, and your profits have returned to normal."

    if profit_boost_days > 0:
        $ profit_boost_days -= 1

        if profit_boost_days == 0:
            $ profit_boost = 1.0
            "The bulk material discount period has ended, and your profits have returned to normal."

    if days <= 0:
        jump day_30

    jump day_start
