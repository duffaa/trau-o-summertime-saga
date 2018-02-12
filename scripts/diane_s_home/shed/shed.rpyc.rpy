label shed:
    $ location_count = "Diane's Shed"
    if aunt_had_sex:
        if gTimer.is_dark():
            if quest12 in completed_quests and quest13 not in quest_list and aunt.started(aunt_breeding_help):
                scene shed_night with None
                show aunt 89 at right
                show player 11 at left
                dia "Eu tenho {b}algo{/b} para você fazer."
                show aunt 88
                player_name "..."
                show player 21
                player_name "Sem problema! O que é?"
                show aunt 87
                show player 13
                dia "Eu tenho essa... {b}Encomenda{/b}, quero que você pegue para mim."
                show aunt 88
                show player 10
                player_name "Oh, ok."
                player_name "Onde está?"
                show aunt 89
                show player 13
                dia "Você terá que pegar no {b}shopping{/b}..."
                show aunt 90
                show player 11
                dia "...Tem uma loja chamada {b}Pink{/b}."
                dia "Eles estarão em meu nome!"
                show aunt 88
                show player 29
                player_name "Na loja {b}Pink{/b}?!"
                show player 21
                player_name "..."
                player_name "Mas, o que é isso?"
                show aunt 87
                show player 13
                dia "É algo para você... Mas é {b}surpresa{/b}!"
                show aunt 88
                show player 11
                player_name "!!!"
                show player 21
                player_name "Sério?"
                show player 108f
                player_name "O shopping está fechado agora, porém..."
                show player 21
                player_name "Eu posso ir amanhã."
                show aunt 90
                show player 13
                dia "Esse é o meu garoto..."
                show aunt 89
                $ quest_list.append(quest13)
                $ aunt_breeding_help.status = True
    else:

        scene expression gTimer.image("shed{}")
        if pump not in inventory.items and quest08 not in completed_quests:
            show pump_object at Position(xpos = 118, ypos = 437)

        if shed_dialogue == 0:
            show player 35 at left with dissolve
            player_name "Woah..."
            show player 34
            player_name "...Que celeiro estranho."
            player_name "Pro que todas essas caixas... e correntes?!"
            show player 43
            player_name "Não importa, vou tentar {b}achar a bomba{/b}..."
            $ shed_dialogue = 1
            hide player 43 with dissolve

        elif shed_dialogue == 1 and drink_milk_offer == True and aunt_shed_scene == False and gTimer.is_evening():
            scene shed_blur_night
            show aunt 57 at right with dissolve
            window hide
            pause
            show aunt 58 at right
            window hide
            pause
            show aunt 57 at right
            window hide
            pause
            show aunt 58 at right
            window hide
            pause
            show aunt 57 at right
            show player 11 at left with dissolve
            player_name "..."
            show player 23 at left
            player_name "{b}Tia Diane{/b}!??"
            show aunt 59 at right with hpunch
            show player 22 at left
            dia "!!!"
            show aunt 60 at right
            dia "O que você está fazendo aqui??!"
            show aunt 64 at right
            show player 29 at left
            player_name "Eu vi a porta aberta! E-"
            show player 3 at left
            player_name "..."
            show player 21 at left
            player_name "...Isso é a {b}bomba de tirar leite{/b}?"
            show aunt 61 at right
            show player 5 at left
            dia "{b}*suspiro*{/b}"
            show aunt 62 at right
            show player 11 at left
            dia "Sim, {b}[firstname]{/b}... Eu... gosto de me ordenhar às vezes..."
            show aunt 64 at right
            show player 12 at left
            player_name "Espera..."
            if drank_milk == True:
                player_name "É o leite que você me fez beber no outro dia??!"
            else:

                player_name "É o leite que você me ofereceu para beber o outro dia?!"
            show aunt 61 at right
            show player 11 at left
            dia "Eu sei... devia ter te contado..."
            show aunt 60 at right
            show player 5 at left
            dia "Mas é tudo natural, e não tive mais ninguém para provar!!"
            show aunt 61 at right
            dia "Você poderia me perdoar?"
            menu:
                "Está tudo bem.":
                    show aunt 64 at right
                    show player 21 at left
                    player_name "Está tudo bem, {b}tia Diane{/b}."
                    player_name "Não precisa se desculpar..."
                    show aunt 63 at right
                    show player 17 at left
                    if drank_milk == True:
                        player_name "...Na verdade, eu gostei!"
                    else:

                        player_name "...Estou feliz que você me ofereceu!"
                    show aunt 62 at right
                    show player 13 at left
                    dia "Isso é... tão fofo..."
                    show aunt 63 at right
                    show player 29 at left
                    player_name "Eu... deveria ir para casa agora."
                    show aunt 62 at right
                    show player 3 at left
                    dia "Sim, e eu estou indo pra dentro..."
                    dia "E, por favor-"
                    show aunt 64 at right
                    show player 21 at left
                    player_name "Não vou contar para a {b}[mom_name]{/b}. Não se preocupe."
                    show aunt 63 at right
                    show player 13 at left
                    dia "Obrigada."
                    hide player 13 at left with dissolve
                    hide aunt 63 at right with dissolve
                "Não, isso é errado.":

                    show aunt 64 at right
                    show player 12 at left
                    player_name "Não seia, {b}tia Diane{/b}."
                    if drank_milk == True:
                        player_name "Foi muito errado me fazer beber isso..."
                    else:

                        player_name "Foi muito errado me oferecer isso..."
                    show aunt 61 at right
                    show player 90 at left
                    dia "Eu sei..."
                    dia "Me desculpa!"
                    show aunt 64 at right
                    show player 12 at left
                    player_name "Estou indo para {b}casa{/b} agora..."
                    show aunt 60 at right
                    show player 13 at left
                    dia "Mas-"
                    show aunt 64 at right
                    show player 24 at left
                    player_name "Tchau..."
                    hide aunt 64 at right with dissolve
                    hide player 24 at left with dissolve
            $ aunt_shed_scene = True
    $ callScreen(location_count)

