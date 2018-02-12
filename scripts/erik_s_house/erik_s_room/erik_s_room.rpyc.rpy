label erik_room_dialogue:
    $ location_count = "Erik's Room"
    if erik.over(erik_crown_card) and not erik.known(erik_orcette):
        scene expression gTimer.image("erik_house_bedroom{}_b")
        show player 12 with dissolve
        player_name "( Huh, {b}Erik{/b} não está aqui, ele deve estar no porão... )"
        hide player with dissolve
    elif erik.completed(erik_bullying) and not erik.known(erik_bullying_2):
        jump erik_bullying
    elif erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        scene expression gTimer.image("erik_house_bedroom{}_b")
        show player 30 with dissolve
        player_name "Huh?"
        player_name "( {b}Erik{/b} normalmente está no computador. )"
        show player 12
        player_name "( Ele deve estar no porão... )"
        hide player with dissolve
    elif erik.over(erik_path_split) and erik.started(erik_sex_ed):
        jump erik_sex_ed
    elif June.started(june_intro):
        jump june_intro
    elif erik.started(erik_breastfeeding):
        scene expression gTimer.image("erik_house_bedroom{}_b")
        show player 12 with dissolve
        player_name "( Ninguém aqui? )"
        show player 14
        player_name "( Deve estar no porão... )"
        show player 11
        pause
        show player 10
        player_name "Huh?"
        player_name "( Acho que ouvi algo vindo do quarto da {b}Sra. Johnson{/b}. )"
        show player 12
        player_name "( Eu deveria ver onde o {b}Erik{/b} está... )"
        hide player with dissolve
        $ erik_breastfeeding.finish()

    if is_here("erik"):
        if not erik.started(erik_card_hunt) and not is_here("june"):
            $ playSound("<loop 3>audio/ambience_erikroom.ogg")
    $ callScreen(location_count)

label june_intro:
    scene expression gTimer.image("erik_house_bedroom{}_b")
    show player 1 at left
    show erik 4 at right
    with dissolve
    eri "Eae, cara."
    eri "Você falou com minha mãe?"
    show player 14
    show erik 1
    player_name "Sim, ela acha que pode ser uma boa ideia você conhecer outras garotas..."
    show player 1
    show erik 5
    eri "Oh, sério?"
    show player 14
    show erik 1
    player_name "Uhum, e eu concordo com ela!"
    show erik 3c
    player_name "Eu posso tentar te ajudar..."
    show player 11
    show erik 3b
    eri "Não sei, {b}[firstname]{/b}."
    show erik 3
    eri "Não acho que vou achar a garota certa para mim..."
    show player 10
    show erik 2
    player_name "O quê?"
    show player 11
    show erik 3b
    eri "Alguém que goste de mim!"
    show player 10
    show erik 3c
    player_name "Como assim?"
    show erik 3b
    show player 11
    eri "Estou gordo, não sou bom em conversa com outras pessoas..."
    show player 5
    eri "... Perceba isso, cara, sou um trabaplhão..."
    show erik 3
    eri "... A única coisa em que eu sou bom, é em jogar!"
    show player 10
    show erik 3c
    player_name "E?"
    show player 14
    player_name "E se eu achar uma garota que goste de jogar?"
    show player 1
    show erik 5
    eri "Uma garota que goste de jogar..."
    show erik 4
    eri "Eu... Acho que sim?"
    show player 4
    show erik 1
    player_name "Hmm..."
    show player 14
    player_name "Você conhece alguma garota na escola que jogue video game?"
    show player 11
    show erik 4
    eri "...Tem uma garota da outra sala... Ela é fofa."
    show player 14
    show erik 1
    player_name "Tem uma garota na escola que você gosta?"
    show player 1
    show erik 5
    eri "Não sei... ela parece... legal!"
    show player 14
    show erik 1
    player_name "Qual o nome dela?"
    show player 1
    show erik 4
    eri "Acho que é {b}June{/b}."
    show player 14
    show erik 1
    player_name "Você já conversou com ela?"
    show player 1
    show erik 14
    eri "Uma vez..."
    eri "... Eu, uh, eu perguntei pra ela..."
    show player 11
    show erik 3
    eri "Não, na verdade não."
    show erik 3b
    eri "Eu acho que pegou emprestado um dos meus lápis, uma vez..."
    show player 14
    show erik 3c
    player_name "Por que você não conversa com ela?!"
    show player 11
    show erik 3
    eri "Não consigo!"
    show erik 3b
    eri "Sou MUITO tímido..."
    eri "... e eu nem sei o que eu falaria com ela."
    show player 35
    show erik 3c
    player_name "Tá, certo, isso pode ser um pouco mais difícil do que eu imaginava."
    show player 11
    show erik 3
    eri "Talvez devessemos desistir..."
    show erik 2
    eri "*suspiro*"
    show player 10
    player_name "O quê?!"
    show player 14
    show erik 3c
    player_name "Não, {b}Erik{/b}!"
    player_name "Você vai ver! Acho que ela vai gostar de você..."
    player_name "Onde que ela geralmente está?"
    show player 1
    show erik 1
    eri "Hmm..."
    show erik 5
    eri "Eu já vi ela no laboratório de informática várias vezes."
    show player 14
    show erik 1
    player_name "No {b}laboratório de informática{/b} da {b}escola{/b}?"
    show player 1
    show erik 4
    eri "Sim. Fica no segundo andar..."
    show player 14
    show erik 1
    player_name "Vou ver ela, talvez eu consiga algo para você."
    show player 1
    show erik 4
    eri "Ok, valeu, cara."
    show erik 1
    $ june_intro.finish()
    jump erik_talk

