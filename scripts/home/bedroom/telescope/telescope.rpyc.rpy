default erik_mom_seen = False
default mia_bear_seen = False

label telescope:
    scene black
    $ M_player.set("telescope active", True)
    $ M_player.set("telescope selection", None)
    show screen telescope
    call screen telescope_fake

label erik_bedroom:
    if sister.started(sis_telescope01):
        scene
        show windowerikday 3a
        player_name "( A mãe do {b}Erik{/b} está ali. )"
        show windowerikday 3b with fastdissolve
        player_name "( Ela deve estar dando uma olhada nele... )"
        show windowerikday 3c with fastdissolve
        player_name "..."
        player_name "( ELes estão se beijando na boca? Isso é estranho... )"
        show windowerikday 3d with fastdissolve
        player_name "( Mas que... )"
        player_name "( Ele agarrou os peitos dela?? )"
        show windowerikday 3l with fastdissolve
        player_name "( Ela está fechando a cortina... )"
        show windowerikday 2 with fastdissolve
        pause
        hide windowerikday
        hide screen telescope
        show telescope_caught 1
        with dissolve

        sis "( Hmm... Me pergunto o que eles vão fazer. )"
        show telescope_caught 3 with dissolve
        pause
        show telescope_caught 5
        sis "( O que você está fazendo? )"
        scene telescope_window
        show player 357 at Position(xpos=456,ypos=758)
        with dissolve
        pause
        show sis 137 at right with fastdissolve
        pause
        show sis 138
        sis "Se divertindo?"
        show sis 137
        show player 358 at Position(xpos=448)
        player_name "!!!" with vpunch
        show player 360 at Position(ypos=768)
        show sis 136 at Position(xpos=952)
        player_name "O que você está fazendo aqui?!"
        show player 361
        show sis 135
        sis "A pergunta certa é, o que você está fazendo aí?"
        sis "Você não tem coisas melhores pra fazer do que espiar os vizinhos?"
        show player 360
        show sis 136
        player_name "Eu... não sei sobre o que você está falando!"
        show player 361
        show sis 135
        sis "Ah, você está olhando os pássaros então?"
        show player 360
        show sis 136
        player_name "Talvez eu esteja!"
        show player 359
        show sis 135
        sis "Hah! Você é patético..."
        hide sis with fastdissolve
        pause
        show player 360
        player_name "Você poderia pelo menos fechar minha porta!"
        $ sis_telescope01.finish()
        jump bedroom_dialogue

    elif gTimer.is_morning():
        if erik_telescope_random == 0:
            scene windowerikmorning01
            if gTimer.is_weekend():
                player_name "( Ele não está no quarto. )"
            else:
                player_name "( Ele já deve ter ido pra escola. )"
        else:

            scene windowerikmorning02
            if gTimer.is_weekend():
                player_name "( Ele deve ter ficado a noite toda jogando... )"
            else:
                player_name "( Ele está jogando? Ele devia estar se preparando pra escola... )"

    elif gTimer.is_afternoon():
        if erik_telescope_random == 0:
            scene windowerikday 1
            player_name "( Ele não está em casa. )"
        elif erik_telescope_random == 1 and erik.over(erik_orcette_2):
            scene windowerikday04a_b
            player_name "( O que o Erik está olhando? )"
            player_name "( Isso parece estranhamente familiar... )"
        elif erik_telescope_random == 2 and erik.over(erik_vr):
            scene windowerikday05a_b
            player_name "Uhh!!" with hpunch
            player_name "( Posso ver por que ele estava tão entusiasmado pra comprar... )"
        else:
            scene windowerikday 2
            player_name "( A cortina está fechada, ele deve estar fazendo aquelas coisas de novo. )"
    else:

        if erik_telescope_random == 0:
            scene windoweriknight01
            player_name "( Ele tá sempre jogando esse jogo... )"
        else:
            scene windoweriknight02
            player_name "( A cortina está fechada. Ele deve estar fazendo aquilo de novo. )"
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label erikmom_bedroom:
    if sister.started(sis_telescope03):
        show windowmomday 3a
        player_name "( Woah! Ela está totalmente pelada!! )"
        show windowmomday 3b with fastdissolve
        player_name "( É uma bola... com um dildo?! )"
        show windowmomday 3c with fastdissolve
        player_name "( Por que ela não fechou a cortina? )"
        show windowmomday 3c-d
        player_name "( Parece que ela queria ser vista... )"
        player_name "( Acho que ela sabe... )"
        player_name "( Ela está me olhando agora. )"
        hide windowmomday
        hide screen telescope
        show telescope_caught 1
        with dissolve

        sis "( Hmm... Eu me pergunto o que ele está fazendo. )"
        show telescope_caught 3 with dissolve
        pause
        show telescope_caught 5
        sis "( No flagra! )"
        scene telescope_window
        show player 357 at Position(xpos=456,ypos=758)
        with dissolve
        pause
        show sis 136 at Position(xpos=725,ypos=0,xanchor=0,yanchor=0) with fastdissolve
        pause
        show sis 135
        sis "Meu Deus, você é um pervertido!!"
        show sis 136
        show player 358 at Position(xpos=448)
        player_name "!!!" with vpunch
        show player 360 at Position(ypos=768)
        player_name "Como você-"
        show player 361
        show sis 135
        sis "Oh, eu sabia que você ia estar aqui."
        sis "Você nunca está satisfeito o bastante com esse telescópio..."
        sis "Vamos ver o que você achou agora."
        show player 360 at Position(ypos=768)
        show sis 136
        player_name "Espera-"
        show player 361
        show sis 138
        sis "Saia."
        show player 361 at left
        show sis 142 at Position(xpos=284,ypos=231)
        with fastdissolve
        sis "Vamos ver..."
        show sis 140 at Position(ypos=229)
        pause
        show windowmomday 3c-d with dissolve
        sis "{b}Sra. Johnson{/b}?!!"
        sis "Caralho..."
        sis "Ela é uma safada, não é?"
        scene telescope_window
        show player 361 at left
        show sis 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
        with dissolve
        pause
        show sis 142 at Position(xpos=284,ypos=231,xanchor=0,yanchor=0)
        sis "Ela sempre faz essas coisas na janela?"
        show sis 140 at Position(xpos=284,ypos=229,xanchor=0,yanchor=0)
        sis "Parece que ela queria ser vista..."
        show player 360
        player_name "...Acho que sim."
        show player 361
        sis "Isso é excitante... O jeito que ela cavalga na bola..."
        show sis 145_146_147_148 at Position(xpos=286,ypos=229,xanchor=0,yanchor=0) with fastdissolve
        pause
        show player 364
        player_name "!!!"
        show player 361
        sis "Adorei o jeito que a bunda dela balança."
        show player 362
        sis "Queria ser eu sentando naquela bola..."
        show sis 144 at Position(ypos=231)
        show player 361
        sis "Qual o problema?"
        sis "Sua {b}irmã{/b} mais velha não pode se divertir?"
        show player 360
        show sis 143
        player_name "Eu não disse isso..."
        show player 361
        show sis 144
        sis "O que você prefere?"
        sis "Assistir a {b}Sra. Johnson{/b}... ou assistir a {b}mim{/b}?"
        show player 360
        show sis 143
        player_name "Não sei..."
        show sis 139 at right with fastdissolve
        show player 361
        sis "Oops!"
        sis "Olha isso..."
        sis "Estou toda {b}molhada{/b}!"
        sis "Eu deveria ficar com ela... Talvez trocar por algo..."
        hide sis with dissolve
        pause
        show player 362
        pause
        $ sis_telescope03.finish()
        $ sister.add_event(sis_shower_cuddle04)
        jump bedroom_dialogue

    elif gTimer.is_morning():
        if erik_mom_seen == False:
            scene windowmommorning01
            player_name "( ...essa é a {b}mão do Erik{/b}?! )"
            scene windowmommorning01b
            player_name "( Ah! Ela está se vestindo... )"
            scene windowmommorning01c
            player_name "( Não!! Só mais um pouquinho! )"
            scene windowmommorning01d
            player_name "( Merda! O show acabou... )"
            $ erik_mom_seen = True
        else:

            scene windowmomday02
            player_name "( A cortina está fechada. Ela não deve estar em casa. )"
    elif gTimer.is_afternoon():
        if erikmom_telescope_random == 0:
            scene windowmomday01
            player_name "( Ela não está em casa. )"
        elif erikmom_telescope_random == 1 and erik.over(erik_thief_2):
            show windowmomday 3a
            player_name "( Woah... ela está totalmente pelada!! )"
            show windowmomday 3b with fastdissolve
            player_name "( Isso é uma bola... com um dildo?! )"
            show windowmomday 3c with fastdissolve
            player_name "( Por que ela não fechou a cortina? )"
            show windowmomday 3c-d
            player_name "( Parece que ela queria ser vista... )"
            player_name "( Acho que ela sabe... )"
            player_name "( Ela está olhando para mim. )"
        else:
            scene windowmomday02
            player_name "( A cortina está fechada. Ela não deve estar em casa. )"
    else:
        if erikmom_telescope_random == 0:
            scene windowmomnight03
            player_name "( ...Ela está treinando yoga? )"
            player_name "( ...Na cama? )"
            scene windowmomnight04
            player_name "..."
            player_name "( A {b}mãe do Erik{/b} é tão em forma... )"
            player_name "( ...ela tem um ótimo corpo... )"

        elif erikmom_telescope_random == 1:
            scene windowmomnight01
            player_name "( Ela não está no quarto dela... )"
        else:
            scene windowmomnight02
            player_name "( Ela deve estar dormindo. )"
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label mia_bedroom:
    if sister.started(sis_telescope02):
        scene
        show windowmiaday 3
        player_name "( Oh... )"
        player_name "( O que a {b}Mia{/b} está fazendo? )"
        player_name "( Espero que ela não seja vista fazendo isso... )"
        hide windowmiaday
        hide screen telescope
        show telescope_caught 1
        with dissolve

        sis "( Hmm... Me pergunto o que ele está fazendo. )"
        show telescope_caught 3 with dissolve
        pause
        show telescope_caught 5
        sis "( De novo?! )"
        scene telescope_window
        show player 357 at Position(xpos=456,ypos=758)
        with dissolve
        pause
        show sis 137 at right with fastdissolve
        pause
        show sis 138
        sis "Você parece gostar disso."
        show sis 137
        show player 358 at Position(xpos=448)
        player_name "!!!" with vpunch
        show player 360 at Position(ypos=768)
        player_name "Você poderia de vir aqui assim?!"
        show sis 138
        show player 361
        sis "Eu só ia pegar um lápis emprestado."
        sis "Não achei que você estaria espiando os vizinho de novo..."
        show player 360
        show sis 137
        player_name "Não estou!"
        show player 361
        show sis 138
        sis "Oh, é?"
        sis "Deixa eu ver então."
        show player 360
        show sis 137
        player_name "O quê?"
        show player 361
        show sis 138
        sis "Saia."
        show player 361 at left
        show sis 142 at Position(xpos=806,ypos=768)
        with fastdissolve
        sis "Vamos ver..."
        show sis 140
        pause
        show windowmiaday 3 with dissolve
        pause
        scene telescope_window
        show player 361 at left
        show sis 140 at Position(xpos=545,ypos=768)
        with dissolve
        sis "... é aquela garota da sua sala?"
        show sis 142
        sis "Você gosta de ver garotas se masturbando?"
        show sis 141
        show player 360
        player_name "Não é isso! Eu..."
        player_name "Isso foi um acidente, eu não sabia que ela estava lá!"
        show sis 142
        show player 361
        sis "Uhum, sei."
        sis "Aposto que você adora ver as coisas que ela faz..."
        sis "Você bate punheta enquanto espia ela?"
        show sis 141
        show player 360
        player_name "Não..."
        show sis 142
        show player 361
        sis "Haha! Claro..."
        show sis 138 at right with fastdissolve
        sis "Esqueça o lápis..."
        sis "Vou deixar você terminar o que começou..."
        hide sis with fastdissolve
        show player 359
        pause
        $ sis_telescope02.finish()
        $ sister.add_event(sis_hallway02)
        jump bedroom_dialogue

    elif gTimer.is_morning():
        if mia_telescope_random == 0:
            scene windowmiamorning01
            if gTimer.dayOfWeek() == "Sun":
                player_name "( Ela está se preparando pra igreja. )"
            elif gTimer.is_weekend():
                player_name "( O que ela está fazendo hoje? )"
            else:
                player_name "( Ela está se preparando pra escola. )"
        else:
            scene windowmiamorning02
            player_name "( Muito tarde... Sempre perco a melhor parte! )"

    elif gTimer.is_afternoon():
        if mia_telescope_random == 0:
            scene windowmiaday 1
            player_name "( A cortina está fechada. Ela não deve estar em casa. )"
        else:
            scene windowmiaday 2
            player_name "( Ela não está em casa. )"
    else:
        if mia_telescope_random == 0:
            scene windowmianight01
            player_name "( Ela está sempre lendo ou estudando... )"

        elif mia_telescope_random == 1 and mia_bear_seen == False:
            scene windowmianight03a_b
            player_name "( O que ela está fazendo? )"
            player_name "..."
            player_name "( Ela está... )"
            player_name "( ...Cavalgando no {b}ursinho{/b}? )"
            player_name "( Wow... )"
            player_name "( Isso é excitante- )"
            scene windowmianight03c with hpunch
            player_name "!!!"
            scene windowmianight03d
            player_name "( Ah, merda! )"
            player_name "( Acho que ela foi pega... )"
            player_name "( A {b}mãe{/b} dela deve estar puta... Ela é sempre tão rigorosa com ela... )"
            $ M_mia.set("telescope teddy seen", True)
            $ mia_bear_seen = True
        else:

            scene windowmianight02
            player_name "( Ela deve estar domindo. )"
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label helen_room:
    if gTimer.is_morning():
        scene windowhelenmorning01
        player_name "( A mãe da {b}Mia{/b} está sempre rezando de manhã... )"
    elif gTimer.is_afternoon():
        scene windowhelenday01
        player_name "( Eles não estão em casa... )"
    else:
        if helen_telescope_random == 0:
            scene windowhelennight01
            player_name "( É estranho eles terem camas separadas... )"
            player_name "( ...Nunca vi eles dormirem juntos. )"
        else:
            scene window_helen_night02
            player_name "( Puts. )"
            player_name "( Parece que a {b}Helen{/b} está brava com ele... )"
            player_name "..."
            player_name "( {b}Harold{/b} sempre tão triste... )"
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake

