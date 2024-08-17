################################################################################
# Stats screen.
#
# This displays RPG-like statistics.
################################################################################

default player_hp = 15
default player_hp_max = 42
default eileen_hp = 100
default eileen_hp_max = 100

default player_lv = 4
default eileen_lv = 99

define e = Character("Eileen")

label test:
    scene bg club

    show angel happy

    jump screens_menu

# This screen displays a single stat.
screen single_stat(name, hp, hp_max, lv, xalign):
    frame:
        xalign xalign

        vbox:
            spacing 5

            hbox:
                text "[name!t]" min_width 220
                text _(" Lv. [lv]")

            hbox:
                text _("HP"):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 180
                    ysize 26

                text " [hp]/[hp_max]":
                    yalign 0.5

# This screen uses single_stat to display two stats at once.
screen stats():
    use single_stat(_("Player"), player_hp, player_hp_max, player_lv, 0.0)
    use single_stat(_("Eileen"), eileen_hp, eileen_hp_max, eileen_lv, 1.0)

################################################################################
# Day picker
#
# This code displays a day picker, including statistics and a way of choosing
# an action for each period of the day.
################################################################################

# This constant defines the periods in the day.
define day_periods = [ _('Morning'), _('Afternoon'), _('Evening') ]

# This constant defines what to do in each period.
define day_choices = [ _('Study'), _('Exercise'), _('Eat'), _('Drink'), _('Be Merry') ]

# This is a dictionary mapping a period to a
default day_plan = {
    'Morning' : 'Eat',
    'Afternoon' : 'Drink',
    'Evening' : 'Be Merry'
    }

# These variables display statistics to the player.
default stat_strength = 10
default stat_intelligence = 25
default stat_moxie = 100
default stat_chutzpah = 75

# These styles are used to style the various stats.
style stat_text is default:
    min_width 200
    textalign 1.0
    yalign 0.5

style stat_hbox is hbox:
    spacing 10

style stat_vbox:
    spacing 5

# This is the day planner screen. It displays the
screen day_planner():
    # This vbox organizes everything.
    vbox:
        spacing 5

        # A frame containing all the stats.
        frame:
            style_prefix "stat"
            xpadding 150
            xfill True

            vbox:
                hbox:
                    text _("Strength")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Intelligence")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Moxie")
                    bar value StaticValue(stat_strength, 100)

                hbox:
                    text _("Chutzpah")
                    bar value StaticValue(stat_strength, 100)

        # A grid of three frames, one for each of the periods in the day.
        grid 3 1:
            spacing 5
            xfill True

            for p in day_periods:
                frame:
                    xfill True

                    vbox:
                        label p

                        null height 5

                        for i in day_choices:
                            textbutton i action SetDict(day_plan, p, i)

        # This is a grid containing two empty space and the done button,
        # so everything lines up.
        grid 3 1:
            xfill True
            spacing 5

            null

            frame:
                textbutton _("Done"):
                    action Return(True)
                    xfill True

                    text_xalign 0.5

            null

label screens_menu:
    menu:
        e "What would you like to know about screens?"

        "What screens can do.":
            call screens_demo

        "Special screen statements.":
            call screens_control

        "That's it.":
            return

    jump screens_menu

label screens_demo:
    e "Screens are how we create the user interface in Ren'Py. With the exception of images and transitions, everything you see comes from a screen."

    e "When I'm speaking to you, I'm using the 'say' screen. It's responsible for taking dialogue and presenting it to the player."

    menu:
        e "And when the menu statement displays an in-game choice, the 'choice' screen is used. Got it?"

        "Yes.":
            pass

        "I do.":
            pass

    e "Text input uses the 'input' screen, NVL mode uses the 'nvl' screen, and so on."

    e "More than one screen can be displayed at once. For example, the buttons at the bottom - Back, History, Skip, and so on - are all displayed by a quick_menu screen that's shown all of the time."

    e "There are a lot of special screens, like 'main_menu', 'load', 'save', and 'preferences'. Rather than list them all here, I'll {a=https://www.renpy.org/doc/html/screen_special.html}send you to the documentation{/a}."

    e "In a newly created project, all these screens live in screens.rpy. You can edit that file in order to change them."

    e "You aren't limited to these screens either. In Ren'Py, you can make your own screens, and use them for your game's interface."

    $ player_hp = 15

    show screen stats
    with dissolve

    e "For example, in an RPG like visual novel, a screen can display the player's statistics."

    $ player_hp = 42

    e "Which reminds me, I should probably heal you."

    hide screen stats
    show screen day_planner

    e "Complex screens can be the basis of whole game mechanics. A stats screen like this can be the basis of dating and life-sims."

    hide screen day_planner
    with dissolve

    e "While screens might be complex, they're really just the result of a lot of simple parts working together to make something larger than all of them."

    return

label screens_control:
    show screen increment

    e "Click the button"

    hide screen increment

    show screen press

    e "Press the key"

    hide screen press

    return

screen increment():
    default n = 0

    frame:
        xalign 0.5 ypos 50
        vbox:
            if n > 2:
                text "n = [n]" color "#cfc"
            else:
                text "n = [n]" color "#fcc"

            textbutton "Increase" action SetScreenVariable("n", n + 1)

screen press():
    frame:
        xalign 0.5 ypos 50

        text "Now press 'a'."

    on "show" action Notify("The screen was just shown.")

    key "a" action Notify("You pressed the 'a' key.")
