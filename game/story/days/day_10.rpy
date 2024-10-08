label day_10:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    show mentor
    with dissolve

    mentor smile2 "Well done, [player_name]!"
    mentor "You’ve made it to the halfway point."

    player "Thanks,{w=0.1} I appeciate it."

    play sound ring

    "You suddenly receive a call."
    "It’s [competitor.name]."

    show mentor at right
    with move

    show competitor comeon
    with dissolve

    competitor "Well,{w=0.1} well,{w=0.1} well,{w=0.1} [player_name].{w=0.3} Did you really think I wouldn’t notice you trying to creep into {i}{b}my{/b}{/i} territory?"
    
    player "[competitor.name]...{w=0.3} what are you doing?"

    show competitor mock

    competitor "What I’m doing is putting you {i}out{/i} of business."
    competitor "You’ve made it this far, but now it’s time for you to step aside."
    competitor "This industry ain’t big enough for both of us."

    show competitor naruhodo

    "[competitor.name] laughs, the sound sending a chill down your spine."

    show competitor comeon

    competitor "By the end of this week,{w=0.1} “[business_name]” will be no more,{w=0.2} and I’ll be here to pick up the pieces."
    competitor "You can count on it."

    hide competitor 
    with dissolve

    pause 1.0

    show mentor at center
    with move

    mentor "I’ve gathered some information about [competitor.name]’s vulnerabilities."
    mentor "You could launch a counterattack, but it’s risky and costly."

    menu:
        "What should you do?"

        "Launch a counterattack ({color=#85bb65}-$3,000{/color}).":
            if money >= 3000:
                $ money -= 3000
                $ outcome = renpy.random.choice([True, False])

                if outcome:
                    $ profit_boost_days = 7
                    $ profit_boost = 1.5

                    player "I’m not going down without a fight, [competitor.name]. Let’s see who comes out on top."

                    hide mentor 
                    with dissolve 

                    show competitor naruhodo
                    with dissolve

                    competitor "Hah! You think you can beat me? You’re in for a rude awakening, [player_name]."

                    "Your counterattack is a success! [competitor.name]’s business falters, and your profits will increase by 50%% for the next 7 days."

                    show competitor argue2

                    competitor "No... this can’t be happening. You... how did you...?"

                    player "Looks like you underestimated me, [competitor.name]."

                else:
                    $ profit_reduction_days = 7
                    $ profit_reduction = 0.75

                    player "This is risky, but I have to take a chance."

                    hide mentor 
                    with dissolve 

                    show competitor naruhodo
                    with dissolve

                    competitor "A chance? Oh please, you’re just handing me victory on a silver platter."

                    "Unfortunately, the counterattack backfires. You lose $3,000 and your profits will be reduced by 25%% for the next 7 days."

                    show competitor comeon

                    competitor "I told you, [player_name]. You never stood a chance against me. Enjoy watching your little business crumble."

                    player "This isn’t over, [competitor.name]..."

            else:
                "You don’t have enough money to launch the counterattack."

        "Play it safe.":
            player "I can’t afford to take that kind of risk right now. I’ll focus on keeping my business stable."

            show competitor comeon

            competitor "How pathetic. You’re just going to roll over and let me win? Suit yourself, [player_name]. When this is all over, there will only be one company standing, and it won’t be yours."

            mentor "Sometimes playing it safe is the right call, but remember, [competitor.name] won’t stop coming after you."
            "You decide to play it safe, avoiding confrontation but missing out on a potential opportunity."

    hide competitor with dissolve

    "The call ends, and the tension lingers in the air."
    "You’ve made your decision, but the stakes are higher than ever."

    return