label erik_sex_ed:
    scene expression gTimer.image("eriks_room{}_c")
    show player 13 at left
    show erik 5 at right
    with dissolve
    eri "Hey, {b}[firstname]{/b}!"
    eri "Você falou com minha mãe?"
    show erik 1
    show player 14
    player_name "Sim, ela disse que precisa pensar sobre isso..."
    show player 13
    show erik 5
    eri "Talvez não devessemos ter-"
    show erik 1b
    show player 11
    erimom "Garoto?"
    erimom "Você podem vir aqui, por favor?"
    show erik 1
    show player 10
    player_name "É sua mãe?"
    show player 5
    show erik 5
    eri "Sim... Acho que ela está no quarto dela."
    show erik 1
    show player 14
    player_name "Ela quer que vamos lá..."
    show player 13
    show erik 5
    eri "Por quê?"
    show erik 1
    show player 14
    player_name "Vamos descobrir..."
    hide player
    hide erik
    with dissolve
    $ erik_sex_ed.finish()
    $ callScreen(location_count)

label erik_bullying:
    scene expression gTimer.image("eriks_room{}_c")
    show player 13 at left with dissolve
    show erik 5 at right with dissolve
    eri "Eae, {b}[firstname]{/b}."
    eri "Como você está?"
    show erik 1
    show player 14
    player_name "Estou bem."
    show player 12
    player_name "E você?"
    player_name "Você andou faltando na escola ou algo do tipo?"
    show player 5
    show erik 2 with dissolve
    eri "..."
    show player 10
    player_name "Está tudo bem?"
    show player 5
    show erik 5 with dissolve
    eri "Minha mãe tem mandou aqui, né?"
    show erik 3b
    show player 10
    player_name "Apenas estou vendo se você está bem, só isso."
    show player 5
    show erik 5
    eri "Bom... {b}Dexter{/b} está na minha cola desde que você parou de ir..."
    eri "É difícil ir à escola sabendo que ele estará lá também. Esperando..."
    show erik 3b
    show player 12
    player_name "O que houve enquanto eu estava fora?"
    show player 5
    show erik 5
    eri "Algumas semanas atrás, eu estava sentado na cantina e ele apareceu..."
    show erik 3
    eri "...Ele exigiu uma cópia da tarefa das aulas da {b}Sra. Bissette{/b}."
    show player 12
    player_name "E o que você fez?"
    show player 11
    show erik 5
    eri "Eu disse não!"
    eri "Mas, ele disse que iria me prender em um armário, se eu não fizesse o que ele pediu..."
    show erik 3b
    player_name "..."
    show erik 5
    eri "No fim, eu acabei dando a lição de casa."
    show erik 3b
    show player 38 with dissolve
    player_name "E o que houve?"
    show player 11 with dissolve
    show erik 5
    eri "Eu disse a ele que ele não pode me ameaçar o tempo todo."
    eri "E então... Ele me bateu na frente de todo mundo..."
    show erik 2 with dissolve
    show player 16
    pause
    show player 12
    player_name "Escuta, {b}Erik{/b}..."
    show erik 3 with dissolve
    show player 10
    player_name "Estou feliz por você ter me contado."
    show player 30
    player_name "Me diga se ele te incomodar de novo."
    player_name "E espero que ele encha o saco de outra pessoa!"
    show player 13
    show erik 5
    eri "Beleza, valeu {b}[firstname]{/b}."
    show erik 3b
    show player 14
    player_name "Preparado pra ir pra escola então?"
    show player 13
    show erik 5
    eri "Sim, eu acho..."
    eri "Mas, você poderia não contar nada pra minha mãe que estou sendo ameaçado?"
    eri "Não quero que ela se preocupe..."
    show erik 3b
    show player 2
    player_name "Ok."
    hide player
    hide erik
    with dissolve
    $ erik.add_event(erik_bullying_2)
    $ callScreen(location_count)

