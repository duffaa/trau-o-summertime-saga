label diane_front_yard:
    $ location_count = "Diane's Front Yard"
    $ callScreen(location_count)

label diane_front_yard_night_locked:
    show expression gTimer.image("backgrounds/location_diane_front{}_blur.jpg")
    show player 10 with dissolve
    player_name "{b}Tia Diane{/b} provavelmente está dormindo..."
    hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
