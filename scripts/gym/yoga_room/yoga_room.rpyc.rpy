label yoga_room:
    $ location_count = "Yoga Room"
    if mrsj.started(mrsj_yoga_help) and is_here("anna"):
        jump mrsj_yoga_help
    elif not is_here("mrsj") and not is_here("anna"):
        scene expression gTimer.image("yoga_room{}")
        show player 12
        with dissolve
        player_name "( There's no one I know here... )"
        show player 35
        player_name "( I should come back another time, perhaps... )"
        hide player 35 with dissolve
    $ callScreen(location_count)

label mrsj_yoga_help:
    if not Anna.known(anna_intro):
        $ Anna.add_event(anna_intro)
        $ anna_intro.finish()
    scene yoga_room_night
    if yoga_fail_retry:
        show player 385 at left with dissolve
        show anna 2 at right with dissolve
        anna "Pronto para tentar de novo?"
        show anna 1
        show player 386
        player_name "Acho que sei as posições agora."
        show player 385
        anna "Apenas me diga qual posição e eu farei."
    else:

        show player 380 at left with dissolve
        show anna 12 at right with dissolve
        if Anna.known(anna_intro):
            anna "Desculpa?"
        else:
            "Desculpa?"
        show player 385
        if Anna.known(anna_intro):
            anna "Você viu a {b}Sra. Johnson{/b} por aí?"
        else:
            "Você viu a {b}Sra. Johnson{/b} por aí?"
        show anna 11
        show player 384
        player_name "Ela não vai poder vir hoje a noite."
        show player 386
        player_name "Ela me enviou para ajudar a dar aula hoje..."
        show player 385
        show anna 12
        if Anna.known(anna_intro):
            anna "Oh, ela disse o que é para você fazer, {b}[firstname]{/b}?"
        else:
            "Oh, ela disse o que é pra você fazer?"
        show anna 11
        show player 386
        player_name "Bom, {b}Sra. Johnson{/b} me deu essa lista de instruções."
        show player 381
        player_name "Eu olhei um pouco... Acho que consigo."
        if Anna.known(anna_intro):
            show player 386
            player_name "Ela disse que talvez você possa ajudar."
            show player 385
            show anna 2 with dissolve
            anna "Claro, vou ajudar você!"
            anna "E não se preocupe! Apenas me diga qual posição fazer, que eu farei."
        else:

            show player 384
            player_name "Você viu uma mulher chama, {b}Anna{/b}?"
            player_name "{b}Sra. Johnson{/b} disse que ela poderia me ajudar."
            show player 385
            show anna 3 with dissolve
            anna "Sou a {b}Anna{/b}!!"
            show anna 1
            show player 386
            player_name "Ah!!"
            show player 385
            show anna 3
            anna "Espero que você saiba o que está fazendo. Ha ha!"
            show anna 2
            anna "Estarei aqui para te ajudar com os movimentos, não se preocupe."
    hide player
    hide anna
    scene black
    with fade

    scene yoga_front
    show anna 14
    show player 411 at left
    with dissolve
    player_name "Hmm..."
    show player 412
    player_name "Ok, precisamos fazer três posições na ordem certa..."
    show player 411
    show anna 13
    anna "Ummm... Você está pronto?"
    show anna 14
    show player 414 with dissolve
    player_name "Acho que sim."
    show player 413
    show anna 13
    anna "Então, que posição começamos?"
    show anna 14
    show player 412 with dissolve
    $ yoga_position = ""
    $ boner_fail = False
    $ gTimer.tick()
    menu yoga_class:
        player_name "A primeira posição é..."
        "Happy Baby.":

            $ yoga_position = "Happy Baby"
            jump yoga_failure
        "Plow Position.":

            $ yoga_position = "Plow Position"
            jump yoga_failure
        "Downward Dog.":

            $ yoga_position = "Downward Dog"
            show player 414 with dissolve
            player_name "Precisamos fazer a {b}[yoga_position]{/b}?"
            show player 413
            show anna 15
            anna "Ah, certo. Adoro essa posição!"
            show anna 18 with dissolve
            anna "Por que não me encontra na esteira e me ajuda a fazer?"
            show anna 17
            show player 416
            player_name "Uhh... Ok."
            hide player
            show anna 19
            with dissolve
            pause
            pause
            anna "Não se proecupe em fazer força ao me puxar!"
            show anna 19_20
            pause
            show player 411 at left
            show anna 18
            with dissolve
            anna "Isso! Já me sinto mais flexível!"
            show anna 17
            show player 412

        "Terminar seção." if mrsj.completed(mrsj_yoga_help):
            jump yoga_end_lesson

    menu:
        player_name "Ok, a segunda posição, é..."
        "Happy Baby.":

            $ yoga_position = "Happy Baby"
            player_name "...a {b}[yoga_position]{/b}?"
            show player 413 with dissolve
            show anna 18
            anna "Claro!"
            anna "Uma das minhas favoritas."
            anna "Vou ficar de costas para que você possa esticar minhas pernas..."
            show anna 21 with dissolve
            show player 416
            player_name "!!!"
            hide player
            show anna 23
            with dissolve
            player_name "Esticar suas pernas?"
            show anna 24
            anna "Sim!"
            anna "Estique elas..."
            show anna 25 with dissolve
            pause
            pause
            pause
            show anna 27 with dissolve
            anna "Isso é muito bom..."
            show anna 28
            player_name "..."
            anna "Oh!!"
            show anna 26
            player_name "Ha ha! Acho que estamos prontos para a última posição!"
        "Plow Position.":

            $ yoga_position = "Plow Position"
            jump yoga_failure
        "Downward Dog.":

            $ yoga_position = "Downward Dog"
            jump yoga_failure

        "Terminar seção." if mrsj.completed(mrsj_yoga_help):
            jump yoga_end_lesson

    menu:
        player_name "A última posição é a..."
        "Happy Baby.":

            $ yoga_position = "Happy Baby"
            $ boner_fail = True
            jump yoga_failure
        "Plow Position.":

            $ yoga_position = "Plow Position"
            player_name "...{b}[yoga_position]{/b}?"
            show anna 27
            anna "Perfeito!"
            show player 420 at left
            show anna 29
            with dissolve
            pause
            show anna 30
            anna "Tudo o que você precisa fazer é pressionar... sua pélvis contra minha bunda."
            show anna 29
            show player 421
            player_name "Umm... Ok..."
            hide player
            show anna 31
            with dissolve
            pause
            show anna 32
            anna "Ahh, sim!"
            hide anna
            show anna_slow 31_32
            pause
            anna "Um pouco mais!!"
            hide anna_slow 31_32
            show anna_fast 31_32
            pause
            hide anna_fast 31_32
            jump yoga_success
        "Downward Dog.":

            $ yoga_position = "Downward Dog"
            $ boner_fail = True
            jump yoga_failure

        "Terminar seção." if mrsj.completed(mrsj_yoga_help):
            $ boner_fail = True
            jump yoga_end_lesson

    label yoga_failure:
        $ yoga_fail_retry = True
        if boner_fail:
            show player 419 at left
            show anna 21
        else:
            show player 418 at left
        with dissolve
        player_name "Umm... Acho que a {b}[yoga_position]{/b} é a próxima posição."
        player_name "Não tenho muita certeza."
        player_name "Não me lembro..."
        if boner_fail:
            show player 420
        else:
            show player 417
        show anna 13 with dissolve
        if mrsj.started(mrsj_yoga_help):
            anna "Acho que é melhor se terminarmos a seção por enquanto."
        anna "Podemos tentar de novo amanhã."
        if boner_fail:
            show player 419
        else:
            show player 418
        show anna 14
        player_name "Sim..."
        player_name "Desculpa."
        if boner_fail:
            show player 420
        else:
            show player 417
        show anna 13
        if mrsj.started(mrsj_yoga_help):
            anna "Dê uma olhada nas anotações da {b}Sra. Johnson{/b} e memorize as posições para a próxima seção."
        else:
            anna "Dê uma olhada nas anotações da {b}Sra. Johnson{/b} e memorize as posições para a próxima seção."
        if boner_fail:
            show player 419
        else:
            show player 418
        show anna 14
        player_name "Certo. Farei o que for possível..."
        hide anna
        hide player
        with dissolve

        scene yoga_room_night
        show player 24 with dissolve
        player_name "Droga... Não consigo fazer isso."
        if mrsj.started(mrsj_yoga_help):
            player_name "Eu deveria memorizar as posições para a próxima seção."
            show player 25
            player_name "Não posso fazer isso com a {b}Sra. Johnson{/b} e {b}Anna{/b}..."
        else:
            player_name "Eu deveria memorizar as posições e tentar de novo."
        hide player with dissolve
        $ callScreen(location_count)

    label yoga_success:
        show player 420 at left
        show anna 22
        with dissolve
        anna "Foi... ótimo!"
        show anna 21
        show player 419
        player_name "Me... perdoa sobre isso..."
        show player 420
        show anna 15 with dissolve
        anna "Oh! Ha ha!"
        show anna 13
        anna "Está tudo bem!"
        anna "Acontece com todo homem que vem aqui!"
        show anna 16
        anna "E eu não me importo com um puxão... extra..."
        if mrsj.completed(mrsj_yoga_help):
            $ callScreen(location_count)

        $ mrsj_yoga_help.finish()
        $ mrsj.add_event(mrsj_yoga_help_2)
        scene yoga_room_night
        show player 82 at left
        show anna 2 at right
        with dissolve
        anna "Estou impressionada!"
        anna "Você fez muito bem..."
        show anna 3
        anna "...E eu adorei ser sua assistente!"
        show anna 1
        show player 83
        player_name "Só estou querendo ajudar a {b}Sra. Johnson{/b}."
        show player 79 with dissolve
        player_name "Foi bem divertido."
        show player 82 at left with dissolve
        show anna 2
        anna "Tavelz você pudesse dar mais aulas... com minha ajuda?"
        anna "Quer dizer... se você quiser..."
        show anna 1
        show player 79 with dissolve
        player_name "Parece ser divertido!"
        show player 82 at left with dissolve
        show anna 2
        anna "Certifique-se de que venha de noite."
        anna "É quando a {b}Sra. Johnson{/b} não está aqui e eu preciso de ajuda..."
        show anna 1
        show player 83
        player_name "Umm... Claro."
        hide player
        hide anna
        with dissolve
        show unlock43 at truecenter with dissolve
        pause
        hide unlock43 with dissolve
        $ callScreen(location_count)

    label yoga_end_lesson:
        scene yoga_room_night
        if boner_fail:
            show player 82 at left
            show player 79
        else:
            show player 14 at left
        show anna 1 at right
        with dissolve
        player_name "Foi divertido!"
        if boner_fail:
            show player 82 at left with dissolve
        else:
            show player 13
        show anna 3
        anna "Sim!"
        show anna 2
        anna "Você fez muito bem dessa vez. Estou impressionada!"
        show anna 1
        if boner_fail:
            show player 79 with dissolve
        else:
            show player 14
        player_name "Valeu!"
        player_name "Só estava querendo ajudar."
        if boner_fail:
            show player 82 at left with dissolve
        else:
            show player 13
        show anna 2
        anna "Eu não me importaria em fazer isso de novo..."
        anna "...se vocẽ quisesse."
        show anna 1
        if boner_fail:
            show player 79 with dissolve
        else:
            show player 14
        player_name "Sem problemas!"
        if boner_fail:
            show player 82 at left with dissolve
        else:
            show player 13
        show anna 2
        anna "Ótimo! Até a próxima..."
        hide player
        hide anna
        with dissolve
        $ callScreen(location_count)

