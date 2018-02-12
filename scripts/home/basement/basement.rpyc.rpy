label home_basement_dialogue:
    $ location_count = "Basement"
    if M_mom.get_state() == S_mom_wash_clothes:
        scene home_basement_sideview
        show player 324 at Position(xpos=860)
        show mom 136 at Position(xpos=550,ypos=805)
        mom "Oh meu Deus!!"
        show mom 137
        mom "{b}*risadas*{/b}"
        show player 325
        show mom 135
        player_name "O que é isso, {b}[mom_name]{/b}?"
        show player 326
        show mom 136
        mom "Suas roupas! Estão muito sujas!"
        show player 324
        show mom 137
        mom "Posso ver alguém estar trabalhando muito lá fora!"
        show player 325
        show mom 135
        player_name "Desculpa, eu deveria ter usado outra coisa..."
        show player 324
        show mom 136
        mom "Está tudo bem, querido! Vamos limpar tudo.."
        mom "Apenas me dê sua camisa e sua bermuda, para que eu possa colocar para lavar."
        show player 325
        show mom 135
        player_name "Está tudo bem, {b}[mom_name]{/b}. Posso fazer isso sozinho."
        show player 324
        show mom 136
        mom "Oh vamos lá! Eu estava prestes a ligar a máquina de lavar."
        show mom 135
        show player 327 at Position(xoffset=-27) with fastdissolve
        pause
        scene home_basement_cutscene with fade
        show text "Essa foi a primeira vez que eu estava me despindo na frente da {b}[mom_name]{/b}. \nEu estava um pouco tímido, mas ela estava tranquila sobre isso. \nEla se inclinou para colocar na máquina... se mostrando pra mim.\nEu queria desviar o olhar, mas não conseguia... Fiquei excitado por isso." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text
        scene home_basement_sideview
        show player 330 at Position(xpos=860)
        show mom 142 at Position(xpos=550,ypos=805)
        with fade
        mom "( Ele provavelmente vai usar essa cueca fedida o dia todo. )"
        mom "( Devo limpar agora antes de deixar no quarto dele... )"
        show mom 136
        mom "Querido..."
        show player 332
        mom "Você... quer que eu lave todas suas roupas?"
        show mom 135
        player_name "!!!"
        show player 331
        player_name "Ah, não, tá tudo bem, {b}[mom_name]{/b}..."
        show mom 136
        show player 330
        mom "Você estava suando o dia todo... Você deveria tirar e ir tomar banho!"
        show mom 135
        show player 333
        player_name "Mãeee-"
        show mom 136
        show player 330
        mom "Ah, por favor! Não é a primeira vez que eu te vejo pelado, querido!"
        mom "Você se sentirá melhor depois de ter tudo limpo."
        show mom 138
        show player 334 with fastdissolve
        pause
        show player 335 with fastdissolve
        pause
        show player 336 with fastdissolve
        pause 0.1
        show mom 139
        show player 337 at Position(xpos=855) with vpunch
        pause
        show mom 140
        show player 338 at Position(xpos=853)
        mom "Ooops!!"
        mom "Oh meu..."
        mom "Querido, aqui... vamos... Umm..."
        mom "Tenho umas toalhas para cobrir..."
        show mom 141 with fastdissolve
        pause
        show player 339 at Position(xpos=845)
        show mom 142
        with fastdissolve
        pause
        show player 341
        player_name "Desculpa, {b}[mom_name]{/b}!"
        show player 340
        show mom 143
        mom "Ah, tudo bem, querido."
        mom "Essas cosias acontecem."
        show mom 140
        mom "É normal!"
        show mom 142
        mom "Hmm..."
        show mom 143
        mom "Essa toalha é um pouco pequena, mas acho que servirá..."
        mom "Apenas apresse-se para o banho e certifique-se de se limpar-"
        mom "Se limpar sozinho!"
        show mom 142
        show player 341
        player_name "Ok..."
        hide player with dissolve

        show mom 139
        mom "( Oh meu...)"
        mom "( ...Eu não tinha idéia de que ele tinha tantos... hormônios. )"
        scene black with fade
        $ M_mom.trigger(T_mom_clean_clothes)
        $ gTimer.tick()
        $ location_count = "Bedroom"
        $ unlock_ui()

    elif M_mom.get_state() == S_mom_close_valve:
        scene home_basement
        show player 34 with dissolve
        player_name "( A válvula de água deve estar ao lado do aquecedor de água. )"
        player_name "( É melhor desligá-lo antes que inunde o andar de cima. )"
        hide player with dissolve

    elif M_mom.get_state() == S_mom_lotion_adventure and M_mom.is_set("retrieved lotion"):
        jump mom_lotion_fun

    elif M_mom.get_state() == S_mom_give_laundry:
        scene home_basement_c
        show mom 125 at right
        show player 277 at left
        with dissolve
        player_name "Eae, {b}[mom_name]{/b}!"
        show player 276
        player_name "Aqui está a roupa que você pediu."
        show player 13
        show mom 121
        with dissolve
        pause
        show mom 123
        mom "Obrigada, querido."
        mom "Mas isso não é o que eu realmente queria."
        show mom 124
        show player 10
        player_name "Ah é? O que eu esqueci?"
        show player 5
        show mom 123
        mom "Bobinho."
        show mom 63 with dissolve
        mom "Deixei essas anotações esta manhã porque não consegui tirar você da minha mente."
        show mom 61
        show player 11
        player_name "!!!"
        show mom 39
        mom "Eu quero você e esse seu pau."
        show mom 62
        show player 1
        mom "Quero que você me coma."
        show mom 61
        show player 2
        player_name "Cccc-Claro!"
        show player 13
        show mom 62
        mom "Tire suas roupas."
        show player 11
        show mom 125
        player_name "!!!"
        show player 297
        player_name "Vamos fazer isso aqui?!"
        show player 13
        show mom 62
        mom "{b}[sis]{/b} não vai nos encontrar aqui."
        show player 21
        show mom 125
        player_name "Tá... bom."
        jump basement_mom_sex
    $ callScreen(location_count)


