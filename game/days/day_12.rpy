label day_12:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg room morning
    with fade

    show friend
    with dissolve

    friend "Hey, [player_name], do you have a minute?"

    player "Sure, what’s up?"

    friend "I’m a bit short on cash at the moment and I know you’re doing pretty well right now."

    friend "I’ll be blunt—{w=0.3}do you have a job for me?"

    player "Uh{w=0.1}.{w=0.1}.{w=0.1}.{w=0.3} I don’t have any specific roles yet."

    player "However, I could use a hand delivering some scales to the office. How does that sound?"

    friend confident3 "Works for me. How much does it pay for the day?"

    menu:
            "It pays $250. Does that work? ({color=#85bb65}-$250{/color})":
                if money >= 250:
                    $ money -= 250
                    friend "Sounds great. Thanks, [player_name]!"
                    "After [friend.name] completed his job, you saw your sales increase for the day."
                    $ money += 500
                else:
                    player "Oh no, I forgot... I actually don’t have the funds right now. Sorry, [friend.name]!"

            "Actually, now isn’t the best time.":
                player "I’m not certain if I need any help right now."
                player "I’ll have to pass."
                friend shut "That’s not cool, [player_name], you got my hopes up."
                "You anger [friend.name],{w=0.2} but remember that part of doing business means you can’t please everyone."

    return  