label anna_yoga_button_dialogue:
    scene yoga_room_night
    show anna 2 at right
    show player 13 at left
    with dissolve
    anna "Olá, {b}[firstname]{/b}."
    show anna 1
    show player 14
    player_name "Oi, {b}Anna{/b}."
    show player 13
    show anna 2
    anna "E aí?"
    show anna 1
    menu:
        "Onde está a {b}Sra. Johnson{/b}?":
            show player 14
            player_name "Estou procurando pela {b}Sra. Johnson{/b}."
            show player 30
            player_name "Você sabe onde eu poderia achar ela?"
            show player 5
            show anna 2
            anna "Ela normalmente dá aula de tarde."
            anna "Ela deve estar em casa agora..."
            show anna 1
            show player 14
            player_name "Ah. Entendi. Valeu!"
            show player 13
            show anna 3
            anna "Sem problemas!"
            show anna 1

        "Yoga" if mrsj.completed(mrsj_yoga_help):
            show player 10
            player_name "Quer praticar yoga comigo?"
            show player 5
            show anna 3
            anna "Claro!!"
            show anna 2
            anna "Gosto quando alguém me ajuda a chegar nessas... posições difícieis..."
            show anna 1
            show player 33
            player_name "Beleza, você é bem flexível pelo que eu me lembro."
            show player 13
            show anna 2
            anna "Certo, vamos achar um tapete de yoga..."
            hide anna
            scene location_yoga_front
            with fade
            show player 413 at left
            show anna 13
            with dissolve
            anna "Que posições devemos praticar?"
            $ yoga_position = ""
            $ boner_fail = False
            $ gTimer.tick()
            jump yoga_class
    $ callScreen(location_count)