label basement_mom_sex:
    $ M_mom.set('sex speed', .175)
    $ location_count = "Basement"
    $ cum = False
    $ anim_toggle = False
    $ xray = False
    if M_mom.get_state() != S_mom_give_laundry and randomizer() <= 50:
        $ mom_basement_rand = True
    else:
        $ mom_basement_rand = False
    if mom_basement_rand:
        scene home_basement_c
        show mom 62 at right
        show player 13 at left
        with dissolve
        mom "Sente-se na lavadora para a {b}mamãe{/b}."
    scene home_basement_sex_01
    show player 270 zorder 1 at Position(xpos=466,ypos=768)
    show mom 107 zorder 0 at Position(xpos=200)
    with fade
    pause
    show player 271 at Position(xpos=655,ypos=768)
    pause
    if mom_basement_rand:
        player_name "Assim?"
        show mom 108
        mom "Perceiro."
        mom "O seu pau é perfeito."
    else:
        show mom 108
        mom "Minha vez..."
    show mom 109 at Position(xpos=205)
    pause
    show mom 110
    pause
    show mom 111 at Position(xpos=207)
    pause
    show mom 112 at Position(xpos=196)
    pause
    show mom 113 at Position(xpos=203)
    pause
    show mom 114
    pause
    show mom 115
    if mom_basement_rand:
        mom "Agora sente-se e deixe a {b}[mom_name]{/b} ajudá-lo com isso."
    else:
        mom "Gosta do que vê?"
        show mom 114
        player_name "Você é linda, {b}[mom_name]{/b}."
        show mom 115
        mom "Sente-se e relaxe, querido."
        mom "Vamos começar devagar..."
    hide player
    hide mom
    show moms 124 at Position(xpos=650)
    with dissolve
    pause
    show moms 125 at Position(xpos=655) with dissolve
    pause
    show moms 126f with dissolve
    mom "Oh!"
    show moms 126e
    pause
    show moms 126d
    pause
    show moms 126c
    pause
    show moms 126b
    pause
    show moms 126
    if mom_basement_rand:
        mom "Mmmm..."
        mom "Mal consigo colocar tudo."
    else:
        mom "Ahh..."
        player_name "!!!"
        player_name "Você é tão quente..."
    label basement_mom_sex_loop:
        hide screen basement_mom_sex_options
        show screen sex_anim_buttons
        pause
        if anim_toggle == True:
            $ animcounter = 0
            while animcounter < 4:
                hide screen sex_anim_buttons
                show moms 126_126b_126c_126d_126e_126f_126g_126h_126i_126j at Position(xpos=655)
                pause 4
                if mom_basement_rand:
                    if animcounter == 1:
                        mom "Oh, querido!{p=1}{nw}"
                        mom "Siiiim!{p=1}{nw}"
                    if animcounter == 2:
                        mom "Ahh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh!{p=1}{nw}"
                else:
                    if animcounter == 1:
                        mom "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh, querido!!!{p=1}{nw}"
                        player_name "Uhhh...{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:
            $ animcounter = 0
            while animcounter < 4:
                hide screen sex_anim_buttons
                show moms 126
                pause
                show moms 126b
                pause
                show moms 126c
                pause
                show moms 126d
                pause
                show moms 126e
                pause
                show moms 126f
                pause
                show moms 126g
                pause
                show moms 126h
                pause
                show moms 126i
                pause
                show moms 126j
                pause
                if mom_basement_rand:
                    if animcounter == 1:
                        mom "Oh, querido!{p=1}{nw}"
                        mom "Siiim{p=1}{nw}"
                    if animcounter == 2:
                        mom "Ahh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh!{p=1}{nw}"
                else:
                    if animcounter == 1:
                        mom "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 3:
                        mom "Oh, querido!!!{p=1}{nw}"
                        player_name "Uhhh...{p=1}{nw}"
                $ animcounter += 1
        show screen basement_mom_sex_options
        pause
        jump basement_mom_sex_loop

