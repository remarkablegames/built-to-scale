default days = 30
default money = 0

screen info():
    frame:
        xalign 1.0 ypos 0
        vbox:
            text "Money: $[money]"
            bar value AnimatedValue(money, goal) xalign 0.5 xsize 335
            null height 15
            text "Days Remaining: [days]"
            bar value AnimatedValue(days, 30) xalign 0.5 xsize 335
