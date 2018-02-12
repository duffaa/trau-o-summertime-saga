label kitchen_dialogue:
    $ location_count = "Diane's Kitchen"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if aunt.started(aunt_breeding_bull) and quest12 in completed_quests:
        scene location_diane_kitchen_closeup with None
        show player 1 at left
        show aunt 88 at right
        with dissolve
        pause
        show aunt 89
        dia "Bom dia, querido!"
        show aunt 88
        show player 36
        player_name "Bom dia, {b}tia Diane{/b}."
        show player 13
        show aunt 92
        dia "Então... eu estive pensando sobre o que você me disse a noite TODA."
        dia "Não é uma decisão fácil, e não quero que seja algo que me arrependa."
        show aunt 87
        dia "Mas, sua proposta parece tão tentadora e tem vários benefícios, então..."
        show aunt 89
        dia "Eu decidi aceitar sua ideia de procriar!"
        show player 17
        show aunt 88
        player_name "Sério? Estou feliz que você tenha gostado!"
        show player 13
        show aunt 90
        dia "Se eu quiser trabalhar nesse mercado, eu vou precisar seios trablhando muito!"
        show aunt 87
        dia "Eu quero que isso tenha sucesso, então é melhor nos focarmos no guia."
        show aunt 89
        dia "Além disso, isso é uma grande mudança para mim. É tão... primata!"
        show aunt 88
        show player 21
        player_name "Sério?"
        show player 13
        show aunt 90
        dia "Claro!"
        show aunt 92
        show player 11
        dia "Mas, eu tenho esse pequeno problema..."
        show aunt 89
        dia "Eu não tenho certeza onde eu posso encontrar, sabe ... um touro jovem e saudável!"
        dia "Mas está tudo bem. Posso começar a elaborar os detalhes."
        show aunt 88
        show player 14
        player_name "Feliz que eu pude ajudar! Estou feliz por você estar feliz!"
        show player 13
        show aunt 89
        dia "Obrigada."
        dia "Ah, e se você acha que conhece quem quiser, você sabe, seja adequado para mim, você me avisa."
        show aunt 88
        show player 21
        player_name "Uhh... Certo!"
        hide player
        hide aunt
        with dissolve
        $ aunt_breeding_bull.finish()

    elif aunt.started(aunt_mouse_attack):
        scene dianekitchen with None
        show player 10 with dissolve
        player_name "Estranho. Ela também não está aqui."
        player_name "( Pensei que... )"
        show player 11
        dia "EEEEEEKKKKKKK!"
        show player 23f
        player_name "Mas que..."
        player_name "( É a {b}tia Diane{/b} gritando?! )"
        hide player with dissolve

    elif aunt_drink_active == True:
        $ callScreen(location_count)
    else:

        if not aunt.known(aunt_drunken_splur) and aunt_count < 8 or aunt.over(aunt_drunken_splur) and aunt_count < 8:
            scene dianekitchen1
            player_name "( Não tem ninguém aqui. )"
            player_name "( {b}Tia Diane{/b} está no jardim. )"
    $ callScreen(location_count)

label mouse_attack:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "( Não posso simplesmente sair, {b}tia Diane{/b} deve estar em perigo. )"
    hide player with dissolve
    $ callScreen(location_count)

label kitchen_drink:
    scene dianekitchen
    show player 133 with dissolve
    player_name "( Deve ser isso... )"
    show player 135
    player_name "Annnd... aqui."
    show player 132
    show expression "characters/xtra/char_xtra_01.png" at Position(xpos = 638, ypos = 519)
    player_name "Hmm..."
    show player 133
    player_name "( Talvez eu devesse adicionar um pouco mais? )"
    $ aunt_drink_made = True
    menu:
        "Não.":
            show player 133
            player_name "Nah. Já é o suficiente..."
            player_name "( {b}Tia Diane{/b} fica muito... amável, quando toma algumas bebidas. )"
            show player 134
            player_name "( Isso já é bom o bastante... )"
            $ in_garden = True
            $ lock_ui()
            jump garden_dialogue
        "Sim.":

            show player 135
            player_name "Apeeeenas... {b}um pouquinho mais{/b}!"
            show player 134
            player_name "( Perfeito... )"
            $ aunt_extra_shot = True
            $ in_garden = True
            $ lock_ui()
            jump garden_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
