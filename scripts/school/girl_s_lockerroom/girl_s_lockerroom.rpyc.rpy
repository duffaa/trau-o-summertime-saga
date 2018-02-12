label girl_lockerroom_dialogue:
    $ location_count = "School Girl's Lockerroom"
    if not judith_sobbing:
        scene girl_lockerroom
        show player 106 at left with dissolve
        player_name "Uau! Tem um buraco gigante no chão..."
        player_name "( Agora eu entendo porque fechar! )"
        show player 90
        player_name "..."
        show player 10
        player_name "( Ainda ouço choros. )"
        player_name "( É de {b}alguém aqui{/b}... )"
        $ judith_sobbing = True
        hide player 10 with dissolve
    $ callScreen(location_count)

label judith_toilet:
    if not judith_daylock:
        if not judith_sex_sequence_unlocked:
            scene toilet_stall
            $ left_hall_dialogue_count = 4
            show judith 11 zorder 1 at Position( xpos = 310, ypos = 768) with dissolve
            window hide
            pause
            show player 106f zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
            player_name "!!!"
            jud "{b}*choros*{/b}"
            show player 108
            player_name "{b}Judith{/b}?!"
            show judith 13
            show player 109
            jud "...Oi, {b}[firstname]{/b}."
            show judith 12
            show player 108
            player_name "Você está bem?"
            show judith 13
            show player 109
            jud "Só queria ficar longe de todos."
            show judith 12
            show player 108
            player_name "Como assim?"
            show judith 13
            show player 109
            jud "Ninguém gosta de mim... E todos riem do meu corpo..."
            jud "...pelo menos aqui eu não vou ser uma piada."
            show judith 12
            show player 108
            player_name "Você não pode deixar as pessoas fazerem isso!"
            show judith 13
            show player 109
            jud "Tem certeza. Mas eu sou feia..."
            menu:
                "Você não é feia!":
                    show player 111
                    show judith 12
                    player_name "Não acho que você seja tão feia!!"
                    show judith 15
                    show player 110
                    jud "...Sério?"
                    show judith 14
                    show player 111
                    player_name "Sim!"
                    player_name "Acho que você é bonita!"
                    show judith 15
                    show player 110
                    jud "Essa é... a coisa mais bonita que alguém já me disse..."
                    show judith 14
                    show player 111
                    player_name "Só estou sendo honesto... E eu sei que não sou o único!"
                    player_name "Você só tem que ignorar tudo isso."
                    show judith 15
                    show player 110
                    jud "Tem razão..."
                    show judith 14
                    show player 111
                    player_name "Que seja, deveriamos sair e ir para a aula."
                    show judith 17
                    show player 106f
                    jud "Espera!!"
                    jud "Fique mais um pouco aqui... Aqui {b}comigo{/b}..."
                    menu:
                        "Ok.":
                            show judith 16
                            show player 111
                            player_name "Oh... Ok."
                            show judith 17
                            show player 110
                            jud "Você se lembra do outro dia quando..."
                            jud "...Estávamos no banheiro? Na frente da {b}Annie{/b}?"
                            show judith 16
                            show player 111
                            player_name "Sim?"
                            show judith 17
                            show player 110
                            jud "Então, eu... eu gostei do jeito que você me olhou."
                            show judith 16
                            show player 106f
                            player_name "!!!"
                            show judith 17
                            jud "Não foi só seus olhos... Seu corpo também reagiu."
                            show judith 16
                            player_name "..."
                            show judith 17
                            jud "Foi meus {b}peitos{/b} que fizeram... você feliz? {b}Aí em baixo{/b}?"
                            show judith 16
                            show player 111
                            player_name "Des... Desculpa!"
                            show judith 17
                            show player 106f
                            jud "Não se desculpe!!"
                            jud "...Eu gostei e..."
                            jud "...Estava pensando se você, sabe, quisesse ver de novo?"
                            menu:
                                "Claro.":
                                    show judith 16
                                    show player 111
                                    player_name "Acho que sim..."
                                    show judith 17
                                    show player 106f
                                    jud "Veja."
                                    hide player
                                    show judith 18 at Position(xpos = 447, ypos = 768)
                                    player_name "!!!"
                                    show judith 19
                                    window hide
                                    pause
                                    show judith 20
                                    window hide
                                    pause
                                    show judith 21
                                    window hide
                                    pause
                                    show judith 22
                                    window hide
                                    pause
                                    show judith 24
                                    jud "É tão... bonito..."
                                    jud "...E grosso."
                                    show judith 23
                                    player_name "{b}*Gasp*{/b}"
                                    show judith 24
                                    jud "Adoro sentir isso na minha mão..."
                                    show judith 25_23
                                    pause 4
                                    jud "..."
                                    show judith 23
                                    jud "Você quer tocar meus seios?"
                                    menu:
                                        "Sim.":
                                            $ judith_sex_sequence_unlocked = True
                                            player_name "Sim! Adoraria..."
                                            show judith 33
                                            player_name "..."
                                            show judith 34
                                            player_name "Wow..."
                                            show judith 35
                                            jud "Vai em frente!"
                                            jud "Toque... Mas seja gentil! Eles são bem sensíveis..."
                                            show judith 36_37_38
                                            pause 4
                                            show judith 39 with hpunch
                                            jud "*gemendo*"
                                            player_name "!!!"
                                            show judith 33
                                            jud "É muito. Meu corpo fica todo distorcido quando você toca meus mamilos..."
                                            show judith 4f zorder 1 at Position( xpos = 310, ypos = 768)
                                            show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
                                            player_name "Não queria te machucar."
                                            show player 13f
                                            show judith 5f
                                            jud "Não, sem problemas! É muito bom... Só que sou sensível..."
                                            show judith 4f
                                            show player 10f
                                            player_name "Talvez devessemos parar..."
                                            show player 13f
                                            show judith 5f
                                            jud "Sim... Obrigada por ficar aqui comigo, me sinto melhor..."
                                            show judith 2f
                                            jud "...E se você quiser, poderíamos fazer isso novamente, outra hora..."
                                            show judith 4f
                                            show player 17f
                                            player_name "Eu adoraria!"
                                            show judith 5f
                                            show player 13f
                                            jud "Te vejo depois então."
                                            hide player
                                            hide judith
                                            with dissolve
                                            jump left_hall_dialogue
                                        "Devemos parar.":

                                            show judith 24
                                            player_name "Acho que devemos parar..."
                                            show judith 6f zorder 1 at Position( xpos = 310, ypos = 768)
                                            show player 112 zorder 0 at Position (xpos = 639, ypos = 768)
                                            player_name "Não podemos nos atrasar para a aula, {b}Annie{/b} pode nos achar aqui..."
                                            show player 13f
                                            show judith 2f
                                            jud "Entendo. Agradeço por ficar comigo..."
                                            show judith 3f
                                            jud "...E se você quiser, podemos fazer isso de novo, outra hora..."
                                            show judith 4f
                                            show player 17f
                                            player_name "Adoraria!"
                                            show player 13f
                                            show judith 5f
                                            jud "Te vejo mais tarde então."
                                            hide player
                                            hide judith
                                            with dissolve
                                            jump left_hall_dialogue
                                "Não posso.":

                                    show judith 16
                                    show player 108
                                    player_name "Não posso fazer isso agora, {b}Judith{/b}..."
                                    player_name "E outra, deveriamos ir... Não quero me atrasar e a {b}Annie{/b} pode nos achar aqui..."
                                    show judith 13
                                    show player 109
                                    jud "Oh..."
                                    jud "Pode ir então. Acho que vou ficar mais um pouco aqui..."
                                    show player 111
                                    show judith 14
                                    player_name "Certo, te vejo mais tarde então."
                                    jump left_hall_dialogue
                        "Deveríamos ir.":

                            show judith 16
                            show player 108
                            player_name "Deveríamos ir... Não quero me atrasar e a {b}Annie{/b} já está na minha cola..."
                            show judith 13
                            show player 109
                            jud "Oh..."
                            jud "Pode ir. Vou ficar mais um pouco aqui..."
                            show judith 14
                            show player 111
                            player_name "Certo, até mais."
                            jump left_hall_dialogue
                "Eu sei...":

                    show judith 12
                    show player 108
                    player_name "Eu sei, mas você tem que superar isso!"
                    show player 109
                    jud "..."
                    show judith 11
                    jud "{b}*choranco*{/b}"
                    show player 108
                    player_name "Desculpa..."
                    show player 106f
                    jud "Quero ficar sozinha agora."
                    show player 108
                    player_name "Te vejo depois então..."
                    jump left_hall_dialogue
        else:

            scene toilet_stall
            show judith 14 zorder 1 at Position( xpos = 310, ypos = 768)
            show player 111 zorder 0 at Position (xpos = 639, ypos = 768) with dissolve
            player_name "Oi!"
            show judith 15
            show player 110
            jud "Estava esperando que você viesse me ver..."
            jud "Alguém viu você entrando aqui?"
            show judith 14
            show player 108
            player_name "Acho que não."
            show judith 14
            show player 110
            jud "Oh, ótimo..."
            jud "Emm... Então? O que você quer fazer?"
            call screen judith_stage01
    else:

        scene toilet_stall
        show player 11 with dissolve
        player_name "..."
        show player 10
        player_name "( {b}Judith{/b} não está aqui. )"
        player_name "( Ela deve ter ido pra casa, ou ainda está na aula. )"
        show player 108f
        player_name "( Eu deveria tentar voltar {b}amanhã{/b}. )"
        hide player 108f
        jump girl_lockerroom_dialogue

