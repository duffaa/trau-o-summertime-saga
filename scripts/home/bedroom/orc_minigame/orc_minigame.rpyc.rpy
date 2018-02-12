init python:
    def orcHit():
        global life
        global slider_time
        if orc_slider.xpos >= 470 and orc_slider.xpos <= 527:
            life -= 1
            slider_time -= 0.75
            renpy.jump("orc_battle_hit")
        else:
            renpy.jump("orc_battle_fail")

transform orc_slide1:
    xpos 229
    ypos 695
    ease slider_time xpos 772
    ease slider_time xpos 229
    repeat

transform orc_slide2:
    xpos 772
    ypos 695
    ease slider_time xpos 229
    ease slider_time xpos 772
    repeat

image orc_slider = "buttons/arrows_02.png"

label orc_battle_prep:
    $ life = 3
    $ slider_time = 3.5
    jump orc_battle_start

label orc_battle_start:
    $ location_count = "Orc Battle"
    $ x = renpy.random.randint(0,99)
    if x < 74:
        $ orc_slider = At(ImageReference("orc_slider"), orc_slide1)
    else:
        $ orc_slider = At(ImageReference("orc_slider"), orc_slide2)
    scene expression "backgrounds/minigame07a.jpg"
    if life > 2:
        show expression "buttons/health_01.png" as life1 at Position(xpos=432, ypos=667)
    if life > 1:
        show expression "buttons/health_01.png" as life2 at Position(xpos=509, ypos=667)
    if life > 0:
        show expression "buttons/health_01.png" as life3 at Position(xpos=585, ypos=667)
    show expression orc_slider
    $ callScreen(location_count, False, False)

label orc_battle_hit:
    scene expression "backgrounds/minigame07b.jpg"
    if life > 2:
        show expression "buttons/health_01.png" as life1 at Position(xpos=432, ypos=667)
    if life > 1:
        show expression "buttons/health_01.png" as life2 at Position(xpos=509, ypos=667)
    if life > 0:
        show expression "buttons/health_01.png" as life3 at Position(xpos=585, ypos=667)
    with hpunch
    $ renpy.pause(0.7, hard=True)
    if life > 0:
        jump orc_battle_start
    else:
        jump orc_battle_finish

