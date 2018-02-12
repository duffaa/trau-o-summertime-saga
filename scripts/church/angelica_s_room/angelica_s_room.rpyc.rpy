label church_angelicas_room_dialogue:
    $ location_count = "Angelica's Room"
    if M_mia.get_state() == S_mia_church_plan and gTimer.is_weekend() and gTimer.is_morning():
        scene church_nun_b
        show player 12 with dissolve
        player_name "( Acho que é aqui. )"
        show player 30
        player_name "( Deve ter algo que eu possa vestir aqui... )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_nun_b
        show player 14f at Position (xoffset=1)
        show players robe f
        with dissolve
        player_name "Foi mais fácil do que eu esp-"
        show player 14f at Position (xpos=182)
        show players robe f at left
        show ang 2 at right
        with fastdissolve
        ang "Aqui está você!"
        show ang 1
        show player 23 at Position (xpos=180)
        show players robe
        with fastdissolve
        player_name "!!!" with hpunch
        show player 10
        player_name "Ah, desculpa!"
        player_name "Eu não quis-"
        show player 11
        show ang 2
        ang "Pare."
        show ang 1
        show player 22
        player_name "..."
        show ang 2
        ang "Eu estive observando você esse tempo todo."
        ang "Roubando a roupa do padre... Se passando por nosso padre no confessionário..."
        ang "...E mentindo para quela pobre mulher."
        show ang 1
        show player 10
        player_name "Não é o que você está pensando!"
        player_name "Eu estava querendo ajudar ela..."
        show player 11
        show ang 2
        ang "Ajudar?"
        ang "A única pessoa que você pode ajudar agora, é você mesmo..."
        ang "...Porque estou pensando em te entregar às autoridades."
        show ang 1
        show player 22
        player_name "!!!"
        show ang 2
        ang "A menos que... você faça algumas coisas para mim."
        show ang 1
        show player 11
        player_name "..."
        show player 12
        player_name "Eu não acho que eu possa ser-"
        show player 11
        show ang 2
        ang "Venha me visitar em uma semana."
        ang "E eu explicarei o que eu preciso..."
        ang "...E não tente se esconder de mim, ou todos saberão o que você fez..."
        ang "...Especialmente com aquela senhora. Aquela que se confessou!"
        show ang 1
        show player 10
        player_name "Por favor, não diga nada a ela... Eu volto. Eu prometo."
        show player 11
        show ang 2
        ang "Bom."
        ang "Agora, devolva o que roubou e sai dos quartos..."
        show ang 1
        hide players robe
        show player 444 at left
        with dissolve
        player_name "..."
        hide player
        hide ang
        with dissolve
        $ gTimer.tick()
        $ M_mia.trigger(T_mia_priest_outfit)

    elif M_mia.get_state() == S_mia_church_night_visit and gTimer.is_dark():
        scene church_nun_n_c
        show ang 1 at right
        show player 10 at left
        with dissolve
        player_name "Olá, {b}Irmã Angelica{/b}..."
        show player 5
        show ang 2
        ang "Sabia que podia contar com você."
        ang "Você valoriza nosso acordo... e segredos."
        ang "Por isso acredito que você me ajudará..."
        show ang 1
        show player 12
        player_name "Então, do que você precisa??"
        show player 5
        show ang 2
        ang "Eu realizo um sacrifício privado à noite... em meu quarto..."
        show player 11
        ang "Seu objetivo é ajudar os membros da nossa igreja a lutar com suas impurezas..."
        ang "...Ajudo a expurgar seus pecados!"
        show ang 1
        show player 10
        player_name "Pecadores?"
        show player 11
        show ang 2
        ang "Isso!"
        ang "Mas, para continuar realizando esse sacrifícios, preciso encontrar pecadores..."
        ang "...Recém-escolhidos de nossos adoradores locais!"
        show ang 1
        show player 10
        player_name "Tá, e o que eu deveria fazer?"
        show player 11
        show ang 2
        ang "Quero que você encontre alguém!"
        show ang 1
        show player 10
        player_name "Você quer que eu encontre alguém?!"
        show player 11
        show ang 2
        ang "Sim, pecadores."
        show ang 1
        show player 37 with dissolve
        player_name "..."
        show player 38 with dissolve
        player_name "Mas, eu não conheço ninguém assim... Eu nem-"
        show player 3 with dissolve
        show ang 2
        ang "Você conhec!"
        show ang 1
        show player 12 with dissolve
        player_name "... Mas, quem?!"
        show player 11
        show ang 2
        ang "A moça do confessionário."
        ang "O nome dela é {b}Helen{/b}."
        ang "Ela sempre foi um servo devoto do nosso {b}Senhor{/b}."
        ang "Ela acredita ser muito fiel e nunca concordará com o meu... ritual."
        ang "Mas ela teve uma vergonha depois de conversar com você no confessionário."
        ang "Você conhece os pecados dela."
        ang "E vocẽ me trará ela."
        ang "Eu realmente gosto de expurgar o pecados dos seguidores fiéis."
        ang "É uma das experiências mais... satisfatórias... da nossa religião."
        show ang 1
        show player 22
        player_name "!!!"
        show player 10
        player_name "Você quer que eu traga {b}Helen{/b} aqui?!"
        show player 11
        show ang 2
        ang "No meu quatro, de noite."
        show ang 1
        show player 12
        player_name "Como posso convencê-la a vir aqui?! Não sei como..."
        show player 11
        show ang 2
        ang "Tenho certeza que você dará um jeito."
        ang "Seus interesses estão em jogo aqui..."
        show ang 1
        show player 24
        player_name "{b}*suspiro*{/b}"
        show player 12
        player_name "Ok, vou tentar... mas como esse ritual funciona?"
        show player 5
        show ang 2
        ang "Você descobriará quando for a hora certa."
        show ang 1
        show player 10
        player_name "Eu... eu tenho que ir. Está ficando tarde."
        show player 5
        show ang 2
        ang "Claro! Mas não se esqueça do nosso acordo."
        hide ang with dissolve
        show player 24
        player_name "..."
        hide player with dissolve
        $ M_mia.trigger(T_angelica_ritual_deal)

    elif M_mia.get_state() == S_mia_church_sacrement and gTimer.is_dark():
        scene church_nun_n_c
        show player 5f at right
        show helen 23 at Position (xpos=575)
        show ang 2f at left
        with dissolve
        ang "Obrigada, {b}[firstname]{/b}, por trazer essa maravilhosa discípula para nós!"
        ang "{b}Helen{/b} vem sendo fiel a nossa igreja há muito tempo..."
        ang "...E ela me contou tudo sobre o casamento ter dado errado."
        show ang 1f
        show helen 24
        helen "Eu... Só quero que isso me ajude a lidar com nossos caminhos pecaminosos..."
        show helen 23
        show ang 2f
        ang "Entendo, {b}Helen{/b}."
        ang "Estou feliz por você querer enfrentar seus demônios."
        ang "Você está disposta a seguir meus comandos, a fim de encontrar a luz?"
        show ang 1f
        show helen 24
        helen "Sim. Estou..."
        show helen 23
        show ang 2f
        ang "Ótimo! Haverá três passo para a sua redenção."
        ang "O primeiro passo exige que você se livre de todos os seus bens materiais..."
        show player 11f
        ang "...Tipo {b}suas roupas{/b}."
        ang "Só então seremos capazes de iniciar o processo de expurgar seus pecados!"
        show ang 1f
        show helen 4 at Position (xoffset=2) with dissolve
        helen "Você quer que eu... Me dispa aqui?!"
        show helen 1 at Position (xoffset=2)
        show ang 2f
        ang "Somos criaturas de {b}Deus{/b}, {b}Helen{/b}... Somos todos iguais!"
        ang "Você não deveria ter vergonha de quem você é..."
        show ang 1f
        show helen 25 with dissolve
        helen "..."
        show helen 23
        show ang 2f
        ang "Vai, {b}Helen{/b}. Tire tudo..."
        show ang 1f
        show helen 27
        pause
        show helen 28
        helen "Se isso for necessário, então farei..."
        show player 106f
        show helen 21 with dissolve
        pause
        show player 11f
        show helen 22 at Position (xoffset=-13) with dissolve
        pause
        show helen 33 with dissolve
        show player 23f
        player_name "!!!"
        show ang 2f
        show helen 29
        ang "Ótimo, {b}Helen{/b}."
        show ang 1f
        show helen 33
        helen "..."
        show ang 2f
        show helen 29
        ang "{b}[firstname]{/b}?"
        show ang 1f
        show helen 31
        show player 21f
        player_name "Ehh... sim?"
        show player 5f
        show ang 2f
        show helen 29
        ang "Você pode sair agora, não preciso mais de você essa noite."
        ang "Volte outra hora para que possamos continuar nossas sessões..."
        show ang 1f
        show player 10f
        player_name "Oh, ok."
        player_name "Boa noite então!"
        hide player
        hide helen
        hide ang
        with dissolve
        $ gTimer.tick()
        $ M_mia.trigger(T_helen_angelica_ritual)
        $ location_count = "Town Map"

    elif M_mia.get_state() == S_mia_angelicas_order and gTimer.is_dark():
        scene church_nun_n_c with fade
        show player 23f at right
        show helen 29 at Position (xpos=575)
        show ang 5f at left
        with dissolve
        player_name "!!!"
        show ang 6f
        ang "Qual o problema, {b}[firstname]{/b}?"
        show ang 7f with dissolve
        pause
        show ang 8f
        ang "Você não está tendo nenhum pensamento pecaminoso, não está?"
        show player 22f
        ang "Talvez você devesse tomar o lugar da {b}Helen's{/b}-"
        show ang 7f
        show player 10f
        player_name "Não! Eu... Eu estou surpreso por você não estar vestindo sua roupa!"
        show player 11f
        ang "..."
        show ang 9 with dissolve
        ang "Eu estava mostrando para a {b}Helen{/b} como {b}Deus{/b} abençoa seus poucos escolhidos que são verdadeiramente sagrados e devotos por dentro e por fora."
        ang "Como você pode ver... Ele me abençoou com um corpo sagrado..."
        show ang 10
        pause
        show ang 9
        ang "Certo, {b}Helen{/b}?"
        show ang 10
        show helen 34
        helen "...Sim, seu corpo... é o tempo do nosso {b}Senhor{/b}."
        show helen 33
        show ang 8f with dissolve
        ang "Além disso, a partir deste momento, o sacramento da purificação exige que eu coloque minhas mãos sobre o pecador imundo arrependido."
        ang "Eu prefiro não quero sujar minhas roupas..."
        show ang 6f with dissolve
        ang "Agora, se você não se importar, devo voltar às minhas instruções com a {b}Helen{/b}."
        show ang 9 with dissolve
        ang "E se eu ver desejos pecaminosos aparecerem em suas regiões inferiores, não pensarei duas vezes em fazer o julgamento de {b}Deus{/b} em você..."
        show ang 11
        show player 22f
        player_name "!!!"
        show ang 9
        ang "Entendido?"
        show ang 10
        show player 138f at Position (xoffset=-16) with dissolve
        player_name "S... Si... Sim... {b}Irmã Angelica{/b}."
        hide player
        hide ang
        hide helen
        with dissolve
        $ M_mia.trigger(T_angelica_sinful_thoughts)

    elif M_mia.get_state() == S_mia_angelicas_final_request and strapon in inventory.items and gTimer.is_dark():
        $ location_count = "Church Stairs"
        $ callScreen("Route Warning", False, False)
        $ location_count = "Angelica's Room"
        jump helen_final_sacrament
    $ callScreen(location_count)

