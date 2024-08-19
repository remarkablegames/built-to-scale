label day_19:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "You had to do product recall due to defects found in your scales."

    "This means you have to refund several customers today."

    $ money -= renpy.random.randint(500, 1000)

    return
