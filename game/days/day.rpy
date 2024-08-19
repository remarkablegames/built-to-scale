label day_start:

    $ current_day = 30 - days + 1

    if current_day == 1:
        call day_01
    elif current_day == 3:
        call day_03
    elif current_day == 4:
        call day_04
    elif current_day == 5:
        call day_05
    elif current_day == 6:
        call day_06
    elif current_day == 7:
        call day_07
    elif current_day == 8:
        call day_08
    elif current_day == 9:
        call day_09
    elif current_day == 10:
        call day_10

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

    if days <= 0:
        jump day_30

    jump day_start
