label movie_theatre_dialogue:
    if movie_theatre_count == 0:
        scene movie_lobby
        show player 14 with dissolve
        player_name "Legal!"
        show player 14
        player_name "( Novos filmes chegaram! )"
        show player 17
        player_name "( Hmm... Talvez eu pudesse trazer alguém para um encontro aqui... )"
        hide player 17 with dissolve
        $ movie_theatre_count = 1
    scene movie_lobby
    show movie_desk zorder 2
    show player 1f zorder 3 at right
    show bub 2 zorder 1 at Position(ypos=570, xpos=440)
    bub "Oi!"
    bub "Indo a um encontro, né?"
    show bub 1
    show player 14f
    player_name "Uhh... Sim?"
    show bub 2
    show player 1f
    bub "Óóóótimo!"
    bub "Tem algum filme que você gostaria de assistir?"
    hide bub
    hide player
    hide movie_desk
    scene movie_options
    call screen movieoptions

label after_movie_pick_dialogue:
    scene movie_lobby
    show movie_desk zorder 2
    show player 1f zorder 3 at right
    show bub 2 zorder 1 at Position(ypos=570, xpos=420) with dissolve
    bub "Boa escola!"
    show bub 3 at Position (xpos=470)
    bub "Aqui está seu ticket."
    show bub 1 at Position (xpos=420)
    show player 14f
    player_name "Valeu."
    show player 1f
    show bub 2
    bub "Não suje os bancos."
    bub "Eu odeio limpar essas coisas!"
    show bub 1
    show player 11f
    player_name "..."
    show bub 2
    bub "Divirta-se!"
    jump watch_movie

label watch_movie:
    scene movie with fade
    show popup_unfinished at truecenter with dissolve
    $ renpy.pause()
    hide popup_unfinished with dissolve
    hide movie
    jump mall_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
