label pizza_minigame:
    if bike not in inventory.items:
        scene location_pizza_blur with None
        show player 35 with dissolve
        player_name "Preciso achar uma {b}bicicleta{/b} ou algo do tipo, Serei muito lento a pé. Alguma coisa sobre rodas ajudará."
        hide player with dissolve
        jump pizza_interior_dialogue

    $ vehicle_movement = 3
    $ time_count = 100

    $ pizza_bg_sky_xpos = 0
    $ pizza_bg_road_xpos = 0
    $ pizza_bg_forest_xpos = 0
    $ pizza_bg_houses_xpos = 0

    $ pizza_slice01_xpos = 0
    $ pizza_slice02_xpos = 0
    $ pizza_slice03_xpos = 0

    $ pizza01_delivered = 0
    $ pizza02_delivered = 0
    $ pizza03_delivered = 0

    $ pizza_positions = [1200, 1800, 2400, 3000, 3600, 4200]
    $ delivery_positions = []

    $ renpy.random.shuffle(pizza_houses)

    $ counter = 0
    $ position_corrector = 0
    while (counter < 6):
        if pizza_houses[counter] == pizza_house_01 or pizza_houses[counter] == pizza_house_02:
            $ position_corrector = 408
        elif pizza_houses[counter] == pizza_house_03 or pizza_houses[counter] == pizza_house_04:
            $ position_corrector = 400
        elif pizza_houses[counter] == pizza_house_05 or pizza_houses[counter] == pizza_house_06:
            $ position_corrector = 274

        $ position_counter = counter + 1
        while (position_counter < 6):
            $ pizza_positions[position_counter] += position_corrector
            $ position_counter += 1

        $ pizza_positions[counter] += (position_corrector / 2)
        $ counter += 1

    $ renpy.random.shuffle(pizza_positions)

    $ random_position = renpy.random.choice(pizza_positions)
    $ counter = 0
    while (counter < 3):
        while (random_position in delivery_positions):
            $ random_position = renpy.random.choice(pizza_positions)
        $ delivery_positions += [random_position]
        $ counter += 1

    $ renpy.random.shuffle(delivery_positions)
    $ pizza_slice01_xpos = delivery_positions[0] - 63
    $ pizza_slice02_xpos = delivery_positions[1] - 63
    $ pizza_slice03_xpos = delivery_positions[2] - 66

    show screen pizza_minigame
    call screen pizza_minigame_buttons

label pizza_delivered:
    $ pizza_earnings = 0
    if pizza01_delivered == 1:
        $ pizza_earnings += 80
    if pizza02_delivered == 1:
        $ pizza_earnings += 80
    if pizza03_delivered == 1:
        $ pizza_earnings += 80

    if pizza01_delivered == 1 and pizza02_delivered == 1 and pizza03_delivered == 1:
        scene pizza_behind_c with None
        show xtra 12 zorder 2 with None
        show maria 1 zorder 1 at left
        show tony 2 zorder 1 at Position(xpos=400)
        show player 1f zorder 3 at right
        with dissolve
        tony "Sabia que podia contar com você, garoto!"
        show tony 1
        show player 14f
        player_name "Fiz bem?"
        show tony 2
        show player 1f
        tony "Muito bem!"
        tony "Aqui está o pagamento, volte mais tarde para mais encomendas!"
        show tony 1
        show player 17f
        player_name "Valeu, {b}Tony{/b}!"
    else:


        scene pizza_behind_c with None
        show xtra 12 zorder 2 with None
        show maria 1 zorder 1 at left
        show tony 4 zorder 1 at Position(xpos=400)
        show player 5f zorder 3 at right
        with dissolve
        tony "Recebi algumas  reclamação dos clientes..."
        tony "Eles disseram que a pizza chegou tarde e que estavam frias."
        show tony 1
        show player 10f
        player_name "Desculpa, Tony. Eu devo ter lido o endereço errado..."
        show player 11f
        show tony 2
        tony "Está tudo bem, garoto. Você é novo nisso, você melhorará ao longo do tempo."
        show player 1f
        tony "Aqui está o seu pagamento pelo trabalho que você fez, volte mais tarde quando tivermos mais entregas."
        show player 17f
        show tony 1
        player_name "Valeu, {b}Tony{/b}!"


    show unlock35 zorder 3 at truecenter
    show text "{size=30}{b}[pizza_earnings]{/b}{/size}" zorder 4 at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ inventory.money += pizza_earnings
    $ renpy.pause()
    hide text "{b}[pizza_earnings]{/b}"
    hide unlock35
    with dissolve
    hide player
    hide tony
    hide maria
    with dissolve
    hide xtra
    hide location_pizza_blur
    $ gTimer.tick()
    if gTimer.is_dark():
        jump map_dialogue
    else:
        jump pizza_interior_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