label judith_kiss:
    $ judith_daylock = True
    show player 108
    show judith 14
    player_name "Hmm... Você já beijou alguém?"
    show judith 15
    show player 110
    jud "Vocẽ quer dizer... Beijo, beijo?"
    show judith 14
    show player 17f
    player_name "Sim, é!"
    show judith 13
    show player 110
    jud "Não..."
    show judith 14
    show player 17f
    player_name "Vamos tentar então!"
    show judith 4f
    show player 110
    jud "..."
    hide player
    show judith 31_32 at Position ( xpos = 380, ypos = 768)
    with dissolve
    pause 4
    show judith 5f zorder 1 at Position( xpos = 320, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 640, ypos = 768)
    with dissolve
    jud "Isso foi... bom..."
    show judith 4f
    show player 17f
    player_name "Um pouco estranho eu acho. Ha ha."
    show judith 5f
    show player 11f
    jud "Vamos fazer outra coisa!"
    show judith 4f
    show player 14f
    player_name "Ok..."
    call screen judith_stage02

label judith_handjob:
    show player 111
    show judith 16
    player_name "Tipo da última vez?"
    show judith 17
    show player 106f
    jud "Deixa que eu faço."
    hide player
    show judith 18 at Position(xpos = 465, ypos = 768)
    player_name "!!!"
    show judith 19
    window hide
    pause
    show judith 20
    window hide
    pause
    show judith 21
    window hide
    pause
    show judith 22
    window hide
    pause
    show judith 24
    jud "É tão... bonito..."
    jud "...e grosso."
    show judith 23
    player_name "{b}*Gasp*{/b}"
    show judith 24
    jud "Adoro sentir nas minhas mãos..."
    show judith 25_23
    pause 4
    player_name "É tão... bom!"
    show judith 24
    jud "Você quer que eu pare?"
    call screen judith_stage03

