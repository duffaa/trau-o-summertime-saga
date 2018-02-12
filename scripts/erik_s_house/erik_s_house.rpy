default erik_mail = []
default poker_drunk = False
default erik_drunk = False

label erik_house_dialogue:
    $ location_count = "Erik's House"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if gTimer.is_morning():
        if not erik.known(erik_intro):
            scene erikhouse
            show player 2 at left with dissolve
            show erik 1 at right with dissolve
            player_name "Eai, {b}Erik{/b}!"
            show erik 5 at right
            show player 1 at left
            eri "Eae, {b}[firstname]{/b} ..."
            show player 10 at left
            show erik 1 at right
            player_name "Você parece muito cansado... Está tudo bem?"
            show erik 3 at right
            show player 5 at left
            eri "Fiquei a noite toda jogando esse jogo novo..."
            show erik 2 at right
            show player 5 at left
            eri "...E eu odeio ir para a escola."
            show erik 3 at right
            eri "Queria ficar em casa o dia todo."
            show player 10 at left
            show erik 1 at right
            player_name "To ligado, entendi..."
            show erik 3 at right
            show player 24 at left
            eri "Lamento pelo seu {b}pai{/b}... Espero que sua família esteja bem."
            show player 25 at left
            show erik 1 at right
            player_name "Estamos bem... Valeu por perguntar..."
            player_name "Nós realmente devemos ir antes de chegar atrasado para a aula."
            hide player 25 at left with dissolve
            hide erik 1 at right with dissolve

            show unlock13 at truecenter
            $ renpy.pause()
            hide unlock13 with dissolve
            $ loc_school_unlocked = True
            $ erik.add_event(erik_intro)
            hide erikhouse

        elif erik.started(erik_intro):
            scene erikhouse
            show player 11 at left
            show erik 5 at right
            eri "Não deveriamos ir para a {b}escola{/b}?"
            show erik 1 at right
            show player 14 at left
            player_name "Uhum. Tem razão..."
            hide player 14 at left
            hide erik 1 at right
            hide erikhouse

        elif erik.over(erik_intro) and not gTimer.is_weekend():
            scene erikhouse
            show player 12 with dissolve
            player_name "( Não tem ninguém aqui... )"
            show player 35
            player_name "( {b}Erik{/b} já deve ter saido para a {b}escola{/b}. )"
            hide player 35 with dissolve
            hide erikhouse
        $ callScreen(location_count)
    else:

        if not mrsj.known(mrsj_intro) and gTimer.is_afternoon():
            scene erikhouse
            show player 1 at left with dissolve
            show erikmom 2 at right with dissolve
            erimom "Oi, {b}[firstname]{/b}!"
            show erikmom 1 at right
            show player 14 at left
            player_name "Oi, {b}Sra. Johnson{/b}! Só vim ver o {b}Erik{/b}!"
            show erikmom 4 at right
            show player 1 at left
            eri "Eae, {b}[firstname]{/b}!"
            show erikmom 5 at right
            show player 11 at left
            erimom "Aqui está meu garotinho!"
            show erikmom 6 at right
            eri "{b}Mãe{/b}! Já te disse pra não me chamar assim..."
            show erikmom 7 at right
            show player 5 at left
            erimom "{b}Erik{/b} me falou sobre seu pai..."
            erimom "Lamento por isso. Fale se você precisar de alguma ajuda, ok?"
            show erikmom 8 at right
            show player 10 at left
            player_name "Ok, {b}Sra. Johnson{/b}."
            show erikmom 7 at right
            show player 13 at left
            erimom "Beleza! Vou deixar vocês conversarem! Tenho que ir para a minha aula de yoga."
            show erikmom 8 at right
            show player 1 at left
            erimom "Cuide do meu garoto, {b}[firstname]{/b}!"
            erimom "Ele tem muita sorte de ter você como amigo."
            erimom "Tchau, menino!"
            show erikmom 6 at right
            eri "Tchau, {b}mãe{/b}."
            hide erikmom 6 at right with dissolve
            show erik 1 at right with dissolve
            show player 14 at left
            player_name "Cara... Tua mãe é tão bonita!"
            show erik 3 at right
            show player 1 at left
            eri "Um... Sim... Eu acho..."
            show erik 1 at right
            show player 26 at left
            player_name "Tipo... Pra idade dela, Quer dizer... Cara, ela estã em uma BOA forma..."
            show erik 5 at right
            show player 1 at left
            eri "Não sei... Ela fica bastante na {b}academia{/b}."
            eri "Ela dá aula de yoga na {b}academia{/b}."
            show erik 1 at right
            show player 14 at left
            player_name "Mas eai, você quer sair... ou?"
            show erik 3 at right
            show player 11 at left
            eri "Não posso agora. Tenho que... Baixar esse jogo e-"
            show erik 1 at right
            show player 12 at left
            player_name "Beleza, {b}Erik{/b}. Até outro dia."
            show player 36 at left
            show erik 7 at right
            eri "Beleza. Até..."
            hide player 36 at left with dissolve
            hide erik 7 at right with dissolve
            hide erikhouse
            $ mrsj.add_event(mrsj_intro)
    $ callScreen(location_count)

