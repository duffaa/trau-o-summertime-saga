default art_classroom_first_visit = True

label art_classroom_dialogue:
    $ location_count = "Art Classroom"
    if art_classroom_first_visit == True:
        scene art_classroom_c
        show ross 1 zorder 1 at left
        show player 1f zorder 1 at right
        show xtra 22 as table zorder 0
        show xtra 23 as basket zorder 0 at Position (ypos = 635)
        show xtra 24 as fruit zorder 0 at Position (ypos = 565)
        with dissolve
        show ross 2
        ross "{b}[firstname]{/b}!!"
        ross "É ótimo ver que você voltou às aulas!"
        show ross 1
        show player 14f
        player_name "Oi, {b}Sra. Ross{/b}!"
        player_name "Senti falta das suas aulas."
        show ross 2
        show player 13f
        ross "Você perdeu um mês inteiro de estudos das frutas, mas podemos consertar isso."
        show ross 1
        show player 12f
        player_name "Estudo das frutas?"
        show ross 2
        show player 11f
        ross "Sim, claro!"
        ross "Estivemos explorando as belas formas e curvas de frutas!"
        show ross 1
        show player 10f
        player_name "Entendi..."
        show ross 2
        show player 5f
        ross "Não se preocupe. Mais tarde resolveremos isso."
        ross "Sei que você tem uma mente criativa, {b}[firstname]{/b}!"
        show ross 1
        show player 14f
        player_name "Acho que sim... Eu gosto de desenhar minhas coisas..."
        show ross 2
        show player 13f
        ross "Com a minha ajuda e o tipo certo de estudos de desenho de vida..."
        ross "...Você se formará com uma nota perfeita!"
        show ross 1
        show player 14f
        player_name "Sério?! Valeu, {b}Sra. Ross{/b}!"
        show player 18f
        player_name "Farei o meu melhor!"
        show ross 2
        show player 13f
        ross "Esse é o espírito da arte!"
        hide ross
        hide player
        hide fruit
        hide basket
        hide table
        with dissolve
        $ art_classroom_first_visit = False

    if M_mia.get_state() == S_mia_find_easel:
        scene art_classroom_b
        show player 4 with dissolve
        player_name "Hmm..."
        show player 12 with dissolve
        player_name "Vamos ver se eu acho um {b}cavalete{/b}, eu poderia usar para desenhar umas tatuagens..."
        hide player with dissolve
        $ M_mia.trigger(T_mia_easel_found)
    $ callScreen(location_count)

label ross_button_dialogue:
    scene art_classroom_c with None
    show ross 1 zorder 1 at left
    show player 1f zorder 1 at right
    show xtra 22 as table zorder 0
    show xtra 23 as basket zorder 0 at Position (ypos = 635)
    show xtra 24 as fruit zorder 0 at Position (ypos = 565)
    with dissolve
    show player 14f
    player_name "Oi, {b}Sra. Ross{/b}."
    show ross 2
    show player 13f
    ross "Olá, {b}[firstname]{/b}!"
    ross "Pronto para deixar as mãos sujas hoje?"
    show ross 1
    show player 17f
    player_name "Haha. Acho que sim."
    show ross 2
    show player 13f
    ross "Tem algo que você gostaria de falar?"
    show ross 1
    show player 4f
    menu:
        "Na verdade não.":
            show player 2f
            player_name "Não, {b}Sra. Ross{/b}."
            player_name "Eu estava pensando no que vamos fazer hoje."
            show ross 2
            show player 1f
            ross "Ah, sim."
            ross "Por que você não pega uma tela?"
            ross "Podemos pintar frutas juntos!!"
            show ross 1
            show player 14f
            player_name "Claro, {b}Sra. Ross{/b}."
            show ross 2
            show player 13f
            ross "Esse é o espírito da arte!"
    hide ross
    hide player
    hide fruit
    hide basket
    hide table
    with dissolve
    $ callScreen(location_count)

label easel_dialogue:
    scene art_classroom_b
    if M_mia.get_state() == S_mia_show_tattoo:
        show player 14 with dissolve
        player_name "( Eu deveria mostrar o desenho para a {b}Mia{/b} primeiro, antes de fazer outro. )"
        hide player with dissolve
    else:

        show player 35 with dissolve
        player_name "( O que eu deveria desenhar hoje? )"
        menu:
            "Ideias de tatuagem.":
                scene school_art_tattoos
                player_name "Hmm..."
                player_name "( O que eu deveria desenhar para a {b}Mia{/b}... )"
                call screen tattoos
                hide player with dissolve
                scene school_art_cs01
                with fade
                show text "Eu já desenhei tantas coisas antes...\n...Mas, fazer algo do tipo para a {b}Mia{/b} me deixou muito nervoso!\nEspero que seja o que ela quer..." at Position (xpos= 512, ypos = 700) with dissolve
                with dissolve
                pause
                hide text
                hide school_art_cs01
                with dissolve
                scene art_classroom_b
                show player 381 with dissolve
                player_name "Nada mal!"
                show player 386
                player_name "( Eu deveria ir mostrar par a {b}Mia{/b} o que eu fiz. )"
                player_name "( Espero que ela goste... )"
                hide player with dissolve
                $ M_mia.trigger(T_mia_visit)
                show expression [drawn_tattoo] at truecenter with dissolve
                $ inventory.items.append(tattoo_choices[drawn_tattoo])
                pause
                hide expression [drawn_tattoo] with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
