default dex_first_visit = True

label basket_court_dialogue:
    $ location_count = "Basket Ball Court"
    if M_dex.get_state() == S_dex_start and is_here("dexter"):
        scene basketball_b
        show player 5 at left
        show dexter 3 at right
        with dissolve
        dex "Que que cê tá fazendo aqui?"
        show dexter 1
        show player 12
        player_name "Por que você se importa? Talvez eu esteja aqui apenas para treinar."
        show player 11
        show dexter 3
        dex "Hah!"
        dex "Essa foi boa."
        show dexter 1
        show player 25
        player_name "*suspiro*"
        show player 12
        player_name "O que você quer, {b}Dexter{/b}?"
        show player 5
        show dexter 6 with dissolve
        dex "Apenas fique longe da minha quadra, entendeu?"
        hide dexter with dissolve
        show player 24
        player_name "..."
        hide player with dissolve
        $ M_dex.trigger(T_dex_territory)
    $ callScreen(location_count)

label dexter_court_dialogue:
    scene basketball_b
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "Não disse pra você ficar longe?"
    dex "O que um fracassado como você quer?"
    show dexter 1
    menu:
        "Desafiar.":
            show player 12
            player_name "Estou aqui para te desafair, {b}Dexter{/b}."
            show player 5
            show dexter 3
            dex "Ha ha!"
            dex "Para o quẽ?!"
            show dexter 1
            show player 10
            player_name "Para uh..."
            show player 5
            show dexter 3
            dex "Cê sabe que eu te venço em qualquer coisa."
            show dexter 4 with dissolve
            dex "Agora cai fora antes que eu te de uma surra."
            $ M_dex.trigger(T_dex_challenge)
        "Nada.":

            show player 10
            player_name "Eu... ehh... não quis encomodar você."
            player_name "Tenho que ir para a aula."
            show player 5
            show dexter 3
            dex "Vaza, fracassado."
    hide dexter
    hide player
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
