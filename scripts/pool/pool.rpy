label pool_dialogue:
    $ location_count = "Pool"
    $ used_changing_girls = []
    if not gTimer.is_dark():
        if banned_from_pool:
            scene pool
            show player 108f at left with dissolve
            player_name "( Não posso ficar aqui. )"
            player_name "( Fui {b}banido{/b} da piscina. )"
            show player 34 at left
            player_name "Hmm..."
            show player 35 at left
            player_name "( Talvez eu devesse voltar quando {b}ninguém estiver aqui{/b}... )"
            hide player 35 at left with dissolve
            hide pool
            hide ui
            jump map_dialogue

        elif gloryhole_done == 1 and not banned_from_pool:
            scene pool
            if wearing_swimsuit:
                show player 53f at left with dissolve
            else:
                show player 1 at left with dissolve
            show ronda 8 at right with dissolve
            ron "Isso é o suficiente..."
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 51f at left
            else:
                show player 11 at left
            player_name "..."
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            player_name "Como assim?"
            show ronda 8 at right
            if wearing_swimsuit == True:
                show player 51f at left
            else:
                show player 13 at left
            ron "...Sério?"
            ron "Você acha que sou idiota?"
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            show ronda 10 at right
            player_name "...O quê?"
            show ronda 8 at right
            if wearing_swimsuit:
                show player 53f at left
            else:
                show player 13 at left
            ron "Você passou uma hora na sala de salva-vidas com a {b}Cassie{/b}."
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            player_name "...E?"
            show ronda 8 at right
            if wearing_swimsuit:
                show player 53f at left
            else:
                show player 13 at left
            ron "Seu desempenho dramático na piscina antes: Mostrando para todo mundo sua... ereção..."
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 21 at left
            player_name "O que você quer dizer?"
            show ronda 8 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            ron "Todo mundo sabe que a {b}Cassie{/b} leva caras que ela gosta para lá!!!"
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45 at left
            else:
                show player 37 at left
            player_name "Você acha que ela gosta de mim?"
            show ronda 9 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            ron "{b}MEU DEUS{/b}! Para de se fazer de burro!"
            ron "Você não acha que ela ficou impressionada com seu pinto {b}gigante{/b}?!"
            ron "É o único motivo pelo que ela levou {b}você lá{/b}!!!"
            show ronda 10 at right
            if wearing_swimsuit == True:
                show player 45
            else:
                show player 21 at left
            player_name "...Você acha que meu pinto é tão grande assim?"
            show ronda 9 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 22 at left
            ron "!!!"
            ron "Não é-"
            ron "Não estou falando isso!"
            show ronda 10 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            player_name "..."
            show ronda 8 at right
            ron "Ela é uma vagabunda, ok?"
            show ronda 10 at right
            if wearing_swimsuit:
                show player 50f at left
            else:
                show player 17 at left
            player_name "...Ela foi muito legal comigo na verdade."
            show ronda 8 at right
            if wearing_swimsuit:
                show player 51f at left
            else:
                show player 11 at left
            ron "Ugh. Seu porco..."
            hide player
            hide ronda 8 at right
            with dissolve
            hide pool
            $ gloryhole_done = 2
        $ callScreen(location_count)
    else:

        if banned_from_pool:
            scene pool_night zorder 1
            show player 14 zorder 2 at left with dissolve
            player_name "( Aqui vamos nós! )"
            show player 17 zorder 2 at left
            player_name "( Posso finalmente nada em paz! )"
            show player 11 at left
            player_name "{b}*Barulho de água*{/b}"
            show player 90 at left
            player_name "..."
            show player 127 at left
            player_name "( Tem alguém na piscina? )"
            player_name "( Não enxergo muito no escuro... )"
            hide player with dissolve
            scene pool_night02
            with dissolve
            scene pool_night03
            with Dissolve(0.2)
            scene pool_night04
            with Dissolve(0.2)
            scene pool_night05
            with Dissolve(0.2)
            show player 17 at left with dissolve
            player_name "( Acho que não sou o único que tive essa ideia! )"
            player_name "( Tô indo também! )"
            show player 8 at left
            player_name "Aqui vou eu!!"
            jump in_pool_dialogue
        else:

            scene pool_night
            if wearing_swimsuit:
                show player 49f with dissolve
            else:
                show player 2 with dissolve
            player_name "( A {b}piscina{/b} está fechada. Acho que não posso nadar agora. )"
            hide player with dissolve
            hide pool_night
    $ callScreen(location_count)