label erik_cards:
    if eriks_cards in inventory.items:
        show erik 1 at right
        show player 14 at left
        player_name "Achei suas cartas, {b}Erik{/b}!"
        show player 239_240
        pause
        show player 374 with dissolve
        player_name "Toma..."
        show player 5 with dissolve
        show erik 36 at Position (xpos=1014) with dissolve
        eri "Valeu!"
        eri "Aqui, veja essa nova carta."
        eri "Não tem como eu perder no torneio com essa..."
        show erik 38
        eri "..."
        eri "Onde está?"
        pause
        show player 11
        eri "Não! Não está aqui!"
        show player 12
        player_name "Qual é a carta?"
        show player 11
        show erik 37
        eri "É a {b}Cock Crown of Thorns{/b}!"
        show erik 2 at right with dissolve
        eri "Nem fodendo..."
        eri "Eu vou perder agora."
        show erik 3
        eri "Era a minha... preciosa..."
        show player 34
        player_name "Hmm..."
        show player 33
        player_name "Tenho uma ideia."
        show player 13
        show erik 5
        eri "Sério?"
        show erik 3b
        show player 17
        player_name "Não se preocupe, {b}Erik{/b}. Vou procurar essa cata."
        show player 13
        show erik 5
        eri "Como?"
        show erik 3b
        show player 35
        player_name "Acho que já vi essa carta na {b}Cosmic Cumics{/b} algumas semanas atrás."
        show player 13
        show erik 5
        eri "Mas... não é muito caro?"
        show erik 5b
        eri "E eu não tenho muito dinheiro..."
        show erik 3b
        pause
        show player 14
        player_name "Sem problemas! Eu tô trabalhano para minha {b}tia Diane{/b}."
        show player 13
        show erik 4
        eri "Você é o melhor, cara!"
        show erik 1
        show player 14
        player_name "Sem problemas, {b}Erik{/b}! Não me importo em te ajudar..."
        show player 17
        player_name "...E você tem que vencer esse torneio!"
        $ inventory.items.remove(eriks_cards)
        $ erik_card_hunt.finish()
        $ erik.add_event(erik_crown_card)
    else:
        show erik 1 at right
        show player 10 at left
        player_name "Onde você viu sua carta pela última vez?"
        show player 11
        show erik 5
        eri "Hmm... Na última vez ela estava aqui."
        eri "Eu estava jogando no porão... Mas, minha mãe deve ter colocado em algum lugar..."
        show erik 1
        show player 14
        player_name "Vou te ajudar a encontrar."
        show player 13
        show erik 5
        eri "Valeu."
        show erik 3
        eri "Tenho que achar antes do torneio no próximo fim de semana..."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_crown_card:
    if card02 in inventory.items:
        show erik 1 at right
        show player 14 at left
        player_name "Consegui a carta que você queria."
        show player 13
        show erik 4
        eri "A {b}Cock Crown of Thorns{/b}!?"
        show erik 1
        show player 2
        player_name "Essa mesmo!"
        show player 239_240
        pause
        show player 372 with dissolve
        player_name "Aqui..."
        show player 13 with dissolve
        show erik 40 at Position (xpos=1014) with dissolve
        eri "Você é demais! Muito obrigado!"
        eri "Com essa carta, minha vitória está garantida!"
        eri "Eu vou ser imparável! Os plebeus se curvarão diante de mim..."
        show erik 39
        show player 17
        player_name "Ha ha."
        show player 13
        pause
        show erik 41
        eri "Espere um segundo."
        show erik 36 with dissolve
        eri "Quero que você pegue fique com essa carta..."
        show erik 30 at Position (xpos=1025) with dissolve
        show player 10
        player_name "Carta?"
        show player 11
        show erik 31
        eri "É uma das minhas favortias... Mas eu tenho ela repetida..."
        show erik 1 with dissolve
        show player 371 with dissolve
        player_name "Huh..."
        hide player
        hide erik
        with dissolve
        show card_03_c at Position (ypos=650) with dissolve
        pause
        hide card_03_c with dissolve
        show erik 1 at right
        show player 370 at left
        with dissolve
        player_name "...Valeu!"
        show player 13 with dissolve
        show erik 4
        eri "Sem problemas!"
        eri "Foi muito bom você ter me conseguido a carta."
        eri "Além disso, eu sei que você vai cuidar dela corretamente."
        show erik 1
        show player 14
        player_name "Certo, valeu!"
        show player 13
        show erik 5
        eri "Apenas... Certifique-se de mantê-la fora da luz solar para que ele não estrague."
        show erik 1
        show player 17
        player_name "Ha ha, prometo..."
        $ inventory.items.remove(card02)
        show unlock37 at truecenter with dissolve
        $ inventory.items.append(card03)
        pause
        hide unlock37 with dissolve
        $ erik_crown_card.finish()
    else:
        show erik 1 at right
        show player 10 at left
        player_name "Qual carta você precisava mesmo?"
        show player 11
        show erik 5
        eri "Hmm... Se chama {b}Cock Crown of Thorns{/b}."
        eri "Você disse que viu na {b}Cosmic Cumics{/b}?"
        show erik 1
        show player 14
        player_name "Ah, certo!"
        player_name "Vou ver se está lá..."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_package:
    if orcette in inventory.items:
        show erik 1 at right
        show player 376 at left with dissolve
        player_name "Aqui, seu novo brinquedo!"
        show player 378
        show erik 4
        eri "O que? Você já pegou?"
        show erik 1
        show player 376
        player_name "Uhum!"
        show player 13 with dissolve
        show erik 43 at Position (xpos=1014) with dissolve
        eri "Ótimo!"
        eri "Isso é... incrível!"
        eri "Eles até colocaram as cores iguais..."
        show player 14
        player_name "Você já usou isso antes?"
        show player 13
        show erik 44
        eri "Não, mas sempre quis!"
        eri "É que... minha mãe piraria se descobrice."
        show erik 42
        show player 12
        player_name "Uhh... Acho que não, sua mãe é bem legal!"
        show player 13
        show erik 44
        eri "Maybe..."
        show erik 42
        show player 12
        player_name "Isso é... fácil de limpar?"
        show player 13
        show erik 43
        eri "Vem com instruções, mas eu deveria ter que lavar isso."
        show erik 42
        pause
        show erik 43
        pause
        show player 18
        player_name "..."
        show player 17
        player_name "Oh {b}Erik{/b}..."
        show player 18
        show erik 44
        eri "O quê?!"
        show erik 42
        show player 14
        player_name "Nada."
        show player 13
        show erik 43
        pause
        show player 33
        player_name "Eu deveria deixar vocês sozinho..."
        show player 13
        show erik 44
        eri "{b}[firstname]{/b}, obrigado novamente."
        show erik 43
        show player 14
        player_name "De nada..."
        player_name "...Apenas não se esqueça de trancar a porta!"
        $ inventory.items.remove(orcette)
        $ erik_orcette_2.finish()
        $ event_wait_till = gTimer.gameDay() + 2
    else:
        show erik 1 at right
        show player 12 at left
        player_name "Qual era o item que você queria mesmo?"
        show player 13
        show erik 5
        eri "É tipo um tubo de plástico... Se chama {b}Orcette{/b}..."
        eri "Você consegue achar na internet."
        eri "Certifique-se de entregar na sua casa e que minha mãe não veja isso."
        show erik 1
        show player 14
        player_name "Certo, entendi."
        show player 13
        show erik 4
        eri "Valeu, [firstname]."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_vr_game:
    if game02 in inventory.items and virtualsaga in inventory.items:
        show erik 1 at right with dissolve
        show player 14 at left with dissolve
        player_name "Comprei!"
        show player 239_240
        pause
        show player 400
        player_name "Comprei o óculos de realidade virtual!"
        show player 399
        show erik 4
        eri "Ah, sério?!"
        show player 13 with dissolve
        show erik 46 with dissolve
        eri "Wow... Deve ter sido muito caro..."
        show erik 47
        eri "Quanto custou?!"
        show erik 45
        show player 17
        player_name "Ehh, não se preocupe com isso."
        show player 14
        player_name "Eu estava guardando dinheiro."
        show player 13
        show erik 46
        eri "Isso é... incrível."
        show erik 45
        show player 12
        player_name "Ah, o jogo também!"
        show player 13
        show erik 47
        eri "Valeu, {b}[firstname]{/b}."
        eri "Falei sobre trazer pessoas para o porão para a mamãe."
        eri "Ela não se importou muito."
        eri "Ela sempre quer que eu tenha amigos mesmo..."
        show erik 45
        show player 14
        player_name "Ótimo!"
        show player 33
        player_name "Hmm... Estou pensando em quem podemos convidar."
        show player 13
        show erik 47
        eri "Não tenho ninugém em mente, mas eu irei com quem você encontrar!"
        show erik 45
        show player 14
        player_name "Ok!"
        show player 13
        show erik 46
        eri "Obrigado novamente pelo óculos VR! Mal posso esperar para usar!"
        show erik 49 with dissolve
        show player 14
        player_name "De nada."
        eri "Incrível..."
        show erik 49
        pause
        player_name "Até mais, {b}Erik{/b}."
        $ inventory.items.remove(game02)
        $ inventory.items.remove(virtualsaga)
        $ erik_vr.finish()
    else:
        show erik 1 at right
        show player 10 at left
        with dissolve
        player_name "O que você queria em troca do porão mesmo?"
        show player 5
        show erik 5
        eri "Hmm... O Óculos VR, {b}Virtual Saga X{/b}..."
        show erik 4
        eri "...E o jogo chamado {b}World of Orcette{/b}..."
        show erik 1
        show player 10
        player_name "Onde vende mesmo?"
        show player 5
        show erik 5
        eri "Na {b}Cosmic Cumics{/b}."
        show erik 1
        show player 14
        player_name "Beleza, vou ver se acho.."
        show player 13
        show erik 4
        eri "Valeu, {b}[firstname]{/b}!"
    hide player
    hide erik
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
