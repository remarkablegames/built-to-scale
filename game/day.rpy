label day_start:

    if days == 30:
        call day_1

    jump activities

label day_end:

    jump day_start