label cassie_button_dialogue:
    scene location_pool_closeup1
    show cassie 2 at right
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    cas "Posso te ajudar com algo?"
    show cassie 4
    if wearing_swimsuit:
        show player 45
    else:
        show player 108f
    player_name "Umm... Quais eram as {b}regras{/b} mesmo?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 1
    show cassie 2
    cas "Você não pode nadar com essas roupas..."
    show cassie 3
    cas "Você tem que usar um desses {b}provadores{/b} para colocar a {b}roupa de nadar{/b}!"
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    show cassie 4
    player_name "Oh. Certo! Valeu!"
    $ callScreen(location_count)

label ronda_button_dialogue:
    scene location_pool_closeup2
    if gloryhole_done == 0:
        if wearing_swimsuit:
            show player 53f at left with dissolve
        else:
            show player 1 at left with dissolve
        show ronda 5 at right with dissolve
        ron "..."
        show ronda 6 at right
        ron "O que você está fazendo aqui?"
        show ronda 5 at right
        if wearing_swimsuit:
            show player 50f at left
        else:
            show player 17 at left
        player_name "Me exercitando!"
        player_name "Eu achei que eu tinha que começar em algum lugar, e isso pode me ajudar a me preparar para as qualificatórias!"
        show ronda 6 at right
        if wearing_swimsuit:
            show player 51 at left
        else:
            show player 11 at left
        ron "Olha: Eu não vou ajudar você, muito menos iria na água ao mesmo tempo que você... Então, esqueça, ok?"
        show ronda 5 at right
        if wearing_swimsuit:
            show player 53 at left
        else:
            show player 26 at left
        player_name "Tudo bem!"
        player_name "Posso fazer isso sozinho..."
        show ronda 7 at right
        if wearing_swimsuit:
            show player 51 at left
        else:
            show player 11 at left
        ron "Ugh... Que seja."
        $ pool_count = 4
        hide player
        hide ronda 7 at right
        with dissolve
        hide pool
    else:

        if wearing_swimsuit:
            show player 53f at left with dissolve
        else:
            show player 1 at left with dissolve
        show ronda 8 at right with dissolve
        ron "Veio para fazer uma visitinha para a Cassie?"
        show ronda 10 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 12 at left
        player_name "Uhh... Só estou aqui para nadar."
        show ronda 8 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 11 at left
        ron "Pare de fingir..."
        ron "...Você não está aqui para treinar igual a mim."
        show ronda 8 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 12 at left
        player_name "Uhh... ok?"
        show ronda 9 at right
        if wearing_swimsuit:
            show player 51f at left
        else:
            show player 11 at left
        ron "Ugh... você é patético."
        hide player
        hide ronda 9 at right
        with dissolve
    $ callScreen(location_count)

label poolrules01_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    show cassie 1 at right with dissolve
    cas "{b}*APITO*{/b}"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 22 at left
    player_name "!!!"
    show cassie 2 at right
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 11 at left
    cas "Ei!"
    cas "Você não pode ir nadar assim!"
    cas "Você tem que se trocar primeiro!"
    if quest03 not in completed_quests:
        $ quest_list.append(quest03)
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 29 at left
    show cassie 4 at right
    player_name "Desculpa! É minha primeira vez aqui..."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 13 at left
    show cassie 2 at right
    cas "Use um dos {b}três provadores{/b}..."
    show cassie 3 at right
    cas "...E se você não tem uma {b}roupa de natação{/b}, não poderei deixar você nadar!"
    show cassie 4 at right
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    player_name "Certo! Entendi!"
    hide player
    hide cassie 4 at right
    with dissolve
    $ callScreen(location_count)

label poolrules02_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53 at left with dissolve
    else:
        show player 1 at left with dissolve
    show cassie 1 at right with dissolve
    cas "{b}*APITO*{/b}"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 22 at left
    player_name "!!!"
    show cassie 2 at right
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 11 at left
    cas "Ei! {b}[firstname]{/b}!!"
    cas "Você esqueceu de se trocar de novo?"
    cas "Você sabe que tem que se trocar primeiro..."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 29 at left
    show cassie 4 at right
    player_name "Ah, sim, {b}Cassie{/b}!"
    player_name "Desculpa, eu esqueci!"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 13 at left
    show cassie 2 at right
    cas "Você deveria usar a sala de salva-vidas... Ninguém está usando isso..."
    show cassie 4 at right
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    player_name "Ok! Valeu..."
    hide player
    hide cassie 4 at right
    with dissolve
    $ callScreen(location_count)

