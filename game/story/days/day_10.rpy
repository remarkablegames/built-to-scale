label day_10:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    show mentor
    with dissolve

    mentor smile2 "Well done,{w=.2} [player_name]!"
    mentor "You’ve made it to the halfway point."

    player "Thanks,{w=.1} I appeciate it."

    play sound ring

    "You suddenly receive a call."
    "It’s [competitor.name]."

    show mentor at right
    with move

    show competitor comeon
    with dissolve

    competitor "Well,{w=.1} well,{w=.1} well,{w=.1} [player_name]."
    competitor "Did you really think I wouldn’t notice you trying to creep into {i}{b}my{/b}{/i} territory?"

    player "[competitor.name]...{w=.3} what are you doing?"

    competitor mock "What I’m doing is putting you {i}out{/i} of business."
    competitor "You’ve made it this far,{w=.1} but now it’s time for you to step aside."
    competitor "This industry ain’t big enough for both of us."

    show competitor naruhodo

    "[competitor.name] laughs,{w=.1} the sound sending a chill down your spine."

    competitor comeon "By the end of this week,{w=.1} “[business_name]” will be no more,{w=.2} and I’ll be here to pick up the pieces."
    competitor "You can count on it."

    hide competitor 
    with dissolve

    pause 1

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

                    player "I’m not going down without a fight,{w=.1} [competitor.name]."
                    player "Let’s see who comes out on top."

                    hide mentor 
                    with dissolve 

                    show competitor naruhodo
                    with dissolve

                    competitor "Hah!{w=.3} You think you can beat me?"
                    competitor "You’re in for a rude awakening, [player_name]."

                    "Your counterattack is a success!"
                    "[competitor.name]’s business falters,{w=.1} and your profits will increase by 50%% for the next 7 days."

                    competitor verymad "No...{w=.3} this can’t be happening."
                    competitor "You...{w=.2} how did you...?"

                    player "Looks like you underestimated me,{w=.1} [competitor.name]."

                else:
                    $ profit_reduction_days = 7
                    $ profit_reduction = 0.75

                    player "This is risky,{w=.1} but I have to take a chance."

                    hide mentor 
                    with dissolve 

                    show competitor naruhodo
                    with dissolve

                    competitor "A chance?{w=.3} Oh please,{w=.1} you’re just handing me victory on a silver platter."

                    "Unfortunately,{w=.1} the counterattack backfires."
                    "You lose $3,000 and your profits will be reduced by 25%% for the next 7 days."

                    competitor comeon "I told you,{w=.1} [player_name].{w=.3} You never stood a chance against me."
                    competitor "Enjoy watching your little business crumble."

                    player "This isn’t over,{w=.1} [competitor.name]..."

            else:
                "You don’t have enough money to launch the counterattack."

        "Play it safe.":
            player "I can’t afford to take that kind of risk right now."
            player "I’ll focus on keeping my business stable."

            hide mentor
            with dissolve

            show competitor comeon

            competitor "How pathetic.{w=.3} You’re just going to roll over and let me win?"
            competitor "Suit yourself,{w=.1} [player_name]."
            competitor "When this is all over,{w=.1} there will only be one company standing,{w=.1} and it won’t be yours."

            hide competitor
            with dissolve

            show mentor
            with dissolve

            mentor "Sometimes playing it safe is the right call,{w=.1} but remember,{w=.1} [competitor.name] won’t stop coming after you."
            "You decide to play it safe,{w=.1} avoiding confrontation but missing out on a potential opportunity."

    hide competitor with dissolve

    "The call ends,{w=.1} and the tension lingers in the air."
    "You’ve made your decision,{w=.1} but the stakes are higher than ever."

    return