label basement_mom_sex_cum:
    hide screen basement_mom_sex_options
    player_name "{b}[mom_name]{/b}!"
    show white
    show moms 129 at Position(xpos=609) with vpunch
    hide white with dissolve
    if mom_basement_rand:
        mom "Oh, querido!"
        mom "Estou gozando!"
        show moms 129 with flash
        mom "AHH!!!"
    else:
        mom "Ahh!!!"
    jump basement_mom_sex_after

label basement_mom_sex_after:
    if M_mom.get_state() == S_mom_give_laundry:
        show moms 132 at Position(xpos=650) with fade
        mom "Obrigado por me trazer a roupa..."
        show moms 131
        player_name "Sem problemas, {b}[mom_name]{/b}."
        show moms 132
        mom "Me conte se você quizer fazer isso novamente aqui embaixo."
        show moms 131
        player_name "Definitivamente."
    elif mom_basement_rand:
        show moms 130 at Position(xpos=650) with fade
        mom "Você pode me avisar quando estiver quase..."
        show moms 131
        player_name "Desculpa, {b}[mom_name]{/b}."
        player_name "Eu não pude segurar..."
        player_name "Foi tão bom..."
        show moms 132
        mom "Tudo bem. Vamos nos limpar..."
    else:
        show moms 132 at Position(xpos=650) with fade
        mom "Foi ótimo, querido."
        mom "Obrigada por me convidar!"
        show moms 131
        player_name "Sem problemas!"
    $ gTimer.tick()
    if M_mom.get_state() == S_mom_give_laundry:
        jump basement_confession_kiss
    $ callScreen(location_count)

label basement_confession_kiss:
    scene home_basement_c
    show player 227 at Position(xpos=200)
    show mom 73 at Position(xpos=650)
    with fade
    mom "Querido..."
    if randomizer() <= M_mom.get('mom concerned'):
        if M_mom.get('mom concerned') > 0:
            $ M_mom.set('mom concerned', M_mom.get('mom concerned') - 20)
        if M_mom.get('mom concerned') < 0:
            $ M_mom.set('mom concerned', 0)
        mom "Quero que me diga se você não quiser mais fazer isso, ok?"
        show player 228
        show mom 76
        player_name "Não, sem problemas, {b}[mom_name]{/b}..."
        player_name "Eu sempre quis fazer isso com vocẽ."
        show player 227
        show mom 77
        mom "Sério?"
        show player 228
        player_name "Sim, é tudo o que penso em fazer quando te vejo..."
        show player 227
        show mom 75
        mom "Você é sempre tão fofo..."
    mom "Me beije."
    hide player
    show mom 80 at Position(xpos=500)
    with dissolve
    pause
    show mom 79 with dissolve
    pause
    show mom 80 with dissolve
    pause
    show player 228 at Position(xpos=200)
    show mom 78 at Position(xpos=650)
    with dissolve
    player_name "Te amo, {b}[mom_name]{/b}!"
    show player 227
    show mom 75
    mom "Também te amo, querido..."
    scene home_basement
    hide mom
    hide player
    with fade
    $ M_mom.trigger(T_mom_basement_fun)
    $ unlock_ui()
    $ callScreen(location_count)

