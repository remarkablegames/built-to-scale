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
   
    mentor "The day will end when you either run out of energy or it’s too late to keep working."
    mentor "Make sure to balance your tasks wisely!"

    mentor "If you find yourself running low on energy,{w=0.1} don’t worry!"
    mentor "You can always grab an energy drink to keep yourself going."
    mentor "And when you earn enough money,{w=0.2} you’ll be able to purchase all sorts of useful items that can help you stay ahead."

    mentor "So are you ready to start?"
    mentor "Remember, success doesn’t just come from hard work,{w=0.2} it comes from working smart, balancing your time, and knowing when to push forward and when to rest."
    mentor smile "You got this!"

    jump day_start
