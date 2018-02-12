label erik_indoors:
    $ location_count = "Erik's House Entrance"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if erik.over(erik_gf) and not erik.known(erik_gf_2):
        scene expression gTimer.image("erik_inside{}_b")
        show player 14 at left
        show june 2 at Position (xpos=700)
        show erik 1 at right
        with dissolve
        player_name "Ah, olá pessoal!"
        show player 1
        show erik 4
        eri "Olá, {b}[firstname]{/b}!"
        show june 3
        show erik 1
        june "Oi!"
        show player 14
        show june 2
        player_name "Não sabia que vocês já estavam saindo!"
        show player 1
        show erik 4
        eri "Nós estamos jogando bastante o Ork Bork..."
        show erik 1
        show june 6
        june "Ha ha. Sim, estamos viciados!"
        show june 2
        show player 14
        player_name "Então, vocês estão se dando bem, huh?"
        show player 1
        show erik 4
        eri "Sim, na verdade temos que fazer coisas... no meu err... quarto."
        show erik 1
        show player 11
        show june 3
        june "Sim, temos que, uhm... ver algo?"
        show player 14
        show june 2
        player_name "Oh... Entendi!"
        show player 17
        player_name "Está tudo bem, volto outra hora."
        show player 14
        player_name "Vejo vocês depois!"
        show player 1
        show erik 4
        eri "Até mais, mano."
        hide player
        hide june
        hide erik
        with dissolve
        $ erik.add_event(erik_gf_2)
        $ erik_gf_2.finish()

    elif erik.over(erik_path_split) and erik.started(erik_sex_ed):
        $ lock_ui()
        label erik_sex_ed_block:
            scene expression gTimer.image("erik_inside{}_b")
            show player 14
            with dissolve
            player_name "Eu deveria ver se o {b}Erik{/b} está no quarto dele..."
            hide player with dissolve

    elif mrsj.over(mrsj_poker_night) and not mrsj.known(mrsj_poker_night_2):
        scene expression gTimer.image("erik_inside{}_b")
        show erikmom 17 at right
        show player 1 at left
        with dissolve
        erimom "{b}[firstname]{/b}!"
        show player 11
        erimom "Posso falar com você antes de você falar com o {b}Erik{/b}?"
        show erikmom 14
        show player 14
        player_name "Claro, {b}Sra. Johnson{/b}."
        show erikmom 20
        show player 11
        erimom "Eu... eu não me lembro muito de ontem a noite."
        show erikmom 19
        erimom "Seja lá o que tenha acontecido, quero me desculpar."
        show player 13
        erimom "Bebi muito, e eu não deveria fazer essas coisas com vocês."
        show erikmom 19c
        show player 10
        player_name "Ah, está tudo bem, Sra. Johnson..."
        show erikmom 19
        show player 13
        erimom "Você não está bravo, certo?"
        show erikmom 19c
        show player 14
        player_name "Claro que não."
        player_name "Achei divertido!"
        show erikmom 19
        show player 1
        erimom "E o {b}Erik{/b}?"
        erimom "Se divertiu também?"
        show player 14
        show erikmom 14
        player_name "Eu... eu acho que sim?"
        show erikmom 17
        show player 1
        erimom "Ótimo... desde que vocês não achassem estranho..."
        show erikmom 19c
        show player 14
        player_name "Você conversou com ele sobre isso?"
        show erikmom 19
        show player 11
        erimom "Não! Claro que não."
        show erikmom 20
        erimom "Não quero deixar isso mais estranho do que já é."
        show erikmom 19
        erimom "Mas... Você poderia falar com ele por mim?"
        erimom "Só quero ter certeza que ele não esteja bravo por isso."
        show erikmom 14
        show player 14
        player_name "Sem problemas, {b}Sra. Johnson{/b}. Eu falo com ele."
        show erikmom 18
        show player 1
        erimom "Obrigada, você é tão gentil."
        hide player
        hide erikmom
        with dissolve
        $ mrsj.add_event(mrsj_poker_night_2)
        $ mrsj_poker_night_2.finish()

    elif erik.over(erik_thief_2) and not mrsj.known(mrsj_poker_night):
        scene expression gTimer.image("erik_inside{}_b")
        show player 14 at left
        show erik 1 zorder 1 at right
        with dissolve
        player_name "Eae, {b}Erik{/b}."
        show erik 4
        show player 1
        eri "Eae, encontrou alguém?"
        show erik 1
        show player 10
        player_name "Ainda não, todo mundo está sempre muito ocupado e não quer vim."
        show erik 5
        show player 11
        eri "Até a {b}Mia{/b}?"
        show erik 1
        show player 10
        player_name "Acho que ela está ocupada com a tarefa."
        show erik 3
        show player 5
        eri "Aww cara, e quem mais iria jogar poker com a gente?"
        show player 1
        show erik 1b at Position(xpos=870)
        show erikmom 17b zorder 2 at right
        with dissolve
        erimom "Algo está errado, bebê?"
        show erik 4b
        show erikmom 14b
        eri "Não, não é nada, {b}mãe{/b}."
        show erik 1b
        show erikmom 18
        erimom "Ah, vamos! Ouvi que vocês estavam falando em convidar amigos."
        show erik 5b
        show erikmom 14b
        eri "Nós não conseguimos achar alguém para jogar poker conosco."
        show erik 1b
        show erikmom 17
        erimom "Ooh, isos parece divertido!"
        show erik 5b
        show erikmom 14b
        eri "Será divertido se tivermos mais pessoas..."
        show erik 1b
        show player 11
        show erikmom 17
        erimom "E eu?"
        show player 13
        show erikmom 18
        erimom "Eu quero jogar..."
        show player 1
        show erik 4b
        show erikmom 14b
        eri "Sério?"
        show erik 1b
        show erikmom 17
        erimom "Claro! Não é justo que meninos bons como vocês não possam encontrar alguém com quem brincar..."
        erimom "Me diga quando vocês precisarem de outro jogador, me avisem, estou sempre pronta para uma boa noite de poker!"
        show erik 1
        show player 14
        show erikmom 14
        player_name "Irado!"
        show player 17
        player_name "Valeu, {b}Sra. Johnson{/b}."
        show player 1
        show erik 1 at right
        hide erikmom
        with dissolve
        pause
        show player 14
        player_name "Cara!! Não acredito que sua mãe vai jogar com a gente."
        show erik 4
        show player 1
        eri "Acho que achamos alguém..."
        hide player
        hide erik
        with dissolve
        $ mrsj.add_event(mrsj_poker_night)

    elif erik.over(erik_thief) and not erik.known(erik_thief_2):
        scene expression gTimer.image("erik_entrance{}_c")
        show erikmom 19 at right
        show player 13 at left
        with dissolve
        erimom "{b}[firstname]{/b}!"
        erimom "Eu só queria agradecer muito, sabe, por você nos proteger."
        show erikmom 20
        erimom "É muito embaraçoso que você tenha que ver meu ex-marido assim..."
        show erikmom 19c
        show player 33
        player_name "Eu só queria ter certeza de que ele não arrombasse sua casa."
        show player 13
        show erikmom 17
        erimom "Tenho sorte de ter um visinho tão maravilhoso..."
        show erikmom 14
        show player 17
        player_name "Ah, valeu!"
        show player 13
        show erikmom 49
        erimom "Eu deveria... dar uma recompensa especial, pelo que você fez..."
        show erikmom 50
        show player 4 with dissolve
        player_name "..."
        show player 29 with dissolve
        player_name "Uhh, não precisa, {b}Sra. Johnson{/b}!"
        show player 13 with dissolve
        show erikmom 49
        erimom "Ah, não. Eu insisto!"
        erimom "Sei de algo que tenho certeza que você vai gostar..."
        show erikmom 50
        show player 17
        player_name "Ha ha, beleza."
        hide player
        hide erikmom
        with dissolve
        $ erik.add_event(erik_thief_2)
        $ erik_thief_2.finish()

    elif mrsj.over(mrsj_yoga_help_2) and not erik.known(erik_breastfeeding):
        scene expression gTimer.image("erik_inside{}_b")
        show player 10 with dissolve
        player_name "( Está tão silencioso, tem alguém em casa? )"
        player_name "( Talvez o {b}Erik{/b} está no quarto dele. )"
        show player 17
        player_name "( Espero que ele não esteja dormindo... ou fazendo outras coisas. )"
        hide player with dissolve
        $ erik.add_event(erik_breastfeeding)
        $ lock_ui()

    elif mrsj.started(mrsj_yoga_help_2):
        scene expression gTimer.image("erik_entrance{}_c")
        show erikmom 17 at right
        show player 17 at left
        with dissolve
        erimom "{b}[firstname]{/b}!!"
        erimom "Como sua primeira vez instruindo uma aula de yoga?"
        show erikmom 14
        show player 14
        player_name "Acho que fui bem."
        show player 13
        show erikmom 17
        erimom "A {b}Anna{/b} ajudou você?"
        show erikmom 14
        show player 14
        player_name "Sim, ela estava lá."
        player_name "Ela é muito boa no yoga..."
        show player 17
        player_name "...flexível!"
        show player 13
        show erikmom 18
        erimom "Ha ha ha!"
        show erikmom 49
        erimom "{b}Anna{/b} consegue ir em qualquer posição que eu ponho ela."
        erimom "Eu deixei ela igual uma rosquinha, uma vez."
        show erikmom 50
        show player 12
        player_name "Sério?"
        show player 11
        show erikmom 49
        erimom "Sim. Ela está muito boa nessas... ocasiões."
        erimom "E um pouco de óleo de bebê também não machuca..."
        show erikmom 50
        show player 13
        player_name "..."
        show erikmom 19
        erimom "Umm... Que seja, você acha que pode fazer de novo?"
        show erikmom 14
        show player 14
        player_name "Bem, ela me convidou para fazer mais yoga com ela na academia à noite."
        show player 13
        show erikmom 18
        erimom "Você deveria ir!"
        show erikmom 49
        erimom "{b}Anna{/b} pode te ensinar muita coisa..."
        show erikmom 50
        show player 17
        player_name "Com certeza, ha ha."
        show player 13
        show erikmom 19
        erimom "Obrigada por me ajudar. De novo."
        show erikmom 17
        erimom "Não ache que eu me esqueci pelo que você fez pela minha família."
        show erikmom 49
        erimom "Eu te devo... muito."
        show erikmom 50
        show player 33
        player_name "Não se preocupe. Sem problemas."
        hide player
        hide erikmom
        with dissolve
        $ mrsj_yoga_help_2.finish()

    elif erik.over(erik_vr) and not mrsj.known(mrsj_yoga_help):
        scene expression gTimer.image("erik_entrance{}_c")
        show erikmom 17 at right
        show player 13 at left
        with dissolve
        erimom "Ah, ótimo!"
        show erikmom 19
        erimom "{b}[firstname]{/b}, Odeio te encomodar, mas você está livre hoje a noite?"
        show erikmom 19c
        show player 10
        player_name "Huh?"
        show player 11
        show erikmom 19
        erimom "Preciso que álugém me substitua na aula de yoga hoje. Tenho outras coisas para fazer."
        show erikmom 14
        show player 12
        player_name "Eu?!"
        show player 5
        show erikmom 49
        erimom "Você acha que pode ajudar sua... vizinha favorita??"
        show erikmom 50
        show player 38 with dissolve
        player_name "Uhh... Eu... posso tentar."
        show player 29 with dissolve
        player_name "Mas não sei muito sobre yoga..."
        show player 11 at left with dissolve
        show erikmom 17
        erimom "É uma aula para iniciantes!"
        erimom "Você se sairá bem!"
        show erikmom 57 with dissolve
        erimom "Aqui está uma lista de posições que você terá que fazer na frente da turma."
        show erikmom 58
        pause
        show erikmom 14
        show player 386
        with dissolve
        player_name "Valeu."
        show player 380
        pause
        show player 384
        player_name "Umm... Essas posições parecem um pouco complicada..."
        show player 385
        show erikmom 17
        erimom "Minha amiga {b}Anna{/b} estará lá para te ajudar."
        show erikmom 18
        erimom "Ela é minha jovem aprendiz. Sempre disposta a ajudar e a agradar."
        show erikmom 14
        show player 386
        player_name "Oh. Ok... Farei o que for possível."
        show player 385
        show erikmom 49
        erimom "Você é tão gentil. Tenha certeza que vou te pagar algum dia!"
        show erikmom 17
        erimom "Tenho que ir, estude esses movimentos!"
        erimom "Tchau!"
        show erikmom 14
        show player 386
        player_name "Tchau, {b}Sra. Johnson{/b}."
        show player 385
        hide erikmom with dissolve

        show unlock41 at truecenter with dissolve
        $ inventory.items.append(instructions1)
        pause
        $ mrsj.add_event(mrsj_yoga_help)
        hide unlock41 with dissolve

        show player 381
        player_name "Deveria dar uma olhada nesses movimentos antes de ir para a aula hoje..."
        hide player with dissolve

    elif mrsj.started(mrsj_intro) and not gTimer.is_morning():
        scene expression gTimer.image("erik_entrance{}_c")
        show player 1 at left
        show erikmom 17 at right
        with dissolve
        erimom "Olá, {b}[firstname]{/b}!"
        show erikmom 14
        show player 36 with dissolve
        player_name "Oi, {b}Sra. Johnson{/b}."
        show player 13 with dissolve
        show erikmom 17
        erimom "Faz um bom tempo desde a sua última visita!"
        show erikmom 14
        show player 10
        player_name "Pois é, eu estava um pouco ocupada."
        player_name "Eu tenho tentado recuperar o atraso na escolar e economizar um pouco de dinheiro para a faculdade."
        show player 13
        show erikmom 17
        erimom "É bom ouvir um jovem, como você, agindo com muita responsabilidade."
        show erikmom 49
        erimom "Certifique-se de economizar algum tempo para as meninas, querido."
        show erikmom 50
        show player 21
        player_name "Claro..."
        show player 13
        pause
        show erikmom 17
        erimom "Certo, estou feliz por ver você novamente!"
        show erikmom 18
        erimom "Você deve estar aqui para ver o {b}Erik{/b}, e não eu."
        show erikmom 17
        erimom "Etá tão quieto por aqui..."
        show erikmom 14
        show player 10
        player_name "O que você quer dizer?"
        show player 5
        show erikmom 19
        erimom "Digo, é que o {b}Erik{/b} não recebe muitas visitas e você e o único melhor amigo dele."
        show erikmom 17
        show player 13
        erimom "Você é sempre bem-vindo nessa casa, dia ou noite."
        show erikmom 49
        erimom "Você é um bom garoto."
        show erikmom 50
        show player 2
        player_name "Valeu, {b}Sra. Johnson{/b}."
        show player 13
        pause
        show player 12
        player_name "Você sabe onde o {b}Erik{/b} está?"
        show player 5
        show erikmom 17
        erimom "Eu acho que o vi ele faz pouco tempo fazendo uma aparição rara fora do quarto dele."
        erimom "He's probably down in the basement right now."
        if not gTimer.is_dark():
            erimom "Alias, tenho que ir."
            show player 13
            erimom "Eu tenho que ensinar aulas de yoga à tarde na academia."
            erimom "Tenho alguns alunos novos e é melhor eu me apressar, para que eu não me atrase!"
            show erikmom 14
            show player 14
            player_name "Ok, divirta-se!"
            show player 13
            show erikmom 17
            erimom "Você também! Diga ao {b}Erik{/b} que eu volto para a janta e que ele não coma muitos doces."
            show erikmom 49
            erimom "Quero que ele esteja com fome essa noite!"
        else:


            show erikmom 18
            erimom "Certo, está ficando um pouco tard."
            show erikmom 17
            show player 13
            erimom "Eu vou para a cama, então divirta-se. Mas lembre-se de manter o volume a um nível baixo se você jogar alguns jogos."
            show erikmom 14
            show player 14
            player_name "Deixarei. Durma bem, {b}Sra. Johnson{/b}!"
        $ mrsj_intro.finish()
        hide erikmom
        hide player
        with dissolve

    elif erik.completed(erik_orcette) and orcette in inventory.items and not erik.known(erik_orcette_2):
        scene expression gTimer.image("erik_entrance{}_c")
        show player 375 at left
        show erikmom 17 at right
        with dissolve
        erimom "Olá, {b}[firstname]{/b}!"
        erimom "Você está procurado pelo {b}Erik{/b}?"
        show erikmom 14
        show player 377
        player_name "!!!"
        show player 376
        player_name "O... olá, {b}Sra. Johnson{/b}."
        show player 378
        erimom "..."
        show erikmom 17
        erimom "O que vocês dois vão fazer..."
        show erikmom 14
        show player 376
        player_name "Ah, nada!"
        show player 377
        show erikmom 49
        erimom "O que é isso que você está segurando?"
        erimom "Algo que você e o {b}Erik{/b} vão brincar juntos?"
        show erikmom 50
        player_name "!!!"
        show player 379
        player_name "Uh.... Sim, tipo isso."
        show player 377
        show erikmom 17
        erimom "Adoro surpresas! O que é isso? Deve ser um jogo novo."
        erimom "Isso é tudo o que o meu bebê quer hoje em dia..."
        show erikmom 14
        show player 379
        player_name "Sim... Um... Não é bem... isso..."
        show player 377
        show erikmom 17
        erimom "Deixa eu ver!"
        show player 23 with dissolve
        show erikmom 43 with dissolve
        player_name "Espera!"
        show player 22
        erimom "!!!"
        show erikmom 44
        erimom "O que é... isso?"
        show erikmom 46
        show player 10
        player_name "É..."
        show player 11
        show erikmom 43
        erimom "Isso é aquelas coisas sobre sexo online?"
        show erikmom 46
        show player 10
        player_name "Uh..."
        show player 24
        show erikmom 44
        erimom "O {b}Erik{/b} te pediu isso?"
        erimom "Já vi isso na tela do computador dele quando entrei no quarto dele uma vez."
        show erikmom 46
        show player 25
        player_name "Não. Não. Isso... é... meu."
        show player 24
        player_name "Eu... Uh... Estou indo... só mostrar para ele..."
        show erikmom 45
        erimom "Ha ha."
        erimom "Meninos e seus brinquedos!"
        show erikmom 46
        player_name "..."
        show player 25
        show erikmom 44
        erimom "Oh, querido... está tudo bem!"
        erimom "Adolescentes explorando a sexualdiade é uma coisa boa!"
        erimom "Talvez se ele brincasse com isso ele... saisse do quarto?"
        erimom "A verdade é que... é bom, garoto."
        show erikmom 46
        show player 22
        player_name "{b}*Gulp*{/b}"
        show erikmom 44
        erimom "{b}Erik{/b} está lá em cima, querido."
        erimom "Ah, e certifique-se de usar o lubrificante com essa coisa."
        erimom "Você não quer queimadura nas suas... partes."
        hide erikmom with dissolve
        show player 377 with dissolve
        pause
        show player 376
        player_name "( Wow... Achei que ela iria ficar brava por essas coisas... )"
        player_name "( Mas ela estava muito tranquila sobr isso? )"
        player_name "( {b}Erik{/b} tem uma mãe legal... )"
        $ erik.add_event(erik_orcette_2)
        hide player with dissolve
    $ callScreen(location_count)