label broken_pipe:
    scene expression gTimer.image("home_basement")
    show popup_pipe_fixed at truecenter with dissolve
    pause
    hide popup_pipe_fixed with dissolve
    scene home_basement_c
    show player 2
    with dissolve
    player_name "Certo, a válvula está fechada."
    player_name "Eu deveria voltar ao {b}banheiro{/b} para ver se consigo consertar a {b}pia{/b}."
    hide player
    with dissolve
    $ M_mom.trigger(T_mom_closed_valve)
    $ callScreen(location_count)

label laundry_dialogue:
    scene home_basement_c
    show mom 123 at right
    show player 1 at left
    with dissolve
    mom "Oh! Olá, querido!"
    mom "Precisa de algo?"
    show mom 124
    menu:
        "Me deixe ajudar.":
            show mom 124
            show player 14
            player_name "{b}[mom_name]{/b}, me de o cesto. Eu lavo a roupa."
            show mom 123
            show player 5
            mom "Está tudo bem, eu faço isso."
            show mom 122
            show player 10
            player_name "Você merece descansar. Você trabalhou muito ao redor da casa."
            player_name "Por favor, deixa..."
            show mom 123
            show player 11
            mom "Tão teimoso..."
            show player 1
            mom "Ok, querido."
            show player 275
            show mom 62
            mom "certifique-se se não misturar as roupas brancas com as coloridas."
            show mom 125
            show player 276
            player_name "Pode deixar, {b}[mom_name]{/b}."
            show mom 63
            show player 275
            mom "Querido..."
            mom "Obrigado por me ajudar ultimamente."
            mom "Está deixando minha vida muito mais fácil..."
            show mom 125
            show player 277
            player_name "No problem!"
            scene help_mom_basement_cutscene with fade
            show text "Recentemente, eu estava ajudando bastante a {b}[mom_name]{/b} na casa. \nEu poderia dizer que ela gostava também, sempre andando por aí e me perguntando como as coisas iam com as meninas na escola... \nSinto que ela tem sido bem próxima a mim ultimamente... \nO jeito que ela me olha, me toca, e fica me encarando toda hora." at Position (xpos= 512, ypos = 700) with dissolve
            pause
            hide text with dissolve
            scene home_basement_c with fade
            show mom 2 at right
            show player 13 at left
            with dissolve
            mom "Agradeço por toda ajuda que você tem me dado."
            mom "Eu aprecio muito."
            show mom 1
            show player 14
            player_name "De nada, {b}[mom_name]{/b}."
            show player 13
            show mom 13
            mom "Ah, antes de você ir!"
            mom "Poderia ir lá em cima e me trazer a {b}loção{/b}, por favor?"
            mom "Estou sentindo minhas pernas um pouco seca."
            show mom 1
            show player 12
            player_name "Onde lá em cima?"
            show player 5
            show mom 13
            mom "Olhe nas {b}gavetas do meu quarto{/b}."
            mom "Deve estar lá."
            show mom 1
            show player 14
            player_name "Ok, já volto!"
            hide player
            hide mom
            with dissolve
            show popup_mombedroom at truecenter with dissolve
            pause
            hide popup_mombedroom with dissolve
            $ M_mom.trigger(T_mom_cleaned_laundry)
            $ lock_ui()
        "Você está ocupada.":

            show player 14
            player_name "Parece que você está ocupada."
            player_name "Volto mais tarde."
    $ M_mom.set("chores", False)
    $ callScreen(location_count)

