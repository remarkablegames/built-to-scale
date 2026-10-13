label day_15:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    show mentor at right
    with dissolve

    mentor smile2 "Good to see that you’re doing well today!"

    player "Thanks,{w=.1} I appeciate your help."

    show friend at left, flip
    with dissolve

    friend "Hey,{w=.1} [player_name],{w=.1} I thought I’d stop by to check out your office."

    player "[friend.name]!"
    player "Come on in,{w=.2} let me introduce you to someone."
    player "[friend.name],{w=.2} this is my mentor,{w=.2} [mentor.name]."
    player "He’s been helping me with the business."

    friend "Nice to meet you!"
    friend "[player_name] talks about you all the time."

    mentor smile "Likewise.{w=.2} I’ve heard a lot about you too."
    mentor "It’s great to finally put a face to the name."

    "You all chat for a bit,{w=.1} but suddenly,{w=.2} the door swings open."

    show competitor comeon
    with dissolve

    pause 1

    show mentor disagree2 at right
    show friend shut at left, flip

    competitor naruhodo "Well,{w=.2} isn’t this a cozy little gathering?"
    competitor "Still playing pretend,{w=.2} are we,{w=.1} [player_name]?"

    show competitor mock2

    player "{cps=10}[competitor.name]..."

    friend mad "{cps=10}Wait...{w=.2} [competitor.name]?{/cps}{w=.3} You’re...{w=.2} here?"

    competitor comeon "Oh,{w=.1} [friend.name]!{w=.3} Didn’t think you’d be here too."
    competitor "Still wrapped around [player_name]’s little finger,{w=.1} I suppose."

    player "What do you want,{w=.1} [competitor.name]?"

    competitor talking "I’m just here to remind you that you’re way out of your league."

    competitor @ comeon "Your little mentor can’t save you,{w=.1} and [friend.name] here—well..."

    competitor "I’m sure he’ll realize sooner or later which of us is actually going to succeed."

    mentor disagree2 "[competitor.name],{w=.1} we’re all just trying to build our own paths here."
    mentor "No need for this hostility."

    competitor "Hostility?{w=.3} Please.{w=.2} I’m just calling it like it is."
    competitor "[player_name],{w=.1} you’re in over your head,{w=.1} and soon everyone will see that."

    friend shut "[competitor.name]...{w=.2} why are you doing this?{w=.2} I thought you were different."

    competitor mock "Oh,{w=.1} [friend.name],{w=.1} you’re so naive."
    competitor "Business is business,{w=.1} and I don’t have time for small talk.{w=.3} I’m here to win."

    player "Enough,{w=.1} [competitor.name].{w=.3} Get out of my office."

    competitor comeon "Fine,{w=.1} I’ll go.{w=.3} But don’t say I didn’t warn you when it all comes crumbling down."

    hide competitor with dissolve

    show friend thinking at left, flip
    with dissolve

    friend ohman "I didn’t realize she was your competition...{w=.3} I should’ve seen it sooner."

    mentor aha "Don’t worry,{w=.1} [friend.name]."
    mentor "[player_name] has what it takes."
    mentor "[competitor.name] might be fierce,{w=.1} but we’re stronger together."

    player "Thanks,{w=.1} this just proves we need to stay focused."

    hide friend
    hide mentor
    with dissolve

    "As [competitor.name] leaves,{w=.1} the tension lingers."
    "[friend.name] looks shaken,{w=.1} but your resolve only hardens."
    "[competitor.name]’s games are getting more dangerous,{w=.1} and you need to stay sharp."

    return
