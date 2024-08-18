label day_start:

    $ current_day = 30 - days + 1

    if current_day == 1:
        call day_01

    jump activities

label day_end:

    if days <= 0:
        jump day_30

    jump day_start
