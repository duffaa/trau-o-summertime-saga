label dianebedroom_dialogue:
    $ location_count = "Diane's Bedroom"
    if aunt.started(aunt_drunken_splur):
        scene dianebedroom_b with None
        show diane_passedout_b at Position(xanchor = 0, yanchor = 0, xpos = 228, ypos = 141)
        show player 13 at left
        player_name "( Parece que ela chegou até a cama. )"
        show player 11
        player_name "( Ela está bem? )"
        hide player with dissolve
    $ callScreen(location_count)

label diane_bedroom_dialogue:
    if aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur):
        scene dianebed with None
        show diane 5
        player_name "!!!"
        player_name "( Seus peitos ainda estão saindo de seu macacão. )"
        player_name "( Não sei porque ela acha que o corpo dela é feio e velho. )"
        player_name "..."
        player_name "( Eu deveria deixar ela aqui e ir cuidar do jardim... )"
        $ unlock_ui()
        $ aunt_drunken_splur.finish()

    elif aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack):
        scene dianebedroom_closeup with None
        show aunt 152 at Position (xpos = 695)
        pause
        show player 23 at left with dissolve
        player_name "{b}Tia Diane{/b}!"
        player_name "O que está acontecendo?!"
        show aunt 152
        show player 22 at left
        dia "EEEEEKKKKKK!!!!"
        show aunt 154
        dia "Me ajuda!"
        show aunt 153
        pause
        show player 23
        player_name "O que foi?!"
        show aunt 154
        show player 11
        dia "R-RAA-RAA-RAAATOOO!"
        show aunt 152
        dia "BEM ALI!"
        hide player
        show aunt 155
        with dissolve
        pause
        show aunt 156
        player_name "O quê? Não vejo nada..."
        show aunt 155
        dia "Não, bem ali!"
        show aunt 156
        player_name "Continuo não vendo nenhum rato."
        show aunt 155
        dia "O rabo dele está ali entre esses tênis!"
        show aunt 155b
        pause
        show aunt 156
        player_name "{b}Tia Diane{/b}..."
        player_name "Acho que esse rato é só a corda do tênis."
        show aunt 155
        dia "O quê? Sério!?"
        show aunt 156
        player_name "Uhum."
        show aunt 155
        dia "..."
        dia "Tá, me ponha no chão então. É melhor você não estar mentindo!"
        show aunt 156
        player_name "Não se preocupe, a corda do sapato não morderá."
        show player 14 at Position(xpos=200)
        show aunt 144 at Position(xpos=650)
        with dissolve
        player_name "Você está bem?"
        show player 13
        show aunt 146
        dia "Sim, estou bem."
        dia "Entretando me sinto meio envergonhada por gritar por um sapato."
        show aunt 147
        dia "Eu juro que tinha visto isso sem mexer..."
        show aunt 148
        show player 10
        player_name "Você me assustou!"
        player_name "Achei que você estava sendo assaltada ou algo do tipo..."
        show player 5
        show aunt 145
        dia "Desculpa! Apenas sua {b}tia{/b} gritando por um rato imaginário. Haha."
        show aunt 144
        pause
        show aunt 149
        dia "Confesso que... foi bem fofo da sua parte vir me salvar."
        show aunt 150
        show player 29 at Position(xoffset=26)
        player_name "Oh, Eu ehhh... É apenas instinto..."
        show player 13
        show aunt 149
        dia "Ah, como eu queria alguém como você por aqui!"
        show aunt 151
        dia "Alguém forte... Disposto a me proteger, e satisf-"
        show aunt 144b
        dia "!!!"
        show aunt 147
        dia "Oh, céus! Estou quase pelada!!"
        show aunt 148
        show player 14
        player_name "Está tudo bem, {b}tia Diane{/b}. Não me importo."
        show aunt 144
        player_name "Estou feliz por você estar segura."
        show player 13
        show aunt 149
        dia "Continuo muito mal."
        show aunt 151
        dia "Sinto muito que você teve que ver esse corpo velho."
        show aunt 150
        show player 33
        player_name "Não acho que você está tão velha."
        show player 13
        show aunt 147
        dia "Sério?"
        show aunt 150
        show player 26
        player_name "Sim, você... está bonita, eu acho."
        show player 13
        show aunt 148
        dia "!!!"
        pause
        show player 11
        show aunt 146
        dia "Hahaha!"
        dia "Você sabe como me fazer rir."
        show player 13
        show aunt 145
        dia "Obrigada, {b}[firstname]{/b}, por tudo. Você é um querido."
        show player 14
        show aunt 144
        player_name "De nada, {b}tia Diane{/b}."
        show player 26
        pause
        show player 25
        show aunt 150
        pause
        show aunt 149
        dia "Melhor eu terminar de me trocar..."
        show player 29
        show aunt 150
        player_name "E eu provavelmente deveria ir cuidar do jardim."
        hide player with dissolve
        scene dianeentrance
        show player 33 with dissolve
        player_name "(Wow...)"
        player_name "(Nunca pensei que veria {b}tia Diane{/b} assim.)"
        show player 203
        player_name "(...)"
        player_name "(Ela está... muito gostosa.)"
        hide player with dissolve
        $ unlock_ui()
        $ aunt_mouse_attack.finish()
        $ aunt.complete_events(aunt_mouse_attack)
        jump dianelobby_dialogue
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
