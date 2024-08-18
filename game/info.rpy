default days = 30
default money = 0

screen info():
    frame:
        xalign 1.0 ypos 0
        vbox:
            text "Money: {color=#85bb65}$[money]{/color}"
            null height 15
            text "Remaining Days: {color=#0099cc}[days]{/color}"