label mrsj_sex_ed:
    scene erik_house_upstairs_n_c01
    show erik 5f at Position (xpos=300)
    show player 13 at left
    show erikmom 14 at right
    with dissolve
    eri "Oi, {b}mãe{/b}!"
    eri "Você...precisa de algo?"
    show erik 1f
    show erikmom 19
    erimom "Ouça, garoto."
    erimom "Sei que vocês estavam falando sobre isso, então..."
    erimom "Eu pensei nisso, e como vocês dois estão bem com isso..."
    show erikmom 49
    erimom "Eu aceito dar aulas sobre...educação sexual."
    show erikmom 50
    show player 23
    player_name "!!!"
    show erik 5f
    eri "M...{b}Mãe{/b}, você tem certeza?"
    show erik 1f
    show erikmom 49
    show player 18
    erimom "Claro, bebê!"
    erimom "Não vejo problema se isso ficar só entre nós!!"
    show erikmom 50
    show player 14
    player_name "Eu...Eu não me importo com isso, {b}Sra. Johnson{/b}..."
    show player 11
    show erikmom 52
    erimom "Mas!!" with hpunch
    erimom "Antes de começarmos as aulas... Preciso de algo de vocŝ."
    show player 5
    show erikmom 14
    show erik 4f
    eri "O que vocês precisam, {b}mãe{/b}?"
    show erik 1f
    show erikmom 19
    show player 13
    erimom "...Eu nunca fiz sexo com dois ao mesmo tempo."
    show erikmom 49
    erimom "Quero um livro sobre posições sexuais com mais de um parceiro."
    erimom "Já ouvi falar sobre um livro chamadp {b}Karma Sutra{/b} que têm posições antigas."
    erimom "Veja se vocês conseguem achar esse livro."
    show erikmom 52
    erimom "E tem mais uma coisa..."
    show erikmom 14
    show erik 5f
    eri "Ah, é?"
    show erik 1f
    show erikmom 49
    erimom "Sim, se vocês forem transar, quero me certificar que eu não engravide!"
    show erikmom 50
    player_name "..."
    show erikmom 49
    erimom "Preciso de {b}pílulas anticoncepcionais{/b}..."
    show erikmom 50
    show erik 5f
    eri "Não podemos usar camisinha?"
    show erik 1f
    show erikmom 52
    erimom "Mesmo com camisinha, ainda é arriscado!!"
    show erikmom 49
    erimom "E se eu usar pilulas, podemos fazer sem camisinha..."
    show erikmom 50
    show player 83
    show erik 58f
    player_name "!!!"
    show player 82
    show erikmom 20
    pause
    erimom "..."
    show erikmom 18
    erimom "Ha ha!"
    show player 81
    player_name "!!!" with hpunch
    show player 78
    show erikmom 49
    erimom "Eu posso ver que vocês dois, estão muito entusiasmados com o início dessas aulas de sexo comigo..."
    show erikmom 50
    show erik 56f
    eri "Desculpa, {b}mãe{/b}."
    show erik 57f
    show erikmom 49
    erimom "Está tudo bem, bebê."
    show player 80
    erimom "Quanto mais cedo vocês me ajudarem, mais cedo podemos começar!"
    show erikmom 50
    show erik 58f
    eri "Certo, {b}mãe{/b}!"
    show erik 57f
    show player 83
    player_name "Vamos procurar o que você precisa, {b}Sra. Johnson{/b}!"
    hide player
    hide erikmom
    hide erik
    with dissolve
    scene black with fade
    pause

    $ location_count = "Erik's House Entrance"
    scene expression gTimer.image("erik_entrance{}_c")
    show erik 4 at right
    show player 13 at left
    with dissolve
    eri "Não acredito que {b}mamãe{/b} aceitou fazer sexo com nós dois..."
    show erik 1
    show player 17
    player_name "Acho que somos muito sortuods..."
    show player 13
    show erik 3
    eri "Nunca transei antes..."
    show erik 3c
    show player 14
    player_name "Bem, sua mãe planeja nos ensinar. E vai ser incrível!"
    show player 13
    show erik 5
    eri "Mas como vamos conseguir as coisas que ela pediu?"
    show erik 1
    show player 34
    player_name "Hmm..."
    show player 35
    player_name "Acho que tenho uma ideia."
    show player 13
    show erik 5
    eri "Ah, é?"
    show erik 1
    show player 14
    player_name "Tenho certeza que o hospital tem essas pílulas..."
    show player 33
    player_name "E o Kama Sutra, na biblioteca!"
    show player 13
    show erik 5
    eri "Espero que sim."
    show erik 1
    show player 14
    player_name "Volto assim que eu encontrar algo..."
    hide player
    hide erik
    with dissolve
    $ erik.complete_events(erik_sex_ed)
    $ mrsj.add_event(mrsj_sex_ed)
    $ unlock_ui()
    $ callScreen(location_count)