label mrsj_yoga_button_dialogue:
    scene expression gTimer.image("yoga_room{}")
    if not mrsj.known(mrsj_yoga_intro):
        show player 1 at left with dissolve
        show erikmom 10 at right with dissolve
        player_name "Umm-"
        show player 11 at left
        window hide
        pause
        player_name "..."
        show erikmom 11 at right
        window hide
        pause
        show erikmom 12 at right
        window hide
        pause
        show erikmom 13 at right with hpunch
        erimom "Oh!"
        show player 18 at left
        erimom "...{b}[firstname]{/b}?"
        show erikmom 14 at right
        show player 17 at left
        player_name "Oi, {b}Mrs. Johnson{/b}!"
        show erikmom 17 at right
        show player 1 at left
        erimom "O que você está fazendo aqui?"
        show erikmom 14 at right
        show player 29 at left
        player_name "Eu... vi você na {b}academia{/b}!"
        player_name "Decidi vir aqui dar um oi!"
        show player 13 at left
        show erikmom 18 at right
        erimom "Isso é tão fofo!"
        show erikmom 17 at right
        erimom "Então, você está treinando agora?"
        show erikmom 14 at right
        show player 21 at left
        player_name "Haha. Sim..."
        player_name "...Comecei a treinar para ficar em forma!"
        show erikmom 19 at right
        show player 11 at left
        erimom "Creio que você vai ficar bem {b}duro{/b}-"
        erimom "..."
        show player 13 at left
        show erikmom 18 at right
        erimom "Digo, {b}forte{/b}!"
        show erikmom 14 at right
        show player 17 at left
        player_name "Espero que sim..."
        show erikmom 17 at right
        show player 1 at left
        erimom "Que seja, tem algo que você queira falar?"
        $ mrsj.add_event(mrsj_yoga_intro)
        $ mrsj_yoga_intro.finish()
    else:

        show player 14 at left
        show erikmom 14 at right
        with dissolve
        player_name "Oi, {b}Sra. Johnson{/b}!"
        show player 1 at left
        show erikmom 17 at right
        erimom "Oi, {b}[firstname]{/b}!"
        show player 11 at left
        show erikmom 18 at right
        erimom "Você está começando a ficar em forma, jovem!"
        show player 29 at left
        show erikmom 14 at right
        player_name "Oh. Valeu..."
        player_name "Igual você..."
        show player 1 at left
        show erikmom 17 at right
        erimom "Algo que você queira conversar?"

    menu erikmom_options_repeat:
        "Como está o Erik?":
            show player 10 at left
            show erikmom 14 at right
            player_name "Como está o {b}Erik{/b}?"
            player_name "Mal vejo ele."
            show erikmom 18 at right
            show player 5 at left
            erimom "Bom... Você sabe como ele está!"
            erimom "Ele ama aqueles jogos..."
            show player 10 at left
            show erikmom 14 at right
            player_name "Sim, mas isso está ficando pior ultimamente."
            player_name "Eu nem recebo mais mensagens dele..."
            show erikmom 19 at right
            show player 5 at left
            erimom "..."
            show erikmom 20 at right
            show player 11 at left
            erimom "Você sabe, o {b}pai{/b} nos deixou quando ele nasceu então..."
            erimom "...Ele teve uma infância solitária!"
            show erikmom 19 at right
            show player 12 at left
            player_name "...Nunca soube disso..."
            show erikmom 20 at right
            show player 11 at left
            erimom "Ele nunca teve um {b}pai{/b} ou {b}irmão{/b}!"
            erimom "E nem uma outra mulher... A não ser sua mãe..."
            show erikmom 19 at right
            erimom "...Então eu tento dar toda atenção que ele precisa!"
            show erikmom 14 at right
            show player 21 at left
            player_name "...Entendi. Acho que entendi."
            show erikmom 18 at right
            show player 13 at left
            erimom "De qualquer forma, eu quero agradecer por ser tão amigável com o meu filho!"
            erimom "Você é um bom amigo dele..."
            show erikmom 14 at right
            show player 17 at left
            player_name "Nós sempre fomos amigos, então..."
            show erikmom 18 at right
            show player 1 at left
            erimom "Vou falar pra ele mandar mais mensagens para você!"
            show erikmom 14 at right
            show player 14 at left
            player_name "Está tudo bem, só queria ter certeza que ele estava bem."
            show erikmom 17 at right
            show player 1 at left
            erimom "Algo a mais que você queira conversar?"
            jump erikmom_options_repeat
        "O que era aquilo?":

            show erikmom 14 at right
            show player 14 at left
            player_name "Qual era aquela {b}posição de yoga{/b} que você estava fazendo antes?"
            show erikmom 13 at right
            show player 13 at left
            show player 1 at left
            erimom "Ah, vou te mostrar!"
            show erikmom 12 at right
            show player 11 at left
            erimom "Você começa assim!"
            show erikmom 11 at right
            window hide
            pause
            show player 21 at left
            show erikmom 10 at right
            window hide
            pause
            erimom "Até nos seus joelhos!"
            window hide
            pause
            show player 21 at left
            player_name "Uhhh..."
            player_name "...Sim..."
            show player 11 at left
            erimom "É chamada de {b}Cat Cow{/b}!"
            show erikmom 11 at right
            window hide
            pause
            show erikmom 12 at right
            window hide
            pause
            show erikmom 13 at right
            show player 18 at left
            erimom "Não é tão difícil, né?"
            if not Anna.known(anna_intro):
                show anna 12f at Position (xpos=600)
                show erikmom 13 at right
                show player 13
                with dissolve
                anna "Olá, {b}Sra. Johnson{/b}."
                show anna 5f
                anna "Não me diga que você começou sem mim."
                show anna 4f
                show erikmom 18
                erimom "Claro que não! Só estava conversano com o amigo do meu filho!"
                show anna 11 at Position (xpos=700) with dissolve
                show erikmom 17b
                erimom "{b}Anna{/b}, esse é o {b}[firstname]{/b}. {b}[firstname]{/b}, essa é minha amiga, {b}Anna{/b}."
                show erikmom 14
                show player 36 with dissolve
                player_name "Hi!"
                show player 13 with dissolve
                show erikmom 14b
                show anna 12
                anna "Você é amigo do {b}Erik{/b}?"
                show anna 11
                show player 14
                show erikmom 14
                player_name "Sim. Somos amigos há anos."
                show player 12
                player_name "Você é professora aqui também?"
                show player 5
                show anna 2 with dissolve
                show erikmom 14b
                anna "Oh, não. Só estudo."
                show anna 1
                show player 13
                show erikmom 17
                erimom "{b}Anna{/b} é uma das minhas melhores alunas. Ela poderia ensinar se quisesse!"
                show erikmom 14b
                show anna 3
                anna "Ah, não acho! Ha ha!"
                show anna 2
                anna "Ela é uma excelente professora e sou apenas uma novata."
                show anna 1
                show erikmom 17
                erimom "{b}Anna{/b}, você só está sendo humilde."
                show erikmom 17b
                erimom "Ela pode ser iniciante, mas é muito talentosa... e bem flexível."
                show erikmom 14b
                show anna 3
                anna "Ha ha."
                show anna 2
                anna "Eu tenho que ir e me preparar para a seção."
                show anna 3
                anna "Tchau, {b}Sra. Johnson{/b}!"
                show anna 1
                show erikmom 17b
                erimom "Até mais."
                show erikmom 14b
                show anna 2
                anna "Foi um prazer te conhecer, {b}[firstname]{/b}."
                show anna 1
                show player 14
                show erikmom 14
                player_name "Tchau!"
                $ Anna.add_event(anna_intro)
                $ anna_intro.finish()
                hide anna with dissolve
            show erikmom 17 at right
            show player 1 at left
            erimom "Algo a mais que você queira conversar?"
            jump erikmom_options_repeat
        "Vocẽ está em uma ótima forma!":

            show erikmom 14 at right
            show player 29 at left
            player_name "Tenho que t falar, {b}Sra. Johnson{/b}, você está em uma ótima forma!"
            player_name "Você se exercita muito?"
            show erikmom 18 at right
            show player 13 at left
            erimom "Aw... Você é tão gentil!"
            show erikmom 17 at right
            erimom "Bem, eu venho aqui sempre que posso e tento usar a academia..."
            erimom "...Eu também faço corridas! E eu também faço yoga no meu quarto durante a noite...."
            show erikmom 19 at right
            show player 21 at left
            player_name "Bom, está funcionando!"
            show player 13 at left
            erimom "Você acha?"
            show erikmom 15 at right
            show player 11 at left
            erimom "Minha {b}bunda{/b} ainda está um pouco grande..."
            show erikmom 16 at right
            show player 23 at left
            erimom "...E meus {b}seios{/b} não são mais como costumavam ser..."
            player_name "..."
            show player 28 at left
            show erikmom 19 at right
            player_name "*gulp*"
            show player 1 at left
            show erikmom 18 at right
            erimom "Algo a mais que você queira conversar?"
            jump erikmom_options_repeat
        "Tenho que ir treinar!":

            show erikmom 14 at right
            show player 14 at left
            player_name "Eu deveria voltar ao treino!"
            show erikmom 18 at right
            show player 1 at left
            erimom "Então tá bom!"
            show erikmom 14 at right
            show player 17 at left
            player_name "Tchau, {b}Sra. Johnson{/b}!"
            hide player 17 at left with dissolve
            hide erikmom 14 at right with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