label priest_outfit:
    scene church_nun_b
    show player 444f with dissolve
    player_name "..."
    player_name "( Essa coisa é pesada! )"
    show player 106f at Position (xoffset=1)
    show players robe f
    with dissolve
    player_name "Hmm..."
    show player 33f at Position (xoffset=1)
    player_name "( Parece que vai funcionar. )"
    show player 14f at Position (xoffset=1)
    player_name "( Vamos ver se consigo me aproximar da {b}Helen{/b}... )"
    hide player
    hide players robe
    with dissolve
    $ lock_ui()
    $ M_mia.trigger(T_mia_priest_outfit)
    $ callScreen(location_count)

label angelicas_room_dialogue:
    if M_helen.is_set('helen route'):
        jump angelica_room_new_dialogue

    elif M_mia.is_set('mia route'):
        scene church_nun_n_c with fade
        show ang 2f at left
        show player 5f at right
        with dissolve
        ang "O que você está fazendo aqui?"
        show ang 1f
        show player 10f
        player_name "Você ainda está realizando o sacrifício da purificação?"
        show player 5f
        show ang 2f
        ang "Poderia estar, mas não tenho nenhum outro pecador no momento..."
        ang "{b}Helen{/b} não me visita mais."
        ang "Ela provavelmente está tendo seus pecados sendo expurgado pelo seu marido como falamos."
        show ang 1f
        show player 12f
        player_name "Você está bem?"
        player_name "Você parece triste."
        show player 5f
        show ang 2f
        ang "Estou bem. Não preciso mais de seus serviços."
        ang "Saia."
        show ang 1f
        show player 10f
        player_name "Ok."
        hide player
        hide ang
        with dissolve

    elif M_mia.get_state() == S_mia_harolds_thoughts:
        scene church_nun_n_c
        show player 12 with dissolve
        player_name "( Eu deveria falar com {b}Harold{/b} antes de ver a {b}Irmã Angelica{/b}. )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_find_sinners:
        scene church_nun_n_c
        show ang 1 at right
        show player 12 at left
        with dissolve
        player_name "Olá, {b}Irmã Angelica{/b}..."
        show player 5
        show ang 2
        ang "...Sim?"
        ang "O que você quer?"
        show ang 1
        menu:
            "Encontrar pecadores.":
                show player 12
                player_name "O que você precisa que eu fizesse por você mesmo?"
                show player 5
                show ang 2
                ang "Preciso que você encontre pecadores para o meu sacrifício."
                ang "Traga {b}Helen{/b}, a mulher do confessionário, para que nos conhecemos..."
                show ang 1
                show player 12
                player_name "Oh, certo... Você quer que eu a convença."
                player_name "Certo. Vou ver o que posso fazer..."
                hide player
                hide ang
                with dissolve

    elif M_mia.get_state() == S_mia_angelicas_whip:
        scene church_nun_n_c with fade
        show player 5f at right
        show helen 29 at Position (xpos=575)
        show ang 5f at left
        with dissolve
        menu:
            "O chicote.":
                if whip in inventory.items:
                    $ inventory.items.remove(whip)
                    jump helen_sacrement_training_part2
                show ang 6f
                ang "Você me trouxe o {b}chicote{/b} para o ritual de flagelação em meu sacrifício de purificação?"
                show ang 5f
                show player 10f
                player_name "Não..."
                show player 5f
                show ang 6f
                ang "Então por que você está aqui?"
                show ang 5f
                show player 12f
                player_name "Onde você disse que eu posso encontrar mesmo?"
                show player 5f
                show ang 6f
                ang "Tenho certeza de que alguém de sua idade conhece lugares impuros e pecaminosos que vendem essas coisas."
                ang "Agora pare de testar minha paciência e me traga um chicote."
                hide ang
                hide helen
                with dissolve
                show player 10f
                player_name "( Talvez a {b}loja Pink no shopping{/b} venda algo do tipo. )"
                hide player with dissolve
            "Nada.":

                show player 10f
                player_name "Nada."
                show player 5f
                show ang 6f
                ang "Então saia. Estou ocupada."
                ang "Eu vou visitá-lo quando eu precisar de sua ajuda."
                hide player
                hide ang
                hide helen
                with dissolve
    else:

        scene church_nun_n_c with fade
        show player 10f at right
        show helen 37 at Position (xpos=575)
        show ang 5f at left
        with dissolve
        player_name "Oi, {b}Irmã Angelica{/b}..."
        show player 5f
        show ang 6f
        ang "...Pois não?"
        ang "O que é que você quer?"
        show ang 5f
        menu:
            "Cintaralho." if M_mia.get_state() in [S_mia_harolds_thoughts, S_mia_angelicas_final_request] and strapon not in inventory.items:
                show player 460f at Position (xoffset=-1) with dissolve
                player_name "Você quis me entregar essas fotografias, certo?"
                show player 461f at Position (xoffset=-1)
                show ang 9 with dissolve
                ang "Sim."
                ang "Não cometo erros."
                ang "Agora vá e compre!"
                hide ang
                hide helen
                with dissolve
                show player 5f with dissolve
                player_name "..."
                show player 10f
                player_name "( Acho que minha última tarefa é arranjar {b}uma cintaralha{/b}. )"
                player_name "( Único lugar que deve vender isso é na {b}Pink{/b}... )"
                hide player with dissolve
            "Nada.":

                show player 10f
                player_name "Nada."
                show player 5f
                show ang 6f
                ang "Então sai. Estou ocupada."
                ang "Eu vou visitá-lo quando eu precisar de sua ajuda."
                hide player
                hide ang
                hide helen
                with dissolve
    $ callScreen(location_count)

