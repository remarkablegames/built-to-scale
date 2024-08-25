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

    stop music fadeout 1
    queue music electro_2d fadein 1

    scene bg bus stop morning
    with fade

    show mentor
    with dissolve

    queue music [electro_2e, electro_2f]

    mentor @ thinking "What are the steps to success?"
    mentor "You’ll need to focus on three key areas:{w=0.2} {b}Energy{/b}{w=0.2}, {b}Intelligence{/b}{w=0.2}, and {b}Charisma{/b}."

    jump stats_explanation

label stats_explanation:
    show screen stats

    menu:
        mentor "What do you want to know?"

        "{color=#40e0d0}Energy{/color}":
            mentor @ thinking "You’ll need energy to accomplish all your tasks for the day."
            mentor "Every action,{w=0.2} from making sales to working out,{w=.2} requires energy."

            jump stats_explanation

        "{color=#ffbf00}Intelligence{/color}":
            mentor @ thinking "The higher your intelligence, the more sales you will make."
            mentor "Smarts can also unlock new business opportunities."

            jump stats_explanation

        "{color=#ccccff}Charisma{/color}":
            mentor "Charisma is a multiplier for marketing and sales."
            mentor "You can use this skill to charm competitors and clients."

            jump stats_explanation

        "Continue":
            jump stats_outro

label stats_outro:

    mentor @ thinking "You should end the day when it gets late."
    mentor aha "If you’re low on energy,{w=0.1} go to the shop or return home to rest."
    mentor "Success is the result of luck,{w=0.1} preparation,{w=0.1} and choices you’ve made."
    mentor smile2 "Good luck!"

    jump day_start
