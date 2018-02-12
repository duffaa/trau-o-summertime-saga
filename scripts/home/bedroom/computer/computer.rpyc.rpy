default current_camshow = 1

label MC_computer:
    if gTimer.is_night():
        scene bedroom_night
        show player 24 at left
        player_name "( Estou tão cansado agora, eu deveria ir pra cama... )"
        hide player 17 at left
        $ callScreen(location_count)
    else:
        call screen MC_computer

label MC_pass_check:
    if MC_pass.lower().strip() == "cookies":
        scene expression gTimer.image("backgrounds/computer_player_01{}.jpg")
        $ MC_comp_locked = False
        call screen MC_computer
    else:
        scene expression gTimer.image("backgrounds/computer_player_01{}.jpg")
        show sis_wrong_pass at Position(xpos=570, ypos= 448) with dissolve
        $ renpy.pause()
        hide sis_wrong_pass with dissolve
        call screen MC_computer

label egay_search_dialogue:
    if erik.started(erik_orcette):
        scene player_computer_bg
        show player_computer_egay_search
        player_name "( Hmm ... Acho que deveria pesquisar o item que Erik queria. )"
        player_name "( O que era mesmo? )"
        hide player_computer_egay_search
        hide player_computer_bg
    show screen MC_computer
    call screen egay("Search")

label egay_purchased_dialogue:
    scene player_computer_bg
    show player_computer_egay_purchased
    player_name "( Parece que a entrega chegará na {b}terça-feita{/b}. )"
    hide player_computer_egay_purchased
    hide player_computer_bg
    show screen MC_computer
    call screen egay("Purchased")

label egay_search:
    if erik.started(erik_orcette):
        if egay_search.lower() == "orcette":
            show screen MC_computer
            call screen egay("Found")
    show screen MC_computer
    call screen egay("Fail")

