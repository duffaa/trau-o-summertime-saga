default hill_first_visit = True

label hill_dialogue:
    $ location_count = "Hill"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 129>audio/ambience_ravenhill.ogg"):
            $ playSound("<loop 129>audio/ambience_ravenhill.ogg")
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if hill_first_visit and not M_mia.get_state() == S_mia_find_harold:
        scene expression gTimer.image("hill{}_b")
        show player 32 with dissolve
        player_name "Uau! Que bela visão!"
        show player 14 at Position(xpos = 444)
        player_name "( Lugar perfeito para trazer uma garota num encontro... )"
        show player 4 at Position(xpos = 450)
        player_name "( ...se eu tivesse um carro! )"
        hide player with dissolve
        $ hill_first_visit = False

    elif M_mia.get_state() == S_mia_find_harold:
        scene expression gTimer.image("hill{}")
        show harold_car_02 at Position (xpos=575,ypos=550)
        show player 31 with dissolve
        player_name "..."
        show player 32
        player_name "( Estou vendo um carro de polícia. )"
        player_name "( Será que é o {b}Harold{/b}? )"
        hide player with dissolve
    $ callScreen(location_count)

label hill_tree:
    scene expression gTimer.image("location_lair_hill_tree{}")
    if scroll not in inventory.items:
        if not gTimer.is_dark():
            show expression "private/objects/object_scroll_01.png" at Position(xalign = 0.45, yalign = 0.65)
        else:
            show expression "private/objects/object_scroll_01_night.png" at Position(xalign = 0.45, yalign = 0.65)
        player_name "O que é isso? Um pergaminho antigo?"
        player_name "Há quanto tempo isso está aqui?"
        call screen hill_tree
        show popup_item_scroll1 at truecenter with dissolve
        $ inventory.items.append(scroll)
        pause
        hide popup_item_scroll1 with dissolve
    else:

        pause
    $ callScreen(location_count)

label harolds_car_dialogue:
    scene hill_c
    show harold 28 at right
    show player 10 at left
    with dissolve
    player_name "{b}Harold{/b}?!"
    show player 11
    show harold 19
    harold "Hey... O que você {b}*Hic*{/b} está fazendo aqui... Você não deveria estar dormindo?"
    show harold 18
    show player 12
    player_name "Ehh... É meio dia, senhor."
    show player 11
    show harold 20
    harold "Oh, sim. Certo."
    show harold 19
    harold "Então esqueça..."
    show harold 18
    show player 10
    player_name "Você está bem, senhor?"
    show player 5
    show harold 19
    harold "Acho que vou {b}*Hic*{/b} sobreviver..."
    harold "...Minha mulher está se virando {b}*Hic*{/b} sem mim... Então, por que não conseguiria?!"
    show harold 20
    harold "Eu posso cuidar de mim mesmo {b}*Hic*{/b}... Não preciso da ajuda de ninguém..."
    show harold 19
    harold "Perai... O que você estava me perguntando mesmo???"
    show harold 18
    show player 11
    player_name "?!?"
    show player 12
    player_name "Bom, {b}Mia{/b} e {b}Helen{/b} não ouviram notícias suas há dias... Elas estavam preocupadas com você..."
    player_name "...E eu disse que iria me certificar que vocẽ estava bem."
    player_name "Até seus colegas de trabalho estavam preocupados."
    show player 10
    player_name "Acho que muitas pessoas se importam com você!"
    show player 5
    show harold 19
    harold "Mesmo?!"
    harold "Eu {b}*Hic*{/b}, err... Espera, como você me encontrou?!"
    show harold 18
    show player 12
    player_name "Eu fui perguntar no seu escritório..."
    player_name "...E vi uma foto antiga sua com a {b}Helen{/b} na sua mesa."
    player_name "Quando vcoês costumavam passar um tempo aqui."
    show player 5
    show harold 27
    harold "..."
    show harold 28
    harold "*suspiro*"
    show harold 20
    harold "As coisas eram mais {b}*Hic*{/b}... fácies naquele tempo..."
    harold "Eu era feliz... e me sentia eu mesmo, não fingia ser alguém que não era, sabe?"
    harold "Eu nem sei quem eu sou mais..."
    show harold 18
    show player 10
    player_name "Por que você não volta a ser como era antes?"
    show player 5
    show harold 19
    harold "O quê {b}*Hic*{/b}... Como assim?"
    show harold 18
    show player 10
    player_name "Você deixou de ser você mesmo... Talvez esse seja o problema!"
    show player 5
    show harold 28
    harold "..."
    show harold 20
    harold "Talvez você esteja certo..."
    show harold 19
    harold "...Mas {b}Helen{/b} não é mais a mesma também."
    show harold 18
    show player 14
    player_name "Acho que ela também pode mudar!"
    player_name "Dê a ela uma chance..."
    show player 13
    show harold 19
    harold "Tenho que admitir, você fez um ótimo trabalho me procurando..."
    harold "...E fico grato por você ajudar minha família."
    show harold 18
    show player 10
    player_name "Só queria ver vocês felizes de novo."
    show player 5
    show harold 27
    harold "..."
    show harold 20
    harold "Eu deveria {b}*Hic*{/b} voltar para a delegacia..."
    harold "...E então eu ligo para casa."
    show harold 19
    harold "Até mais, garoto!"
    show harold 18
    show player 36 with dissolve
    player_name "Cuide-se, {b}Harold{/b}!"
    show player 13
    hide harold
    with dissolve
    pause
    show player 12
    player_name "( Isso foi... interessante... )"
    player_name "( Talvez eu devesse contar a {b}Mia{/b} que eu encontrei e ele estava bem... )"
    hide player with dissolve
    $ M_mia.trigger(T_harold_found)
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