label helen_sacrement_training_part2:
    scene church_nun_n_c with fade
    show helen 29 at Position (xpos=575)
    show player 5f at right
    show ang 6f at left
    with dissolve
    ang "Então?"
    ang "Você trouxe o que eu queria?"
    show ang 5f
    show player 12f
    player_name "Sim, acho que achei."
    show player 239_240f with dissolve
    pause
    show player 455f
    player_name "Isso serve?"
    show player 456f
    ang "Hmm..."
    hide helen
    show helen 29 at Position (xpos=575)
    show player 5f
    show ang 18f
    with dissolve
    ang "Estou impressionada."
    ang "Você parece ter um ótimo olho para a precisão bíblica."
    show ang 17f
    show helen 30
    helen "O que você vai fazer com esse chicote?"
    show helen 29
    show ang 18f
    ang "Quieta."
    show helen 33
    show ang 17f
    show player 10f
    player_name "É melhor eu ir para casa. Está ficando tarde."
    show player 11f
    show ang 18f
    ang "Espera. Quero que você fique para o próximo passo da purificação da {b}Helen's{/b}."
    ang "{b}Helen{/b} me disse que viu você contaminando o corpo dela outro dia."
    ang "Parece que ela está puxando você para seus caminhos perversos e pecaminosos."
    show ang 17f
    show helen 32
    helen "Desculpa, {b}[firstname]{/b} I-"
    show helen 33
    show ang 18f
    ang "Quieta!"
    show ang 17f
    pause
    show ang 18f
    ang "Como você pode ver: {b}Helen{/b} ainda não me obedece."
    ang "Quero que você testemunhe seu castigo..."
    ang "...E veja como eu expurgo todos os seus atos vil de seu corpo."
    show ang 17f
    show helen 30
    helen "!!!"
    show player 22f
    player_name "!!!"
    helen "Isso não vai doer? eu acho que-"
    show helen 29
    show ang 18f
    ang "{b}Helen{/b}, algre-se! Hoje começa o 2º passo do sacrifício da purificação!"
    ang "Isso vai doer, mas a dor é o resultado do pecado."
    ang "Uma vez que você é capaz de tolerar a dor, você estará mais perto da redenção."
    ang "Agora. Eu quero que você tire todas as suas roupas."
    show ang 17f
    show helen 33
    helen "..."
    show helen 30
    helen "Mas, {b}[firstname]{/b} está aqui... Não é inapropriado?"
    show helen 29
    show ang 18f
    ang "{b}Helen{/b}. Não estou pedindo que você comece a se masturbar na frente dele como você estava antes."
    ang "Além disso, seu corpo estragado pelo pecado não deve deixar nenhum homem excitado."
    show ang 17f
    show helen 33
    helen "..."
    show ang 18f
    ang "Lembre-se, você veio a mim procurando uma maneira de perdão e para tornar seu corpo sagrado."
    show ang 17f
    show helen 34
    helen "T... Tudo bem. Se isso for me deixar bem aos olhos de {b}Deus{/b}."
    show helen 35 at Position (xoffset=12) with dissolve
    pause
    show player 106f
    show helen 36 with dissolve
    pause
    show player 11f
    show helen 38 with dissolve
    show ang 12 at left with dissolve
    ang "Isso. Agora, vem aqui."
    show helen 37 at Position (xpos=464) with dissolve
    show ang 13 with dissolve
    pause
    show ang 14 with dissolve
    ang "Eu estou impedindo você, {b}Helen{/b}, que os seus desejos pecaminosos tomem conta de você."
    hide helen
    show ang 15
    with dissolve
    ang "Enquanto te dou chicotadas, aprenderá o que te esepra no inferno se você não se submeter às minhas.... às vontades de {b}Deus{/b}"
    helen "O quê?"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312)
    hide player
    with dissolve
    ang "Quieta! Pare de me questionar!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    helen "Owwww!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Arrpenda-se {b}Helen{/b}!"
    ang "Sinta a ira de {b}Deus{/b} pelas suas costas!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Owww! Chega! Por favor!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Não desista tão fácil, {b}Helen{/b}!"
    ang "Você precisa disso!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Owww!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Implore para mim... Implore para o perdão!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Owwwwwww!"
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Você é tão suja, pecadora..."
    ang "{b}Helen{/b}, preciso ouvir você dizer isso..."
    helen "Eu-"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhh! Eu me arrependo! Eu... me arrependo!"
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhhh! Por favor, {b}Irmã{/b}... puna... meu corpo..."
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "O que é isso? Você está gostando, {b}Helen{/b}?"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhhh!!! Siiiiiim!!! Digo... não... eu..."
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Uma prostituta! Primeiro, você estava se masturbando na frente desse jovem e agora está gostando de ser espancada."
    ang "Quero ouvir você dizer isso, sua prostituta. Confessa-me!"
    show ang 17 at Position (xoffset=312)
    helen "Eu..."
    helen "Eu sou uma puta..."
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "Tão vulgar, {b}Helen{/b}. Agora peça-me para levar mais chicotas... puta."
    show ang 17 at Position (xoffset=312)

    helen "..."
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show helen whip 1 at Position (xpos=161)
    show ang 18 at Position (xoffset=312) with dissolve
    ang "PEÇA!"
    show ang 17 at Position (xoffset=312)

    helen "Chicoteie meu corpo de vagabunda, {b}Irmã{/b}! Me ajude!"
    hide helen
    show ang 19
    with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Mais {b}Irmã{/b}... Eu quero... mais..."
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    show ang 19 with dissolve
    pause
    show ang 20 with dissolve
    "*CRACK!*" with hpunch
    helen "Ahhhhhhh!!!"
    show helen whip 2 at left
    show ang 17 at Position (xoffset=312) with dissolve
    helen "Ohhhhh..."
    show ang 18 at Position (xoffset=312)
    ang "Uma pecadora tão pervertida, tão pecaminosa você..."
    ang "Eu vou gostar dos nossos rituais futuros..."
    show ang 17 at Position (xoffset=312)
    pause

    show ang 18f at Position (xpos=300) with dissolve
    ang "{b}[firstname]{/b}?"
    show ang 17f
    show player 24f at right with dissolve
    player_name "Sim?"
    show ang 18f
    ang "Você foi muito bom também."
    ang "Não foi, {b}Helen{/b}?"
    show ang 17f
    show player 22f
    helen "Sim..."
    show ang 18f
    ang "Agradeça-o por trazer o chicote, {b}Helen{/b}."
    show ang 17f
    show player 11f
    helen "Muito... obrigada... {b}[firstname]{/b}..."

    show ang 18f
    ang "Você pode ir, {b}[firstname]{/b}."
    ang "{b}Helen{/b} exigirá treinamento adicional, mas primeiro eu preciso tê-la mais subordinada e mais tolerante com as dores deste mundo."
    ang "Talvez, quando chegar a hora, eu possa usar você para algo um pouco mais... completo, se você quiser."
    show ang 17f
    show player 10f
    player_name "Não sei n-"
    show player 11f
    show ang 18f
    ang "Saia. Eu te procuro quando precisar de você."
    hide ang
    hide helen
    hide player
    with dissolve
    scene black with fade
    pause

    scene church_stairs_n with fade
    show player 12
    player_name "Que loucura! Eu deveria dizer algo a alguém, mas {b}Irmã Angelica{/b} parecia ter tanto controle sobre {b}Helen{/b}."
    player_name "{b}Helen{/b} provavelmente diria que ela está participando voluntariamente..."
    show player 25
    player_name "Eu deveria falar com ela e ver se ela está bem."
    hide player with dissolve
    $ gTimer.tick()
    $ M_mia.trigger(T_helen_torture)
    $ location_count = "Town Map"
    $ callScreen(location_count)