label mrsj_sex_ed_2:
    scene erik_house_upstairs_n_c01
    show erik 4f at Position (xpos=300)
    show player 13 at left
    show erikmom 14 at right
    with dissolve
    eri "Ei, {b}mãe{/b}."
    show erik 1f
    show erikmom 17
    erimom "Oi, garotos!"
    erimom "Como vocês estão?"
    show erikmom 14
    show erik 4f
    eri "Achamos umas coisas que podem ajudar...com as aulas."
    show erik 1f
    show player 239_240 with dissolve
    pause
    show player 425 with dissolve
    player_name "Aqui está o que achamos, {b}Sra. Johnson{/b}!"
    show player 13
    show erikmom 63
    with dissolve
    erimom "Ah, maravilhoso!"
    erimom "Eu vou ter que me preparar para as nossas pequenas lições juntos..."
    erimom "Talvez você dois devessem me visitar de noite no meu quarto... Ou deveriamos chamar de, a nossa sala de aula!"
    erimom "Ha ha."
    hide player
    hide erikmom
    hide erik
    with dissolve
    scene black with fade
    pause

    $ location_count = "Erik's House Entrance"
    scene expression gTimer.image("erik_entrance{}_c")
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "Quando deveriamos visitar a mamãe?"
    show erik 1
    show player 14
    player_name "Vou tentar vir assim que possível..."
    player_name "Mas vcoê pode fazer isso com ela quando você quiser!"
    show player 13
    show erik 4
    eri "Tens razão..."
    eri "Valeu por nos ajudar, {b}[firstname]{/b}."
    hide player
    hide erik
    with dissolve
    $ inventory.items.remove(kamasutra)
    $ inventory.items.remove(birth_control_pills)
    $ mrsj_sex_ed.finish()
    $ callScreen(location_count)

