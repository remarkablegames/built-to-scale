label day_18:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    play sound knock

    "As you’re working late into the night,{w=.1} your door swings open."
    "It’s [competitor.name]."

    show competitor comeon
    with dissolve

    player "{alpha=0.7}(thinking){/alpha} {i}What is it now?"

    competitor naruhodo "Evening,{w=.1} [player_name].{w=.3} I’ve got a little proposition for you."

    player "[competitor.name],{w=.1} if this is another one of your games..."

    competitor mock2 "Oh,{w=.1} it is,{w=.1} but this one could make or break you."
    competitor naruhodo "I’ve just secured a deal with a huge supplier,{w=.1} but they’re willing to work with either one of us."
    competitor "I could let you have it—{w=.2}if you beat me in a sales challenge."

    player "{alpha=0.7}(thinking){/alpha} {i}A challenge..."

    competitor think talking "The terms are simple."
    competitor talking "First,{w=.1} whoever makes the most sales in the next 48 hours gets the supplier."
    competitor comeon "Second,{w=.1} the loser gives the winner $5,000."
    competitor "Are you in?"

    if money >= 5000:
        menu:
            "Will you accept the bet?"

            "Accept the challenge.":
                $ outcome = renpy.random.choice([True, False])

                if outcome:
                    $ money += 5000
                    $ profit_boost_days = 4
                    $ profit_boost = 1.5
                    player "Bring it on,{w=.1} [competitor.name].{w=.3} I’ll take that deal."

                    competitor mad "We’ll see who’s laughing at the end of this."

                    hide competitor with dissolve
                    
                    "You work tirelessly over the next 48 hours,{w=.1} and your efforts pay off."
                    "You beat [competitor.name],{w=.1} securing the deal and increasing your profits by 50%% for the next 3 days."

                else:
                    $ money -= 5000
                    player "I’ll take your challenge,{w=.1} [competitor.name]."
                    player "Let’s see who comes out on top."

                    competitor comeon "I hope you enjoy losing money,{w=.1} because you’re about to get burned."

                    hide competitor with dissolve

                    "Despite your efforts,{w=.1} [competitor.name] outmaneuvers you,{w=.1} and you lose the challenge—{w=.3}and $5,000 in the process."

            "Decline the challenge.":
                player "I’m not falling for your tricks,{w=.1} [competitor.name].{w=.3} I’ll build my own path."

                competitor tired "Coward.{w=.2} But I expected as much from someone like you."
                competitor "Enjoy watching me succeed while you stay stuck in the trenches."

                "You refuse the challenge,{w=.1} choosing stability over risk,{w=.1} but [competitor.name]’s words linger in your mind."
    else:
        player "I don’t have $5,000 right now.{w=.3} I can’t accept your challenge."

        competitor mock2 "How unfortunate for you.{w=.3} Well{w=.1} when you’re ready to play with the big leagues,{w=.1} come find me."
        "You missed out on [competitor.name]’s challenge,{w=.1} but perhaps it was for the best."

    hide competitor with dissolve
    "With the conversation over,{w=.1} you reflect on your decision and prepare for the days ahead."

    return
