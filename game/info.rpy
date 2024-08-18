default days = 30
default money = 0

screen info():
    frame:
        xalign 1.0 ypos 0
        vbox:
            text "Money: $[money]"
            null height 15
            text "Days Remaining: [days]"
