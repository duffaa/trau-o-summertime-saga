default pizza_count = 0
default pizza_dialogue_advance = False
default pizza_seen = False
default deliver_pizzas = False

label pizza_exterior_dialogue:
    $ location_count = "Pizzeria Exterior"
    if pizza_seen == False:
        scene expression gTimer.image("backgrounds/location_pizza_outside{}.jpg")
        show player 14 with dissolve
        player_name "( Tony’s Pizza. Ele é conhecido por fazer a melhor pizza da cidade. )"
        hide player with dissolve
        $ pizza_seen = True
    $ callScreen(location_count)

label pizza_interior_dialogue:
    $ location_count = "Pizzeria Interior"
    $ tick_skip_active = False
    if pizza_count == 0 and pizza_dialogue_advance == False:
        scene location_pizza_blur
        show player 10f at right with dissolve
        show tony 1 at Position(xpos = 300, ypos = 768) with dissolve
        player_name "Olá! Alguém está-"
        show tony 2
        show player 11f
        tony "Eyyy, olha aí!"
        tony "Alto, jovem e bonito."
        tony "Me lembra de mim quando eu era jovem."
        show tony 1
        show player 10f
        player_name "Eu?"
        show tony 3
        show player 13f
        tony "Sim, você, me diga: Você está procurando por um emprego?"
        show tony 1
        show player 14f
        player_name "Sim, estou."
        show tony 2
        show player 203f
        tony "Ótimo. Eu poderia usar alguém como você."
        show player 10f
        show tony 1
        player_name "Alguém como eu?"
        show player 11f
        show tony 2
        tony "Claro! Alguém como você! Espere aqui, vou trazer minha eposa."
        show player 203f
        show maria 1 at left
        show tony 2
        tony "Maria: esse é o {b}[firstname]{/b}, {b}[firstname]{/b}: essa é a Maria."
        show tony 1
        show maria 2
        maria "Oi, {b}[firstname]{/b}. Eu acho que você vai ser o novo ajudante."
        show player 14f
        show maria 1
        player_name "Sim, parece que sim."
        show player 203f
        show maria 3
        maria "Tony, rápida pergunta: Sabemos se esse garoto é bom??"
        show maria 1
        show tony 2
        tony "Nós não, mas olhe para ele! Ele é jovem, cheio de energia, e ele parece saudável!"
        tony "O que mais precisamos?"
        show maria 2
        show player 11f
        show tony 1
        maria "Alguém que trabalhe, porque o último garoto que você contratou, era um adolescente preguiçoso."
        show maria 1
        show tony 3
        tony "Ele vai trabalhar. Prometo. Não é, {b}[firstname]{/b}?"
        show tony 1
        show player 14f
        player_name "Claro. Você está oferecendo, e eu preciso de um emprego."
        show tony 2
        show player 203f
        tony "Então está resolvido! Volte mais tarde e discutiremos mais as coisas."
        show maria 2
        tonymaria "Tenha um ótimo dia!"
        $ pizza_dialogue_advance = True
        hide tony
        hide maria
        hide player
    $ callScreen(location_count)

label tony_dialogue:
    if deliver_pizzas == False:
        scene pizza_behind_c with None
        show xtra 12 zorder 2 with None
        show maria 1 zorder 1 at left
        show tony 2 zorder 1 at Position(xpos=400)
        show player 1f zorder 3 at right
        with dissolve
        tony "Ei, garoto!"
        tony "Pronto pra trabalhar?"
        show tony 1
        show player 14f
        player_name "Claro!"
        show tony 2
        show player 1f
        tony "Ótimo! Antes de começarmos, certifique-se de que você tenha uma {b}bicicleta{/b} ou algo do tipo - algo - que te faça andar mais rápido."
        tony "Pegue as caixas no balcão e entregue para o endereço certo!"
        tony "Ah, os nossos clientes amam as pizzas quentinhas."
        tony "Então, o quanto antes você entregar, maior será seu pagamento!"
        show tony 1
        show player 14f
        player_name "Parece bom, {b}Tony{/b}!"
        hide player
        hide tony
        hide maria
        with dissolve
        hide xtra
        $ deliver_pizzas = True
    else:

        scene pizza_behind_c with None
        show xtra 12 zorder 2 with None
        show maria 1 zorder 1 at left
        show tony 2 zorder 1 at Position(xpos=400)
        show player 1f zorder 3 at right
        with dissolve
        tony "As caixas estão aqui, garoto!"
        hide player
        hide tony
        hide maria
        with dissolve
        hide xtra
    $ callScreen(location_count)

label pizza_closed:
    scene expression "backgrounds/location_pizza_outside_night.jpg"
    show player 14 with dissolve
    player_name "Não posso trabalhar a noite!"
    hide player
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
