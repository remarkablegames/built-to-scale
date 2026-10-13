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

    competitor "Well,{w=.1} well,{w=.1} well."
    competitor "So this is the office where all the noise is coming from."

    player "Who are you?"

    competitor naruhodo "Oh,{w=.1} how rude of me."
    competitor "I’m [competitor.name]."

    player "{cps=10}..."

    competitor comeon "You can consider me your competitor."
    competitor "I run a real business in this town."
    competitor naruhodo "Scales, you say?{w=.2} Cute.{w=.2} But don’t get too comfortable."

    player "What do you mean by that?"

    competitor comeon "I mean,{w=.1} it’s only a matter of time before your little operation folds."
    competitor @ naruhodo "I have the resources,{w=.1} the connections,{w=.1} and well...{w=.3} the brains."
    competitor "What do you have?{w=.3} Hope?"

    player "I have determination.{w=.3} That should be more than enough."

    competitor @ mock "Ha! Determination?{w=.2} Adorable.{w=.2}"
    competitor "Here’s a tip:{w=.3} stay out of my way,{w=.1} and maybe you won’t get crushed."
    competitor naruhodo "This town ain’t big enough for two scale businesses,{w=.2} and I don’t like to share."

    player "I’m not backing down."

    competitor comeon "Good,{w=.1} I like a challenge."
    competitor "Just don’t say I didn’t warn you when your precious little dream is cut short."
    competitor" Now,{w=.1} if you’ll excuse me,{w=.2} I have a real company to run."

    hide competitor 
    with dissolve 

    "The door slams shut as [competitor.name] leaves,{w=.2} her words echoing in the air."
    "It looks like you’ve made your first enemy."

    return