label poolrules03_dialogue:
    scene pool
    if wearing_swimsuit:
        show player 53f at left with dissolve
    else:
        show player 1 at left with dissolve
    show cassie 1 at right with dissolve
    cas "{b}*APITO*{/b}"
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 22 at left
    player_name "!!!"
    show cassie 2 at right
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 11 at left
    cas "Ei!"
    cas "Essa é a sala de salva-vidas!"
    cas "Você não pode ir aí. É só para empregados."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 29 at left
    show cassie 4 at right
    player_name "Desculpa! É minha primeira vez aqui..."
    if wearing_swimsuit:
        show player 51f at left
    else:
        show player 13 at left
    show cassie 2 at right
    cas "Use um dos {b}três provadores{/b}..."
    show cassie 4 at right
    if wearing_swimsuit:
        show player 50f at left
    else:
        show player 17 at left
    player_name "Certo! Entendi!"
    hide player
    hide cassie 4 at right
    with dissolve
    $ callScreen(location_count)

label pool_cutscene01:
    $ first_swim = False
    $ almost_drowned = True
    show poolcutscene01 with dissolve
    show text "É a minha primeira vez na piscina desde que eu estava na escola.\nSó dei algumas voltas e já estou cansado!\nSó mais umas voltas..." at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide text with dissolve

    scene black with dissolve
    with Pause(0.5)

    show poolcutscene01b with dissolve
    show text "O que está acontecendo...\nNão tenho mais forças... tão pesado...\nNão posso-" at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide text with dissolve

    hide poolcutscene01
    hide poolcutscene01b with dissolve

    $ changing_count = 0

    scene black with dissolve
    with Pause(0.5)
    jump rescued_dialogue

label pool_cutscene02:
    show poolcutscene01 with dissolve
    show text "Não é a minha primeira vez na piscina e eu aprendi a me acelerar.\nEu sou capaz de fazer algumas voltas sem problemas e terminar meu treinamento!." at Position (xpos= 512, ypos = 700) with dissolve
    $ renpy.pause ()
    hide ui
    hide text with dissolve
    scene black with dissolve
    hide poolcutscene01

    $ changing_count = 0

    with Pause(0.3)
    if not ronda_after_swimming:
        jump ronda_after_swimming
    else:
        jump pool_dialogue

label ronda_after_swimming:
    scene pool
    show player 46 at left with dissolve
    show ronda 6 at right with dissolve
    ron "Nada mal!"
    ron "Pelo menos você não se afogou desta vez..."
    show ronda 5 at right
    show player 47 at left
    player_name "Uhh... Valeu?"
    show player 48 at left
    show ronda 8 at right
    ron "Não fique muito feliz. Eu já vi cachorros nadar melhor..."
    hide player
    hide ronda 8 at right
    with dissolve
    hide pool
    $ ronda_after_swimming = True
    $ callScreen(location_count)

