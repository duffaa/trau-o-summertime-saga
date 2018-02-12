default left_hall_cult_seen = False

label left_hall_dialogue:
    $ location_count = "School Left Hallway"
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not gTimer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if not gTimer.is_dark():
        if left_hall_dialogue_count == 0 and not left_hall_dialogue_advancement:
            scene lefthall
            show player 2 at left with dissolve
            show judith 6 at right with dissolve
            player_name "Oi, {b}Judith{/b}..."
            show player 11 at left
            player_name "..."
            show player 10 at left
            player_name "Está tudo bem?"
            show player 5 at left
            show judith 3 at right
            jud "Oh, oi, {b}[firstname]{/b}..."
            jud "Não estou me sentindo muito bem; Eu deveria ir pra casa."
            show player 10 at left
            show judith 1 at right
            player_name "VOcê não vai pra educação física?"
            show player 5 at left
            show judith 2 at right
            jud "Bom..."
            show judith 6 at right
            jud "...e..."
            show judith 3 at right
            jud "... Não posso ir pro vestiário masculino."
            show player 10 at left
            show judith 1 at right
            player_name "Ah sim, ovui falarem sobre isso... que merda."
            show player 5 at left
            show judith 2 at right
            jud "Eu não me sinto confortável sobre isso, como as outras garotas."
            show judith 6 at right
            show player 34 at left
            player_name "Bom..."
            show player 35 at left
            show judith 1 at right
            player_name "A aula está começando em breve, então provavelmente não há muitas pessoas lá."
            show player 1 at left
            show judith 5 at right
            jud "Sim, tem razão..."
            show player 2 at left
            show judith 4 at right
            player_name "Eu posso entrar com você, para ter certeza de que você esteja bem..."
            show player 33 at left
            player_name "...E eu não vou olhar!"
            show player 13 at left
            show judith 5 at right
            jud "Ok... me siga então."
            hide player 13 at left with dissolve
            hide judith 5 at left with dissolve
            $ left_hall_dialogue_advancement = True

        elif left_hall_dialogue_count == 2 and not left_hall_dialogue_advancement:
            scene lefthall
            show judith 10 at left with dissolve
            show latinas 19 at right with dissolve
            lopez "Veja se não são esses peitos nojentos!"
            show latinas 18 at right
            show judith 7 at left
            jud "..."
            show latinas 20 at right
            show judith 8 at left
            martinez "Ela deve ser muito pobre para comprar um sutiã..."
            show latinas 18 at right
            show judith 7 at left
            jud "Não é isso!!"
            show latinas 22 at right
            show judith 10 at left
            lopez "Você acha que vai chamar a atenção dos meninos, mostrando suas tetas assim?"
            show latinas 18 at right
            show judith 7 at left
            jud "Meus peitos são muito sensíveis!! Machuca quando eu uso sutiã..."
            jud "Eu me sinto mais confortável assim!!"
            show latinas 22 at right
            show judith 10 at left
            lopez "Haha!"
            show latinas 21 at right
            show judith 9 at left
            martinez "É melhor não ficar por aqui..."
            martinez "PUTA! Você acabou de ouvir? Este é o nosso território, então, saia!"
            show latinas 18 at right
            show player 12 at Position( xpos = 290, ypos = 768)
            hide judith 9
            show judith 9 at left
            with dissolve
            player_name "O que está acontecendo aqui?!"
            show player 114
            jud "{b}*chorando*{/b}"
            hide combo 7 at left
            show player 90 at Position( xpos = 290, ypos = 768)
            show judith 9 at left
            show latinas 20 at right
            martinez "Você defende essa puta feia agora??"
            show latinas 19 at right
            lopez "Anda, branquelo!"
            show latinas 18 at right
            show player 113
            player_name "Você está bem, {b}Judith{/b}?"
            show latinas 20 at right
            hide judith
            $ judith_in_toilet = True
            show player 90 at left
            with dissolve
            martinez "E aí, branquelo, você não vai correr atrás da sua puta?"
            show latinas 18 at right
            show player 12 at left
            player_name "Você não precisava fazer isso..."
            show latinas 20 at right
            martinez "Faremos o que nós quisermos!"
            show latinas 22 at right
            lopez "Haha! Até!"
            hide player 12 at right with dissolve
            hide latinas 22 at right with dissolve
            $ left_hall_dialogue_advancement = True

        elif left_hall_dialogue_count == 3 and not girl_lockerroom_unlocked:
            scene lefthall
            show player 11 with dissolve
            player_name "..."
            show player 10
            player_name "...Onde está a {b}Judith{/b}?"
            player_name "( Ela geralmente fica no corredor. )"
            show player 34
            player_name "Hmm..."
            show player 35
            player_name "( Consig {b}ouvir{/b} algo... )"
            show player 10
            player_name "( É alguém... chorando? )"
            show player 12
            player_name "( Parece que o choro vem do {b}vestiário feminino{/b}... )"
            hide player 12 with dissolve
            $ girl_lockerroom_unlocked = True
    else:

        if quest11 in quest_list and quest11 not in completed_quests and not left_hall_cult_seen:
            scene cult_event 5
            with dissolve
            window hide
            $ renpy.pause()
            scene cult_event 6
            with Dissolve(0.3)
            $ renpy.pause()
            scene expression "backgrounds/location_lefthall_night.jpg"
            with Dissolve(0.3)
            scene lefthall_night
            show player 11 at left with dissolve
            show erik 1 at right with dissolve
            player_name "..."
            show player 12
            player_name "Eles entraram no depósito?"
            show player 90
            show erik 5
            eri "Por que elas vão ali?"
            show player 35
            show erik 1
            player_name "A pergunta é: como eles poderiam caber lá?"
            player_name "Deve levar para outro lugar..."
            show player 34
            show erik 5
            eri "Podemos ir agora?"
            show player 12
            show erik 1
            player_name "Vamos apenas manter o nosso plano original e olhar em volta."
            show player 1
            show erik 3
            eri "Ok..."
            hide player 1 with dissolve
            hide erik 3 with dissolve
            $ left_hall_cult_seen = True
    $ callScreen(location_count)

