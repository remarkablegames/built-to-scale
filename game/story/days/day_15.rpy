label day_15:

    stop music fadeout 1
    queue music orchestral_waltz

    scene bg office
    with fade

    show mentor smile2 at right
    with dissolve

    mentor "Good to see you again, [player_name]!{w=0.3} You’re doing well!"

    player "Thanks, [mentor.name].{w=0.2} I appeciate your help."

    show friend at left, flip
    with dissolve

    friend "Hey, [player_name], I thought I’d stop by to check out your office!"

    player "[friend.name]! Great to see you. Come on in, let me introduce you to someone."

    player "[friend.name], this is my mentor, [mentor.name]. He’s been helping me with the business."

    friend "Nice to meet you! [player_name] talks about you all the time."

    mentor smile "Likewise.{w=0.2} I’ve heard a lot about you too.{w=0.2} It’s great to finally put a face to the name."

    "You all chat for a bit,{w=0.1} but suddenly,{w=0.2} the door swings open."

    show competitor comeon
    with dissolve

    show mentor disagree2 at right
    show friend shut at left, flip
    show competitor naruhodo

    competitor "Well, isn’t this a cozy little gathering? Still playing pretend, are we, [player_name]?"

    show competitor mock2

    player "[competitor.name]..."

    friend mad "Wait... [competitor.name]? You’re... here?"

    show competitor comeon

    competitor "Oh, [friend.name]! Didn’t think you’d be here too. Still wrapped around [player_name]’s little finger, I see."

    player "What do you want, [competitor.name]?"

    show competitor talking

    competitor "I’m just here to remind you that you’re way out of your league."

    show competitor comeon

    competitor "Your little mentor can’t save you, and [friend.name] here — well..."

    show competitor talking

    competitor "I’m sure he’ll realize sooner or later which of us is actually going to succeed."

    mentor disagree2 "[competitor.name], we’re all just trying to build our own paths here. No need for this hostility."

    show competitor talking

    competitor "Hostility? Please. I’m just calling it like it is. [player_name], you’re in over your head, and soon everyone will see that."

    friend shut "[competitor.name]... why are you doing this? I thought you were different."

    show competitor mock

    competitor "Oh, [friend.name], you’re so naive. Business is business, and I don’t have time for small talk. I’m here to win."

    player "Enough, [competitor.name]. Get out of my office."

    show competitor comeon

    competitor "Fine, I’ll go. But don’t say I didn’t warn you when it all comes crashing down."

    hide competitor with dissolve

    show friend thinking at left, flip
    with dissolve

    friend ohman "I didn’t realize she was your competition... I should’ve seen it sooner."

    mentor aha "Don’t worry, [friend.name]. [player_name] has what it takes. [competitor.name] might be fierce, but we’re stronger together."

    player "Thanks, both of you. This just proves we need to stay focused."

    hide friend
    hide mentor
    with dissolve

    "As [competitor.name] leaves, the tension lingers.{w=0.3} [friend.name] looks shaken, but your resolve only hardens."
    "[competitor.name]’s games are getting more dangerous, and you need to stay sharp."

    return