label orc_battle_finish:
    $ location_count = "Bedroom"
    scene expression "backgrounds/minigame07c.jpg" with dissolve
    $ renpy.pause(0.7, hard=True)
    scene expression "backgrounds/minigame07d.jpg" with dissolve
    $ renpy.pause(1, hard=True)
    scene expression Animation("backgrounds/minigame07e.jpg", 0.5, "backgrounds/minigame07f.jpg", 0.5) with fade
    pause
    $ gTimer.tick()
    if not June.known(june_cosplay):
        scene bedroom_sex2
        if June.over(june_mc_help_2):
            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with fastdissolve
            player_name "Uhh..."
            show june_sitting 12
            show player_sitting 5
            june "Parece que tivemos o mesmo fim."
            show player_sitting 3
            june "Desculpa..."
            show june_sitting 13
            show player_sitting 4
            player_name "Nah, tudo bem!"
            show june_sitting 12
            show player_sitting 5
            june "Você ainda acha estranho?"
            show june_sitting 13
        else:

            show june_sitting 9 at center
            with fade
            player_name "..."
            show june_sitting 13 at Position(xpos=300,ypos=787)
            show player_sitting 4 at right
            with fastdissolve
            player_name "Uhh..."
            show june_sitting 12
            show player_sitting 5
            june "Eu... Eu não sabia como o jogo terminava, eu juro!"
            show june_sitting 13
            show player_sitting 4
            player_name "Isso foi... inesperado?"
            show june_sitting 12
            show player_sitting 3
            june "Isso é tão vergonhoso..."
            show june_sitting 13
            show player_sitting 4
            player_name "Nah, está tudo bem!"
            show june_sitting 12
            show player_sitting 5
            june "Você não achou isso tão estranho?"
            show june_sitting 13
            $ june_mc_help_2.finish()
        menu:
            "É nojento.":
                show june_sitting 13 at Position(xpos=300,ypos=787)
                show player_sitting 4 at right
                player_name "Sei lá... é meio nojento?"
                show player_sitting 5
                june "..."
                show player_sitting 6
                player_name "Mas, que seja, tudo bem."
                show player_sitting 1
                show june_sitting 12
                june "Desculpa... Se eu soubesse..."
                june "Você ainda quer jogar comigo?"
                show player_sitting 2
                show june_sitting 13
                player_name "Claro, é divertido!"
                show player_sitting 1
                show june_sitting 12
                june "Obrigada... De qualquer mdoo, tenho que ir, está ficando tarde."
                show player_sitting 2
                show june_sitting 11
                player_name "Okay!"
                player_name "Durma bem!"
                show player_sitting 1
                show june_sitting 10
                june "Você também, {b}[firstname]{/b}."
            "É excitante!":

                show player_sitting 2 at right
                show june_sitting 11 at Position(xpos=300,ypos=787)
                player_name "Nah, é meio engraçado... "
                player_name "... e excitante."
                show june_sitting 10
                show player_sitting 1
                june "Sério? Você... acha?"
                show june_sitting 11
                show player_sitting 2
                player_name "Sim, acho qu orcs podem ser bem sexys!"
                show player_sitting 1
                june "..."
                show june_sitting 10
                june "Eu... Eu adoro orcs..."
                show player_sitting 5
                june "Na verdade, eu estava planejando fazer cosplay de orc..."
                show player_sitting 2
                show june_sitting 11
                player_name "Um cosplay de orc? Pra que?"
                show player_sitting 1
                show june_sitting 10
                june "Estava pensando em ir a comic com vestida de orc..."
                show june_sitting 12
                june "... mas tem um problema."
                june "Não acho que vou conseguir todas as partes da fantasia a tempo."
                show player_sitting 2
                show june_sitting 11
                player_name "Isso parece legal!"
                show player_sitting 1
                show june_sitting 10
                june "Você acha?"
                show player_sitting 2
                show june_sitting 11
                player_name "O que está faltando?"
                show player_sitting 1
                show june_sitting 10
                june "Eu tenho minha pintura corporal... Mas eu preciso das orelhas, dos dentes e... da cinta."
                show player_sitting 2
                show june_sitting 11
                player_name "Acho que posso achar elas para você!"
                show player_sitting 1
                show june_sitting 10
                june "Sério? Você faria isso para mim??"
                show player_sitting 2
                show june_sitting 11
                player_name "Posso tentar!"
                show player_sitting 6
                player_name "Eu acho que você ficaria linda vestida de orc!"
                show player_sitting 1
                june "..."
                show player_sitting 3
                show june_sitting 10
                june "Isso é fofo. Obrigada, {b}[firstname]{/b}."
                show player_sitting 2
                show june_sitting 11
                player_name "Bom, acho que é hora de dormir..."
                show player_sitting 1
                show june_sitting 10
                june "Sim, eu deveria ir pra casa também..."
                june "Valeu por passar um tempo junto comigo! Foi divertido."
                show player_sitting 6
                show june_sitting 11
                player_name "Sim, foi mesmo."
                show player_sitting 1
                show june_sitting 10
                june "Me avise se você achar as outras partes da fantasia!"
                june "Até amanhã?"
                show player_sitting 2
                show june_sitting 11
                player_name "Claro!"
                player_name "Vamos, te levo até lá fora."
                scene bedroom_night
                show player 35
                with fade
                player_name "Hmm... Estou pensando onde eu poderia encontrar essas {b}peças da fantasia{/b}."
                player_name "Talvez eu devesse dar uma olhada no {b}shopping{/b}?"
                show player 55 at Position(xoffset=12)
                player_name "*Yawn*"
                show player 56
                player_name "Vou amanhã, preciso dormir..."
                hide player with dissolve
                $ June.add_event(june_cosplay)
                jump sleeping
    else:

        scene bedroom_sex2
        show june_sitting 2 at Position(xpos=300,ypos=787)
        show player_sitting 1 at right
        with fade
        june "Finalmente! Estava tentando zerar fazem dias..."
        show june_sitting 3
        june "Você está ficando bom nisso."
        show june_sitting 4
        show player_sitting 6
        player_name "Acho que o jogo é bem viciante!"
        show june_sitting 1
        show player_sitting 2
        player_name "Ei, que horas são?"
        show june_sitting 5
        show player_sitting 5
        june "Ah, merda, já passa da meia noite..."
        show june_sitting 6
        show player_sitting 4
        player_name "Oh, estamos há bastante tempo aqui então..."
        player_name "Parece que perdemos a noção do tempo."
        show june_sitting 5
        show player_sitting 1
        june "Eu deveria ir pra casa, meus pais devem estar preocupados."
        show june_sitting 3
        june "Agradeço pela noite, {b}[firstname]{/b}."
        show june_sitting 4
        show player_sitting 2
        player_name "Vejo você na escola?"
        show player_sitting 1
        show june_sitting 3
        june "Claro!"
    $ callScreen(location_count)

label orc_battle_fail:
    $ location_count = "Bedroom"
    $ gTimer.tick()
    scene bedroom_sex2
    show june_sitting 4 at Position(xpos=300,ypos=787)
    show player_sitting 4 at right
    with fade
    player_name "Oops..."
    show player_sitting 3
    show june_sitting 3
    june "Huh, acho que temos treinar mais."
    show player_sitting 4
    show june_sitting 4
    player_name "Ha ha, desculpa."
    show player_sitting 3
    show june_sitting 3
    june "Tudo bem, vamos conseguir fazer isso!"
    show player_sitting 6
    show june_sitting 4
    player_name "Espero que sim! Além do mais, sou um péssimo parceiro..."
    show player_sitting 1
    show june_sitting 3
    june "Bom, tenho que ir, está ficando bem tarde."
    june "Me avise se você quiser jogar de novo!"
    show player_sitting 2
    show june_sitting 4
    player_name "Ok!"
    player_name "Durma bem!"
    show player_sitting 1
    show june_sitting 3
    june "Você também, {b}[firstname]{/b}."
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