label changing01_dialogue:
    $ rand_girl = renpy.random.choice(changing_girls)
    if wearing_swimsuit:
        scene changeroom01
        show player 45 with dissolve
        player_name "Uhm..."
        player_name "( Já me troquei... Não preciso ir aí. )"
        hide player 45 with dissolve
        hide changeroom01
        $ callScreen(location_count)

    elif changing_count == 0 and not wearing_swimsuit:
        scene changeroom01
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1 at right with dissolve
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2 at right with dissolve
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3 at right with dissolve
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4 at right with dissolve
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5 at right with dissolve
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6 at right with dissolve
        else:
            jump changing01_dialogue
        show player 1 at left with dissolve
        window hide
        pause
        show player 23 at left with hpunch
        player_name "..."
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1b at right
            $ used_changing_girls.append("girl1")
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2b at right
            $ used_changing_girls.append("girl2")
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3b at right
            $ used_changing_girls.append("girl3")
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4b at right
            $ used_changing_girls.append("girl4")
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5b at right
            $ used_changing_girls.append("girl5")
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6b at right
            $ used_changing_girls.append("girl6")
        if rand_girl == "girl1":
            Character("Emma") "Ei! Saia daqui!!!"
        elif rand_girl == "girl2":
            Character("Lily") "O que você está fazendo, aberração?!"
        elif rand_girl == "girl3":
            Character("Olivia") "Ei, você devia me pagar uma bebida primeiro!"
        elif rand_girl == "girl4":
            Character("Ivy") "Ei, você devia me pagar uma bebida primeiro!"
        elif rand_girl == "girl5":
            Character("Amelie") "Ei! Cai fora daqui!!!"
        elif rand_girl == "girl6":
            Character("Sammy") "O que você está fazendo, aberração?!"
        show player 42 at left
        player_name "Oops!"
        player_name "...Desculpa!"
        hide player 42 at left with dissolve
        hide changing
        hide changeroom01
        $ changing_count = 1
        $ callScreen(location_count)

    elif changing_count == 1 and not wearing_swimsuit:
        scene changeroom01
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1 at right with dissolve
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2 at right with dissolve
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3 at right with dissolve
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4 at right with dissolve
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5 at right with dissolve
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6 at right with dissolve
        else:
            jump changing01_dialogue
        show player 1 at left with dissolve
        window hide
        pause
        show player 23 at left with hpunch
        player_name "..."
        if rand_girl == "girl1" and rand_girl not in used_changing_girls:
            show changing 1b at right
            $ used_changing_girls.append("girl1")
        elif rand_girl == "girl2" and rand_girl not in used_changing_girls:
            show changing 2b at right
            $ used_changing_girls.append("girl2")
        elif rand_girl == "girl3" and rand_girl not in used_changing_girls:
            show changing 3b at right
            $ used_changing_girls.append("girl3")
        elif rand_girl == "girl4" and rand_girl not in used_changing_girls:
            show changing 4b at right
            $ used_changing_girls.append("girl4")
        elif rand_girl == "girl5" and rand_girl not in used_changing_girls:
            show changing 5b at right
            $ used_changing_girls.append("girl5")
        elif rand_girl == "girl6" and rand_girl not in used_changing_girls:
            show changing 6b at right
            $ used_changing_girls.append("girl6")
        if rand_girl == "girl1":
            Character("Emma") "Ei! Saia daqui!!!"
        elif rand_girl == "girl2":
            Character("Lily") "O que você está fazendo, aberração?!"
        elif rand_girl == "girl3":
            Character("Olivia") "Ei, você devia me pagar uma bebida primeiro!"
        elif rand_girl == "girl4":
            Character("Ivy") "Ei, você devia me pagar uma bebida primeiro!"
        elif rand_girl == "girl5":
            Character("Amelie") "Ei! Cai fora daqui!!!"
        elif rand_girl == "girl6":
            Character("Sammy") "O que você está fazendo, aberração?!"
        show player 42 at left
        player_name "Oops!"
        player_name "...Desculpa!"
        hide changing with dissolve
        $ changing_count = 2
        if first_time_changing:
            $ first_time_changing = False
            jump caught_dialogue
        hide player 42 at left with dissolve
        hide changeroom01
        $ callScreen(location_count)

    elif changing_count == 2 and not wearing_swimsuit:
        scene changeroom01
        show player 43 with dissolve
        player_name "Finalmente! Um provador vazio!"
        show player 35
        player_name "( Eles deveriam deixar um aviso quando alguém estiver usando... )"
        show player 8
        window hide
        pause
        hide player 8
        show player 44
        player_name "( Aqui! Tudo pronto! )"
        hide player 44
        hide changeroom01
        $ wearing_swimsuit = True
        $ changing_count = 3
        $ poolrules_count = 3
        $ used_changing_girls = []
    $ callScreen(location_count)