label backyard:
    if gTimer.is_morning():
        scene windowbackyardday01
        player_name "( O tapete de yoga da {b}Sra. Johnson's{/b} está aqui... )"
        player_name "( ...Não tem ninguém aí. )"
    elif gTimer.is_afternoon():
        if backyard_telescope_random == 0:
            scene windowbackyardday01
            player_name "( O tapete de yoga da {b}Sra. Johnson's{/b} está aqui... )"
            player_name "( ...Não tem ninguém aí. )"
        elif backyard_telescope_random == 1:
            scene windowbackyardday02
            player_name "( Cara... )"
            player_name "( A {b}mãe do Erik{/b} é tão... flexível... )"
        elif backyard_telescope_random == 2:
            scene windowbackyardday03
            player_name "( {b}Sra. Johnson{/b} está sempre praticando yoga... )"
            player_name "( Acho que ela gosta de ficar em forma. )"
        else:
            scene windowbackyardday04
            player_name "( Aí sim... )"
            player_name "( Minha posição favorita. )"
            player_name "( Meu pau fica tão duro quando ela faz isso... não sei por que. )"
    else:
        scene windowbackyardnight01
        player_name "( O tapete de yoga da {b}Sra. Johnson's{/b} está aqui. )"
    $ M_player.set("telescope active", True)
    show screen telescope
    call screen telescope_fake
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
