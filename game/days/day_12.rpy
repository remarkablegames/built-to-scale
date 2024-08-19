label day_12:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg room morning light off
    with fade

    show friend
    with dissolve

    friend "Hey, [player_name], do you have a minute to chat?"

    player "Sure, [friend.name]. What’s up?"

    friend "I’m a bit short on cash at the moment and I know you’re doing pretty well right now."

    friend "I’ll be blunt - do you have a job for me?"

    player "Umm... I don’t have any specific roles yet."

    player "However, I could use a hand delivering some scales to the office. How does that sound?"

    friend confident3 "Works for me. How much does it pay for the day?"

    menu:
            "It pays $250. Does that work?":
                if money >= 250:
                    $ money -= 250
                    friend "Sounds great. Thanks, [player_name]!"
                    "After [friend.name] completed his job, you saw your sales increase for the day."
                    $ money += 500
                else:
                    player "Oh no, I forgot... I actually don’t have the funds right now. Sorry, [friend.name]!"

            "Actually, now isn’t the best time.":
                player "I am not certain yet if I need any help. I’ll have to pass right now."
                friend shut "That’s not cool, [player_name], you got my hopes up."
                "You anger [friend.name], but then remember that part of being in business means you can’t please everyone."

    return  
