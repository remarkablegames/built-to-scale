init python:
    BLEEP_CHANNEL = "bleep"
    renpy.music.register_channel(BLEEP_CHANNEL, mixer="voice", loop=True)


    def make_voice(filename):
        def callback(event, **kwargs):
            if event == "show_done":
                renpy.music.play(f"voice/{filename}.ogg", channel=BLEEP_CHANNEL, relative_volume=2)

            elif event in ("slow_done", "end"):
                renpy.music.stop(channel=BLEEP_CHANNEL, fadeout=.2)

        return callback


    def dismiss_callback() -> bool:
        renpy.sound.play("ui/click.ogg")
        return True


    config.say_allow_dismiss = dismiss_callback


define competitor = Character("Ava", color="#ee4b2b", image="competitor", callback=make_voice("bleep021"))
define company = Character("Company", color="#e5e4e2", callback=make_voice("bleep003"))
define friend = Character("Riley", color="#e4d00a", image="friend", callback=make_voice("bleep027"))
define mentor = Character("Jasper", color="#9fe2bf", image="mentor", callback=make_voice("bleep019"))
define narrator = Character(None, callback=make_voice("bleep029"))
define player = Character("[player_name]", color="#c8c8ff", callback=make_voice("bleep030"))
define supplier = Character("Supplier", color="#e5e4e2", callback=make_voice("bleep001"))
