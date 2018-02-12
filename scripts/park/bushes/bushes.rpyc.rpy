label park_bushes_dialogue:
    $ location_count = "Park Bushes"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if erik.started(erik_father_treasure):
        scene expression gTimer.image("park_bushes{}_b")
        show player 4 with dissolve
        player_name "Hmm..."
        show player 12 with dissolve
        player_name "( Parece um local bem escondido aqui. )"
        show player 14
        player_name "( Talvez o pai do {b}Erik{/b} esteja falando a verdade. )"
        player_name "( Let's look around. )"
        hide player with dissolve
    elif M_mia.get_state() == S_mia_stolen_goods and not erik.over(erik_thief):
        scene expression gTimer.image("park_bushes{}_b")
        show player 4 with dissolve
        player_name "Hmm..."
        show player 12 with dissolve
        player_name "( Parece ser um lugar bom para esconder coisas. )"
        show player 14
        player_name "( Vou dar uma olhada. )"
        hide player with dissolve
    $ callScreen(location_count)

label park_bushes_bag_dialogue:
    $ location_count = "Park Bushes Bag"
    scene park_bag
    show expression "objects/object_key_02.png" at Position(xpos = 594, ypos = 473)
    if erik.started(erik_father_treasure):
        player_name "Wow!"
        player_name "( Tantas coisas aqui! )"
        player_name "( O pai do {b}Erik{/b} deve estar pegando essas coisas há um bom tempo. )"
        player_name "Hmm..."
        player_name "( Tem uma chave bem estranha qui... )"
        $ erik_father_treasure.finish()

    elif M_mia.get_state() == S_mia_stolen_goods and not erik.over(erik_thief):
        player_name "Woaa!"
        player_name "( Quanta coisa aqui! )"
        player_name "( Deve ser onde o ladrão esconde as coisas. )"
        player_name "( Ele deve estar pegando esses itens há um bom tempo. )"
        player_name "Hmm..."
        player_name "( Tem uma chave bem estranha aqui... )"
    $ callScreen(location_count, False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