label caught_dialogue:
    scene changeroom01
    show player 5f at right
    show cassie 61 at left
    with dissolve
    cas "O que está acontecendo aqui?!"
    show cassie 60
    show player 22f
    player_name "!!!"
    show cassie 59
    show player 13f
    cas "{b}Você{/b} de novo?!"
    cas "Acabei de receber uma queixa de assédio-"
    show cassie 60
    show player 10f
    player_name "Não, não é isso que parece!!"
    show player 11f
    show cassie 59
    cas "Para mim, parece que você está tentando assistir as meninas se trocando..."
    show player 10f
    show cassie 60
    player_name "Eu só queria achar um provador-"
    show player 5f
    show cassie 59
    cas "E você não pensou em verificar primeiro??"
    show player 10f
    show cassie 60
    player_name "Mas, não tem uma porta para bater-"
    show player 11f
    show cassie 59
    cas "Dê suas desculpas para outra pessoa."
    show player 23f with hpunch
    cas "Você está {b}banido{/b} dessa piscina."
    show player 10f
    show cassie 60
    player_name "O quê?!"
    player_name "Mas eu preciso me exercitar para os testes da escola-"
    show player 5f
    show cassie 61
    cas "E desde quando isso é um problema meu?"
    cas "Quero que você {b}saia{/b} agora."
    show player 10f
    show cassie 60
    player_name "..."
    $ banned_from_pool = True
    $ used_changing_girls = []
    hide player
    hide cassie
    hide changeroom01
    hide ui
    jump map_dialogue

label in_pool_dialogue:
    scene pool_water_night
    show cassie 62 zorder 2 at right
    with fade
    window hide
    pause
    show player 115 zorder 1 at Position(xpos = 230, ypos = 470) with Dissolve(0.3)
    window hide
    show player 116 zorder 1 at left
    show cassie 63 zorder 2
    with Dissolve(0.4)
    cas "!!!"
    show player 123 at left with dissolve
    player_name "AH! MERDA!"
    show cassie 73
    player_name "Você está {b}pelada{/b}!!?"
    show cassie 67
    show player 125 at left
    cas "O QUE VOCÊ ESTÁ FAZENDO AQUI??!"
    show player 120 at left
    show cassie 73
    player_name "Hey! Você é a {b}salva vidas{/b} que trabalha aqui de tarde!!"
    show player 121 at left
    show cassie 72
    cas "..."
    show player 124 at left
    show cassie 67
    cas "Espere... Você é aquele pervertido espiando as meninas!"
    show player 125 at left
    cas "Eu não disse que você não está banido aqui??"
    show player 120 at left
    show cassie 66
    player_name "Ei!! {b}NÃO{/b} era o que eu estava fazendo!"
    show player 126 at left
    player_name "E eu estou banido aqui durante o dia, então eu tive que ir à noite!"
    show player 120 at left
    player_name "...Espera..."
    show cassie 73
    player_name "O que {b}VOCÊ{/b} está fazendo aqui pelada de noite??"
    show player 121 at left
    show cassie 64
    cas "I... Ugh... Não diga pra ninguém!"
    show player 124 at left
    cas "Nós dois podemos ter problemas por estar aqui tão tarde..."
    show cassie 65
    show player 126 at left
    player_name "Bem... Eu não vou contar a ninguém, mas você tem que me deixar treinar de novo!"
    show cassie 64
    show player 122 at left
    cas "Ugh... Me traga uma toalha..."
    show cassie 65
    show player 118 at left
    window hide
    pause
    show player 119 at left
    player_name "Aqui."
    show player 117 at left
    show cassie 68
    with dissolve
    cas "Valeu."
    show cassie 69
    cas "..."
    show player 124 at left
    show cassie 68
    cas "Desculpa por te expulsar da piscina..."
    cas "Eu vou deixar você vir aqui próxima vez, eu prometo."
    show player 122 at left
    show cassie 70
    player_name "Valeu!"
    player_name "Eu vou fazer algumas voltas agora Se você não se importa."
    show player 124 at left
    show cassie 71
    cas "Você está louco?! Vamos sair antes que alguém nos veja!"
    show player 126 at left
    show cassie 70
    player_name "Ok, ok!"
    $ banned_from_pool = False
    hide cassie
    hide player
    with dissolve
    hide pool_water_night
    hide ui
    jump map_dialogue

label rescued_dialogue:
    scene rescued
    show cassie 6 at Position (xpos = 564, ypos = 768) with dissolve
    cas "OK, ESCUTEM TODOS!!!"
    cas "AFASTEM-SE!"
    show cassie 7
    cas "Tenho que fazer um {b}SALVAMENTO{/b}!"
    show cassie 8
    window hide
    pause
    show cassie 8
    cas "Ok, isso via funcionar..."
    show cassie 9
    window hide
    pause
    show cassie 8
    cas "Vamos..."
    show cassie 9
    window hide
    pause
    show cassie 10
    window hide
    pause
    show cassie 11
    window hide
    pause
    show cassie 12 with hpunch
    window hide
    pause
    show cassie 12
    cas "..."
    show cassie 13
    cas "Nada para ver aqui, pessoal!!!"
    cas "Vocês podem voltar para a piscina agora..."
    show cassie 15
    player_name "{b}*Tosse*{/b}"
    show cassie 14
    cas "...Tudo bem, você está causando muitos problemas por aqui..."
    cas "Eu estou levando você na minha sala até que você esteja apto para ir."
    hide cassie 1
    hide rescued
    jump medic_dialogue

