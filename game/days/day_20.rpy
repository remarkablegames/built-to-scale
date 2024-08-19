label day_20:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "Your scales started selling like hotcakes due to organic word-of-mouth today."

    "Sales are looking great!"

    $ money += renpy.random.randint(250, 750)

    return