label mom_lotion_fun:
    if M_mom.is_set("lotion fun"):
        if location_count == "Basement":
            scene home_basement_c
        elif location_count == "Kitchen":
            scene homekitchen_closeup
            if M_mom.is_set("sex available"):
                show mom 1 at right
                show player 485 at left
                with dissolve
                player_name "Aqui, {b}[mom_name]{/b}!"
                show player 484
                show mom 2
                mom "Obrigada, querido."
                mom "Deixe-me apenas sentar no balcão, então você não precisa se curvar."
                show mom 183 with dissolve
                pause
                show mom 184 zorder 2
                show mom_robe 184f zorder 2
                with dissolve
                pause
                show mom 185
                show mom_robe 185j
                with dissolve
                pause
                hide player
                show player 487c zorder 1
                show player_arms 488 zorder 3
                with dissolve
                pause
                show player_arms 488b
                with dissolve
                pause
                show player_arms 488c_488d with dissolve
                show player 487g
                show mom 185b
                mom "Ai, isso faz cócegas!"
                show mom 185g
                mom "Você gosta de cuidar da mamãe, não gosta?"
                show mom 185f
                show player 487f
                player_name "Sempre!"
                show player 487g
                show player_arms 488c_488d_488e with dissolve
                pause
                show mom 185b
                mom "Tenho que confessar, você tem sido um ótimo garoto..."
                mom "...Mas eu sei por que você gosta disso."
                show mom 185f
                show player 487
                player_name "..."
                show mom 185g
                mom "Você gosta do pequeno show que lhe dou..."
                show mom 185f
                show player 487g
                player_name "!!!"
                show mom 185g
                mom "Sua massagem me excita tanto."
                show mom 185b
                show player 487d
                mom "Continue me massageando e talvez você me ajude com outra coisa..."
                show mom 185f
                show player 487f
                player_name "Sim, senhora!"
                show player 487g
                show mom_robe 185k
                show player_arms 488e_488f
                with dissolve
                pause
                show mom 185b
                mom "Isso é realmente bom."
                hide player_arms
                show player 13 at Position (xoffset=-118)
                hide mom_robe
                show mom 189
                with dissolve
                mom "Parece que até minhas roupas querem sair."
                show mom 188
                show player 26 at Position (xoffset=-118)
                player_name "E quando foi que sua calcinha saiu?"
                show player 13 at Position (xoffset=-118)
                show mom 189
                mom "{b}*risada*{/b}"
                show mom 187
                mom "Achei que você não ia perceber."
                show mom 189
                mom "Bem, então, você está pronto para fazer outra coisa?"
                show mom 188
                show player 14 at Position (xoffset=-118)
                player_name "Claro!"
                show player 110f at Position (xoffset=-118)
                show mom 191
                show mom_robe 191b zorder 2
                with dissolve
                mom "Então seja um bom garoto e me faça gozar com seus dedos..."
                show mom 190
                show player 26 at Position (xoffset=-119)
                player_name "Sim, {b}[mom_name]{/b}."
                show player finger 193b zorder 3
                show mom 192
                show mom_robe 194b
                with dissolve
                $ inventory.items.remove(lotion)
                $ M_mom.set("fetch lotion", False)
                $ M_mom.set("retrieved lotion", False)
                $ unlock_ui()
                pause
                $ M_mom.set("sex speed", .225)
                $ M_mom.set("sex flip", False)
                $ M_mom.set("robe on", True)
                $ first_pass = True
                jump mom_finger_loop
        show mom 1 at right
        show player 485 at left
        with dissolve
        player_name "Achei!"
        show player 484
        show mom 2
        mom "Ótimo! Espere um segundo."
        show player 486
        show mom 183 with dissolve
        pause
        show mom 184b zorder 2
        show mom_robe 184e zorder 2
        with dissolve
        mom "Pronto!"
        show player 484
        show mom 185
        show mom_robe 185h
        with dissolve
        pause
        hide player
        show player 487c zorder 1
        show player_arms 488 zorder 3
        with dissolve
        pause
        show player_arms 488b
        with dissolve
        show mom 185d
        mom "Oh! Isso é gelado."
        show player 487d
        mom "Passe a loção na sua mão antes de passar em mim."
        show player 487c
        show mom 185
        show player_arms 488c_488d with dissolve
        show mom 185b
        mom "Isso é bom."
        show mom 185
        show player 487f
        show player_arms 488b with dissolve
        player_name "Bom!"
        show player 487g
        show player_arms 488c_488d with dissolve
        pause
        show player 487f
        show player_arms 488 with dissolve
        player_name "Algo mais?"
        show player 487g
        show mom 185c
        mom "Hmm?"
        show player 487e
        player_name "Você quer que eu aplique a loção em outro lugar?"
        show player 487d
        show mom 185d
        mom "Oh..."
        show mom 185g
        mom "Umm... Se você não se importa, você pode passar um pouco mais pra cima..."
        show mom 185f
        show player 487e
        player_name "O... Ok..."
        show player_arms 488b with dissolve
        show player 487c
        pause
        show player_arms 488c_488d_488e with dissolve
        show mom 185d
        mom "Mmm... Leve suas mãos mais para o fundo."
        show player_arms 488e with dissolve
        mom "Sentiu o nó?"
        mom "Tente esfregar isso..."
        show mom 185c
        show player 487b
        player_name "O... Ok..."
        show player 487c
        show player_arms 488e_488f with dissolve
        pause
        show mom 185b
        mom "Mmm... Isso é bom."
        show mom 185
        show player 487f
        player_name "!!!"
        show player 487g
        player_name "( Ela está ficando bem ralaxaa! )"
        player_name "( Me pergunto se ela sabe que eu consigo ver além da calcinha dela! )"
        show mom 185d
        mom "Oh, seus dedos são tão bons."
        mom "Vocẽ andou praticando?"
        show mom 185g
        mom "Alguma garota amará a atenção e ajuda que você dá."
        show mom 185d
        mom "Oh! Bem aí..."
        show mom 185f
        pause
        show mom_robe 185i with dissolve
        pause
        show mom 185e
        mom "!!!"
        hide player_arms
        show player 3 at Position (xpos=420)
        show xtra 21 zorder 2 at Position (xpos=289)
        hide mom_robe
        show mom 187
        with dissolve
        mom "...Um... Obrigada, Sweetie..."
        show mom 186
        show player 29
        player_name "...De nada..."
        show player 3
        show mom 187
        mom "Bom, eu devia... um..."
        if location_count == "Basement":
            mom "Eu deveria terminar de... de lavar as roupas..."
            mom "Vá lá pra cima e... um..."
        elif location_count == "Kitchen":
            mom "Eu deveria terminar de lavar a louça..."
        show mom 186
        show player 29
        player_name "Sim... Está quase pronto."
        show player 3
        show mom 187
        mom "Obrigada... de novo, querido."
        show mom 186
        show player 29
        player_name "De nada."

        if location_count == "Basement":
            $ location_count = "Living Room"
            scene home_livingroom_b with fade
        elif location_count == "Kitchen":
            $ location_count = "Entrance"
            scene home_entrance with fade
        show player 24 with dissolve
        player_name "Caralho..."
        player_name "Acho que ela percebeu que eu estava olhando..."
        show player 34
        pause
        show player 35
        player_name "Ela estava ficando molhada?"
        show player 43
        pause
        show player 81 with dissolve
        pause
        show player 83
        player_name "Melhor eu achar algo pra fazer."
    else:

        scene home_basement_c
        show mom 1 at right
        show player 485 at left
        with dissolve
        player_name "Aqui, {b}[mom_name]{/b}!"
        show player 484
        show mom 2
        mom "Obrigada, querido."
        show mom 8b
        mom "Ow!"
        show player 486
        pause
        show mom 11b
        mom "Minhas costas estão me matando."
        mom "É ruim ficar velha..."
        show mom 10b
        menu:
            "Ajudar.":
                show player 485
                player_name "Quer ajdua?"
                show player 484
                show mom 13
                mom "Oh?"
                mom "Você diz... com a loção?"
                show mom 10b
                show player 485
                player_name "Bom, sim... Se você quiser."
                show player 484
                show mom 11b
                mom "Você faria isso pra sua velha mãe?"
                show mom 10b
                show player 485
                player_name "Você não é velha {b}[mom_name]{/b}."
                player_name "Mas percebi que você está com dor."
                player_name "Por que você não se senta e descansa!"
                show player 484
                show mom 14
                mom "..."
                show mom 2
                mom "É uma oferta... bem tentadora."
                mom "Obrigada, Sweetie."
                mom "Um segundo."
                mom "Só deixa eu sentar aqui..."
                show player 486
                show mom 183 with dissolve
                pause
                show mom 184 zorder 2
                show mom_robe 184e zorder 2
                with dissolve
                show player 485
                player_name "Onde você quer a loção?"
                show player 484
                show mom 184b
                mom "Ponha um pouco no meu joelho."
                show mom 184
                show player 485
                player_name "Ok."
                show player 484
                show mom 185
                show mom_robe 185h
                with dissolve
                pause
                hide player
                show player 487c zorder 1
                show player_arms 488 zorder 3
                with dissolve
                pause
                show player_arms 488b
                with dissolve
                player_name "!!!"
                show mom 185c
                show player 487b
                player_name "Oops!"
                show player 487d
                show mom 185b
                mom "Oh, Sweetie..."
                show mom 185d
                mom "Foi muito creme."
                show mom 185
                show player 487b
                player_name "Desculpa, {b}[mom_name]{/b}."
                show player 487c
                show player_arms 488c_488d with dissolve
                show player 487
                show mom 185d
                mom "É bom."
                show mom 185
                show player 487c
                show player_arms 488b with dissolve
                player_name "..."
                show player_arms 488c_488d with dissolve
                pause
                show player_arms 488 with dissolve
                show player 487e
                player_name "Passei a maioria da loção."
                player_name "O oque você quer que eu faça com o resto?"
                show player 487d
                show mom 185b
                mom "Acho que você pode passar um pouco mais acima da minha perna."
                show mom 185
                show player 487b
                player_name "Certo..."
                show player 487c
                show player_arms 488b with dissolve
                pause
                show player_arms 488c_488d_488e with dissolve
                pause
                show mom 185d
                mom "Mmm... Sua mãe está bem fundo."
                show player_arms 488e with dissolve
                mom "Sentiu esse nó?"
                mom "Tente passar aí..."
                show mom 185c
                show player 487b
                player_name "O... Ok..."
                show player 487c
                show player_arms 488e_488f with dissolve
                pause
                show mom 185b
                mom "Mmm... Isso é gostoso."
                show mom 185
                show player 487f
                player_name "!!!"
                show player 487g
                player_name "( Ela está bem relaxada agora! )"
                player_name "( Me pergunto se ela sabe que estou vendo atraves da sua calcinha! )"
                show mom 185d
                mom "Oh, seus dedos são ótimo."
                mom "Você andou praticando?"
                show mom 185g
                mom "Alguma garota vai adorar sua ajuda e atenção."
                show mom 185d
                mom "Oh! Bem aí..."
                show mom 185f
                pause
                show mom_robe 185i with dissolve
                pause
                show mom 185e
                mom "!!!"
                hide player_arms
                show player 3 at Position (xpos=420)
                show xtra 21 zorder 2 at Position (xpos=289)
                hide mom_robe
                show mom 187
                with dissolve
                mom "...Um... Obrigada, Sweetie..."
                show mom 186
                show player 29
                player_name "...De nada..."
                show player 3
                show mom 187
                mom "Olha, eu deveia... um..."
                mom "Eu deveria terminar de... lavar roupa..."
                mom "Vai lá pra cima e... um..."
                show mom 186
                show player 29
                player_name "Sim... Estou pronto."
                show player 3
                show mom 187
                mom "Obrigada... de novo, querido."
                show mom 186
                show player 29
                player_name "De nada."
                scene home_livingroom_b with fade
                $ location_count = "Living Room"
                show player 24 with dissolve
                player_name "Caramba..."
                player_name "Acho que ela percebeu que eu estava olhando..."
                show player 34
                pause
                show player 35
                player_name "Ela ficou molhada?"
                show player 43
                pause
                show player 81 with dissolve
                pause
                show player 83
                player_name "Tenho que arranjar algo pra fazer."
                $ M_mom.set("lotion fun", True)
            "Sair.":

                show player 485
                player_name "Algo a mais, {b}[mom_name]{/b}?"
                show player 484
                show mom 11b
                mom "Não, já está bom."
                mom "Obrigada, querido."
                show mom 10b
                show player 485
                player_name "De nada, {b}[mom_name]{/b}."
        $ M_mom.trigger(T_mom_lotion_applied)
    hide player
    hide mom
    with dissolve
    $ inventory.items.remove(lotion)
    $ M_mom.set("fetch lotion", False)
    $ M_mom.set("retrieved lotion", False)
    $ gTimer.tick()
    $ unlock_ui()
    $ callScreen(location_count)

label basement_mom_faster_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') - 0.05)
    jump basement_mom_sex_loop

label basement_mom_slower_sex:
    $ M_mom.set('sex speed', M_mom.get('sex speed') + 0.05)
    jump basement_mom_sex_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
