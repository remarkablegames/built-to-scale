label day_21:

    stop music fadeout 1
    queue music electro_2a
    queue music electro_2b

    scene bg office with fade

    if equity == 100 and money >= goal:
        player "I made it. Every decision, every risk, every sleepless night... it all paid off." 
        player "I kept full control of the company, and with over $[goal:,] in the bank, the future is wide open."

        show mentor smile
        with dissolve

        mentor "I knew you had it in you, [player_name]." 
        mentor "You didn’t just meet the goal—you crushed it."
        mentor "Full control, a healthy bank account, and a growing business. The future’s yours to shape."

        show friend at left, flip
        with dissolve

        friend "Way to go, [player_name]! I believed in you the whole time. Sort of."

        show competitor mad at right
        with dissolve

        competitor "I can’t believe you actually pulled it off, [player_name]." 
        competitor "Full control and a massive profit? You may have won this round, but don’t think for a second that this is over."

        player "It’s over when I say it’s over, [competitor.name]. And right now, I’m just getting started."

        mentor "You’re no longer just a dreamer. You’re a true entrepreneur."
        mentor "Congratulations, [player_name]."
        mentor "The road ahead will be challenging, but you’ve shown you can handle anything."

        player "Thanks, [mentor.name]. Looks like we’re built to scale."

    elif equity == 100 and money < goal:
        player "I managed to keep full control of the company, but with less than $[goal:,] in the bank... it doesn’t feel like a total victory."

        show mentor smile
        with dissolve

        mentor "You’ve done well to maintain full control, [player_name]. That alone is a huge accomplishment." 
        "But remember, the financial side is just as important."

        show friend at left, flip
        with dissolve

        friend "You did your best, [player_name]. Hang in there!"

        show competitor mad at right
        with dissolve

        competitor "Full control but less than $[goal:,]? You barely made it." 
        competitor "Don’t get too comfortable, [player_name]. Next time, you won’t be so lucky."

        player "I may not have hit every mark, but I’m still here." 
        player "And with full control of the company, I’ll keep pushing forward."

        mentor "You’ve still got the reins, [player_name]."
        mentor "With determination and careful planning, you can turn things around and grow the business even more."

        player "You’re right. I may not be where I want to be yet, but I still have control of my company, and that’s something."

    elif equity < 100 and money >= goal:
        player "I’ve made it. Over $[goal:,] in the bank, but at what cost?" 
        player "I had to give up some control of the company to get here." 
        player "I’ve won... but it doesn’t feel like a complete victory."

        show friend at left, flip
        with dissolve

        friend "You crushed your money goal, [player_name]! Don’t let the equity part bring you down."

        show mentor smile
        with dissolve

        mentor "You’ve done an impressive job, [player_name]. With over $[goal:,], your business is in a strong position." 
        mentor "But remember, you no longer have full control. You’ll have to work with others to shape the future of “[business_name]”."

        show competitor sadsmile at right
        with dissolve

        competitor "You gave up control and still made more than $[goal:,]?" 
        competitor "I should have been tougher on you! But enjoy it while it lasts, [player_name]." 
        competitor "It’s only a matter of time before I come out on top."

        player "I made the sacrifices I had to in order to survive. It wasn’t easy, but I know it was the right choice at the time."

        mentor "True. You adapted, made tough decisions, and built something strong." 
        mentor "Keep your head up, [player_name]." 
        mentor "Even with shared control, you can still steer “[business_name]” to greatness."

        player "I know. I just have to keep fighting for what I believe in." 
        player "The business may not be entirely mine, but the vision is."

    elif equity < 100 and money < goal:
        player "This... this isn’t where I thought I’d end up." 
        player "Less than $[goal:,] in the bank, and I don’t even have full control of my own company." 
        player "It feels like everything slipped away."

        show mentor sad smile
        with dissolve

        show friend at left, flip
        with dissolve 

        friend "You did your best, [player_name]. We’ll go for walk to cheer you up."

        mentor "I know this isn’t the outcome you were hoping for, [player_name]." 
        mentor "You fought hard, but sometimes the road to success is longer and harder than we expect." 
        mentor "It doesn’t mean it’s over."

        show competitor tired at right
        with dissolve

        competitor "I’ve been tough on you, [player_name]. But... I didn’t expect it to end like this for you."

        player "I gave it my all, but in the end, it feels like I’ve lost more than I’ve gained." 
        player "I don’t know if I can keep going like this."

        show competitor argue2 at right

        competitor "Business is brutal. Trust me, I know." 
        competitor "It doesn’t always go the way we want. But you’re a fighter, and even if I don’t show it, I respect that."

        show mentor

        mentor @ thinking "Don’t let this be the end." 
        mentor "You’ve learned valuable lessons, and you’re still standing." 
        mentor "There’s a way forward, but it may take more time and even tougher decisions."

        player "Maybe you’re right. Maybe this isn’t the end, just... another challenge."
        player "I’m not ready to give up, but it’s hard to see the path forward right now."

        show competitor sadsmile at right

        competitor "You’re stronger than you think, [player_name]."
        competitor "You’ve still got something left in you, even if it doesn’t feel like it right now." 
        competitor "Just don’t lose sight of who you are."

        player "Guess the business is not built to scale."

    hide screen stats
    hide screen info

    scene black
    with fade

    "The future of your business may be uncertain,{w=0.2} but one thing is clear:{w=0.3} you’re not done yet."
    "Your journey continues, and the lessons you’ve learned will guide you for the rest of your life."

    "{b}End{/b}."

    return
