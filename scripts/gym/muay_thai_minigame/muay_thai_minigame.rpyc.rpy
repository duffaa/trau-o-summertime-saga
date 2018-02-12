init python:
    panty_lie_seen = False
    class Arrow:
        def __init__(self, image = "", passive = ""):
            self.image = image
            self.passive = passive

    class Key:
        def __init__(self, image = "", passive = ""):
            self.image = image
            self.passive = passive

    def add_arrow(Arrow):
        task_list.append(Arrow)

    def add_key(Key):
        task_list.append(Key)

label bag_minigame_listing:
    $ renpy.random.shuffle(arrow_list)
    $ renpy.random.shuffle(keyboard_list)
    $ task_list = []
    $ move_list = []
    if training_tier == 1:
        $ move_list_number = 4
        $ time_count = 3
        $ timer_range = 3

    elif training_tier == 2:
        $ move_list_number = 6
        $ time_count = 4.5
        $ timer_range = 4.5

    elif training_tier == 3:
        $ move_list_number = 8
        $ time_count = 6
        $ timer_range = 6

    elif training_tier == 4:
        $ move_list_number = 10
        $ time_count = 7.5
        $ timer_range = 7.5
    $ a = 0
    while (a < move_list_number):
        if renpy.variant("pc"):
            $ b = renpy.random.randint(0, 1)
            if b == 0:
                $ move_list += [renpy.random.choice(arrow_list)]
            else:

                $ move_list += [renpy.random.choice(keyboard_list)]
        else:

            $ move_list += [renpy.random.choice(arrow_list)]
        $ a += 1
    $ renpy.random.shuffle(move_list)
    $ arrow_index = 0
    call screen bag_minigame

label bag_minigame_attack:
    if cheat_pass:
        $ training_done = True
        $ cheat_pass = False
    if training_tier == 1:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a with hpunch
    elif training_tier == 2:
        $ playSound("audio/sfx_punch1.ogg", loop = False)
        show minigame02a2 with hpunch
    elif training_tier == 3:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a3 with hpunch
    elif training_tier == 4:
        $ playSound("audio/sfx_punch2.ogg", loop = False)
        show minigame02a4 with hpunch
    player_name "Huah!!"
    jump training01_done_dialogue

