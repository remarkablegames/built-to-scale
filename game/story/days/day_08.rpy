label day_08:

    stop music fadeout 1

    scene bg office
    with fade

    play sound buzz

    "Your phone buzzes with a notification."

    queue music orchestral_waltz

    "It’s an email from a company you’ve never heard before."

    company "Dear [player_name],"
    company "We’ve been monitoring your progress in the scales industry,{w=0.2} and we’re impressed with what you’ve accomplished so far."
    company "Our company believes that by combining our resources and your innovative approach,{w=0.2} we could revolutionize the market together."
    company "This partnership could take your business to the next level."
    company "We’d handle the distribution,{w=0.2} while you focus on expanding your brand and developing new products."
    company "Are you interested in joining forces?"

    show mentor
    with dissolve

    mentor "This could be a big opportunity,{w=0.1} but there’s always a risk when it comes to partnerships."

    menu:
        "What are you going to do?"

        "Yes, partner with the company.":
            $ outcome = renpy.random.choice([True, False])

            if outcome:
                $ money += 200

                player "This could be the boost I need to take my business to the next level. Let’s go for it."

                "You sign the partnership agreement, and the collaboration pays off."
                "Their resources boost your business, and you earn $200 from the partnership!"

            else:
                if money >= 70:
                    $ money -= 70

                    player "This could be the boost I need to take my business to the next level. Let’s go for it."

                    "Unfortunately, the partnership doesn’t go as planned. Their resources fall short, and you experience delays and financial losses. You lose $70 in the process."

                else:
                    $ money = 0

                    player "This could be the boost I need to take my business to the next level. Let’s go for it."

                    "The partnership failed, but you didn’t have enough money to lose the full $70. Your money is now at $0."

        "No, I’d rather remain independent.":
            player "I appreciate the offer, but I believe it’s best for me to stay independent for now."

            "You politely decline the partnership offer. Staying independent means more control, but you’ll miss out on their resources for now."

    hide mentor with dissolve        

    return