label door18_locked_dialogue:
    if location_count == "Erik's House":
        scene erikhouse
    elif location_count == "Erik's Backyard":
        scene eriks_backyard_b
    show player 11 at left
    show erik 5 at right
    eri "Umm... Por que estamos indo para minha casa?"
    eri "Não deveriamos estar indo para a {b}escola{/b}?"
    show erik 1 at right
    show player 14 at left
    player_name "Ah, sim! Tem razão..."
    hide player 14 at left
    hide erik 1 at right
    $ callScreen(location_count)

label unfinished_dialogue4:
    scene erikhouse
    show player 14
    player_name "Ainda não tem nada para fazer aqui, o jogo ainda está em desenvolvimento!"
    show player 26
    player_name "Mas já já, você poderá visitar {b}Erik{/b}... E falar com a mãe dele!"
    show player 17
    player_name "Volte quando a próxima versão do jogo sair!"
    hide player 17 with dissolve
    $ callScreen(location_count)

label erik_gf_stolen:
    if location_count == "Erik's House":
        scene expression gTimer.image("erikhouse{}")
    elif location_count == "Erik's Backyard":
        scene expression gTimer.image("eriks_backyard{}_b")
    show player 10
    with dissolve
    player_name "Eu não deveria tornar isso mais estranho do que já é..."
    player_name "Vou esperar até amanhã para falar com ele."
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_thief_block:
    scene erikhouse_night
    show player 2 with dissolve
    player_name "Eu deveria pegar o {b}ladrão{/b}."
    hide player 2 with dissolve
    $ callScreen(location_count)

label closed_erik:
    if not gTimer.is_dark():
        if location_count == "Erik's House":
            scene erikhouse
        elif location_count == "Erik's Backyard":
            scene eriks_backyard_b
        show player 12 with dissolve
        player_name "( Não tem ninugém aqui... )"
        show player 35
        player_name "{b}Erik{/b} já deve ter saido para a {b}escola{/b}."
    else:

        if location_count == "Erik's House":
            scene erikhouse_night
        elif location_count == "Erik's Backyard":
            scene eriks_backyard_n_b
        show player 2 with dissolve
        player_name "( {b}Erik{/b} deve estar dormindo. Deveria voltar amanhã. )"
        hide player 2 with dissolve
    $ callScreen(location_count)

label closed_erik_weekend:
    if location_count == "Erik's House":
        scene erikhouse
    elif location_count == "Erik's Backyard":
        scene eriks_backyard_b
    show player 12 with dissolve
    player_name "( Não tem ninguém em casa. )"
    show player 35
    player_name "( {b}Erik{/b} deve ter saído com a sua mãe para algum lugar. )"
    hide player 35 with dissolve
    $ callScreen(location_count)

label erik_mailbox:
    scene expression gTimer.image("erik_mailbox{}")
    if m_magazine in erik_mail:
        show expression "objects/object_mailbox_item01_closeup.png" with dissolve
        player_name "( Huh. Uma revista. O que será que é... )"
        player_name "( Milfness? Acho que é para a {b}Sra. Johnson{/b}. Não sabia que ela assinava essas coisas... )"
        player_name "( É melhor eu colocar isso de volta. )"
        hide expression "objects/object_mailbox_item01_closeup.png" with dissolve

    elif m_dad_letter in erik_mail:
        player_name "( Eu não sabia que eles receberam cartas. Para quem será que é... )"
        player_name "( É para o {b}Erik{/b}. )"
        menu:
            "Deixar.":
                call screen erik_mailbox
            "Abrir.":

                show expression "objects/object_mailbox_item03_closeup.png" at Position(xpos = 565, ypos = 768) with dissolve
                player_name "( Uma carta do pai dele?! )"
                player_name "( Eu não sabia que ele ainda estava tentando contatá-lo... )"
                player_name "Melhor eu devolver isso."
                hide expression "objects/object_mailbox_item03_closeup.png" with dissolve
                call screen erik_mailbox
        $ erik_mailbox_items.remove(dad_letter)
    elif m_pizza_pamphlet in erik_mail:
        player_name "( Parece ser propaganda. )"
        show expression "objects/object_mailbox_item02_closeup.png" with dissolve
        player_name "( Tony's Pizza. Não vou lá faz tempo. )"
        player_name "( Melhor eu colocar de volta. )"
        hide expression "objects/object_mailbox_item02_closeup.png" with dissolve
        if not loc_pizza_unlocked:
            show expression "boxes/popup_pizza.png" at truecenter with dissolve
            $ renpy.pause()
            hide expression "boxes/popup_pizza.png" with dissolve
            $ loc_pizza_unlocked = True

    elif m_newspaper in erik_mail:
        player_name "( Notícias locais. Pode ser interessante... )"
        show expression "objects/object_newspaper.png" with dissolve
        player_name "( O ladrão ainda está a solta? E eu achando que iriam pegar ele. )"
        player_name "( Melhor devolver isso. )"
        hide expression "objects/object_newspaper.png" with dissolve
    call screen erik_mailbox

label erik_house:
    $ location_count = "Erik's House"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