label training01_payment_dialogue:
    scene expression gTimer.image("training{}_b")
    pause 0.001
    show player 1 at left
    show master 2 at right
    with dissolve
    if (not sister.completed(sis_panty02) and pStats.dex() == 2) or (not sister.completed(sis_panty03) and pStats.dex() == 5) or (not sister.completed(sis_panty04) and pStats.dex() == 7):
        mas "Não posso ensinar mais nada no momento."
        mas "Vá para o mundo e obtenha mais experiência de vida! Talvez ficar mais tempo a mulher que te deu essas calcinhas!"
        show player 40 at left
        show master 6 at right
        player_name "Sim, {b}Mestre Somrak{/b}!!!"

    elif training_skip_payment:
        mas "Ahh!"
        mas "Você voltou!"
        mas "Você quer continuar com o treino, jovem aprendiz?"
        show master 1
        menu:
            "Treinar.":
                show player 40 at left
                show master 6 at right
                player_name "Sim, {b}Mestre Somrak{/b}!!!"
                show master 2
                show player 1
                mas "Ótimo, ótimo! Vamos começar então!"
                hide player
                hide master
                with dissolve
                jump training_during_dialogue

            "Pular Mini-Game (Trapaça)" if cheat_mode:
                $ cheat_pass = True
                show player 40 at left
                show master 6 at right
                player_name "Sim, {b}Mestre Somrak{/b}!!!"
                show master 2
                show player 1
                mas "Ótimo, ótimo. Vamos começar então."
                hide player
                hide master
                with dissolve
                jump training_during_dialogue
            "Esqueça.":

                show master 5 at right
                show player 10 at left
                player_name "Na verdade, esqueça..."
                show master 4
                show player 11
                mas "Volte quando mudar de ideia, jovem aprendiz!"
                show master 6
                show player 40
                player_name "Claro, {b}Mestre Somrak{/b}!!!"
                hide player
                hide master
                with dissolve
    else:

        mas "Ahh!"
        mas "Você voltou!"
        mas "Você me trouxe o que eu queria?"
        show master 1
        if panties in inventory.items:
            menu:
                "Tenho a calcinha." if training_tier == 1 and sister.completed(sis_panty01):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Sim..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff*{/b}"
                    show master 3
                    mas "Muito bom!" with fastdissolve
                    show player 12
                    player_name "Me custou caro... É melhor o treino compensar."
                    show player 1
                    show master 4
                    mas "O Muay Thai não tem preço, jovem aprendiz!"
                    show master 2
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 6
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_shower_cuddle01)
                    jump training_during_dialogue

                "Tenho a calcinha. (Trapaça)" if training_tier == 1 and sister.completed(sis_panty01) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Sim..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff({/b}"
                    show master 3
                    mas "Muito bom!" with fastdissolve
                    show player 12
                    player_name "Me custou caro... É melhor o treino compensar."
                    show player 1
                    show master 4
                    mas "O Muay Thai não tem preço, jovem aprendiz!"
                    show master 2
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 6
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_shower_cuddle01)
                    jump training_during_dialogue

                "Tenho a calcinha." if training_tier == 2 and sister.completed(sis_panty02):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Sim..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff*{/b}"
                    show master 3
                    mas "Muito bom!" with fastdissolve
                    show player 12
                    player_name "Me custou caro... É melhor o treino compensar."
                    show player 1
                    show master 4
                    mas "O Muay Thai não tem preço, jovem aprendiz!"
                    show master 2
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 6
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ inventory.items.remove(panties)


                    jump training_during_dialogue

                "Tenho a calcinha. (Trapaça)" if training_tier == 2 and sister.completed(sis_panty02) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Sim, {b}Mestre Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Sim..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 15
                    pause
                    show master 16
                    pause
                    player_name "..."
                    show master 17
                    mas "Muito bom, jovem aprendiz!" with fastdissolve
                    show player 1
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 16
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)


                    jump training_during_dialogue

                "Tenho a calcinha." if training_tier == 3 and sister.completed(sis_panty03):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Sim, {b}Mestre Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Sim..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 12
                    pause
                    show master 13
                    pause
                    show master 14
                    pause
                    mas "Muito bom, jovem aprendiz!" with fastdissolve
                    show player 1
                    show master 2
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 6
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam02)
                    jump training_during_dialogue

                "Tenho a calcinha. (Trapaça)" if training_tier == 3 and sister.completed(sis_panty03) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Sim, {b}Mestre Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Sim..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 12
                    pause
                    show master 13
                    pause
                    show master 3
                    mas "Muito bom, jovem aprendiz!" 
                    with fastdissolve
                    show player 1
                    show master 2
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 6
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam02)
                    jump training_during_dialogue

                "Tenho a calcinha." if training_tier == 4 and sister.completed(sis_panty04):
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 314 at Position (xpos=38)
                    show master 6 at right
                    player_name "Sim, {b}Mestre Somrak{/b}!"
                    show player 1 at left
                    show master 11
                    mas "Sim..." with fastdissolve
                    show master 8
                    player_name "..." with fastdissolve
                    show player 1
                    mas "{b}*Sniff*{/b}"
                    pause
                    show player 11
                    show master 14
                    pause
                    show master 15
                    pause
                    show master 16
                    pause
                    player_name "..."
                    show master 17
                    show master 3
                    mas "Muito bom, jovem aprendiz!" with fastdissolve
                    show player 40
                    show master 16
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 17
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam03)
                    jump training_during_dialogue

                "Tenho a calcinha. (Trapaça)" if training_tier == 4 and sister.completed(sis_panty04) and cheat_mode:
                    $ cheat_pass = True
                    $ panty_lie_seen = False
                    show player 239_240
                    pause
                    show player 39 at Position (xpos=38)
                    show master 9 at right
                    mas "Sim..." with fastdissolve
                    show player 30 at left
                    show master 8
                    player_name "..." with fastdissolve
                    show player 11
                    mas "{b}*Sniff*{/b}"
                    show master 3
                    mas "Muito bom!" with fastdissolve
                    show player 12
                    player_name "Me custou caro... É melhor o treino compensar."
                    show player 1
                    show master 4
                    mas "O Muay Thai não tem preço, jovem aprendiz!"
                    show master 2
                    mas "Você está pronto para treinar?"
                    show player 40
                    show master 6
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player 40
                    hide master 6
                    with dissolve
                    $ inventory.items.remove(panties)
                    $ sister.add_event(sis_webcam03)
                    jump training_during_dialogue
                "Esqueça.":

                    show master 5 at right
                    show player 10 at left
                    player_name "Na verdade, esqueça..."
                    show master 4
                    show player 11
                    mas "Volte quando mudar de ideia, jovem aprendiz!"
                    show master 6
                    show player 40
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
        else:


            menu:
                "Tenho a calcinha." if not panty_lie_seen:
                    show master 2 at right
                    show player 11 at left
                    mas "Não estou vendo nenhuma calcinha, jovem aprendiz."
                    show master 5
                    show player 10
                    player_name "Ah, sim, sobre isso..."
                    player_name "Ainda não encontrei..."
                    show master 4
                    show player 11
                    mas "Continue procurando, jovem aprendiz!"
                    show player 1
                    mas "Volte quando encontrar,!"
                    show master 6
                    show player 40
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master with dissolve
                    $ panty_lie_seen = True

                "<>Tenho a calcinha." if panty_lie_seen:
                    $ pass
                "Esqueça.":

                    show master 5 at right
                    show player 10 at left
                    player_name "Na verdade, esqueça..."
                    show master 4
                    show player 11
                    mas "Volte quando você mudar de ideia, jovem aprendiz!"
                    show master 6
                    show player 40
                    player_name "Sim, {b}Mestre Somrak{/b}!!!"
                    hide player
                    hide master
                    with dissolve
    $ callScreen(location_count)