label medic_dialogue:
    if gloryhole_done == 0:
        $ gloryhole_done = 1
    scene changeroom02
    if medic_dialogue_count == 0:
        show cassie 36 with dissolve
        cas "Como você está se sentindo?"
        show cassie 38
        player_name "{b}*Tosse*{/b}"
        show cassie 37
        player_name "Acho que estou bem..."
        show cassie 36
        cas "Estou feliz que você esteja vivo..."
        show cassie 41
        cas "...Você não sabe como nadar??!"
        show cassie 38
        player_name "{b}*Tosse*{/b}, não é assim..."
        show cassie 37
        player_name "...Eu, {b}*tosse*{/b}, estou treinando..."
        player_name "...E fiquei sem forças."
        show cassie 41
        cas "Olha, é ótimo que você esteja treinando, mas você tem que começar com calma."
        cas "Não me importo que você fique na piscina e continue treinando, mas..."
        cas "...Não posso deixá-lo andar assim..."
        show cassie 38
        player_name "Eu, {b}*tosse*{/b}, sinto muito por isso."
        show cassie 39
        player_name "Quando senti você me tocando, seus lábios... Eu..."
        player_name "...Eu não sei por que isso fica acontecendo..."
        show cassie 40
        cas "Haha!"
        cas "Hmmm... Bom..."
        show cassie 41
        cas "Você já... sabe, com uma mulher?"
        show cassie 44
        player_name "Sim... Claro! Tipo, várias vezes..."
        show cassie 41
        cas "...Sério?"
        show cassie 39
        player_name "{b}*suspiro*{/b}"
        player_name "Eu quase namorei uma menina uma vez..."
        show cassie 40
        cas "Haha!"
        cas "Só isso??"
        show cassie 39
        player_name "Sim! ...nós tocamos nossas mãos e essas coisas..."
        player_name "...Mas então, {b}isso{/b} aconteceu... Ela gritou e..."
        player_name "Que seja, faz muito tempo."
        show cassie 41
        cas "Wow... então você é virgem?"
        show cassie 39
        player_name "Eu, eu acho que sim?"
        show cassie 40
        cas "Que fofo."
        show cassie 45
        player_name "..."
        show cassie 46
        cas "Você se importa se eu der uma olhada neste problema que temos aqui??"
        player_name "Uhh... Pode ir."
        show cassie 42 with hpunch
        window hide
        pause
        show cassie 43 with hpunch
        window hide
        pause
        show cassie 42 with hpunch
        window hide
        pause
        show cassie 46
        cas "Certo, eu sei como consertar isso."
        cas "Escuta..."
        show cassie 47 at Position (xpos=447)
        cas "Tudo o que você tem a fazer, é colocar seu pau naquele buraco na parede."
        cas "Vai se sentir algo quente do outro lado..."
        show cassie 49
        cas "...E então, você vai se sentir {b}muito{/b} melhor depois disso. Confie em mim..."
        show cassie 48
        player_name "Você quer dizer... que eu tenho que colocar o meu pênis naquele buraco?!"
        show cassie 49
        cas "Sim! Simples, não?"
        menu:
            "Beleza, vamos lá.":
                show cassie 37 at center
                player_name "Uhmm... Ok, mas você não pode olhar."
                show cassie 46
                cas "Ah, não se preocupe..."
                show cassie 44
                player_name "Por quê? Você vai sair?"
                show cassie 40
                cas "Clara! Já volto..."
                hide cassie 1 with dissolve
                hide changeroom02
                $ pool_count = 1
                $ medic_dialogue_count = 1
                jump gloryhole_medic
            "Acho que é melhor não.":

                show cassie 39 at center
                player_name "Não sei... Não me sinto confortável com isso."
                show cassie 41
                cas "..."
                show cassie 41
                cas "É por isso que você nunca ficou com uma garota..."
                show cassie 44
                player_name "Vou esperar um pouco até que vá embora..."
                player_name "Obrigado por ter me salvo..."
                show cassie 41
                cas "...Claro, sem problemas..."
                hide cassie 41 with dissolve
                hide changeroom02
                $ medic_dialogue_count = 2
                jump pool_dialogue

    if medic_dialogue_count == 1:
        show player 49 at right with dissolve
        show cassie 58 at left with dissolve
        player_name "Woah... Isso foi..."
        show cassie 50 at left
        show player 53 at right
        cas "...Incrível, né?"
        show player 52 at right
        show cassie 53 at left
        player_name "Sim..."
        show cassie 52 at left
        show player 51 at right
        cas "Escute, esta sala de médicos não é aberta ao público, ok?"
        cas "Então eu não posso deixar qualquer um entrar aqui toda hora..."
        show cassie 54 at left
        cas "...mas para você, vou abrir uma exceção."
        show cassie 53 at left
        show player 52 at right
        player_name "Sério?"
        show cassie 52 at left
        show player 51 at right
        cas "Só não conte pra ninguém, ok?"
        show cassie 53 at left
        show player 50 at right
        player_name "...claro, {b}Cassie{/b}!"
        show cassie 55 at left
        show player 52 at right
        cas "Certo, até a próxima... grandão!"
        hide player 52 at right with dissolve
        hide cassie 55 at left with dissolve

        show unlock19 at truecenter
        $ renpy.pause()
        hide unlock19 with dissolve

        $ medic_dialogue_count = 2
        hide changeroom02
        jump pool_dialogue

    if medic_dialogue_count == 2:
        if wearing_swimsuit:
            show player 51 at right
        else:
            show player 1f at right with dissolve
        show cassie 52 at left with dissolve
        cas "Eu pensei ter visto você entrar aqui..."
        show cassie 53 at left
        if wearing_swimsuit:
            show player 49 at right
        else:
            show player 14f at right
        player_name "Oi, {b}Cassie{/b}!"
        show cassie 52 at left
        if wearing_swimsuit:
            show player 51 at right
        else:
            show player 1f at right with dissolve
        cas "Deixa eu adivinhar..."
        cas "Você está tendo problemas aí em baixo de novo, não é, grandão?"
        show cassie 54 at left
        cas "Você precisa de um... alívio?"
        if wearing_swimsuit:
            show player 51 at right
        else:
            show player 29f at right
        show cassie 53 at left
        player_name "Bem..."
        menu:
            "Eu adoraria.":
                if wearing_swimsuit:
                    show player 52 at right
                else:
                    show player 21f at right
                show cassie 53 at left
                player_name "Sim, preciso..."
                show cassie 52 at left
                if wearing_swimsuit:
                    show player 53 at right
                else:
                    show player 13f at right
                cas "Foi o que eu pensei..."
                show cassie 53 at left
                if wearing_swimsuit:
                    show player 52 at right
                else:
                    show player 21f at right
                player_name "Você acha que posso fazer isso novamente? E... colocar no buraco?"
                show cassie 55 at left
                if wearing_swimsuit:
                    show player 53 at right
                else:
                    show player 13f at right
                cas "Claro! Apenas ponha lá que eu volto em um minuto..."
                hide player
                hide cassie 55 at left
                with dissolve
                hide changeroom02
                $ medic_dialogue_count = 3
                jump gloryhole_medic
            "Só me trocando.":

                if wearing_swimsuit:
                    show player 50 at right
                else:
                    show player 17f at right
                show cassie 53 at left
                player_name "Na verdade, eu só estava me trocando..."
                show cassie 57 at left
                if wearing_swimsuit:
                    show player 51 at right
                else:
                    show player 11f at right
                cas "..."
                show cassie 56 at left
                cas "Certo, que pena..."
                show cassie 57 at left
                if wearing_swimsuit:
                    show player 52 at right
                else:
                    show player 10f at right
                player_name "Desculpa..."
                player_name "Eu adoraria passar um tempo aqui, mas eu tenho que voltar para o meu treinamento!"
                show cassie 55 at left
                if wearing_swimsuit:
                    show player 53 at right
                else:
                    show player 1f at right
                cas "...Está bem. Volta para lá, então."
                hide cassie 55 at left with dissolve
                show player 8f at right with dissolve
                window hide
                pause
                hide player 8f at right
                if wearing_swimsuit:
                    show player 33f at right
                    $ wearing_swimsuit = False
                    $ changing_count = 0
                else:
                    show player 44f at right
                    $ wearing_swimsuit = True
                player_name "Aqui estamos! Tudo pronto!"
                $ used_changing_girls = []
                hide player 44 at right with dissolve
                hide changeroom02
                jump pool_dialogue
    else:

        show player 17f at right with dissolve
        show cassie 50 at left with dissolve
        player_name "Isso foi... Incrível..."
        show player 13f at right
        show cassie 51 at left
        cas "Fico feliz que você esteja melhor..."
        show player 14f at right
        show cassie 53 at left
        player_name "Muito obrigado..."
        show cassie 54 at left
        show player 1f at right
        cas "Mantenha isso só entre nós, ok?"
        show cassie 53 at left
        show player 18f at right
        player_name "Sim, claro!"
        show cassie 55 at left
        show player 1f at right
        cas "Certo... Te vejo na próxima."
        $ medic_dialogue_count = 2
        hide player 1f at right with dissolve
        hide cassie 55 at left with dissolve
        hide changeroom02
        jump pool_dialogue

