label mrsj_room:
    $ location_count = "Mrs Johnson's Room"
    if erik.in_progress(erik_breastfeeding):
        jump erik_breastfeeding
    elif erik.in_progress(erik_sex_ed):
        jump mrsj_sex_ed
    elif mrsj.started(mrsj_sex_ed) and kamasutra in inventory.items and birth_control_pills in inventory.items:
        jump mrsj_sex_ed_2
    $ callScreen(location_count)

label mrsj_ball:
    scene expression gTimer.image("mrsj_ball{}")
    show popup_unfinished at truecenter with dissolve
    $ renpy.pause()
    hide popup_unfinished with dissolve
    $ callScreen(location_count)

label mrsj_private_yoga:
    $ gTimer.tick()
    $ location_count = "Erik's House Entrance"
    $ mrsj_filled = True
    $ M_erimom.set('sex speed', .4)
    show player 435 at left
    show erikmom 53 at Position(xpos=734,ypos=650)
    player_name "Posso ver suas aulas de yoga privadas?"
    show erikmom 54
    show player 434
    erimom "Tem uma posição que eu sempre quis tentar."
    erimom "Mas nunca tive alguém que me ajudasse... a menos que você quisesse?"
    show erikmom 53
    show player 435
    player_name "Claro, {b}Sra. Jonhson{/b}, eu adoraria!"
    show erikmom 54
    show player 434
    erimom "Você acha que tem força o suficiente para fazer?"
    show erikmom 53
    show player 435
    player_name "Posso tentar!"
    show erikmom 54
    show player 434
    erimom "Ok. Comece tirando suas roupas..."
    show erikmom 53
    show player 8 with fastdissolve
    pause
    show player 8b with fastdissolve
    pause
    show player 431b with fastdissolve
    pause
    show player 431 with vpunch
    show erikmom 54
    erimom "Uau!"
    erimom "Nunca vi alguém tão animado assim para uma aula de yoga!"
    erimom "Por que você não se deita na cama comigo?"
    scene erik_upstairs_night_c2
    show erikmomsex 33 at topright
    with fade
    erimom "Você gostou?"
    show erikmomsex 34
    player_name "É bem bonito..."
    show erikmomsex 33
    erimom "Mantenha seus olhos em mim, quero te mostrar um pequeno truque."
    show erikmomsex 35 with fastdissolve
    pause 0.05
    show erikmomsex 36 at Position(yoffset=70) with fastdissolve
    pause 0.2
    show erikmomsex 36_37
    player_name "Woah..."
    pause
    $ anim_toggle = True
    $ xray = False

    label mrsj_private_yoga_pos1_repeat:
        hide screen erimom_private_pos1_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            show erikmomsex 36_37
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 4:
                show erikmomsex 36 at Position(yoffset=70)
                pause
                show erikmomsex 37 at Position(yoffset=60)
                pause
                $ animcounter += 1

        show screen erimom_private_pos1_sex_options
        pause
        jump mrsj_private_yoga_pos1_repeat

        label erimom_private_pos1_switch:
            hide screen erimom_private_pos1_sex_options
            $ M_erimom.set('sex speed', .3)
            show erikmomsex 37 at Position(yoffset=60)
            pause 0.2
            show erikmomsex 38 with fastdissolve
            pause 0.2
            show erikmomsex 39 at Position(yoffset=87) with fastdissolve
            erimom "Vamos para a próxima pose..."
            erimom "... algo para me ajudar a esticar."
            scene erik_upstairs_night_c3
            show erikmomsex 40 at Position(xpos=580,ypos=710)
            with fade
            erimom "Essa posição é mais divertida..."
            erimom "... você apenas tenta ficar aí, deixe-me fazer o trabalho..."
            show erikmomsex 40
            erimom "Você é tão GRANDE, {b}[firstname]{/b}..."
            show erikmomsex 41 with fastdissolve
            pause 0.5
            show erikmomsex 42 at Position(xoffset=-14) with fastdissolve
            pause 0.5
            show erikmomsex 43 at Position(xoffset=-20) with fastdissolve
            pause 0.5
            show erikmomsex 44 at Position(xoffset=-30) with fastdissolve
            erimom "Aaah... tão funo..."
            player_name "{b}Sra. Johnson{/b}, você é tão gostosa..."
            erimom "Vou me mexer agora, tente aguentar por mais um pouco, {b}[firstname]{/b}."
            show erikmomsex 45 at Position(xoffset=-23)
            pause 0.2
            show erikmomsex 46 at Position(xoffset=-19)
            pause 0.2
            show erikmomsex 42_43_44_45_46
            pause
            erimom "Isso!! Continue..."
            pause
            $ anim_toggle = True

            label mrsj_private_yoga_pos2_repeat:
                hide screen erimom_private_pos2_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show erikmomsex 42_43_44_45_46 at Position(xpos=580,ypos=710)
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show erikmomsex 42 at Position(xoffset=-14)
                        pause
                        show erikmomsex 43 at Position(xoffset=-20)
                        pause
                        show erikmomsex 44 at Position(xoffset=-30)
                        pause
                        show erikmomsex 45 at Position(xoffset=-23)
                        pause 
                        show erikmomsex 46 at Position(xoffset=-19)
                        pause
                        $ animcounter += 1

                show screen erimom_private_pos2_sex_options
                pause
                jump mrsj_private_yoga_pos2_repeat

                label erimom_private_pos2_cum:
                    hide screen erimom_private_pos2_sex_options
                    show erikmomsex 42_43_44_45_46
                    erimom "Me segure bem, {b}[firstname]{/b}..."
                    erimom "... goze dentro de mim!"
                    player_name "Você tem certeza?"
                    erimom "Sim, preciso sentir sua energia!"
                    show erikmomsex 47 at Position(xoffset=-34) with vpunch
                    erimom "AHH!!!"
                    show white zorder 4
                    pause 0.3
                    hide white with dissolve
                    erimom "Siiim..."
                    erimom "Adoro a sensação da energia fluindo, pingando..."
                    player_name "Não é perigoso isso dentro de você?"
                    show erikmomsex 48 at Position(xoffset=-13) with dissolve
                    erimom "Estou tomando pílulas, não precisa se preocupar, querido..."
                    scene erik_upstairs_night_c2
                    show erikmom 56 at right
                    show player 426 at left
                    with fade
                    erimom "Você... Você é muito bom, {b}[firstname]{/b}."
                    show player 429
                    show erikmom 55
                    player_name "Você está bem, {b}Sra. Johnson{/b}?"
                    show player 426
                    show erikmom 56
                    erimom "Estou bem, só estou um pouco cansada..."
                    erimom "Espero que eu não esteja muito dolorida para fazer o yoga amanhã."
                    show player 427
                    show erikmom 55
                    player_name "O... {b}Erik{/b} não se importa em passarmos um tempo junto?"
                    show player 428
                    show erikmom 56
                    erimom "Oh, ele não pensa mais sobre isso..."
                    show player 426
                    erimom "Ele está muito ocupado passando um tempo com a namorada."
                    erimom "Acho que você pode aprender muito se vier em mais sessões..."
                    erimom "... mas acho que preciso tirar um cochilo agora."
                    erimom "Sinta-se livre em voltar, estarei te esperando todas as noites."
                    show player 429
                    show erikmom 55
                    player_name "Claro, {b}Sra. Jonhson{/b}!"
    $ callScreen(location_count)