label erik_breastfeeding:
    scene erik_house_cs01_01b with fade
    show text "Essa foi a primeira vez que fui ao quarto da {b}Sra. Johnson{/b}.\nMesmo que eu sempre soube que a mãe do {b}Erik{/b} sempre foi muito próxima a ele...\nNão imaginava ver ele... mamando..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    scene erik_house_cs02 with fade
    show text "As expressões nas caras deles diziam tudo...\n...Eu não deveria estar aqui. Tudo estaria bem...\n...Se eu tivesse batido primeiro.\nInstintivamente, eu fechei a porta e decidi que deveria sair." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    $ location_count = "Erik's House Entrance"
    scene expression gTimer.image("erik_entrance{}_c")
    show player 22 at left with dissolve
    show erik 2 at Position (xpos=750)
    show erikmom 52 at right
    with dissolve
    erimom "{b}[firstname]{/b}?!"
    erimom "Eu... o que você está fazendo aqui?"
    show erikmom 38
    show player 37 with dissolve
    player_name "{b}Erik{/b}?!"
    show erik 3b with dissolve
    player_name "Eu... hum... estava te procurando."
    show player 24 with dissolve
    show erik 3
    eri "{b}[firstname]{/b}..."
    show erik 2 with dissolve
    show player 25
    player_name "Ouvi as vozes e pensei que..."
    show player 11
    show erik 3b
    eri "Eu...eu quero ir para o meu quarto."
    show erik 2
    show erikmom 19b
    erimom "Está tudo bem eu-"
    hide erik with dissolve
    show erikmom 19c
    show player 22
    erimom "..."
    show erikmom 20
    erimom "Escuta, isso que você viu é algo... normal!"
    show player 5
    show erikmom 19
    erimom "Ele é meu bebêzinho..."
    show erikmom 19c
    show player 10
    player_name "Está tudo bem, {b}Sra. Johnson{/b}."
    player_name "Eu não devia ter entrado assim..."
    show player 5
    pause
    show player 10
    player_name "Poderia dizer ao {b}Erik{/b} que me desculpo?"
    show player 5
    show erikmom 19
    erimom "Não se preocupe. Ele ficará bem..."
    erimom "É que... {b}Erik{/b} não fala muito com as garotas, então eu..."
    show player 11
    erimom "...Eu dei uma atenção especial para ele!"
    erimom "Eu pensei que poderia tirá-lo do seu computador se ele pudesse simplesmente... sentisse um pouco!"
    show erikmom 19c
    show player 5
    player_name "..."
    show erikmom 19
    erimom "Você poderia... sabe. Manter isso em segredo?"
    erimom "Eu não acho que ele gostaria que as outras crianças da escola descobrissem."
    show erikmom 19c
    show player 10
    player_name "Sem problemas, {b}Sra. Johnson{/b}. Não vou contar para ninguém."
    hide player
    hide erikmom
    with dissolve
    $ erik.complete_events(erik_breastfeeding)
    $ erik.add_event(erik_breastfeeding_2)
    $ erik_breastfeeding_2.finish()
    $ unlock_ui()
    $ callScreen(location_count)

label erik_funky_block:
    scene expression gTimer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "Cara... acho que tenho que deixar o Erik sozinho por um tempo."
    hide player with dissolve
    $ callScreen(location_count)

label mrsj_room_locked_dialogue:
    scene expression gTimer.image("erik_inside{}_b")
    show player 10 with dissolve
    player_name "Oops! Sra. Johnson deve ter deixado a porta dela aberta..."
    hide player with dissolve
    $ callScreen(location_count)

label mrsj_filled_block:
    scene expression gTimer.image("erik_inside{}_b")
    show player 10
    with dissolve
    player_name "Eu deveria deixar a {b}Sra. Johnson{/b} descansar."
    player_name "Além do mais, acho que não aguentaria duas aulas no mesmo dia..."
    hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
