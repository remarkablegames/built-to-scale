init python:
    import random

label day_08:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    "Your phone buzzes with a notification. It's an email from a company you've never heard of before."

    "Dear [player_name],"

    "We've been monitoring your progress in the scales industry, and we're impressed with what you've accomplished so far."

    "Our company believes that by combining our resources and your innovative approach, we could revolutionize the market together."

    "This partnership could take your business to the next level. We'd handle the distribution, while you focus on expanding your brand and developing new products."

    "Are you interested in joining forces with us?"

    show mentor at center
    with dissolve

    mentor "This could be a big opportunity, but there's always a risk when it comes to partnerships. What would you like to do?"

    menu:
        "Yes, partner with the company.":

            $ outcome = random.choice(["success", "failure"])

            if outcome == "success":
                $ money += 200
                player "This could be the boost I need to take my business to the next level. Let's go for it."
                "You sign the partnership agreement, and the collaboration pays off. Their resources boost your business, and you earn $200 from the partnership!"

            else:
                if money >= 70:
                    $ money -= 70
                    player "This could be the boost I need to take my business to the next level. Let's go for it."
                    "Unfortunately, the partnership doesn't go as planned. Their resources fall short, and you experience delays and financial losses. You lose $70 in the process."
                else:
                    $ money = 0
                    player "This could be the boost I need to take my business to the next level. Let's go for it."
                    "The partnership failed, but you didn't have enough money to lose the full $70. Your money is now at $0."

        "No, I'd rather remain independent.":
            player "I appreciate the offer, but I believe it's best for me to stay independent for now."
            "You politely decline the partnership offer. Staying independent means more control, but you'll miss out on their resources for now."
            
    hide mentor with dissolve        

    return
