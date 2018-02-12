default attic_first_visit = True
default fishing_rod_taken = False
default ring_taken = False
default cheerleader_outfit_taken = False

label attic_dialogue:
    $ location_count = "Attic"
    if attic_first_visit:
        $ attic_first_visit = False
        scene home_attic_cs with fade
        show text "Usei as chaves e consegui entar no nosso sótão.\nNunca estive aqui antes.\nEu não esperava para ver qual tesouro a [mom_name] e o papai deixaram aqui." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        with dissolve
    $ callScreen(location_count)

label ring:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_ring.png" with dissolve
    player_name "( Parece um anel bem caro! )"
    player_name "( O que estava fazendo todo esse tempo aqui? )"
    hide expression "objects/closeup_ring.png" with dissolve
    show expression "boxes/popup_ring.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_ring.png" with dissolve
    jump attic_dialogue

label cheerleader_outfit:
    scene expression gTimer.image("attic{}")




    show expression "boxes/popup_item_outfit1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_outfit1.png" with dissolve
    jump attic_dialogue

label fishing_rod:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_rod.png" with dissolve
    player_name "That's {b}Dad{/b}'s old {b}fishing rod{/b}!!"
    player_name "( Lembro de quando a gente ia pscar no {b}pier{/b}, quando eu era criança. )"
    player_name "{b}*Sigh*{/b}"
    player_name "Eu sinto falta do {b}papai{/b}..."
    hide expression "objects/closeup_rod.png" with dissolve
    show expression "boxes/popup_item_rod1.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_item_rod1.png" with dissolve
    jump attic_dialogue

label painting:
    scene expression gTimer.image("attic{}")
    show expression "objects/closeup_painting01.png" with dissolve
    player_name "{b}[mom_name]{/b} amava pintar sobre animais..."
    hide expression "objects/closeup_painting01.png" with dissolve
    jump attic_dialogue

label globe:
    scene location_home_attic_globe
    pause
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
