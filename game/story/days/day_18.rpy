label day_18:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    play sound knock

    "As you’re working late into the night, your door swings open."
    "It’s [competitor.name]."

    player "{alpha=0.7}(thinking){/alpha} {i}What is it now?{/i}"

    show competitor comeon
    with dissolve

    competitor naruhodo "Evening, [player_name]. I’ve got a little proposition for you."

    player "[competitor.name], if this is another one of your games..."

    competitor mock2 "Oh, it is, but this one could make or break you."
    competitor naruhodo "I’ve just secured a deal with a huge supplier, but they’re willing to work with either one of us."
    competitor "I could let you have it—if you beat me in a sales challenge."

    player "{alpha=0.7}(thinking){/alpha} {i}A challenge...{/i}"

    competitor think talking "The terms are simple."
    competitor talking "First, whoever makes the most sales in the next 48 hours gets the supplier."
    competitor comeon "Second, the loser gives the winner $5,000. Are you in?"

    if money >= 5000:
        menu:
            "Will you accept the bet?"

            "Accept the challenge.":
                $ outcome = renpy.random.choice([True, False])

                if outcome:
                    $ money += 5000
                    $ profit_boost_days = 4
                    $ profit_boost = 1.5
                    player "Bring it on, [competitor.name]. I’ll take that deal."

                    competitor mad "We’ll see who’s laughing at the end of this."

                    hide competitor with dissolve
                    
                    "You work tirelessly over the next 48 hours, and your efforts pay off."
                    "You beat [competitor.name], securing the deal and increasing your profits by 50%% for the next 3 days."

                else:
                    $ money -= 5000
                    player "I’ll take your challenge, [competitor.name]. Let’s see who comes out on top."

                    competitor comeon "I hope you enjoy losing money, because you’re about to get burned."

                    hide competitor with dissolve

                    "Despite your efforts, [competitor.name] outmaneuvers you, and you lose the challenge — and $5,000 in the process."

            "Decline the challenge.":
                player "I’m not falling for your tricks, [competitor.name]. I’ll build my own path."

                competitor tired "Coward. But I expected as much from someone like you."
                competitor "Enjoy watching me succeed while you stay stuck in the trenches."

                "You refuse the challenge, choosing stability over risk, but [competitor.name]’s words linger in your mind."
    else:
        player "I don’t have $5,000 right now. I can’t accept your challenge."

        competitor mock2 "How unfortunate for you. Well, when you’re ready to play with the big leagues, come find me."
        "You missed out on [competitor.name]’s challenge, but perhaps it was for the best."

    hide competitor with dissolve
    "With the conversation over, you reflect on your decision and prepare for the days ahead."

    return