label webcam_dialogue:
    scene expression gTimer.image("MC_computer{}_b")
    if not connected:
        scene player_computer_bg
        show player_computer_webscreen
        player_name "( Que estranho. Diz que posso me conectar a essa {b}webcam{/b}, mas parece que não posso fazer daqui. )"
        hide player_computer_webscreen
        hide player_computer_bg
        call screen MC_computer

    elif (not shower.occupied("sis", False) and gTimer.is_morning()):
        if sister.started(sis_webcam01):
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(ypos = 746)
            sis "Olá pessoaaaaal!"
            sis "Vocês estão prontos para uma apresentação?"
            sis "Eu estava ansiosa para ficar molhadadinha o dia todo!"
            sis "Ah! Não se esqueça de se inscrever para assistir a próxima parte do show..."
            sis "Por que essa lindinha aqui precisa de dinheiro!"
            show sissex 8 with fastdissolve
            sis "Agora, para meus inscritos especiais..."
            sis "... Quero apresentar esse novo brinquedinho!"
            show sissex 7 with fastdissolve
            pause
            show sissex 10 with fastdissolve
            pause
            show sissex 9
            sis "O {b}Electro Clit{/b}!"
            sis "É um brinquedinho vibrante... para o meu clitóris!"
            show sissex 11
            sis "Eu sempre quis um desse!"
            show sissex 21 at Position(xpos = 543, ypos = 767) with dissolve
            sis "Vamos testar, menino..."
            show sissex 22 with fastdissolve
            sis "Woah! Essa coisa é rápida..."
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow01_loop:
                $ current_camshow = 1
                show sissex 22 at Position(xpos = 543, ypos = 767)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 22
                    hide screen camshow_buttons
                    show sissex 23_24_25_22 at Position(xpos = 543, ypos = 767)
                    pause 8
                    hide sissex 23_24_25_22
                    show sissex 22 at Position(xpos = 543, ypos = 767)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 23
                        pause
                        show sissex 24
                        pause
                        show sissex 25
                        pause
                        show sissex 22
                        pause
                        $ animcounter += 1
                    show sissex 23
                    pause
                    show sissex 24
                    pause
                    show sissex 25
                    pause
                    show sissex 22
                call screen camshow_options

            label sis_camshow01_finish:
                show sissex 25b
                sis "Ahhh!!!" with vpunch
                sis "{b}*ofegante*{/b}"
                sis "Isso foi incrível!"
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "Woah..."
                player_name "( Minha irmã é um camgirl?! )"
                show player 310
                player_name "( Não sei o que pensar sobre isso. )"
                player_name "( É tão estranho ver ela assim... )"
                show player 312
                player_name "Cara, sei que não devia e excitar com essa coisa, mas..."
                show player 310
                player_name "( Acho que é o suficiente por hoje. )"
                hide player
                $ sis_webcam01.finish()
                if not sister.known(sis_telescope01):
                    $ sister.add_event(sis_telescope01)
                $ gTimer.tick()
                $ callScreen(location_count)

        elif sister.started(sis_webcam02):
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(ypos = 746)
            sis "Olá pessoaaaaal!"
            sis "Vocês estão prontos para uma apresentação?"
            sis "Eu estava ansiosa para ficar molhadadinha o dia todo!"
            sis "Ah! Não se esqueça de se inscrever para assistir a próxima parte do show..."
            sis "Por que essa lindinha aqui precisa de dinheiro!"
            show sissex 8 with fastdissolve
            sis "Agora, para os meus inscritos especiais..."
            sis "... Eu tenhoesse novo brinquedo para testar. "
            show sissex 7 with fastdissolve
            pause
            show sissex 13 with fastdissolve
            pause
            show sissex 12
            sis "O {b}Ultra Vibrator 2000{/b}!"
            sis "É um dildo! Grande e com nervos..."
            sis "Agora, já que você continuam pedindo para ver eu enfiar meus brinquedos..."
            sis "... Achei que eu lhes daria um pouco de prazer!"
            sis "Aqui vamos nós, rapazes!"
            show sissex 26 at Position(ypos = 770) with dissolve
            sis "Parece ter o tamanho perfeito para mim."
            sis "Vamos testar..."
            show sissex 27 with fastdissolve
            pause
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow02_loop:
                $ current_camshow = 2
                show sissex 31 at Position(xpos = 512, ypos = 770)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 31
                    hide screen camshow_buttons
                    show sissex 28_29_30_31 at Position(ypos = 770)
                    pause 8
                    hide sissex 28_29_30_31
                    show sissex 31 at Position(ypos = 770)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 28
                        pause
                        show sissex 29
                        pause
                        show sissex 30
                        pause
                        show sissex 31
                        pause
                        $ animcounter += 1
                    show sissex 28
                    pause
                    show sissex 29
                    pause
                    show sissex 30
                    pause
                    show sissex 31
                call screen camshow_options

            label sis_camshow02_finish:
                show sissex 28b
                sis "Oh céus... Eu estou quase lá..."
                show sissex 29b
                sis "Estou... gozando!!"
                show sissex 32
                sis "Ahh!!!" with vpunch
                show sissex 33 with dissolve
                sis "Eu... eu nunca fiz isso antes..."
                sis "Quanta sujeira..."
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "( Então é assim que é um squirt. )"
                show player 310
                player_name "É muito! Ela quase acertou a câmera!"
                player_name "( Não sabia que a {b}[sis_name]{/b} conseguia fazer isso... )"
                hide player
                $ sis_webcam02.finish()
                if not sister.known(sis_telescope02):
                    $ sister.add_event(sis_telescope02)
                $ gTimer.tick()
                $ callScreen(location_count)

        elif sister.started(sis_webcam03):
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(xpos = 534, ypos = 746)
            sis "Olá pessoaaaaal!"
            sis "Vocês estão prontos para uma apresentação?"
            sis "Eu estava ansiosa para ficar molhadadinha o dia todo!"
            sis "Ah! Não se esqueça de se inscrever para assistir a próxima parte do show..."
            sis "Por que essa lindinha aqui precisa de dinheiro!"
            show sissex 8 with fastdissolve
            sis "Agora, para meus inscritos especiais..."
            sis "Eu terei prazer em dobro nessa vez. "
            show sissex 7 with fastdissolve
            pause
            show sissex 19 at Position(xpos = 577) with fastdissolve
            pause
            show sissex 18 with fastdissolve
            sis "O {b}Dual Sybian{/b}!"
            show sissex 20
            sis "Li na internet falarem que eu tenho medo de anal..."
            sis "Então aqui é a que eu NÃO tenho medo disso!"
            sis "Na verdade, por que usar só um buraco?"
            sis "Para os meus fãs, vou fazer penetração dupla!"
            show sissex 18
            sis "Deixe-me subir nesse brinquedo e colocar no meu cu..."
            show sissex 34 at Position(xpos = 344, ypos = 727) with dissolve
            pause
            show sissex 35 at Position(xpos = 473, ypos = 582) with fastdissolve
            sis "... Oh, Deus! É um sentimento estranho."
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow03_loop:
                $ current_camshow = 3
                show sissex 35 at Position(xpos = 473, ypos = 582)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 35
                    hide screen camshow_buttons
                    show sissex 36_37_38_35 at Position(xpos = 473, ypos = 582)
                    pause 8
                    hide sissex 36_37_38_35
                    show sissex 35 at Position(xpos = 473, ypos = 582)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 36 at Position(xpos = 465)
                        pause
                        show sissex 37 at Position(xpos = 518)
                        pause
                        show sissex 38 at Position(xpos = 524)
                        pause
                        show sissex 35 at Position(xpos = 473)
                        pause
                        $ animcounter += 1
                    show sissex 36 at Position(xpos = 465)
                    pause
                    show sissex 37 at Position(xpos = 518)
                    pause
                    show sissex 38 at Position(xpos = 524)
                    pause
                    show sissex 35 at Position(xpos = 473)
                call screen camshow_options

            label sis_camshow03_finish:
                show sissex 39 at Position(xpos = 568)
                sis "Ahhh!!!" with hpunch
                sis "{b}*ofegante*{/b}"
                sis "Nunca gozei tanto assim antes..."
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "Wow..."
                player_name "( Ela ama cavalgar nessa coisa. )"
                show player 310
                player_name "( Eu me pergunto o que mais ela está disposta a fazer na câmera... )"
                hide player
                $ sis_webcam03.finish()
                if not sister.known(sis_telescope03):
                    $ sister.add_event(sis_telescope03)
                $ gTimer.tick()
                $ callScreen(location_count)

        elif sister.over(sis_webcam04):
            $ sis_lastwebcam_show_seen = True
            hide screen MC_webcam
            hide screen MC_computer
            scene player_computer_bg with None
            show player_computer_webscreen_connecting
            $ renpy.pause(2, hard=True)
            hide player_computer_webscreen_connecting
            scene siscam1
            show xtra 16 zorder 2
            show sissex 6 zorder 1 at Position(xpos = 534, ypos = 746)
            sis "Olá pessoaaaaal!"
            sis "Vocês estão prontos para uma apresentação?"
            sis "Eu estava ansiosa para ficar molhadadinha o dia todo!"
            sis "Ah! Não se esqueça de se inscrever para assistir a próxima parte do show..."
            sis "Por que essa lindinha aqui precisa de dinheiro!"
            show sissex 8 with fastdissolve
            sis "Agora, para meus inscritos especiais..."
            sis "... Eu tenho esse brinquedo assustador para testar. "
            show sissex 7 with fastdissolve
            pause
            show sissex 16 with fastdissolve
            pause
            show sissex 15
            sis "Ele se chama..."
            sis "O {b}Bad Monster{/b}!"
            show sissex 17
            sis "Todo mundo estava falando desse brinquedo especial..."
            sis "... e alguns de vocês duvidaram que eu enfiaria na minha buceta."
            show sissex 15
            sis "Eu finalmente consegui comprar!"
            show sissex 17
            sis "Agora, preparem suas carteira, porque estou prestes a domar este monstro!"
            show sissex 40 at Position(xpos = 427)
            sis "Isso precisa de um monte de lubrificante..."
            show sissex 41 at Position(xpos = 423)
            sis "... oh DEUS!"
            sis "É tão grande!"
            $ anim_toggle = False
            $ xray_toggle = False
            label sis_camshow04_loop:
                $ current_camshow = 4
                show sissex 41 at Position(xpos = 423, ypos = 746)
                show screen camshow_buttons
                hide screen camshow_options
                pause
                if anim_toggle:
                    hide sissex 41
                    hide screen camshow_buttons
                    show sissex 42_43_44_41 at Position(xpos = 423, ypos = 746)
                    pause 8
                    hide sissex 42_43_44_41
                    show sissex 41 at Position(xpos = 423, ypos = 746)
                else:

                    hide screen camshow_buttons
                    $ animcounter = 0
                    while (animcounter < 2):
                        show sissex 42 at Position(xpos = 425)
                        pause
                        show sissex 43 at Position(xpos = 426)
                        pause
                        show sissex 44 at Position(xpos = 425)
                        pause
                        show sissex 41 at Position(xpos = 423)
                        pause
                        $ animcounter += 1
                    show sissex 42 at Position(xpos = 425)
                    pause
                    show sissex 43 at Position(xpos = 426)
                    pause
                    show sissex 44 at Position(xpos = 425)
                    pause
                    show sissex 41 at Position(xpos = 423)
                    pause
                call screen camshow_options

            label sis_camshow04_finish:
                show sissex 43 at Position(xpos = 426)
                sis "Ahhh!!!" with vpunch
                show sissex 45 at Position(xpos = 428) with fastdissolve
                sis "Que monstro bom..."
                sis "... minha buceta ficará dolorida por dias!"
                hide xtra
                hide siscam1
                hide sissex
                scene bedroom_desk
                show player 311 at Position(xpos = 672)
                with fade
                player_name "( Eu pensei que essa coisa era apenas só pra mostrar. )"
                player_name "( Mas parece que é possível colocar lá! )"
                player_name "E ela fez com muita facilidade..."
                player_name "( Espero que ela não arranje confusão por ficar fazendo essas coisas na câmera. )"
                hide player
                $ gTimer.tick()
                $ callScreen(location_count)
        else:

            scene player_computer_bg
            show player_computer_webscreen
            player_name "( Não tem nada acontecendo no momento. )"
            hide player_computer_webscreen
            hide player_computer_bg
            show screen MC_computer
            call screen MC_webcam
    else:
        scene player_computer_bg
        show player_computer_webscreen
        player_name "( Não tem nada acontecendo no momento. )"
        hide player_computer_webscreen
        hide player_computer_bg
        show screen MC_computer
        call screen MC_webcam
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
