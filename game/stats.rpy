default energy = 100
default intelligence = 0
default charisma = 0

screen stat(name, amount):
    text "[name]: [amount]"
    bar value AnimatedValue(amount, 100) xalign 0.5 xsize 300

screen stats():
    frame:
        xalign 0 ypos 0
        vbox:
            use stat("Energy", energy)
            null height 15
            use stat("Intelligence", intelligence)
            null height 15
            use stat("Charisma", charisma)

label stats_intro:
    scene bg bus stop morning
    with fade

    show mentor
    with dissolve

    mentor @ thinking "I’m here to guide you as you start this exciting journey."
    mentor @ thinking "Every successful entrepreneur needs more than just business acumen..."
    mentor "You’ll need to focus on three key areas:{w=0.2} {b}Energy{/b}{w=0.2}, {b}Intelligence{/b}{w=0.2}, and {b}Charisma{/b}."

    jump stats_explanation

label stats_explanation:
    show screen stats

    menu:
        mentor "What would you like me to explain?"

        "Energy":
            mentor "Without energy, you won’t have the stamina to make it through the day."
            mentor "Every action you take, from traveling between locations to attending meetings or working out, will require energy."
            mentor "Make sure to keep an eye on this, or you might find yourself running out of steam before the day’s over."

            jump stats_explanation

        "Intelligence":
            mentor "This is going to be crucial when it comes to studying, making smart decisions, and staying ahead of the curve in the business world."
            mentor "You’ll need to work on this if you want to master your craft."

            jump stats_explanation

        "Charisma":
            mentor "Charisma will help you charm your way through social interactions, connect with potential clients, and increase your sales."
            mentor "Whether it’s networking at events or simply getting people to believe in your vision, your charisma is your secret weapon."

            jump stats_explanation

        "Continue":
            jump stats_outro

label stats_outro:

    mentor "Throughout the day,{w=0.1} you’ll be traveling to different locations like the library,{w=0.2} the dorm,{w=0.2} the business office,{w=0.2} the gym,{w=0.2} and even the local shop."
    mentor "Each location offers you a chance to boost a stat in different ways."
    mentor "But remember,{w=0.1} every action will consume your time and energy."

    jump location_explanation

label location_explanation:

    menu:
        mentor "What would you like to know more about?"

        "Library":
            mentor "A place where you can study to increase your intelligence."
            mentor "That's why business smarts are important."

            jump location_explanation

        "Dorm":
            mentor "Your dorm is your home and where you can sit back and relax."
            mentor "You'll be able to sleep here and spend time with your roommate, Riley."

            jump location_explanation

        "Office":
            mentor "This is your office at [business_name]. Here, you're able to sell your product and earn money."
            mentor "The amount of money you earn will depend on various stats; higher intelligence, charisma, and energy, will result in more lucrative deals."

            jump location_explanation
        
        "Gym":
            mentor "You can go to the gym to exercise and increase your charisma. Staying healthy is the best way to maintain a clear mind and body."
            mentor "As a reminder, higher charisma will result in greater sales."

            jump location_explanation

        "Continue":
            jump location_outro

label location_outro:

    mentor "The day will end when you either run out of energy or it’s too late to keep working."
    mentor "Make sure to balance your tasks wisely!"

    mentor "If you find yourself running low on energy,{w=0.1} don’t worry!"
    mentor "You can always grab an energy drink to keep yourself going."
    mentor "And when you earn enough money,{w=0.2} you’ll be able to purchase all sorts of useful items that can help you stay ahead."

    mentor "So are you ready to start?"
    mentor "Remember, success doesn’t just come from hard work,{w=0.2} it comes from working smart, balancing your time, and knowing when to push forward and when to rest."
    mentor smile "You got this!"

    jump day_start
