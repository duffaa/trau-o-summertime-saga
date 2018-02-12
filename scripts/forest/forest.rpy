default forest_count = 0
default awesomo_lured = False
default dirt_pile_done = False

label forest_dialogue:
    $ location_count = "Forest"
    scene expression gTimer.image("forest{}_b")
    if forest_count == 0:
        show player 43 with dissolve
        player_name "Uau!"
        player_name "( Nunca estive aqui antes... )"
        player_name "( É tão... tranquilo... )"
        $ forest_count = 1

    if Anna.started(anna_missing_pup) and not awesomo_lured:
        if gTimer.is_dark():
            show player 4
            player_name "( Está muito tarde para procurar pelo {b}Awesomo{/b}. )"
            hide player
            with dissolve

        elif cookies in inventory.items:
            show player 4 with dissolve
            player_name "( Vamos ver se consigo achar aquele cachorro. )"
            scene forest_closeup
            show player 239 at left
            with dissolve
            player_name "( Agora... )"
            show player 240
            player_name "( ...Tenho que encontrar uma forma de atrair ele... )"
            show player 245 at Position(xpos=8)
            player_name "( ...usando {b}isso{/b}! )"
            show player 246 at left
            pause
            show player 1 with dissolve

            show player 1
            player_name "( Vamos ver se ele vai vim. )"
            show player 31
            player_name "( Ele deve estar por aqui em algum lugar... )"
            $ awesomo_lured = True
            $ inventory.items.remove(cookies)
            hide player
            with dissolve
        else:

            show player 4
            player_name "( Eu deveria encontar alguns {b}biscoitos{/b} para atrair o {b}Awesomo{/b}. )"
            hide player
            with dissolve
    $ callScreen(location_count)

label awesomo_dialogue_button:
    scene forest_closeup
    show player 177
    with dissolve
    player_name "Opa..."

    player_name "O que você está fazendo aqui fora?"
    awesomo "Latido!"
    player_name "Você deixou sua dona preocupada!"
    awesomo "Latido!"
    player_name "Você é bonito..."
    label awesomo_dialogue_loop:
        menu:
            "Dar biscoitos.":
                player_name "Quer um biscoito?"
                show player 178 at Position(xpos=517)
                player_name "Toma..."
                show player 179 with hpunch
                player_name "!!!"
                show player 180
                player_name "Jesus!"
                player_name "Alguém está faminto..."
                show player 181
                player_name "Hmm..."
                show player 182
                player_name "Gostei de você!"
                awesomo "Latido!"
                jump awesomo_dialogue_loop
            "Checar a coleira.":

                show player 177 at center
                player_name "Vamos ver se você é quem eu estava procurando..."
                show awesomo_tag zorder 2 with dissolve
                player_name "{b}Awesomo{/b}... Uhum! É você!"
                $ awesomo = Character("Awesomo")
                hide awesomo_tag

                show player 177
                with dissolve
                player_name "Venha, vou te levar de volta a sua dona."
                player_name "Ela está muito preocupada..."
                awesomo "Latido!"
                player_name "Haha! Certo, vamos..."
                hide player
                scene forest
                with dissolve
                $ inventory.items.append(dog)
    $ callScreen(location_count)

label dirt_pile:
    show location_forest_dirt1 zorder 2 with dissolve
    if shovel in inventory.items:
        player_name "( Tem algo estranho com esse pedaço de terra... )"
        player_name "( Parece ter algo se mexendo aqui em baixo. )"
        player_name "( Talvez eu pudesse escavar? )"
        menu:
            "Escavar com a pá." if shovel in inventory.items:
                player_name "( Vamos ver o quê tem aqui... )"
                hide location_forest_dirt1
                show location_forest_dirt2
                with dissolve
                pause
                show location_forest_dirt3
                with dissolve
                player_name "{b}Minhocas{/b}?!"
                player_name "( Dizem que são ótimas {b}iscas de pesca{/b}. )"
                player_name "( Talvez eu devesse ficar com algumas... )"
                call screen forest_worms
            "Deixar elas aí.":

                player_name "( Pensando bem... )"
                player_name "( Deveria deixar elas aqui... )"
                with dissolve

        player_name "( Tem algo estranho com esse pedaço de terra... )"
        player_name "( Parece ter algo se mexendo aqui em baixo. )"
        player_name "( Preciso encontrar uma {b}pá{/b} para cavar. )"
        hide location_forest_dirt1
        with dissolve
    $ callScreen(location_count)