label mrsj_3some:
    $ gTimer.tick()
    $ location_count = "Erik's House Entrance"
    $ mrsj_filled = True
    show erikmom 39 at right
    show player 21 at left
    show erik 1f zorder 1 at Position(xpos=300)
    player_name "{b}Erik{/b} estávamos pensando, você não poderia nos ensinar algumas coisas?"
    show player 13
    show erik 4f
    eri "É, gostariamos de... transar."
    show erikmom 40
    show erik 1f
    erimom "Eu estava esperando que vocês viessem me visitar para algumas lições."
    show erikmom 39
    show player 21
    player_name "Sério?"
    show player 13
    show erik 4f
    eri "O que você quer que nós fazemos, mãe?"
    show erikmom 40b
    show erik 1f
    erimom "Eu estava lendo o livro que vocês me trouxeram..."
    show erikmom 40
    erimom "... e acho que encontrei o que precisávamos!"
    erimom "E se eu mostrasse a posição para vocês dois?"
    show erikmom 39
    show player 21
    player_name "Po-posição sexual?"
    show player 13
    show erikmom 40
    erimom "Por que vocês não tiram a roupa e se juntam a mim na cama?"
    erimom "Vocês podem seguir minhas instruções..."
    show erik 55f at Position(xoffset=-8)
    show player 8 at Position(xoffset=-27)
    with fastdissolve
    erimom "... e deixar que eu faça o resto."
    scene erik_upstairs_night_c3
    show erikmomsex 20 at topright
    with fade
    erimom "Vamos começar com essa!"
    erimom "Eu estarei em cima do meu bebêzinho, enquanto eu chupo seu pau, {b}[firstname]{/b}..."
    erimom "... tente não gozar!"
    erimom "Quero tentar outras poisções."
    eri "Ok, mãe..."
    show erikmomsex 21_22_23_24_25 with fastdissolve
    pause
    eri "Mãe..."
    eri "É tão bom... dentro de você..."
    $ anim_toggle = True
    $ xray = False
    $ M_erimom.set('sex speed', .4)

    label mrsj_3some_pos1_repeat:
        hide screen mrsj_3some_pos1_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            show erikmomsex 21_22_23_24_25 at topright
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 4:
                show erikmomsex 21
                pause
                show erikmomsex 22
                pause
                show erikmomsex 23
                pause
                show erikmomsex 24
                pause
                show erikmomsex 25
                pause
                $ animcounter += 1

        show screen mrsj_3some_pos1_sex_options
        pause
        jump mrsj_3some_pos1_repeat

        label mrsj_3some_pos1_switch:
            hide screen mrsj_3some_pos1_sex_options
            $ M_erimom.set('sex speed', .3)
            show erikmomsex 26
            erimom "Que tal tentarmos outra coisa..."
            erimom "... quero que vocês me peguem de costas."
            show erikmomsex 27 at Position(xanchor=0,xpos=200,ypos=100) with fade
            erimom "Isso, {b}[firstname]{/b}, assim..."
            erimom "... Quero sentir vocês dois dentro de mim ao mesmo tempo."
            show erikmomsex 28 at Position(yoffset=42) with fastdissolve
            erimom "Ahh... isso!"
            show erikmomsex 28_29_30
            erimom "Mais rápido!!"
            $ anim_toggle = True

            label mrsj_3some_pos2_repeat:
                hide screen mrsj_3some_pos2_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show erikmomsex 28_29_30 at Position(xanchor=0,xpos=200,ypos=100)
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show erikmomsex 28 at Position(yoffset=42)
                        pause
                        show erikmomsex 29 at Position(yoffset=36)
                        pause
                        show erikmomsex 30 at Position(xoffset=-4,yoffset=41)
                        pause
                        $ animcounter += 1

                show screen mrsj_3some_pos2_sex_options
                pause
                jump mrsj_3some_pos2_repeat

                label mrsj_3some_pos2_cum:
                    hide screen mrsj_3some_pos2_sex_options
                    show erikmomsex 28_29_30 at Position(xanchor=0,xpos=200,ypos=100)
                    pause
                    show erikmomsex 31 at Position(xoffset=60,yoffset=42) with hpunch
                    erimom "AHHH!!!"
                    show white zorder 4
                    pause 0.3
                    hide white with dissolve
                    pause
                    show erikmomsex 32 with fastdissolve
                    erimom "Você fez uma grande bagunça com essa gozada!"
                    player_name "Eu gozi dentro... tem problemas?"
                    erimom "Sem problemas, eu estou tomando pílulas..."
                    player_name "Desculpa, {b}Sra. Johnson{/b}."
                    erimom "Sem problemas, querido. Eu adoro sentir a sua porra escorrendo dentro da..."
                    erimom "... Erm, acho que devemos dar uma pausa."
                    scene erik_upstairs_night_c2
                    show erikmom 56 at right
                    show player 426 zorder 2 at left
                    show erik 59f zorder 1 at Position(xpos=300)
                    with fade
                    erimom "Meu deus..."
                    show erik 60f
                    show erikmom 55
                    eri "Você está bem, mãe?"
                    show erik 59f
                    show erikmom 56
                    erimom "Um pouco cansada, bebê..."
                    erimom "... vocês fizeram muito bem."
                    erimom "Acho que eu deveria tirar um cochilo depois disso!"
                    erimom "Sintam-se livres em voltar outra hora..."
                    show erikmom 55
                    show erik 60f
                    eri "Vamos, deveriamos ir descansar."
                    show erik 59f
                    scene erik_inside_b
                    show erik 4 at right
                    show player 1 at left
                    with fade
                    eri "Isso foi incrível!!"
                    show erik 1
                    show player 17
                    player_name "Sim, sua mãe é ótima..."
                    show erik 4
                    show player 1
                    eri "Nunca achei que isso seria tão bom..."
                    show erik 1
                    show player 14
                    player_name "Acho que ela gostou também!"
                    show erik 4
                    show player 1
                    eri "Você deveria voltar outra hora, para que repetissemos..."
                    show erik 1
                    show player 14
                    player_name "Vou tentar, prometo!"
                    show erik 4
                    show player 1
                    eri "Vou jogar uns jogos no meu quarto, até mais."
                    show erik 1
                    show player 14
                    player_name "Beleza, até mais!"
                    hide erik
                    hide player
                    with dissolve
    $ callScreen(location_count)

label erimom_private_pos1_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_private_yoga_pos1_repeat

label erimom_private_pos1_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_private_yoga_pos1_repeat

label erimom_private_pos2_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_private_yoga_pos2_repeat

label erimom_private_pos2_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_private_yoga_pos2_repeat

label mrsj_3some_pos1_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_3some_pos1_repeat

label mrsj_3some_pos1_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_3some_pos1_repeat

label mrsj_3some_pos2_faster_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') - 0.1)
    jump mrsj_3some_pos2_repeat

label mrsj_3some_pos2_slower_sex:
    $ M_erimom.set('sex speed', M_erimom.get('sex speed') + 0.1)
    jump mrsj_3some_pos2_repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