label gloryhole_medic:
    $ gTimer.tick()
    scene changeroom03
    show cassie 16 at Position(xpos = 431, ypos = 768)
    with fade
    window hide
    pause
    show cassie 17
    window hide
    pause
    show cassie 18 with hpunch
    window hide
    pause
    cas "!!!"
    show cassie 19
    cas "Oh wow..."
    cas "( Eu adoro esse pinto... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    cas "( É tão grande... )"
    show cassie 21 at Position (xpos = 440, ypos = 768)
    cas "( ...e duro... )"
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 21 at Position (xpos = 440, ypos = 768)
    window hide
    pause
    show cassie 20 at Position (xpos = 437, ypos = 768)
    window hide
    pause
    show cassie 22 at Position (xpos = 434, ypos = 768) with hpunch
    window hide
    pause
    show cassie 23 at Position (xpos = 430, ypos = 768)
    cas "( Acabou de se contorcer! )"
    show cassie 24 at Position (xpos = 431, ypos = 768)
    cas "( Vamos ver... o que eu deveria fazer com isso? )"
    hide cassie 24
    hide changeroom03
    call screen gloryhole_stage01

label gloryhole_medic_bj:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_27 at Position (xpos = 444, ypos = 768)
    pause 4
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    hide cassie 26_28
    hide changeroom03
    call screen gloryhole_stage02