label mushroom:
    scene forest_closeup
    show player 498 with dissolve
    player_name "Esse deve ser o cogumelo que a {b}Aqua{/b} estava falando."
    player_name "Eu deveria tentar alimentar a {b}SeaSucc{/b} com isso..."
    hide player with dissolve
    show expression "boxes/popup_item_mushroom1.png" at truecenter with dissolve
    $ inventory.items.append(mushroom)
    pause
    hide expression "boxes/popup_item_mushroom1.png" with dissolve
    $ callScreen(location_count)

label worm_popup:
    show expression "boxes/popup_item_worm1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_worm1.png" with dissolve
    $ dirt_pile_done = True
    $ callScreen(location_count)

label altar:
    if M_aqua.is_set("altar pass"):
        scene expression gTimer.image("location_forest_puzzle_day{}")
        pause
        $ callScreen(location_count)

    scene expression gTimer.image("forest_altar{}")
    with fade
    show text "Uma estrutura de pedra no meio da florest." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Parece antiga! E completamente coberta de musgo..." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    if not gTimer.is_dark():
        show text "...e a {b}luz solar{/b} brilha diretamente sobre ela." at Position (xpos= 512, ypos= 700) with dissolve
    else:
        show text "...e o {b}luar{/b} brilhar diretamente sobre ela." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    show text "Isso deve ser o que eu estava procurando." at Position (xpos= 512, ypos= 700) with dissolve
    pause
    hide text
    with dissolve

    if not gTimer.is_dark():
        scene location_forest_puzzle_day
        player_name "Hmm..."
        player_name "Isso parece o negócio que estava no sino da igreja"
        player_name "...Mas tem algo de errado. Isso parece uma estrada sem fim."
        player_name "Hmm, quais eram as pistas mesmo?"
        player_name "Um negócio de pedra, cercado por pedras e com {b}a lua{/b} brilhadno sobre."
        player_name "Deveria pensar sobre isso."
        $ callScreen(location_count)
    else:

        scene location_forest_puzzle_night_closed
        $ gTimer.tick()
        player_name "Bom, isso é estranho."
        player_name "Parece que a lua está afetando isso de alguma forma."
        player_name "Estes símbolos devem ser importantes e parece que posso movê-los para fazer uma imagem..."
        player_name "Talvez seja um puzzle?"
        label altar_puzzle:
            call screen altar_puzzle
            if piecelist[9] == [162,143] and piecelist[18] == [382,20] and piecelist[16] == [600,139] and piecelist[14] == [383,263] and piecelist[10] == [163,385] and piecelist[12] == [603,387] and piecelist[20] == [384,516]:
                call screen altar_puzzle_finish
            jump altar_puzzle
        label altar_puzzle_finish:
            scene expression "location_forest_puzzle_night"
            show expression "objects/object_map_01.png" at Position(xalign = 0.473, yalign = 0.44)
            with None
            show popup_item_map1 at truecenter with dissolve
            $ inventory.items.append(treasure_map)
            pause
            hide popup_item_map1 with dissolve
            $ M_aqua.trigger(T_aqua_altar_puzzle_solve)
        $ callScreen(location_count)

label altar_puzzle_leave:
    scene expression gTimer.image("forest{}_b")
    show player 12 with dissolve
    player_name "Huh... Talvez haja algo que me ajude a como resolver esse puzzle."
    if scroll not in inventory.items:
        player_name "Eu poderia dar outra {b}olhada no sino da igreja{/b} para ver se não deixar nenhuma pista passar."
    else:
        player_name "Talvez esse {b}pergaminho que encontrei na árvore{/b} tenha mais detalhes desse puzzle."
    hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