label locked_shed_dialogue:
    scene garden
    if seen_shed_locked == True:
        show player 34 with dissolve
        player_name "Hmm..."
        show player 35
        player_name "A porta está trancada."
        hide player 35 with dissolve
    else:

        show player 35 at left with dissolve
        player_name "Hmm.. o galpão está trancando. O que será que tem ali dentor?"
        show aunt 8 at right with dissolve
        show player 22 at left
        dia "Você está bisbilhotanto?"
        show aunt 9 at right
        show player 10 at left
        player_name "Uhh, desculpa. Estava vendo suas ferramentas..."
        show aunt 10 at right
        show player 11 at left
        dia "Está bem. Talvez um dia eu te dê um pequeno passeio..."
        show player 21 at left
        show aunt 9 at right
        player_name "Sem problemas, {b}tia Diane{/b}..."
        $ seen_shed_locked = True
        hide player 21 at left with dissolve
        hide aunt 9 at right with dissolve
    $ callScreen(location_count)

label aunt_dialogue_button_night:
    scene location_shed01_night_closeup
    show player 1 at left with dissolve
    show aunt 89 at right with dissolve
    dia "Hei, querido."
    dia "Preparado para aprender a ordenhar?"
    show aunt 88
    show player 17
    player_name "Claro! Adoraria ajudar!"
    show aunt 89
    show player 1
    dia "Bom garoto..."
    dia "Há algo de que você quer falar antes de começar?"
    label dia_default_dialogue_options_night:
        menu:
            "Entrega." if quest13 in quest_list and quest13 not in completed_quests and package not in inventory.items:
                show aunt 88
                show player 10
                player_name "Esqueci onde que tenho que pegar o {b}pacote{/b}."
                show player 29
                player_name "Como eu encontro?"
                show aunt 89
                show player 13
                dia "Você tem que pegar no {b}shopping{/b}."
                show aunt 87
                dia "Tem uma loja chamada {b}Pink{/b}."
                show aunt 89
                dia "Estará no meu nome!"
                show aunt 88
                show player 21
                player_name "Beleza. Entendi!"
                show aunt 89
                show player 13
                dia "Algo mais que você queira falar?"
                jump dia_default_dialogue_options_night

            "Entrega." if quest13 in quest_list and quest13 not in completed_quests and package in inventory.items:
                show player 239_240
                pause
                show aunt 88
                show player 170
                player_name "Peguei a sua {b}encomenda{/b}!"
                show aunt 90
                show player 169
                dia "Excelente!"
                $ completed_quests.append(quest13)
                $ inventory.items.remove(package)
                show aunt 119
                show player 11
                dia "Agora, fique aqui..."
                dia "...Já volto com uma surpresa."
                scene black with dissolve
                $ renpy.pause(0.5)
                scene shed_night

                show aunt 113 at right
                show player 23 at left
                with dissolve
                player_name "!!!" with hpunch
                show aunt 114
                show player 22
                dia "Então?"
                show aunt 115
                dia "...Gostou?"
                show aunt 113
                show player 29
                player_name "É bem... bem sexy, {b}tia Diane{/b}."
                show aunt 114
                show player 13
                dia "Sempre quis vestir isso... mas nunca tive alguém para vestir isso..."
                show aunt 113
                show player 11
                player_name "..."
                show aunt 116
                show player 23
                dia "Eu gosto da maneira como meus seios podem pendurar naturalmente, assim..."
                show player 22
                player_name "..."
                show aunt 114
                dia "Eu achei que isso fosse ajudá-lo a entrar no clima para... {b}ordenhar{/b}..."
                show aunt 113
                show player 29
                player_name "Bom, está funcionando! Haha..."
                show aunt 114
                show player 13
                dia "Então... Uhm..."
                dia "O que você quer fazer agora?"
                jump dia_default_dialogue_options_night

            "Vamos ordenhar!" if quest12 not in completed_quests or quest13 not in completed_quests:
                show aunt 88
                show player 21
                player_name "Estou pronto para começar se você quiser."
                show aunt 87
                show player 11
                dia "Ainda não!"
                show aunt 89
                show player 13
                dia "Você precisa fazer {b}algumas coisinhas{/b} que eu te pedi antes de começarmos..."
                show aunt 88
                show player 21
                player_name "Ah, certo!"
                show player 17
                player_name "Foi mal, vou fazer isso..."
                show aunt 90
                show player 13
                dia "Não se preocupe. nós vamos fazer isso daqui a pouquinho..."


            "Vamos ordenhar!" if quest12 in completed_quests and quest13 in completed_quests:
                if shed_had_sex == False:
                    show aunt 113
                    show player 17
                    player_name "Vamos produzir um pouco de leite!"
                    show aunt 114
                    show player 2
                    dia "Estava esperando você falar isso..."
                    show aunt 112
                    dia "Mas antes de começar, eu tenho que me preparar para a extração de leite!"
                    show aunt 113
                    show player 12
                    player_name "Como você faz isso?"
                    show aunt 117
                    show player 11
                    dia "Com isso!"
                    dia "Eu tenho que prender essas bombas de sucção..."
                    player_name "!!!"
                    show aunt 113
                    show player 21
                    player_name "Elas... machucam?"
                    show aunt 115
                    show player 13
                    dia "Haha. Na verdade não..."
                    show aunt 114
                    dia "Parece um pouco estranho quando bombeia, mas eu gosto!"
                    show aunt 113
                    show player 21
                    player_name "Legal!"
                    show aunt 114
                    show player 11
                    dia "Sabe, eles dizem que as vacas lactam mais quando estão... {b}fertilizadas{/b}..."
                    show aunt 113
                    player_name "..."
                    show player 29
                    player_name "Eu... eu não entendi-"
                    show aunt 112
                    show player 13
                    dia "Só digo que... Vacas grávidas produzem mais leite!"
                    show player 11
                    show aunt 114
                    dia "O que estou tentando dizer é... Sua tia precisa de um touro para... {b}reproduzir{/b}..."
                    show aunt 113
                    show player 23
                    player_name "!!!"
                    show aunt 114
                    show player 22
                    dia "...Você acha que poderia ajudar a {b}titia{/b} com isso?"
                    show aunt 113
                    show player 29
                    player_name "...Sim, Eu... adoraria ajudar..."
                    show aunt 114
                    show player 13
                    dia "Bom garoto!"
                    show player 11
                else:

                    show aunt 113
                    show player 17
                    player_name "Vamos produzir um pouco de leite!"
                    show aunt 114
                    show player 2
                    dia "Estava esperando você falar isso..."
                    dia "Mal pudo esperar para você voltar!"
                    show aunt 112
                    show player 11
                    dia "Mas antes de começarmos, deixe-me entrar no clima!"

                    show player 11
                    show aunt 116
                    dia "Como estou?"
                    show player 21
                    player_name "Linda, {b}tia Diane{/b}!"
                    show player 13
                    show aunt 112
                    dia "Agora, quando você me por na cadeira..."
                    dia "Certifique-se de gozar bem {b}lá no fundo{/b}...."
                    show player 11
                    show aunt 113
                    player_name "!!!"
                    show player 23
                    show aunt 114
                    dia "Eu preciso que meu touro me.... {b}reproduza{/b} bem..."
                    show aunt 112
                    show player 22
                    dia "...Você acha que poderia ajudar a {b}titia{/b} com isso?"
                    show aunt 113
                    show player 29
                    player_name "...Sim, Eu... eu posso te ajudar com isso..."
                    show aunt 115
                    show player 13
                    dia "Esse é o meu garoto!"
                    show player 11
                    show aunt 114
                dia "Vamos preparar a {b}cadeira de ordenhar{/b}..."
                scene shed_closeup 1
                show auntsex 36 at Position (xpos = 571, ypos = 729)
                show expression "characters/aunt/char_aunt_sex_37.png" at Position (xpos = 528, ypos = 769)
                with dissolve
                dia "Agora enfie devagar..."
                dia "...E não solte até que você goze bem {b}fundo{/b} dento de mim..."

                hide expression "characters/aunt/char_aunt_sex_37.png"
                show auntsex 38 at Position (xpos = 544, ypos = 729)
                show expression "characters/aunt/char_aunt_sex_39.png" at Position (xpos = 552, ypos = 769)
                dia "Assim..."
                hide expression "characters/aunt/char_aunt_sex_39.png"
                show auntsex 40 at Position (xpos = 547, ypos = 729)
                show expression "characters/aunt/char_aunt_sex_41.png" at Position (xpos = 549, ypos = 769)
                dia "{b}*Gemido*{/b}"
                hide expression "characters/aunt/char_aunt_sex_41.png"
                $ anim_toggle = False
                $ shed_xray_toggle = False
                $ shed_cow_outfit = True
                $ shed_sex_angle = 0
                $ M_aunt.set('sex speed', .4)

                label shed_sex_loop:
                    scene shed_closeup 1

                    if anim_toggle == True:
                        hide auntsex_cowoutfit
                        hide auntsex_xray
                        hide auntsex_cowoutfit_xray
                        hide auntsex
                        hide screen shed_sex_visuals

                        if shed_sex_angle == 0:
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 39_41 at Position(xpos = 544, ypos = 729)
                            elif shed_cow_outfit == False and shed_xray_toggle == True:
                                show auntsex_xray 42_43 at Position(xpos = 544, ypos = 729)
                            elif shed_cow_outfit == True and shed_xray_toggle == True:
                                show auntsex_cowoutfit_xray 39_41_42_43 at Position(xpos = 544, ypos = 729)
                            else:
                                show auntsex 38_40 at Position(xpos = 544, ypos = 729)
                        else:

                            scene shed_closeup 2
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 51_53 at Position(xpos = 590, ypos = 768)
                            elif shed_cow_outfit == False and shed_xray_toggle == True:
                                show auntsex_xray 46_47 at Position(xpos = 590, ypos = 768)
                            elif shed_cow_outfit == True and shed_xray_toggle == True:
                                show auntsex_cowoutfit_xray 51_53_46_47 at Position(xpos = 590, ypos = 768)
                            else:
                                show auntsex 50_52 at Position(xpos = 590, ypos = 768)
                    else:

                        $ xray = 0
                        $ cow_outfit = 0
                        if shed_sex_angle == 0:
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                        else:

                            scene shed_closeup 2
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                        show screen shed_sex_visuals

                    show screen shed_sex_buttons
                    hide screen shed_sex_options
                    pause
                    if shed_sex_angle == 0:
                        scene shed_closeup 1
                        if anim_toggle == True:
                            hide auntsex_cowoutfit
                            hide auntsex_xray
                            hide auntsex_cowoutfit_xray
                            hide auntsex
                            hide screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 39_41 at Position(xpos = 544, ypos = 729)

                            elif shed_cow_outfit == False and shed_xray_toggle == True:
                                show auntsex_xray 42_43 at Position(xpos = 544, ypos = 729)

                            elif shed_cow_outfit == True and shed_xray_toggle == True:
                                show auntsex_cowoutfit_xray 39_41_42_43 at Position(xpos = 544, ypos = 729)
                            else:

                                show auntsex 38_40 at Position(xpos = 544, ypos = 729)
                            pause 8
                        else:

                            show screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 40 at Position(xpos = 547, ypos = 729)
                    else:

                        scene shed_closeup 2
                        if anim_toggle == True:
                            hide auntsex_cowoutfit
                            hide auntsex_xray
                            hide auntsex_cowoutfit_xray
                            hide auntsex
                            hide screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            if shed_cow_outfit == True and shed_xray_toggle == False:
                                show auntsex_cowoutfit 51_53 at Position(xpos = 590, ypos = 768)

                            elif shed_cow_outfit == False and shed_xray_toggle == True:

                                show auntsex_xray 46_47 at Position(xpos = 590, ypos = 768)
                            elif shed_cow_outfit == True and shed_xray_toggle == True:

                                show auntsex_cowoutfit_xray 51_53_46_47 at Position(xpos = 590, ypos = 768)
                            else:
                                show auntsex 50_52 at Position(xpos = 590, ypos = 768)
                            pause 8
                        else:

                            show screen shed_sex_visuals
                            hide screen shed_sex_buttons
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                            pause
                            $ xray = 0
                            $ cow_outfit = 0
                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                            pause
                            $ xray = 1
                            $ cow_outfit = 1
                            show auntsex 52 at Position(xpos = 595, ypos = 768)
                    call screen shed_sex_options

                label shed_ride:
                    $ shed_xray_toggle = False
                    hide screen shed_sex_visuals
                    scene shed_closeup 3
                    show auntsex 54
                    player_name "Você está tão molhadinha, tia Diane."
                    dia "Eu adoro sentir meu clitóris contra o seu pau duro."
                    dia "Fique parado..."

                    label shed_ride_loop:
                        show screen shed_sex_buttons
                        hide screen shed_sex_options
                        pause
                        hide screen shed_sex_buttons
                        if anim_toggle == True:
                            show auntsex 54_55
                            pause 8.4
                        else:

                            show auntsex 55
                            pause
                            show auntsex 54
                            pause
                            show auntsex 55
                            pause
                            show auntsex 54
                            pause
                            show auntsex 55
                            pause
                            show auntsex 54
                            pause
                            show auntsex 55
                            pause
                        call screen shed_sex_options

                label shed_fuck:
                    show auntsex 56
                    dia "Quero isso dentro de mim agora..."
                    label shed_fuck_loop:
                        show screen shed_sex_buttons
                        hide screen shed_sex_options
                        pause
                        hide screen shed_sex_buttons
                        if anim_toggle == True:
                            show auntsex 58_59_58_57
                            pause 8.5
                        else:

                            show auntsex 57
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 59 at Position(xoffset = 1)
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 57
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 59 at Position(xoffset = 1)
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 57
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                            pause
                            show auntsex 59 at Position(xoffset = 1)
                            pause
                            show auntsex 58 at Position(xoffset = -2)
                        call screen shed_sex_options

                label shed_milk:

                    if anim_toggle == True:
                        show auntsex 61_60
                    else:
                        show auntsex 60 at Position(xoffset = -45)
                    show screen shed_sex_buttons
                    hide screen shed_sex_options
                    pause
                    hide screen shed_sex_buttons
                    if anim_toggle == True:
                        show auntsex 61_60
                        pause 8
                    else:

                        show auntsex 61 at Position(xoffset = -45)
                        pause
                        show auntsex 60 at Position(xoffset = -45)
                        pause
                        show auntsex 61 at Position(xoffset = -45)
                        pause
                        show auntsex 60 at Position(xoffset = -45)
                        pause
                        show auntsex 61 at Position(xoffset = -45)
                        pause
                        show auntsex 60 at Position(xoffset = -45)
                        pause
                        show auntsex 61 at Position(xoffset = -45)
                    pause .3
                    show auntsex 62 at Position(xoffset = -45)
                    player_name "Woa..."
                    player_name "Ela gozou muito!"
                    dia "{b}*ofegante*{/b}"
                    dia "Você me ordenhou..."
                    call screen shed_sex_options

                label shed_sex_cum_in:
                    dia "Não segure..."
                    hide auntsex_cowoutfit
                    hide auntsex_xray
                    hide auntsex_cowoutfit_xray
                    hide screen shed_sex_options
                    label shed_sex_loop_2:
                        $ xray = 0
                        $ cow_outfit = 0
                        if shed_sex_angle == 0:
                            show auntsex 38 at Position(xpos = 544, ypos = 729)
                        else:

                            show auntsex 50 at Position(xpos = 590, ypos = 768)
                        show screen shed_sex_visuals
                        show screen shed_sex_buttons
                        pause
                        if shed_sex_angle == 0:
                            scene shed_closeup 1
                            if anim_toggle == True:
                                hide auntsex 38
                                hide screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                if shed_cow_outfit == True and shed_xray_toggle == False:
                                    show auntsex_cowoutfit 39_41 at Position(xpos = 544, ypos = 729)

                                elif shed_cow_outfit == False and shed_xray_toggle == True:
                                    show auntsex_xray 42_43 at Position(xpos = 544, ypos = 729)

                                elif shed_cow_outfit == True and shed_xray_toggle == True:
                                    show auntsex_cowoutfit_xray 39_41_42_43 at Position(xpos = 544, ypos = 729)
                                else:

                                    show auntsex 38_40 at Position(xpos = 544, ypos = 729)
                                pause 8
                                hide auntsex_cowoutfit 39_41
                                hide auntsex_xray 42_43
                                hide auntsex_cowoutfit_xray 39_41_42_43
                                hide auntsex 38_40
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                            else:

                                show screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 38 at Position(xpos = 544, ypos = 729)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 40 at Position(xpos = 547, ypos = 729)
                        else:

                            scene shed_closeup 2
                            if anim_toggle == True:
                                hide auntsex 50
                                hide screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                if shed_cow_outfit == True and shed_xray_toggle == False:
                                    show auntsex_cowoutfit 51_53 at Position(xpos = 590, ypos = 768)

                                elif shed_cow_outfit == False and shed_xray_toggle == True:
                                    show auntsex_xray 46_47 at Position(xpos = 590, ypos = 768)

                                elif shed_cow_outfit == True and shed_xray_toggle == True:
                                    show auntsex_cowoutfit_xray 51_53_46_47 at Position(xpos = 590, ypos = 768)
                                else:

                                    show auntsex 50_52 at Position(xpos = 590, ypos = 768)
                                pause 8
                                hide auntsex_cowoutfit 51_53
                                hide auntsex_xray 46_47
                                hide auntsex_cowoutfit_xray 51_53_46_47
                                hide auntsex 50_52
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                            else:

                                show screen shed_sex_visuals
                                hide screen shed_sex_buttons
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                                pause
                                $ xray = 0
                                $ cow_outfit = 0
                                show auntsex 50 at Position(xpos = 590, ypos = 768)
                                pause
                                $ xray = 1
                                $ cow_outfit = 1
                                show auntsex 52 at Position(xpos = 595, ypos = 768)
                        show screen shed_sex_visuals
                        $ shed_sex_count += 1
                    if shed_sex_count == 1:
                        hide screen shed_sex_buttons
                        dia "Goze bem lá dentro de mim..."
                        jump shed_sex_loop_2

                    elif shed_sex_count == 2:
                        hide screen shed_sex_buttons
                        dia "Me reproduza!!!"
                        jump shed_sex_loop_2

                    elif shed_sex_count == 3:
                        $ shed_sex_count = 0
                        $ xray = 1
                        $ cow_outfit = 1
                        if shed_sex_angle == 0:
                            scene shed_closeup 1
                            show auntsex 40 at Position (xpos = 547, ypos = 729)
                            show screen shed_sex_visuals
                        else:
                            scene shed_closeup 2
                            show auntsex 52 at Position (xpos = 595, ypos = 768)
                            show screen shed_sex_visuals
                        $ shed_cum = True
                        dia "{b}AAaaahh!!{/b}"
                        hide screen shed_sex_visuals
                        jump shed_sex_end

                label shed_sex_end:


                    if shed_sex_angle == 0:
                        show auntsex 36 at Position (xpos = 571, ypos = 729)
                        show expression "characters/player/char_player_sex_45.png" at Position (xpos = 725, ypos = 264)
                        if shed_cow_outfit == True:
                            show expression "characters/aunt/char_aunt_sex_37.png" at Position (xpos = 528, ypos = 769)
                    else:

                        show auntsex 48
                        show expression "characters/player/char_player_sex_49.png" at Position(xpos = 567, ypos = 495)
                        if shed_cow_outfit == True:
                            show expression "characters/aunt/char_aunt_sex_49.png" at Position (xpos = 481, ypos = 766)
                        pause
                        hide expression "characters/player/char_player_sex_49.png"
                        hide expression "characters/aunt/char_aunt_sex_49.png"
                        show auntsex 46
                        if shed_cow_outfit == True:
                            show expression "characters/aunt/char_aunt_sex_47.png" at Position (xpos = 478, ypos = 766)
                        show expression "characters/player/char_player_sex_50.png" at Position(xpos = 598, ypos = 539)
                    dia "Foi... tanta porra..."
                    player_name "Fiz bem?"
                    dia "Você me reproduziu bem."
                    dia "Valeu..."
                    scene shed_night
                    show player 1 at left
                    show aunt 89 at right
                    with dissolve
                    dia "Muito grata pela sua ajuda..."
                    show aunt 87
                    dia "Sua {b}titia{/b} terá um dos melhores leites da cidade!"
                    show player 2
                    show aunt 88
                    player_name "Eu gostei muito disso. Espero poder ajudá-la novamente em breve!"
                    show player 1
                    show aunt 89
                    dia "Planejo expandir meu negócio de leite, então..."
                    show aunt 90
                    dia "Terei muito trabalho para a feito por aqui!"
                    show aunt 89
                    dia "E uma ajuda sempre é aceita..."
                    show player 17
                    show aunt 88
                    player_name "Será um prazer!"
                    show player 1
                    show aunt 89
                    dia "Está ficando tarde. Você veria ir..."
                    show aunt 92
                    dia "Você não quer deixar sua mãe esperando!"
                    show player 21
                    show aunt 91
                    player_name "Sim."
                    show player 13
                    show aunt 87
                    dia "Lembre-se: É o nosso segredinho."
                    show player 21
                    show aunt 88
                    player_name "Não se preocupe, {b}tia Diane{/b}, não vou contar para ninguém."
                    show player 13
                    show aunt 90
                    dia "Esse é meu lindinho!"
                    show aunt 111 at left
                    dia "Teremos muita {b}diversão{/b} junto..."
                    hide aunt 111 at left
                    $ shed_cum = False
                    $ shed_had_sex = True
                    $ gTimer.tick()
                    $ in_garden = True
                    hide shed
                    jump garden_dialogue
            "Tenho que ir.":

                show aunt 88 at right
                show player 10 at left
                player_name "Adoraria fica e te ordenhar..."
                show aunt 91
                player_name "Mas está ficando muito tarde e a {b}[mom_name]{/b} ficará preocupada."
                show aunt 92
                show player 5
                dia "Que pena..."
                dia "Eu estava esperando por ajuda para me ordenhar..."
                show aunt 91
                show player 10
                player_name "Desculpa... Talvez outra noitr?"
                show aunt 87
                show player 13
                dia "Sem problema... Você sabe onde poderá me encontrar."
                show aunt 88
                show player 21
                player_name "Ok!"
                hide aunt 88 at right with dissolve
                hide player 21 at left with dissolve
    $ callScreen(location_count)

label aunt_shed_faster_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') - 0.1)
    if shed_sex_action == 0:
        jump shed_sex_loop
    if shed_sex_action == 1:
        jump shed_ride_loop
    if shed_sex_action == 2:
        jump shed_fuck_loop
    if shed_sex_action == 3:
        jump shed_milk

label aunt_shed_slower_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') + 0.1)
    if shed_sex_action == 0:
        jump shed_sex_loop
    if shed_sex_action == 1:
        jump shed_ride_loop
    if shed_sex_action == 2:
        jump shed_fuck_loop
    if shed_sex_action == 3:
        jump shed_milk
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
