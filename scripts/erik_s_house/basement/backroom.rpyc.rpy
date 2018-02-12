label erik_basement_backroom_dialogue:
    $ location_count = "Erik's Basement Backroom"
    $ callScreen(location_count)

label backroom_aquarium:
    scene expression "backgrounds/location_erik_basement_aquarium.jpg" with None
    show expression "objects/closeup_box.png" at truecenter with dissolve
    player_name "( Here they are! I better get them back to {b}Erik{/b}. )"
    $ inventory.get_item(eriks_cards)
    hide expression "objects/closeup_box.png" with dissolve
    $ callScreen("Backroom Aquarium", False)

label mrsj_afterpoker_fun:
    scene erik_basement_back_c
    show erikmomsex 1 at left
    with dissolve
    erimom "Eu estava pensando do porque você ter demorado tanto!"
    show erikmomsex 3
    eri "Desculpa, mãe."
    show erikmomsex 1
    erimom "Achei que vocês não queriam passar um tempo comgio..."
    show erikmomsex 2
    player_name "Claro que queremos."
    show erikmomsex 1
    erimom "Vejo que vocês dois não param de olhar para mim."
    erimom "Você gostariam de... me tocar?"
    show erikmomsex 2
    player_name "Podemos?"
    show erikmomsex 3
    eri "Tem certeza, mãe?"
    show erikmomsex 1
    erimom "Por que não tentam?"
    show erikmomsex 4 with fastdissolve
    pause
    show erikmomsex 5
    erimom "Haha!"
    show erikmomsex 6
    erimom "Só isso?"
    erimom "Vocês devem ser tímidos!"
    show erikmomsex 7 with fastdissolve
    erimom "Talvez vocês só precisam de um incentivo..."
    show erikmomsex 8_9 with fastdissolve
    pause 8
    show erikmomsex 10 with fastdissolve
    erimom "Meu deus!"
    erimom "ALguém está excitado..."
    show erikmomsex 11
    erimom "... e quer mais."
    show erikmomsex 12 with fastdissolve
    pause
    show erikmomsex 13_14_13_12
    pause 7.5
    show erikmomsex 12b_13b_14b
    erimom "Eu poderia dar uma ajuda, meninos!"
    erimom "Por que você não chupa meus mamilos, {b}[firstname]{/b}..."
    erimom "... {b}Erik{/b} já sabe o que é para fazer."
    show erikmomsex 15_16_17
    $ anim_toggle = False
    $ xray = False
    label mrsj_afterpoker_fun_repeat:
        show erikmomsex 17
        show screen sex_anim_buttons
        pause
        hide screen sex_anim_buttons
        if anim_toggle:
            show erikmomsex 15_16_17 at left
            pause 8
        else:
            $ animcounter = 0
            while animcounter < 3:
                show erikmomsex 15
                pause
                show erikmomsex 16
                pause
                show erikmomsex 17
                pause
                $ animcounter += 1
        show erikmomsex 17
        menu:
            "Continue.":
                jump mrsj_afterpoker_fun_repeat
            "Fazer ela gozar.":

                show erikmomsex 15_16_17 at left
                pause 8
                show erikmomsex 18
                erimom "Ahhh!!!" with hpunch
                show erikmomsex 19 with fastdissolve
                erimom "Oh meu deus!"
                erimom "Foi bem feito, garotos..."
                erimom "Sinto que vocês dois querem mais..."
                erimom "Eu... eu acho que devemos parar... por hoje, pelo menos."

                scene erik_basement
                show player 1f at Position(xpos=756)
                show erik 1 at Position(xpos=876)
                show erikmom 28f at left
                with fade
                erimom "Certo, garotos! Acho que já é o suficiente por hoje..."
                erimom "Tenho que acordar cedo amanhã."
                show erikmom 27f at Position(xoffset=-1)
                show erik 5
                eri "Desculpa por te atrasar, mãe..."
                show erikmom 28f
                show erik 1
                erimom "Está tudo beeeem! Adorei nossa noite."
                show erikmom 27f at Position(xoffset=-1)
                show player 14f
                player_name "Obrigado por jogar conosco, {b}Sra. Johnson{/b}."
                show erikmom 28f
                show player 1f
                erimom "Foi meu prazer jogar com... com vocês."
                show erikmom 34 at center
                hide erik
                hide player
                with dissolve
                erimom "Me avisem se precisarem de alguém para jogar..."
                show erikmom 35
                player_name "Claro, {b}Sra. Johnson{/b}..."
                $ location_count = "Erik's House"
                $ unlock_ui()
                $ mrsj_afterpoker_fun = False
                $ mrsj_poker_night.finish()
                scene erikhouse_night with fade
                $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