label judith_button_dialogue:
    if left_hall_dialogue_count == 1 and not left_hall_dialogue_advancement:
        scene location_lefthall_closeup
        show player 1 at left with dissolve
        show judith 5 at right with dissolve
        jud "Oi {b}[firstname]{/b}!"
        show player 2 at left
        show judith 4 at right
        player_name "Oi {b}Judith{/b}, como você está?"
        show player 1 at left
        show judith 5 at right
        jud "Oh, estou ótimo!"
        show judith 2 at right
        jud "Eu... Eu só queria agradecer."
        show judith 4 at right
        show player 21 at left
        player_name "Oh. Pelo que?"
        show judith 3 at right
        show player 13 at left
        jud "No vestiario... Você me fez sentir... segura."
        show judith 4 at right
        show player 11 at left
        player_name "Oh..."
        show judith 5 at right
        jud "E, sabe... você enfrentou a {b}Annie{/b}. Achei muito corajoso da sua parte."
        show judith 4 at right
        show player 29 at left
        player_name "Está tudo bem, {b}Judith{/b}. Só queria fazer a coisa certa."
        player_name "Eu deveria ser o desculpe ... por mostrar o meu ... você sabe..."
        show judith 5 at right
        show player 11 at left
        jud "Sem problemas, eu gostei-"
        show judith 3 at right
        jud "Diego... Não me importo, na verdade."
        show judith 5 at right
        jud "Nós simplesmente... nos conhecemos um pouco melhor!"
        show judith 4 at right
        show player 21 at left
        player_name "Haha. Sim. Acho que sim..."
        show judith 5 at right
        show player 1 at left
        jud "Tenho que ir! Te vejo na aula então!"
        show player 14 at left
        show judith 4 at right
        player_name "Até!"
        hide player 14 at left with dissolve
        hide judith 4 at left with dissolve
        $ left_hall_dialogue_advancement = True
    $ callScreen(location_count)

label door64_locked_dialogue:
    scene lefthall
    show player 35 at left
    player_name "(Esta é a aula errada. )"
    $ callScreen(location_count)

label door64_locked2_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( Eu deveria ir para o {b}campo{/b} para minha aula de {b}educação física{/b}. )"
    $ callScreen(location_count)

label door14_locked_dialogue:
    scene lefthall
    show player 35 at left
    player_name "( O depósito está fechado. )"
    $ callScreen(location_count)

label door14b_locked_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( Eu deveria ir para o {b}campo{/b} para minha aula de {b}educação física{/b}. )"
    $ callScreen(location_count)

label door16_locked_dialogue:
    scene lefthall
    show player 35 at left
    player_name "( O vestiário feminino está interditado, eu não deveria ir lá. )"
    $ callScreen(location_count)

label door16b_locked_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( Eu deveria ir para o {b}campo{/b} para minha aula de {b}educação física{/b}. )"
    $ callScreen(location_count)

label door16c_locked_dialogue:
    scene lefthall
    show jersey 10 at left
    player_name "( Preciso tomar banho no {b}vestiário{/b} primeiro. )"
    $ callScreen(location_count)

label denied_access_lefthall:
    scene lefthall_night
    show erik 1f at Position (xpos = 550, ypos = 768)
    show player 34 at Position (xpos = 370, ypos = 768)
    player_name "Hmm..."
    show player 113
    player_name "( Tenho que encontrar {b}outra forma{/b}. )"
    hide player 113
    hide erik 1f
    $ callScreen(location_count)

label denied_access_utility:
    scene lefthall_night
    show player 1 at left
    show erik 1 at right
    with dissolve
    player_name "( Está traancado... )"
    player_name "( Só vou seguir o plano original e dar uma olhada. )"
    hide player 1 with dissolve
    hide erik 1 with dissolve
    $ callScreen(location_count)

label denied_locker_room_dialogue:
    scene lefthall
    show player 10 at left
    player_name "( Melhor evitar o {b}vestiário{/b} por hoje. {b}Dexter{/b} poderá me procurar por lá. )"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
