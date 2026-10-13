label day_21:

    stop music fadeout 1
    queue music electro_2a
    queue music electro_2b

    scene bg office with fade

    if equity == 100 and money >= goal:
        player "I made it."
        player "Every decision,{w=.1} every risk,{w=.1} every sleepless night...{w=.2} it all paid off."
        player "I kept full control of the company,{w=.1} and with over $[goal:,] in the bank,{w=.1} the future is wide open."

        show mentor smile
        with dissolve

        mentor "I knew you had it in you,{w=.1} [player_name]." 
        mentor "You didn’t just meet the goal—{w=.3}you crushed it."
        mentor "Full control,{w=.1} a healthy bank account,{w=.1} and a growing business."
        mentor "The future’s yours to shape."

        play sound woosh

        show friend at left, flip
        with dissolve

        friend "Way to go,{w=.1} [player_name]!"
        friend "I believed in you the whole time.{w=.5} Sort of."

        play sound woosh

        show competitor mad at right
        with dissolve

        competitor "I can’t believe you actually pulled it off,{w=.1} [player_name]."
        competitor "Full control and a massive profit?"
        competitor "You may have won this round,{w=.1} but don’t think for a second that this is over."

        player "It’s over when I say it’s over,{w=.1} [competitor.name]."
        player "And right now,{w=.1} I’m just getting started."

        mentor "You’re no longer just a dreamer.{w=.3} You’re a true entrepreneur."
        mentor "Congratulations,{w=.1} [player_name]."
        mentor "The road ahead will be challenging,{w=.1} but you’ve shown you can handle anything."

        player "Thanks,{w=.1} [mentor.name].{w=.3} Looks like we’re built to scale."

    elif equity == 100 and money < goal:
        player "I managed to keep full control of the company,{w=.1} but with less than $[goal:,] in the bank...{w=.1} it doesn’t feel like a total victory."

        show mentor smile
        with dissolve

        mentor "You’ve done well to maintain full control,{w=.1} [player_name]."
        mentor "That alone is a huge accomplishment."
        mentor "But remember,{w=.1} the financial side is just as important."

        play sound woosh

        show friend at left, flip
        with dissolve

        friend "You did your best,{w=.1} [player_name].{w=.3} Be proud!"

        play sound woosh

        show competitor mad at right
        with dissolve

        competitor "Full control but less than $[goal:,]?{w=.3} You barely made it."
        competitor "Don’t get too comfortable,{w=.1} [player_name]."
        competitor "Next time,{w=.1} you won’t be so lucky."

        player "I may not have hit every mark,{w=.1} but I’m still here."
        player "And with full control of the company,{w=.1} I’ll keep pushing forward."

        mentor "You’ve still got the reins,{w=.1} [player_name]."
        mentor "With determination and careful planning,{w=.1} you can turn things around and grow the business even more."

        player "You’re right.{w=.3} I may not be where I want to be yet,{w=.1} but I still have control of my company,{w=.1} and that’s something."

    elif equity < 100 and money >= goal:
        player "I’ve made it."
        player "Over $[goal:,] in the bank,{w=.1} but at what cost?"
        player "I had to give up some control of the company to get here." 
        player "I’ve won...{w=.2} but it doesn’t feel like a complete victory."

        show friend at left, flip
        with dissolve

        friend "You crushed your money goal,{w=.1} [player_name]!{w=.3} Don’t let the equity part bring you down."

        play sound woosh

        show mentor smile
        with dissolve

        mentor "You’ve done an impressive job,{w=.1} [player_name]."
        mentor "With over $[goal:,],{w=.1} your business is in a strong position."
        mentor "But remember,{w=.1} you no longer have full control."
        mentor "You’ll have to work with others to shape the future of “[business_name]”."

        play sound woosh

        show competitor sadsmile at right
        with dissolve

        competitor "You gave up control and still made more than $[goal:,]?" 
        competitor "I should have been tougher on you!"
        competitor "But enjoy it while it lasts,{w=.1} [player_name]."
        competitor "It’s only a matter of time before I come out on top."

        player "I made the sacrifices I had to in order to survive."
        player "It wasn’t easy,{w=.1} but I know it was the right choice at the time."

        mentor "True.{w=.2} You adapted,{w=.1} made tough decisions,{w=.1} and built something amazing."
        mentor "Keep your head up,{w=.1} [player_name]."
        mentor "Even with shared control,{w=.1} you can still steer “[business_name]” to greatness."

        player "I know.{w=.2} I just have to keep fighting for what I believe in."
        player "The business may not be entirely mine,{w=.1} but the vision is."

    elif equity < 100 and money < goal:
        player "This...{w=.3} this isn’t where I thought I’d end up."
        player "Less than $[goal:,] in the bank,{w=.2} and I don’t even have full control of my own company."
        player "It feels like everything slipped away."

        show mentor sad smile
        with dissolve

        pause 1

        play sound woosh

        show friend at left, flip
        with dissolve 

        friend "You did your best,{w=.1} [player_name]."
        friend "Let’s go on a walk and cheer up."

        mentor "I know this isn’t the outcome you were hoping for,{w=.1} [player_name]."
        mentor "You fought hard,{w=.1} but sometimes the road to success is longer and harder than we expect."
        mentor "It doesn’t mean it’s over."

        play sound woosh

        show competitor tired at right
        with dissolve

        competitor "I’ve been tough on you,{w=.1} [player_name].{w=.3} But...{w=.1} I didn’t expect it to end like this for you."

        player "I gave it my all,{w=.1} but in the end,{w=.1} it feels like I’ve lost more than I’ve gained."
        player "I don’t know if I can keep going like this."

        show competitor argue2 at right

        competitor "Business is brutal.{w=.5} Trust me,{w=.2} I know."
        competitor "It doesn’t always go the way we want.{w=.3} But you’re a fighter{w=.2}, and even if I don’t show it,{w=.1} I respect that."

        show mentor

        mentor @ thinking "Don’t let this be the end." 
        mentor "You’ve learned valuable lessons,{w=.1} and you’re still standing."
        mentor "There’s a way forward,{w=.1} but it may take more time and even tougher decisions."

        player "Maybe you’re right.{w=.1} Maybe this isn’t the end,{w=.1} just...{w=.2} another challenge."
        player "I’m not ready to give up,{w=.2} but it’s hard to see the path forward right now."

        show competitor sadsmile at right

        competitor "You’re stronger than you think,{w=.1} [player_name]."
        competitor "You’ve still got something left in you,{w=.1} even if it doesn’t feel like it right now."
        competitor "Just don’t lose sight of who you are."

        player "Guess the business is not built to scale."

    hide screen stats
    hide screen info

    scene black
    with fade

    "The future of your business may be uncertain,{w=.2} but one thing is clear:{w=.3} you’re not done yet."
    "Your journey continues, and the lessons you’ve learned will guide you for the rest of your life."

    "{b}End{/b}."

    return