label helen_final_sacrament:
    $ inventory.items.remove(strapon_drawing)
    $ inventory.items.remove(strapon)
    $ M_mia.trigger(T_angelicas_final_ritual)
    scene church_nun_n_c with fade
    show helen whip 1 at left
    show ang 5f at Position (xpos=418)
    show player 12f at right
    with dissolve
    player_name "Ah, ótimo. Vocês já estão aqui..."
    show player 5f
    show ang 6f
    ang "Onde mais estaríamos, {b}[firstname]{/b}?"
    show ang 5f
    show player 34f
    player_name "..."
    show player 35f
    player_name "Na igreja, sentada em volta da mesa lendo a bíblia...vestidas?"
    show player 5f
    show ang 8f at Position (xoffset=3) with dissolve
    ang "A alma de {b}Helen's{/b} exige mais do que a educação comum da igreja."
    ang "Ela só precisa completar meu último ritual."
    ang "Já completamos os preparativos pré-rituais..."
    show ang 9 at Position (xoffset=22) with dissolve
    ang "Certo {b}Helen{/b}?"
    show ang 10 at Position (xoffset=22)
    helen "Sim... {b}Irmã Angelica{/b}..."
    helen "Meu corpo... está pronto para o ritual final."
    helen "Quero ser purificada..."
    helen "Eu entendi que preciso ser limpa... desde dentro..."
    show ang 9 at Position (xoffset=22)
    ang "Você tem o objeto necessário para penetrar a carne pecaminosa da {b}Helen's{/b}?"
    show ang 10 at Position (xoffset=22)
    show player 239_240f with dissolve
    pause
    show player 457f with dissolve
    player_name "...Era isso que você queria, certo?"
    show player 458f
    show ang 8f at Position (xoffset=3) with dissolve
    ang "É... perfeito."
    ang "Ponha em mim."
    show ang 28 at Position (xpos=393) with dissolve
    show player 457f
    player_name "Que?"
    show player 458f
    show ang 29
    ang "Eu gaguejei?"
    show ang 28
    show player 457f
    player_name "Certo..."
    hide player
    show ang 30 at right
    with dissolve
    player_name "Hmmm..."
    player_name "Eu acho que não há uma maneira fácil de fazer isso..."
    hide ang
    show ang 32 at Position (xpos=483)
    with dissolve
    ang "Cuidado!"
    show ang 31
    pause
    player_name "( ...Os peitos dela... )"
    player_name "( ...São tão grandes! )"
    show ang 32
    ang "Hey! Mantenha seus dedos lá embaixo..."
    ang "Eu sei usar esse chicote..."
    show ang 31
    player_name "( ... )"
    show ang 33 at Position (xpos=412)
    show player 10f at right
    with dissolve
    player_name "Pronto. Coloquei."
    show player 5f
    pause
    show ang 34
    ang "Você sabia que essa cintaralha tem uma característica especial?"
    show ang 35 at Position (xoffset=79)
    show player 6f
    pause
    show ang 33
    show player 22f
    player_name "!!!" with hpunch
    show player 23f
    player_name "Que-"
    show player 22f
    show ang 34
    ang "Apresse-se e tire sua roupa."
    show ang 33
    show player 23f
    player_name "Tirar a roupa?!"
    show player 10f
    player_name "Você não vai usar isso...em m-"
    show player 11f
    show ang 34
    ang "Todos nós temos que estar expostos ao último ritual de purificação."
    show ang 33
    show player 12f
    player_name "Beleza! Vou tirar a roupa!"
    show player 8f with dissolve
    pause
    show player 261 with dissolve
    pause
    show player 8bf with dissolve
    pause
    show player 64f
    show ang 37
    pause
    show ang 34
    ang "Ora... ora..."
    ang "Isso vai ser interessante..."
    show ang 33
    show player 63f
    pause
    show player 61f at Position (xoffset=-19) with dissolve
    player_name "..."
    show player 68f at Position (xoffset=-19)
    show ang 34f at Position (xpos=475) with dissolve
    ang "{b}Helen{/b}?"
    show ang 33f
    helen "Sim, {b}Irmã Angelica{/b}?"
    show ang 34f
    ang "Você está pronta?"
    show ang 33f
    helen "Sim."
    helen "Purifique-me, {b}Irmã Angelica{/b}."
    show ang 34f
    ang "Boa garota."
    ang "Vire-se e mostre ao {b}[firstname]{/b} a raiz do seu pecado..."
    show ang 33f
    show helen whip 3 with dissolve
    pause
    hide helen
    show ang 22f at left
    with dissolve
    pause
    show ang 23f with dissolve
    pause
    show ang 24f with dissolve
    pause
    show ang 25f with dissolve
    pause
    show player 68bf at Position (xoffset=-19)
    player_name "!!!"
    show ang 26f
    ang "Você gostou, {b}[firstname]{/b}?"
    ang "Da sua... buceta... molhada... e obediente?"
    show player 65f with dissolve
    pause
    show player 66f with dissolve
    pause
    show player 430bf
    show ang 25bf
    ang "!!!"
    show ang 22_23_24f
    pause
    show ang 26f
    ang "O quê foi..."
    show player 430f
    show ang 22_23_24f
    pause
    show ang 26bf
    ang "...Ficando excitado?"
    show ang 26f
    ang "Devo dizer, estou impressionada com a ajuda que você deu a {b}Helen{/b}..."
    show player 67bf
    ang "Você deve se importar com ela..."
    show ang 26bf
    ang "Ou pelo menos seu corpo está ansioso para ajudá-la..."
    show ang 22_23_24f
    pause
    show player 430f
    show ang 25f
    helen "Ohh..."
    show player 430bf
    player_name "Eu... Eu não acho que ela é tão feia quanto você diz que ela é."
    show player 430f
    show ang 26f
    ang "Bom saber..."
    show ang 25f
    pause
    show ang 26f
    ang "Agora, eu tenho certeza que você está se perguntando por que eu pedi o item na foto."
    ang "O último passo do meu sacramento da purificação requer uma longa... vara  de julgamento."
    ang "Sabe... para curar a {b}Helen{/b}, e purificar o corpo dela, ela precisa da semente sagrada."
    ang "Precisa ser plantado bem fundo... dentro dela!"
    ang "Só assim {b}Helen's{/b} a alma interior será recuperada de todos os seus pecados."
    show ang 22_23_24f
    show player 430bf
    player_name "Como assim?"
    show player 430f
    show ang 26f
    ang "Estou gentilmente oferecendo-lhe uma escolha, {b}[firstname]{/b}."
    ang "Ou você me deixa expurgar {b}Helen{/b} e você torna ela pura, e assim ela possa retornar para o marido dela..."
    ang "Ou..."
    ang "Melhor ainda, você expurga ela sozinho..."
    show ang 25f
    show player 67bf
    player_name "..."
    show ang 26f
    ang "E então ela será sua serva sagrada, {b}[firstname]{/b}."
    show ang 22_23_24f
    show player 430bf
    player_name "!!!"
    helen "Por favor, me come!!"
    show ang 26f
    ang "{b}Helen{/b} precisa que um de nós penetramos na sua carne pecaminosa..."
    ang "...Deixo essa decisão em suas mãos."
    show ang 25f
    show player 67cf
    player_name "( Se eu comer a... {b}Helen{/b}. Os pais da {b}Mia{/b} nunca ficarão juntos novamente. )"
    player_name "( E {b}Mia{/b}... {b}Mia{/b} ficará triste. )"
    show player 67bf
    show ang 26f
    ang "Então? Você vai ajudar a {b}Helen{/b}, ou não?"
    show ang 22_23_24f
    menu mia_helen_route_spilt:
        "Comer a {b}Helen{/b}.":
            show player 430bf
            player_name "Eu... Eu vou."
            show player 430f
            show ang 26f
            ang "Perfeito. Suas ações não passarão despercebidas aos olhos do {b}Senhor{/b}, {b}[firstname]{/b}..."
            ang "...Ou meus."
            ang "Então, comecemos o último ritual."
            hide ang
            hide player
            with dissolve
            label helen_mc_churchsex:
                scene church_nun_n_hs_1
                show helens 4_4b
                with fade
                ang "Apenas uma dica, {b}[firstname]{/b}."
                ang "Quero que você vá devagar."
                if not M_helen.get_state() == S_helen_start:
                    ang "A primeira vez é sempre...especial."
                show helens 5 with dissolve
                helen "Ohhhh, {b}[firstname]{/b}!"
                $ M_helen.set('sex speed', .175)
                show helens 6_7_8_9_10 with dissolve
                helen "Ahhhh... Seja gentil...."
                player_name "Está tão...molhada!"
                player_name "Puta mer-"
                ang "Ah ah ah. Estamos em um lugar de adoração."
                ang "Isso. Agora vá mais fundo e não solte sua semente até eu mandar."
                ang "Não se esqueça que eu tenho meu chicote..."
                pause
                $ M_helen.set('sex speed', .125)
                show helens 6_7_8_9_10
                ang "Mais fundo! Rápido, {b}[firstname]{/b}! Faça ela entender o quão pecadora ela é!"
                ang "{b}Helen{/b} precisa entender que ela nunca mais vai estar livre de seu pecado agora!"
                $ M_helen.set('sex speed', .075)
                pause
                $ anim_toggle = True
                $ xray = False

                label helen_mc_churchsex_repeat:
                    hide screen helen_ang_chamber_mc_sex_options
                    show screen xray_scr
                    pause
                    hide screen xray_scr
                    if anim_toggle:
                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 6_7_8_9_10
                            pause 2
                            $ animcounter += 1
                            if animcounter == 1:
                                player_name "Ohhh!!!{p=1}{nw}"
                            if animcounter == 2:
                                helen "Ahhhh!!!{p=1}{nw}"
                            elif animcounter == 4:
                                helen "{b}[firstname]{/b}!!!{p=1}{nw}"
                            pause 4
                    else:

                        $ animcounter = 0
                        while animcounter < 4:
                            show helens 6
                            pause
                            show helens 7
                            pause
                            show helens 8
                            pause
                            show helens 9
                            pause
                            show helens 10
                            pause
                            $ animcounter += 1
                            if animcounter == 1:
                                player_name "Ohhh!!!{p=1}{nw}"
                            if animcounter == 2:
                                helen "Ahhhh!!!{p=1}{nw}"
                            elif animcounter == 4:
                                helen "{b}[firstname]{/b}!!!{p=1}{nw}"

                ang "Agora! {b}[firstname]{/b}, goze!"
                ang "Goze vem fundo na {b}Helen{/b}!"
                show screen helen_ang_chamber_mc_sex_options
                pause
                jump helen_mc_churchsex_repeat

                label helen_ang_chamber_mc_sex_cum:
                    hide screen helen_ang_chamber_mc_sex_options
                    show helens 11_11b with flash
                    player_name "UHHH!!"
                    helen "AHHHH!!!!"
                    show helens 11b with fastdissolve
                    helen "Eu... Eu me sinto...limpa..."
                    show helens 12 with dissolve
                    helen "Ohhh...tão...tão..."
                    scene black with fade
                    pause 1
                    if not M_helen.get_state() == S_helen_start:
                        jump sacrament_complete



                scene church_nun_n_c with fade
                show helen whip 2 at left
                show ang 34 at Position (xpos=412)
                show player 5f at right
                with dissolve
                ang "Que Deus te abençoe, {b}[firstname]{/b}!"
                ang "O corpo da {b}Helen{/b} agora está livre dos pecados..."
                ang "...E você acabou de fazer dela sua serva!"
                show ang 33
                show player 10f
                player_name "O quê... isso significa?"
                show player 5f
                show ang 34
                ang "Você acabou de se fazer {b}Helen's{/b} desejar você."
                ang "Agora ela vai obedecer aos seus comandos..."
                show player 11f
                ang "Você pegou o lugar do marido dela."
                ang "{b}Helen{/b} agora exigirá uma porção diária de sua semente sagrada."
                ang "Para que se mantenha pura e fiel."
                show ang 33
                show player 12f
                player_name "O quê?!"
                show player 22f
                show ang 34
                ang "Não é mesmo, {b}Helen{/b}?"
                show ang 33
                helen "Si...sim... Agora eu sirvo ao, {b}[firstname]{/b}."
                helen "Eu... vou aceitar a semente sagrada... como uma esposa submissa tem que ser."
                show ang 34
                ang "Ótimo, {b}Helen{/b}."
                ang "Isso conclui nosso ritual. Vocês dois podem viver em paz."
                ang "Continuarei a oferecer os rituais do sacramento à noite."
                ang "Sinta-se live para me visitar se você quiser... participar."
                show ang 33
                show player 12f
                player_name "Parece legal..."
                show player 10f
                player_name "...mas tenho que voltar para casa."
                hide player
                hide helen
                hide ang
                with dissolve
                $ M_helen.trigger(T_helen_route)
                $ M_helen.set('helen route', True)
        "Assistir a {b}Irmã Angelica{/b}.":

            show player 67cf
            player_name "Eu..."
            player_name "Eu não posso fazer isso."
            player_name "{b}Helen{/b} precisa do marido dela, e {b}Mia{/b} de seus pais."
            show player 67bf
            show ang 26f
            ang "Tá bom, acho que eu terei que salvar {b}Helen{/b}."
            ang "Afaste-se, {b}[firstname]{/b}."
            show ang 23f
            pause
            show ang 22f
            show player 430f
            player_name "..."
            helen "Obrigada, {b}Irmã Angelica{/b}..."
            hide ang
            hide player
            with dissolve


            scene church_nun_n_hs_2 with fade
            show helens 13 with dissolve
            ang "{b}Helen{/b}, Eu estava ansiosa para esse momento."
            ang "Você sempre foi um dos membros mais devota e piedosa de {b}Deus{/b}."
            ang "Eu sempre quis penetrar a alma de um pecador... e não usar a {b}palavra de Deus{/b}."
            helen "Oh?"
            ang "Você não é melhor que ninguém..."
            ang "Você é pior..."
            ang "Você é uma puta, {b}Helen{/b}."
            ang "Receba minha vara do julgamento!"
            show helens 14 with dissolve
            helen "Ohhh!!!"
            ang "Mais fundo, vagabunda!"
            ang "Tome!"
            $ M_helen.set('sex speed', .175)
            show helens 15_16_17_18_19 with dissolve
            helen "Ohhh!!!"
            helen "Mais rápido! {b}Irmã Angelica{/b}! Mais rápido!"
            $ M_helen.set('sex speed', .125)
            $ anim_toggle = True
            $ xray = False

            label helen_ang_churchsex_repeat:
                hide screen helen_ang_chamber_ang_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show helens 15_16_17_18_19
                    pause 2
                    $ animcounter += 1
                    if animcounter == 1:
                        helen "Ahhhh!!!{p=1}{nw}"
                    if animcounter == 2:
                        helen "Ohhh!!!{p=1}{nw}"
                    elif animcounter == 4:
                        helen "{b}Irmã{/b}!!!{p=1}{nw}"
                    pause 4
                else:

                    $ animcounter = 0
                    while animcounter < 4:
                        show helens 15
                        pause
                        show helens 16
                        pause
                        show helens 17
                        pause
                        show helens 18
                        pause
                        show helens 19
                        pause
                        $ animcounter += 1
                        if animcounter == 1:
                            helen "Ahhhh!!!"
                        if animcounter == 2:
                            helen "Ohhh!!!"
                        elif animcounter == 4:
                            helen "{b}Irmã{/b}!!!"

            helen "Eu estou quaseeee!"
            show screen helen_ang_chamber_ang_sex_options
            pause
            jump helen_ang_churchsex_repeat

            label helen_ang_chamber_ang_sex_cum:
                hide screen helen_ang_chamber_ang_sex_options
                show helens 14 with fastdissolve
                ang "Agora, solte-se dos seus pecados!"
                ang "Goze para mim, {b}Helen{/b}!"
                show helens 20 with flash
                helen "OHHHH!!!!!"
                helen "OHHHHHHHH!!!!"
                show helens 21 with dissolve
                ang "Boa vagabunda..."
                scene black with fade
                pause 1



            scene church_nun_n_c with fade
            show helen whip 2 at left
            show ang 34 at Position (xpos=412)
            show player 5f at right
            with dissolve
            ang "{b}Helen{/b} agora foi purificada."
            ang "Através do meu treinamento, ela se tornou mais submissa."
            ang "Como {b}Deus{/b} exige de todas esposas submissas ao seu marido."
            show ang 33

            helen "Obrigada, {b}Irmã Angelica{/b}."
            show player 11f
            show ang 34
            ang "Sobre você, {b}[firstname]{/b}, estou um pouco desapontada."
            show player 24f
            ang "{b}Deus{/b} pediu ajuda, e você virou as costas..."
            ang "...Você deveria ter sido o único a compartilhar suas sementes com {b}Helen{/b}!"
            show player 5f
            ang "Mas talvez isso seja fé."
            ang "Agradeço pela sua ajuda."
            ang "Eu liberto você de seus deveres e não exigirei mais seus serviços."
            show ang 33
            show player 12f
            player_name "Estou feliz que o nosso acordo acabou."
            show player 10f
            player_name "Eu espero que {b}Helen{/b} se sinta melhor depois disso tudo."
            hide player
            hide helen
            hide ang
            with dissolve
            $ M_mia.trigger(T_mia_route)
    $ gTimer.tick()
    $ location_count = "Town Map"
    $ callScreen(location_count)

