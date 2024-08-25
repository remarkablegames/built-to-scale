default equity = 100
default money = 100
default profit_reduction_days = 0
default profit_reduction = 1.0
default profit_boost_days = 0
default profit_boost = 1.0

screen info():
    frame:
        xalign 1.0 ypos 0
        vbox:
            text "Days Left: [days]"
            bar value AnimatedValue(days, days_total) xalign 0.5 xsize 300
            null height 15

            text "Equity: [equity]%"
            bar value AnimatedValue(equity, 100) xalign 0.5 xsize 300
            null height 15

            text "Money: $[money:,]"
            bar value AnimatedValue(money, goal) xalign 0.5 xsize 300
