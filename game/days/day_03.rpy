label day_03:

    stop music fadeout 1

    scene bg office
    with fade

    play sound knock

    "You hear a knock on the door."

    player "Come in..."

    play music orchestral_waltz

    show competitor comeon
    with dissolve

    competitor "Well,{w=0.1} well,{w=0.1} well.{w=0.2} So this is the office where all the noise is coming from."

    player "Who are you?"

    show competitor naruhodo

    competitor smirk "Oh,{w=0.1} how rude of me.{w=0.2} I’m [competitor.name]."

    player "Hmm..."

    competitor "You can consider me your competitor.{w=0.3} I run a real business in this town."
    competitor "Scales, you say?{w=0.2} Cute.{w=0.2} But don’t get too comfortable."

    player "What do you mean?"

    show competitor comeon

    competitor "I mean,{w=0.1} it’s only a matter of time before your little operation folds."
    competitor "I have the resources,{w=0.2} the connections,{w=0.2} and well{w=0.1}.{w=0.1}.{w=0.1}.{w=0.3} the brains.{w=0.3} What do you have?{w=0.3} Hope?"

    player "I have determination.{w=0.3} That should be more than enough."

    competitor laugh "Ha! Determination?{w=0.2} Adorable.{w=0.2}"
    competitor "Here’s a tip:{w=0.3} stay out of my way,{w=0.1} and maybe you won’t get crushed."
    competitor "This town ain’t big enough for two scale businesses,{w=0.2} and I don’t like to share."

    player "I’m not backing down."

    competitor "Good. I like a challenge.{w=0.2} Just don’t say I didn’t warn you when your precious little dream comes crumbling down."
    competitor" Now,{w=0.1} if you’ll excuse me,{w=0.1} I have a real company to run."

    hide competitor 
    with dissolve 

    "The door slams shut as [competitor.name] leaves, her words echoing in the air. It looks like you’ve made your first enemy."

    return
