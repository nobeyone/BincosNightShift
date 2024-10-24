define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_voice_volume = 0.7

define doug_sykes = Character("Doug Sykes", what_font = r"fonts/digital-7 (mono).ttf")
image doug_sykes_image = "Doug Sykes/mouth shapes/doug sykes AXG.png"

label doug_scene:
    scene bg doug sykes
    play sound "blockbuster.mp3"
    show doug animation
    doug_sykes "Why would I be perfect for the Blockbuster Video Rental Assassination Squad? Take a look at this macrochip on my forehead. Think about how fast the processes must be on this baby. That's right; 1.5 kilobytes per second of downloading and processing."
    menu:
        "You're hired.":
            return
        "Get outta here.":
            return