label training_during_dialogue:
    scene minigame02b
    if training_skip_payment:
        scene minigame02b
        show master 3f at left
        with dissolve
        mas "Você sabe o que tem que fazer, jovem aprendiz!"
        show master 2f
        mas "Como na última vez."
        show master 4f
        mas "Agora, mostre!!"
    else:

        if training_tier == 1:
            show master 3f at left
            with dissolve
            mas "Primeiro, você vai aprender a dar socos!"
            show master 2f
            mas "Você deve construir o poder dos quadris! Comece a partir daí..."
            show master 4f
            mas "...depois vire o ombro, estenda seu cotovelo..."
            show master 10f
            mas "...e {b}ATAQUE{/b}!" with hpunch
            show master 4f
            mas "Agora, mostre!!"

        elif training_tier == 2:
            show master 3f at left
            with dissolve
            mas "Agora, você aprenderá a usar os cotovelos!"
            show master 2f
            mas "É a técnica mais útil de curta distância; isso pode cortar a pele ao redor dos olhos..."
            show master 4f
            mas "...vai de qualquer ângulo, direto do seu ombro..."
            show master 10f
            mas "...e {b}ATAQUE{/b}!" with hpunch
            show master 4f
            mas "Agora, mostre!!"

        elif training_tier == 3:
            show master 3f at left
            with dissolve
            mas "Agora, você aprenderá a usar chutes!"
            show master 2f
            mas "Prenda seu pé no chão, sua força estará aí!"
            show master 4f
            mas "Estique seus quadris, vire seu corpo..."
            show master 10f
            mas "...e {b}ATAQUE{/b}!" with hpunch
            show master 4f
            mas "Agora, mostre!!"

        elif training_tier == 4:
            show master 3f at left
            with dissolve
            mas "Finalmente você aprenderá a usar os joelhos!"
            show master 2f
            mas "Você deve mirar nos nervos ou na cabeça, então com muita força..."
            show master 4f
            mas "...vire seus quadris, prepare para pular..."
            show master 10f
            mas "...e {b}ATAQUE{/b}!" with hpunch
            show master 4f
            mas "Agora, mostre!!"
    $ training_skip_payment = True
    hide master
    with dissolve
    hide minigame02b
    if cheat_pass:
        jump bag_minigame_attack
    jump bag_minigame_listing