label angelica_room_new_dialogue:
    scene church_nun_n_c with fade
    show helen 37 at Position (xpos=575)
    show ang 6f at left
    show player 5f at right
    with dissolve
    ang "Boa noite, {b}[firstname]{/b}. Você veio de ajudar no treinamento da {b}Helen{/b}?"
    show ang 5f
    show player 10f
    player_name "Só se você precisar da minha ajuda."
    show player 5f
    show ang 9 with dissolve
    ang "O {b}Senhor{/b} sempre precisa de ajuda dos seus seguidores."
    ang "Além disso, {b}Helen{/b} estava esperando por você de novo."
    show ang 10
    show helen 39
    helen "Estou feliz que você estej aqui, {b}Mestre{/b}."
    show helen 37
    show ang 9
    ang "{b}Helen{/b}, vamos preparar você para o ritual dessa noite."
    show helen 37 at Position (xpos=464) with dissolve
    show ang 13 with dissolve
    pause
    show ang 14 with dissolve
    ang "Caso você ainda tenha algum impulso pecaminoso."
    hide helen
    show ang 15
    with dissolve
    ang "Gosto de ver você atendendo os meus comandos tão submissamente, {b}Helen{/b}."
    show helen whip 1 at Position (xpos=161)
    hide ang
    show ang 9 at Position (xpos=462)
    with dissolve
    ang "Agora."
    ang "Há algo que você gostaria de ter feito para {b}Helen{/b}?"
    show ang 10
    menu angelica_new_dialouge_repeat:
        "Chicotadas.":
            show player 24f
            player_name "Quero que você dê... chicotadas..."
            show player 29f
            player_name "Esqueça."
            show player 5f
            show ang 9
            ang "Oh?"
            ang "Você está me pedindo para punir {b}Helen{/b}?"
            show ang 10
            show player 24f
            player_name "..."
            show ang 9
            ang "Não se preocupe, {b}[firstname]{/b}."
            ang "{b}Helen{/b}, gosta de ser chicoteada. Não gosta, {b}Helen{/b}?"
            show ang 10
            helen "Sim, {b}Irmã Angelica{/b}."
            show ang 18f at Position (xoffset=27) with dissolve
            ang "Sente-se, {b}[firstname]{/b} e aprecie o show."
            show helen whip 1 at left
            show ang 18 at left
            show ang 18 at Position (xoffset=312)
            hide player
            with dissolve
            ang "Arrependa-se, {b}Helen{/b}!"
            ang "Sinta a ira de {b}Deus{/b} nas suas costas!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Ohhhh!"
            show ang 18 at Position (xoffset=312)
            ang "Implore... Implore por mais!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Mais! Puna meu corpo pecaminoso!"
            show ang 18 at Position (xoffset=312)
            ang "Você é tão safada..."
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 18 at Position (xoffset=312) with dissolve
            ang "Tão puta."
            ang "Me diga...qual pau você prefere?"
            show ang 17 at Position (xoffset=312)
            helen "O qu-"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 18 at Position (xoffset=312) with dissolve
            ang "Quero ouvir você dizer, vagabunda. O pinto do {b}[firstname]{/b} é melhor que o do {b}Harold's{/b}?"
            show ang 17 at Position (xoffset=312)
            helen "..."
            helen "......"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Ahhhhh!!! {b}[firstname]{/b}! Eu... amo... o pauzão dele!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 18 at Position (xoffset=312) with dissolve
            ang "Tão vulgar, {b}Helen{/b}... Agora peça para que eu te espanque mais, sua puta."
            show ang 17 at Position (xoffset=312)
            helen "Espanque meu corpo pecaminoso, {b}Irmã Angelica{/b}! Me ajude!"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 1 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Mais {b}Irmã{/b}... Eu quero... mais..."
            helen "O que... você... está esperando?"
            hide helen
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show ang 19
            with dissolve
            pause
            show ang 20 with dissolve
            "*CRACK!*" with hpunch
            show helen whip 2 at Position (xpos=161)
            show ang 17 at Position (xoffset=312) with dissolve
            helen "Ohhhhhhh!!!"
            show ang 18 at Position (xoffset=312)
            ang "Que pecadora pervertida que você é..."
            hide ang
            hide helen
            with dissolve
            jump sacrament_complete
        "Semente sagrada.":

            show player 10f
            player_name "Estou aqui para ajudar a expurgar os pecados da {b}Helen{/b}."
            show ang 9
            ang "Perfeito. Suas ações não passarão despercebidas aos olhos do {b}Senhor{/b}, {b}[firstname]{/b}..."
            ang "...Ou meus."
            ang "Agora, vamos começar nosso último ritual."
            hide ang
            hide helen
            hide player
            with dissolve
            jump helen_mc_churchsex
        "Abrir {b}Helen{/b}.":

            show player 24f
            player_name "Você poderia... abrir a..."
            show ang 9
            ang "Buceta da {b}Helen{/b}?"
            ang "Talvez eu pudesse."
            ang "Se você ficasse pelado."
            ang "Quero ver como a buceta da {b}Helen{/b} te excita."
            show ang 10
            pause
            player_name "Certo."
            show player 8f with dissolve
            pause
            show player 261 with dissolve
            pause
            show player 8bf with dissolve
            pause
            show player 64f
            show ang 9
            ang "Bom garoto."
            show ang 9f at Position (xoffset=100) with dissolve
            ang "Vire-se {b}Helen{/b}."
            show ang 10f at Position (xoffset=100)
            show helen whip 3 with dissolve
            pause
            hide helen
            show player 68bf at Position (xoffset=-19)
            show ang 22f at left
            with dissolve
            pause
            show ang 23f with dissolve
            pause
            show ang 24f with dissolve
            pause
            show ang 25f with dissolve
            pause
            show ang 22_23_24f
            helen "Ohhhh..."
            show player 65f with dissolve
            pause
            show player 430bf with dissolve
            helen "Ahhhh..."
            show ang 26f
            ang "Você gosta disso?"
            show player 430f
            show ang 25f
            helen "Sim..."
            show ang 26f
            ang "Calada, puta. Perguntei ao {b}[firstname]{/b}."
            show ang 22_23_24f
            show player 430bf
            player_name "Sim."
            pause
            hide player
            hide ang
            with dissolve
            scene black with fade
            pause 1
            jump sacrament_complete
        "Você já pecou?":

            show popup_unfinished at truecenter with dissolve
            $ renpy.pause()
            hide popup_unfinished with dissolve
            jump angelica_new_dialouge_repeat
        "Nada.":

            show player 10f
            player_name "Nada."
            show player 5f
            show ang 6f at Position (xoffset=-22) with dissolve
            ang "Então saia. Estou ocupada agora."
            hide player
            hide ang
            hide helen
            with dissolve
    $ callScreen(location_count)

label sacrament_complete:
    scene church_nun_n_c with fade
    show helen whip 2 at left
    show ang 6f at Position (xpos=434)
    show player 5f at right
    with dissolve
    ang "Sinta-se à vontade para me visitar novamente se você quiser participar do ritual."
    show ang 5f
    show player 10f
    player_name "É melhor eu voltar para casa."
    hide player
    hide helen
    hide ang
    with dissolve
    $ gTimer.tick()
    $ location_count = "Town Map"
    $ callScreen(location_count)

label helen_ang_chamber_ang_faster_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') - 0.05)
    jump helen_ang_churchsex_repeat

label helen_ang_chamber_ang_slower_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') + 0.05)
    jump helen_ang_churchsex_repeat

label helen_ang_chamber_mc_faster_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') - 0.05)
    jump helen_mc_churchsex_repeat

label helen_ang_chamber_mc_slower_sex:
    $ M_helen.set('sex speed', M_helen.get('sex speed') + 0.05)
    jump helen_mc_churchsex_repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
