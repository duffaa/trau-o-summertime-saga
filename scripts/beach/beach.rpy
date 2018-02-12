label beach_dialogue:
    $ location_count = "Beach"
    if getPlayingSound("<loop 2>audio/ambience_beach.ogg"):
        $ playSound("<loop 2>audio/ambience_beach.ogg")
    $ callScreen(location_count)

label beach_island_dialogue:
    $ location_count = "Beach Island"
    if M_aqua.get_state() == S_aqua_treasure_search:
        scene location_beach_island_blur
        show player 11 at left with dissolve
        pause
        show player 10
        player_name "É uma {b}estátua estranha.{/b}"
        show player 2
        player_name "... Mas de acordo com o mapa, o {b}tesouro{/b} deve estar aqui."
        hide player with dissolve
    $ callScreen(location_count)

label beach_statue:
    if shovel not in inventory.items:
        scene location_beach_island_blur
        show player 2 at left
        player_name "( Eu não posso cavar esse {b}tesouro enterrado{/b} sem uma {b}pá.{/b} )"
        show player 4
        player_name "( ...Acho que tenho em {b}casa{/b} em algum lugar. )"
        hide player with dissolve
        $ callScreen(location_count)

    if M_aqua.get_state() == S_aqua_treasure_search:
        scene location_beach_digging01 with fade
        show text "Continuei cavando por horas..." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "...Em pouco tempo, comecei a sentir meus braços doerem." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "O cansaço estava quase me vencendo, eu até pensei em desistir." at Position (xpos= 512, ypos= 700) with dissolve
        pause
        show text "Eu estava no lugar errado?" at Position (xpos= 512, ypos= 700) with dissolve
        with dissolve
        pause
        hide text
        with dissolve

        scene location_beach_digging02 with fade
        show text "... Então, bang! Minha pá atingiu algo!" at Position (xpos= 512, ypos = 700) with dissolve
        pause
        show text "Minha força voltou em um instante enquanto eu me apressava para descobrir o que Ben Dover tinha enterrado." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        show text "...Era um grande baú pesado; Isso! Eu encontrei o tesouro!" at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        with dissolve
        $ M_aqua.trigger(T_aqua_treasure_found)

    if M_aqua.get_state() not in [S_aqua_treasure_search, S_aqua_treasure_unlock]:
        jump treasure_unlocked

    scene location_beach_lock with fade
    player_name "ah cara.."
    player_name "( Parece que eu preciso de uma {b}chave{/b}...E uma {b}combinação{/b} para abrir. )"
    $ callScreen("Treasure Lock", False, False)

label treasure_open:
    if treasure_key not in inventory.items:
        player_name "( Mesmo que eu soubesse a combinação, ainda tenho que encontrar a {b}chave{/b}! )"
    else:

        jump treasure_unlocked
    $ callScreen(location_count)

label treasure_unlocked:
    scene location_beach_treasure
    if M_aqua.get_state() == S_aqua_treasure_unlock:
        show expression "private/objects/object_compass_01.png" at Position(xpos = 537, ypos = 473)
        with fade
        hide expression "private/objects/object_compass_01.png"
        call screen treasure_chest
        show closeup_compass_01 at Position(xalign = 0.5, yalign = 1.0) with dissolve
        player_name "Uau!!"
        player_name "( Não acredito! Achei o tesouro!. )"
        player_name "( Essa deve ser a bússola que o Capitão Terry estava falando. )"
        show popup_item_compass1 at truecenter with dissolve
        $ inventory.items.append(golden_compass)
        pause
        hide popup_item_compass1 with dissolve
        hide closeup_compass_01 with dissolve
        $ M_aqua.trigger(T_aqua_treasure_unlocked)
    else:

        with fade
        pause
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
