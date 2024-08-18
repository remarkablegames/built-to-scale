label actions:

    scene bg living room night
    with fade

    show riley smile at scale(0.9), center
    with dissolve

    player "This is stressful. I know dreams are achievable only through hard work and dedication, but I feel like I don't know where to begin."

    "Your phone buzzes with a notification – an email from a potential supplier."

    player "But as Lao Tzu once said, {i}The journey of a thousand miles begins with one step.{/i}"

    show riley surprised at scale(0.9), center
    with dissolve

    riley "Thinking about your business again?"

    player "Always. It’s all I can think about now. If this works, it could be the start of something big."

    riley "Well, you’ve got the work ethic. I’ve seen you juggle everything before – school, work, family obligations. You’ve got this."

    player "Thanks. I know I’ll need every bit of support I can get."

    riley "Why don't we take a break? Sometimes it's good to clear your head. What do you say – want to study, hit the gym, or head over to the shop?"

    menu:
        "Go to the library to study (+10 Intelligence).":
            $ energy -= 10
            $ intelligence += 10
            player "Studying at the library sounds like a good plan. I could brush up on some knowledge that'll help with the business."

            riley "Sounds good! Expanding your knowledge will definitely help you in the long run."

            jump library

        "Go to the gym to work out (-10 Energy, +10 Charisma).":
            $ energy -= 10
            $ charisma += 10
            player "Working out sounds good. I could use a bit of exercise to clear my mind and boost my energy."

            riley "Great idea! Let's get moving. A good workout can do wonders."

        "Go to the shop (+10 Energy).":
            $ energy += 10
            player "Let's hit the club! I could use some fun and maybe meet new people. Boosting my charisma might help too."

            riley "Awesome! Socializing is a great way to take a break and recharge your social batteries."
        
        "Sell your product at the office (-10 Energy, +10 Charisma).":
            $ energy -= 10
            $ money += 10
            player "I'm going to try to sell my product. Wish me luck!"

            riley "Go for it. You've got this!"
        
        "Go to sleep (Recover Energy).":
            $ energy = 100
            player "Actually, I'm pretty tired, I think I'm going to head to bed. Goodnight!"

            riley "Have a good night. Talk to you tomorrow!"
    
    hide riley with dissolve
    hide player with dissolve

    return