label gloryhole_medic_bjfacefinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 29 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 30 with hpunch
    pause .3
    show cassie 31
    pause .5
    show cassie 31
    cas "Wow... tanta porra..."
    hide cassie 31
    hide changeroom03
    jump medic_dialogue

label gloryhole_medic_bjtitsfinal:
    scene changeroom03
    show cassie 24 at Position (xpos = 431, ypos = 768)
    pause .5
    show cassie 26_28 at Position (xpos = 444, ypos = 768)
    pause 5
    show cassie 32 at Position (xpos = 427, ypos = 768)
    pause .5
    show cassie 33 with hpunch
    pause .3
    show cassie 34
    pause .5
    show cassie 34
    cas "Wow... Você gozou bastante..."
    hide cassie 34
    hide changeroom03
    jump medic_dialogue

label gloryhole_medic_fuck_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( Eu não conheço muito ele para fazer isso... )"
    hide cassie 35
    hide changeroom03
    call screen gloryhole_stage01

label gloryhole_medic_fuckraw_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( Isso é loucura!!! Não posso fazer isso... )"
    hide cassie 35
    hide changeroom03
    call screen gloryhole_stage01

label gloryhole_medic_swallow_fail:
    scene changeroom03
    show cassie 35 at Position (xpos = 431, ypos = 768)
    cas "( Não conheço muito ele para fazer isso... )"
    hide cassie 35
    hide changeroom03
    call screen gloryhole_stage02

label locked_door26_dialogue:
    scene pool
    show player 35 with dissolve
    player_name "( Eu deveria comprar uma {b}roupa de mergulho{/b} antes de me trocar... )"
    player_name "( ...Deve ter algo no {b}shopping{/b}. )"
    hide player 35
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