label judith_keepgoing:
    show judith 25_23
    pause 4
    player_name "É tão... bom!"
    show judith 24
    jud "Você quer que eu pare?"
    call screen judith_stage03

label judith_playwithtits:
    show judith 33
    jud "..."
    show judith 35
    jud "Você gosta deles?"
    show judith 34
    player_name "Sim..."
    show judith 36
    player_name "Seus peitos são tão bonitos e macios..."
    show judith 36_37_38
    pause 4
    show judith 39 with hpunch
    jud "{b}*gemendo*{/b}"
    player_name "!!!"
    show judith 35
    jud "Quer fazer outras coisas?"
    call screen judith_stage03

label judith_cum:
    show judith 25_23
    pause 4
    show judith 26
    pause .3
    show judith 27
    jud "..."
    show judith 28
    jud "Wow, foi muita porra!"
    show judith 29
    player_name "Desculpa! Não queria fazer toda essa sujeira..."
    show judith 28
    jud "Está tudo bem..."
    jud "Sempre quis saber como que era!"
    show judith 30
    player_name "Oh. Ha ha!"
    show judith 5f zorder 1 at Position( xpos = 300, ypos = 768)
    show player 13f zorder 0 at Position (xpos = 623, ypos = 768)
    jud "Podemos fazer de novo..."
    show player 17f
    show judith 4f
    player_name "Eu adoraria!"
    show player 13f
    show judith 5f
    jud "Eu também..."
    show player 2f
    show judith 4f
    player_name "Deveíamos sair daqui..."
    show player 1f
    show judith 5f
    jud "Ok!"
    $ gTimer.tick()
    if not gTimer.is_dark():
        jump left_hall_dialogue
    else:
        jump night_closed_school

label judith_pullpants:
    show judith 24
    jud "Não estou... pronta pra isso ainda."
    show judith 23
    player_name "Oh... Tudo bem! Não precisamos."
    show judith 24
    jud "Talvez outra hora..."
    jud "...Quando eu me sentir mais confortável."
    show judith 23
    player_name "Tudo bem."
    show judith 24
    jud "Podemo fazer outra coisa?"
    call screen judith_stage03
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
