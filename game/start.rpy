label start:
    play music lofi_intro fadein 1.2

    "I see my psychology teacher walking up to me..."

    scene bg school hallway
    with fade

    show teacher at scale(0.6), center
    with dissolve

    queue music lofi_verse

    teacher "Hi there!{w=0.2} What’s your name?"

    python:
        player_name = renpy.input("My name is...", length=32)
        player_name = player_name.strip() or "Player"

    teacher smile "Nice to meet you, [player_name]!"

    teacher "How old are you?"

    $ player_age = int(renpy.input("My age is...", length=3, allow="0123456789") or 0)

    if player_age < 18:
        teacher annoyed "You must be 18 years or older to attend Pysch 101."

        return

    teacher "Welcome to Pysch 101!"

    jump before_class_1