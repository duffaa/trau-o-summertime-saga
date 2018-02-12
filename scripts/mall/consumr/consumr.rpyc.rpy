label consumr:
    $ location_count = "Consumr"
    if quest10 in quest_list and quest10 not in completed_quests:
        scene consumr
        show player 4 with dissolve
        player_name "( Deve ter vários tipos de pesticidas aqui. )"
        show player 10
        player_name "( Não sei qual que eu preciso. )"
        player_name "( Acho que eu deveria perguntar a {b}atendente{/b} assim como a {b}tia Diane{/b} sugeriu. )"
        hide player
    $ callScreen(location_count)

label veronica_dialogue_button:
    scene location_consumr_closeup
    show player 1 at left with dissolve
    show veronica 2 at right with dissolve
    vero "Bem-vindo ao {b}CONSUM-R{/b}! Meu nome é {b}Veronica{/b}."
    show veronica 4
    vero "Como eu poderia te ajudar?"
    menu:
        "Estou bem.":
            show player 2
            show veronica 1
            player_name "Uhm..."
            show player 17
            player_name "Estou bem, valeu!"
            show veronica 4
            show player 1
            vero "Sem problemas!"
            show veronica 2
            vero "Me avise se precisar de algo."

        "Pesticida?" if quest10 in quest_list and quest10 not in completed_quests:
            show veronica 1
            show player 4
            player_name "Uh..."
            show player 12
            player_name "Eu estou procurando por um pesticida?"
            show veronica 4
            show player 1
            vero "Ah, sim! Temos vários tipos de pesticida aqui!"
            show veronica 1
            show player 2
            player_name "Hmm... Quero um contra insetos?"
            show veronica 3
            show player 1
            vero "Ehhhh... Tem vários tipos de pesticidas para insetos..."
            show veronica 2
            show player 11
            vero "Você sabe que tipo de inseto você está lidando?"
            show veronica 1
            show player 10
            player_name "Não sei exatamente qual que é..."
            show veronica 3
            show player 13
            vero "Como ele {b}se parece{/b}?"
            menu:
                "Asas grandes.":
                    show veronica 1
                    show player 35
                    player_name "Ele tem um par e asas grandes..."
                    show veronica 3
                    show player 11
                    vero "Hmm... Pod ser {b}gafanhotos{/b}..."
                    show veronica 4
                    show player 1
                    vero "Pegue o inseticida com {b}tampa vermelha{/b}. O nome é {b}Bug Exterminator{/b}."
                    show veronica 2
                    vero "Esse deverá funcionar!"
                    show veronica 1
                    show player 17
                    player_name "Certo, obrigado!"
                "Asas nas costas.":

                    show veronica 1
                    show player 35
                    player_name "Tem asas grandes..."
                    show veronica 3
                    show player 11
                    vero "Hmm... Talvez seja {b}tesourinhas{/b}... Insetos desagradáveis!"
                    show veronica 4
                    show player 1
                    vero "Acho que o inseticida com a {b}tampa verde{/b}. O nome é {b}Bug Annihilator{/b}."
                    show veronica 2
                    vero "Isso será útil!"
                    show veronica 1
                    show player 17
                    player_name "Certo, valeu!"
                "Manchas brancas.":

                    show veronica 1
                    show player 35
                    player_name "Tem manchas brancas na casca..."
                    show veronica 3
                    show player 11
                    vero "Hmm... Pode ser {b}besouros{/b}..."
                    show veronica 4
                    show player 1
                    vero "Compre um inseticida com {b}tampa azul{/b}. É chamado de {b}Bug Eradicator{/b}."
                    show veronica 2
                    vero "Isso dará conta!"
                    show veronica 1
                    show player 17
                    player_name "Certo, valeu!"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