label training01_done_dialogue:
    $ gTimer.tick()
    if training_tier == 1:
        if pStats.dex() < 2:
            $ pStats.increase("dex")
        if pStats.dex() > 1:
            $ training_skip_payment = False

    elif training_tier == 2:
        if pStats.dex() < 5:
            $ pStats.increase("dex")
        if pStats.dex() > 4:
            $ training_skip_payment = False

    elif training_tier == 3:
        if pStats.dex() < 7:
            $ pStats.increase("dex")
        if pStats.dex() > 6:
            $ training_skip_payment = False

    elif training_tier == 4:
        $ pStats.increase("dex")
    scene expression gTimer.image("training{}_b")
    if training_skip_payment:
        show masterplayer 28 at left
        show master 3 at right
        with dissolve
        mas "Você foi bem, jovem aprendiz!"
        show master 6
        show unlock9 at truecenter
        pause
        hide unlock9 with dissolve
        show master 2
        show masterplayer 27
        mas "No entanto, ainda vejo margem para melhorar!"
        show master 3
        mas "Vá! Descanse!"
        mas "Continuaremos quando você voltar."
        show masterplayer 40
        show master 6
        player_name "Sim! Obrigado, {b}Mestre Somrak{/b}!!!"
        hide masterplayer
        hide master
        with dissolve
    else:

        if training_tier == 1:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Muito bom, jovem aprendiz!"
            show master 2
            mas "Você melhorou, posse perceber isso!"
            show masterplayer 28
            mas "Aqui! Você ganhou uma nova faixa!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            show masterplayer 27
            mas "Agora... para continuar o treino, você terá que..."
            show master 2
            show masterplayer 21
            mas "...me trazer mais {b}calcinhas{/b}!"
            show masterplayer 40
            show master 6
            player_name "Sim! Obrigado, {b}Mestre Somrak{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "Tenho bons pressentimentos sobre ele..."
            $ training_tier = 2

        elif training_tier == 2:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Muito bom, jovem aprendiz!"
            show master 2
            show masterplayer 28
            mas "Você melhorou, posse perceber isso!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Agora, descanse!"
            mas "Falaremos sobre a outra parte do treinamento quando você voltar, jovem aprendiz."
            show masterplayer 40
            show master 6
            player_name "Sim! Obrigado, {b}Mestre Somrak{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "Ele aprende rápido..."
            $ training_tier = 3

        elif training_tier == 3:
            show masterplayer 27 at left
            show master 3 at right
            with dissolve
            mas "Muito bom, jovem aprendiz!"
            show master 2
            show masterplayer 28
            mas "Você melhorou, posse perceber isso!"
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Agora, descanse!"
            mas "Falaremos sobre a outra parte do treinamento quando você voltar, jovem aprendiz."
            show masterplayer 40
            show master 6
            player_name "Sim! Obrigado, {b}Mestre Somrak{/b}!!!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "Ele aprende rápido..."
            $ training_tier = 4

        elif training_tier == 4:
            show masterplayer 28 at left
            show master 3 at right
            with dissolve
            mas "Muito bom, jovem aprendiz!"
            show master 2
            show masterplayer 28
            mas "Ou devo dizer, jovem {b}mestre{/b}?"
            mas "Você passou em todas tarefas que te dei."
            mas "Você melhorou muito desde o primeiro encontro!"
            mas "Agora..."
            show master 6
            show unlock9 at truecenter
            pause
            hide unlock9 with dissolve
            show master 3
            mas "Não tem mais nada pra eu te ensinar."
            show master 2
            mas "...mas não falarei \"não\" para mais {b}calcinhas{/b}!"
            show master 6
            pause
            show master 4
            mas "Agora vá e use suas novas habilidades!" with hpunch
            show masterplayer 40
            show master 6
            player_name "Sim, {b}Mestre Somrak{/b}!!!"
            player_name "Obrigado!"
            hide masterplayer with dissolve
            pause
            show master 2
            mas "Ele m lembra de quando eu era jovem..."
    hide master
    with dissolve
    $ callScreen(location_count)

label training_failed_dialogue:
    scene expression gTimer.image("training{}_b")
    show masterplayer 27 at left
    show master 7 at right
    mas "{b}ERRADO!!{/b}" with vpunch


    mas "Você não ouve! Você luta como um cachorro idiota!"
    mas "Foco! Use menos músculos, mais cérebro!"
    show master 4
    mas "Treine mais, depois volte..."
    hide masterplayer
    hide master
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
