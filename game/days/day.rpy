label day_start:

    $ current_day = 30 - days + 1

    if current_day == 1:
        call day_01
    elif current_day == 3:
        call day_03
    elif current_day == 5:
        call day_05
    elif current_day == 8:
        call day_08

    jump activities

label day_end:

    if days <= 0:
        jump day_30

    jump day_start
