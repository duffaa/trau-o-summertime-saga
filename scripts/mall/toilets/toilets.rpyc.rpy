label mall_toilets:
    $ location_count = "Mall Toilets"
    if rump_n_cunt in magic_numbers:
        scene mall_toilets_event_b
        player_name "( Um segurança? )"
        player_name "( O que está acontecendo aqui... ) "
    $ callScreen(location_count)

label mall_toilets_stall:
    scene mall_toilets_stall
    show player 1 at left with dissolve
    player_name "( Nada aqui... Só algumas manchas na parede. )"
    hide player with dissolve
    $ callScreen(location_count)

label rump_toilets_stall:
    scene mall_toilets_stall
    show rump_overlay zorder 3
    show rump_n_cunt 01_02_03_04 zorder 2 at left
    with fade
    $ renpy.pause(1, hard=True)
    rump "ISSSOOOO!"
    $ renpy.pause(1, hard=True)
    rump "SUA NOJENTAAA!!!"
    $ renpy.pause(1, hard=True)
    call screen button(Image = "boxes/auto_option_generic_02", Label = "rump_toilets_stall_block")

label rump_toilets_stall_block:
    scene mall_toilets_b with fade
    show player 37 at left with dissolve
    player_name "( ... )"
    show player 38
    player_name "( Esse é o prefeito Rump?! )"
    show player 22
    show rump_guard 1 at right
    with hpunch
    player_name "!!!"
    show rump_guard 2
    guard "Ei!"
    guard "Pessoas não são permitidas aqui!"
    guard "Preciso que você saia AGORA!!!"
    scene black with fade
    $ gTimer.tick()
    $ rump_n_cunt = 0
    $ location_count = "Mall"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
