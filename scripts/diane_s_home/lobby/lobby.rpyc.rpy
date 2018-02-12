label dianelobby_dialogue:
    $ location_count = "Diane's Lobby"
    if aunt.started(aunt_mouse_attack):
        scene dianeentrance with None
        show player 22 with dissolve
        dia "AJUDA!"
        dia "RÁPIDO! ME AJUDA!"
        show player 23
        player_name "{b}Tia Diane{/b}?!"
        player_name "ESTOU INDO!"
        show player 22
        dia "EEEEEEEKKKKKKK!"
        hide player with dissolve
    $ callScreen(location_count)

label dianelobby_locked:
    if location_count == "Diane's Kitchen":
        scene dianekitchen
    elif location_count == "Diane's Front Yard":
        scene location_diane_front_blur
    show aunt 3 at right
    show player 11 at left
    with dissolve
    dia "Onde você está indo? O jardim está lá fora, não aqui, querido."
    hide aunt
    hide player
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
