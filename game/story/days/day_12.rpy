label day_12:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg room morning
    with fade

    show friend
    with dissolve

    friend "Hey,{w=.1} [player_name],{w=.1} do you have a minute?"

    player "Sure,{w=.1} what’s up?"

    friend "I’m a bit short on cash at the moment and I know you’re doing pretty well right now."

    friend "I’ll be blunt—{w=.3}do you have a job for me?"

    player "{cps=10}Uh...{/cps}{w=.3} I don’t have any specific roles yet."

    player "However,{w=.1} I could use a hand delivering some scales to the office."
    player "How does that sound?"

    friend @ confident3 "Works for me.{w=.2} How much does it pay for the day?"

    menu:
            "It pays $250. Does that work? ({color=#85bb65}-$250{/color})":
                if money >= 250:
                    $ money -= 250
                    friend "Sounds great.{w=.2} Thanks,{w=.1} [player_name]!"
                    play sound kaching
                    $ money += 500
                    "After [friend.name] completed his job,{w=.1} you saw your sales increase for the day."
                else:
                    player "Oh no,{w=.1} I forgot...{w=.2} I actually don’t have the funds right now."
                    player "Sorry,{w=.1} [friend.name]!"

            "Actually, now isn’t the best time.":
                player "I’m not certain if I need any help right now."
                player "I’ll have to pass."
                friend shut "That’s not cool,{w=.1} [player_name],{w=.1} you got my hopes up."
                "You anger [friend.name],{w=.2} but remember that part of doing business means you can’t please everyone."

    return  
