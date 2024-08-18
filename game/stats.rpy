default energy = 100
default intelligence = 0
default charisma = 0

screen stat(name, amount):
    text name xalign 0.5
    bar value StaticValue(amount, 100) xalign 0.5 xsize 250

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
    scene bg meadow
    with fade

    show angel at scale(0.6), center
    with dissolve

    angel talking "I’m here to guide you as you start this exciting journey."
    angel "Every successful entrepreneur needs more than just business acumen..."
    angel "You’ll need to focus on three key areas:{w=0.2} {b}Energy{/b}{w=0.2}, {b}Intelligence{/b}{w=0.2}, and {b}Charisma{/b}."

    jump stats_explanation

label stats_explanation:
    show screen stats

    menu:
        angel "What do you want to learn more about?"

        "Energy":
            angel "Without energy, you won’t have the stamina to make it through the day."
            angel "Every action you take, from traveling between locations to attending meetings or working out, will require energy."
            angel "Make sure to keep an eye on this, or you might find yourself running out of steam before the day’s over."

            jump stats_explanation

        "Intelligence":
            angel "This is going to be crucial when it comes to studying, making smart decisions, and staying ahead of the curve in the business world."
            angel "You’ll need to work on this if you want to master your craft."

            jump stats_explanation

        "Charisma":
            angel "Charisma will help you charm your way through social interactions, connect with potential clients, and increase your sales."
            angel "Whether it’s networking at events or simply getting people to believe in your vision, your charisma is your secret weapon."

            jump stats_explanation

        "Continue":
            jump stats_outro

label stats_outro:

    angel "Throughout the day,{w=0.1} you’ll be traveling to different places:{w=0.2} library,{w=0.2} dorm,{w=0.2} business office,{w=0.2} gym,{w=0.2} and even the local shop."
    angel "Each location offers you the chance to boost these stats in different ways."
    angel "But remember,{w=0.1} every action you take will consume your energy and time."

label location_menu:

    menu:
        angel "Would you like to learn more about these places?"

        "Library":
            angel "A place where you can study to increase your intelligence."
            angel "That's why business smarts are important."

            jump location_menu

        "Dorm":
            angel "Your dorm is your home and where you can sit back and relax."
            angel "You'll be able to sleep here and spend time with your roommate, Riley."

            jump location_menu

        "Office":
            angel "This is your office at [business_name]. Here, you're able to sell your product and earn money."
            angel "The amount of money you earn will depend on various stats; higher intelligence, charisma, and energy, will result in more lucrative deals."

            jump location_menu
        
        "Gym":
            angel "You can go to the gym to exercise and increase your charisma. Staying healthy is the best way to maintain a clear mind and body."
            angel "As a reminder, higher charisma will result in greater sales."

            jump location_menu

        "Continue":
            jump location_outro
    
label location_outro:

    angel "The day will end when you either run out of energy or it’s too late to keep working."
    angel "Make sure to balance your tasks wisely!"

    angel "If you find yourself running low on energy,{w=0.1} don’t worry!"
    angel "You can always grab an energy drink to keep yourself going."
    angel "And when you earn enough money,{w=0.2} you’ll be able to purchase all sorts of useful items that can help you stay ahead."

    angel "So are you ready to start?"
    angel "Remember, success doesn’t just come from hard work,{w=0.2} it comes from working smart, balancing your time, and knowing when to push forward and when to rest."
    angel "You got this!"

    jump actions
