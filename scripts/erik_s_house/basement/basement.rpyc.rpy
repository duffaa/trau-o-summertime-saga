label erik_basement:
    $ location_count = "Erik's Basement"
    if erik.completed(erik_bullying_3) and not erik.known(erik_vr):
        jump erik_vr
    elif not erik_basement_seen:
        $ poker_table_seen = False
        $ cabinet_seen = False
        scene erik_basement
        show player 14 at left with dissolve
        show erik 1 at right with dissolve
        player_name "Caaraaaa! Esse lugar é do caralho!"
        player_name "Por que você nunca me mostrou antes?"
        show player 1
        show erik 4
        eri "Tinha meus motivos."
        eri "E, bom... Meu pai não queria que eu trouxesse alguém aqui."
        show erik 14
        eri "Alguma coisa sobre isso não me parecia bom..."
        show erik 4
        eri "Mas eu não preciso me preocupar mais com isso!"
        show erik 1
        show player 14
        player_name "Posso dar uma olhada ao redor?"
        show erik 1
        show player 1
        eri "Sinta-se livre."
        show erik 1
        show player 14
        player_name "Legal!"
        show player 1
        show erik 5
        eri "Mas... seja cuidadoso e não quebre nada."
        eri "É a única coisa que me faz lembrar do meu pai..."
        show erik 1
        show player 14
        player_name "Prometo que vou ser cuidadoso."
        hide player with dissolve
        hide erik with dissolve
        $ erik_basement_seen = True
    $ callScreen(location_count)

label poker_table:
    scene erik_basement
    if not poker_table_seen:
        show player 14 at left with dissolve
        show erik 1 at right with dissolve
        player_name "Você tem uma {b}mesa de poker{/b} aqui?"
        show player 1
        show erik 4
        eri "Sim. quer jogar?"
        $ poker_table_seen = True
        menu:
            "Jogar poker com o Erik?"
            "Sim":
                player_name "Queria, mas nunca joguei antes..."
                show player 14
                eri "Está tudo bem, eu explico as regras."
                show player 1
                show erik 4
                player_name "Sendo assim, vamos jogar!"
                show player 14
                show erik 1

                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                $ callScreen(location_count)
            "Não":

                player_name "Talvez outra hora, cara. Não estou com muita vontade hoje."
                show player 14
                show erik 1
                eri "Beleza. Sem problemas."
                show player 1
                show erik 4
                hide player
                hide erik
    else:

        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "Vamos jogar poker!"
        show player 1
        show erik 5
        eri "Acho que podemos tentar..."
        eri "Mas não precisamos de outra pessoa?"
        show erik 1
        show player 4
        player_name "Hmm..."
        player_name "Sim. Tem razão."
        player_name "Temos que {b}achar alguém{/b} que quer jogar conosco."
        hide erik
        hide player
        with dissolve
    $ callScreen(location_count)

label mrsj_poker:
    if poker_bot02 == "erik_mom" and not poker_drunk:
        scene erik_basement_c
        show erikmom 19 at right with fastdissolve
        show erik 1f at Position(xpos=300,ypos=768) with fastdissolve
        show player 1 at left with dissolve
        erimom "Vocês garotos não estão planejando jogar assim, estão?"
        show player 11
        show erikmom 14
        player_name "..."
        show player 10
        player_name "Como assim?"
        show player 11
        show erikmom 18
        erimom "Não se pode jogar poker sem uma boa bebida!"
        show erikmom 14
        show player 1
        show erik 4f
        eri "Uma bebida?"
        show erik 1f
        show erikmom 18
        erimom "Vamos ver o que sobrou na {b}adega{/b}, ok?"
        hide player
        hide erikmom
        hide erik
        with dissolve

    elif poker_bot02 == "erik_mom" and poker_drunk:
        scene poker_table
        show erikmompoker 2 zorder 1 at Position(xpos=857,ypos=626)
        show erikmompokerc1 7 zorder 2 at Position(xpos=815,ypos=584)
        show erikmompokerc2 8 zorder 2 at Position(xpos=910,ypos=387)
        show erikpoker 1 zorder 1 at Position(xpos=153,ypos=626)
        show erikpokerc 9 zorder 2 at Position(xpos=144,ypos=592)
        with fade

        erimom "Então..."
        erimom "Vamos jogar {b}Omaha{/b}, ou {b}Texas Hold'em{/b}?"
        show erikmompoker 1
        player_name "..."
        player_name "Só conhecemos {b}Strip poker{/b}..."
        show erikmompoker 2
        erimom "Ha ha! Vocês estão brincando?"
        show erikmompoker 10 at Position(xpos=856,ypos=627)
        player_name "É a única coisa que as pessoas da escola jogam..."
        show erikpoker 2
        eri "Você não precisa... {b}mãe{/b}."
        show erikpoker 11
        show erikmompoker 9 at Position(xpos=856,ypos=627)
        erimom "Eu aceito!"
        show erikmompoker 4 at Position(xpos=857,ypos=626)
        erimom "Sua mãe não é uma santa. Ela também pode se divertir!"
        show erikmompoker 2
        erimom "Costumava jogar poker antigamente..."
        show erikmompoker 5
        erimom "...E eu era a {b}melhor{/b} nisso!"
        show erikpoker 12
        show erikmompoker 1
        eri "Então, o que faremos agora?"
        show erikpoker 1
        menu mrsj_poker_repeat:
            "Jogar.":
                show erikmompoker 10 at Position(xpos=856,ypos=627)
                show erikpoker 1
                player_name "Vamos jogar!!"
                jump start_poker
            "Como jogar.":

                player_name "Me lembrem de novo, como se joga poker?"
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished at truecenter with dissolve
                jump mrsj_poker_repeat

            "Skip Mini-Game (Cheat)" if cheat_mode:
                menu:
                    "Mrs. Johnson Loses":
                        jump mrsj_lost
                    "Erik Loses":
                        jump erik_lost
                    "[firstname] Loses":
                        jump player_lost
    $ callScreen(location_count)

label cabinet:
    scene erik_basement_cabinet
    if poker_bot02 == "":
        show erik 1 at right
        show player 14 at left
        with dissolve
        player_name "Isso é muito alcool..."
        show player 1
        show erik 4
        eri "Sim, meu pai era cheio disso."
        show erik 1
        show player 14
        player_name "Deveriamos tomar?"
        show player 1
        show erik 4
        eri "Talvez em uma ocasião especial?"
        show erik 1
        show player 4
        player_name "Tem razão."
        player_name "Deveriamos {b}achar alguém{/b} que queira beber conosco."
        hide erik
        hide player
        with dissolve

    elif poker_bot02 == "erik_mom":
        if mrsj.completed(mrsj_poker_night_2):
            show erik 4f at Position(xpos=300)
            show player 1 at left
            show erikmom 14 at right
            with dissolve
            eri "Vou procurar o whiskey!"
            show erik 1f
            show erikmom 19
            show player 11
            erimom "Oh, vocês tem certeza disso?"
            show erikmom 19c
            show player 10
            player_name "Disso o que?"
            show erikmom 19
            show player 11
            erimom "O alcool, vocês se lembram do que aconteceu na última vez, né?"
            show erikmom 19c
            show erik 5f
            eri "Mas nos divertimos, não?"
            show erik 1f
            pause
            show erikmom 14 with fastdissolve
            pause
            show erikmom 17
            show player 1
            erimom "Tem razão..."
            show erikmom 18
            erimom "Oh, se foda, vamos lá!"
        else:

            show erik 5f at Position(xpos=300,ypos=768)
            show player 1 at left
            show erikmom 14 at right
            with dissolve
            eri "Whiskey..."
            eri "Whiskey... whiskey..."
            eri "Whiskey... whiskey... whiskey..."
            eri "Não tem nada além de whiskey aqui..."
            show erik 1f
            show erikmom 17
            erimom "Sua pai só bebia whiskey."
            show erikmom 14
            show player 14
            player_name "Sem problemas!"
            player_name "Vamos usar o que tiver, ha ha!"
            show erik 15
            show player 1
            eri "Deveriamos testar antes de começar a jogar?"
            show erik 16
            show erikmom 22
            erimom "Vamos ver como é o gosto..."
            show erik 20
            show erikmom 21
            show player 185
            with fastdissolve
            eri "Aqui vamos nós..."
            show player 186
            show erik 17
            player_name "Saúde!"
            show player 189
            show erik 19
            show erikmom 25
            with fastdissolve

            pause
            show erikmom 26
            show erik 17
            show player 190
            with fastdissolve
            pause
            show player 191
            player_name "Ugh!!"
            show player 188
            show erikmom 24
            show erik 17
            erimom "Woaa.."
            show erik 20
            show erikmom 14
            eri "Hmm... Não é ruim!"
            show erik 17
            player_name "..."
            show player 187
            player_name "Você gostou disso?!"
            show player 188
            show erik 20
            eri "Yeah, é um pouco doce."
            show player 185
            show erik 17
            show erikmom 18
            erimom "Certo, garotos, vamos começar o jogo!"
        hide erikmom
        hide erik
        hide player
        with dissolve
        $ poker_drunk = True
    $ callScreen(location_count)

label mrsj_afterpoker_fun_block:
    scene erik_basement
    show player 11 at left
    show erik 4 at right
    with dissolve
    eri "Achei que *Hic* iriamos para os fundos..."
    eri "Minha mãe está nos esperando, lembra?"
    show player 14
    show erik 1
    player_name "Oh, ceeeerto!"
    player_name "Vamos lá ver o que ela quer."
    show player 1
    show erik 4
    eri "Con-*Hic*cordo."
    hide erik
    hide player
    with dissolve
    $ callScreen(location_count)

label erik_vr:
    scene location_erik_basement01_closeup
    show erik 15f at right
    show player 13 at left
    with dissolve
    eri "Eae, {b}[firstname]{/b}."
    show erik 15bf
    show player 14
    player_name "Eae!"
    show player 11
    player_name "..."
    show player 12
    player_name "Você está... bebendo?"
    show player 11
    show erik 15f
    eri "Oh, minha mãe quis que eu limpasse aqui."
    eri "Então estou pegando as coisas do papai e jogando as coisas."
    show erik 15bf
    pause
    show player 38 with dissolve
    player_name "!!!" with hpunch
    show player 23 with dissolve
    player_name "Espera!"
    player_name "Não percebesse?"
    show player 18
    show erik 15f
    eri "Huh?"
    show erik 15bf
    show player 14
    player_name "Podemos usar isso tudo!!"
    show player 13
    show erik 5 with dissolve
    eri "Pra que?"
    show erik 3b
    show player 17
    player_name "Bom, tenho uma ideia."
    show player 14
    player_name "E se colocarmos essa bebida para ser útil!"
    show player 17
    player_name "Digo, é uma vergonha desperdiçar isso tudo..."
    show player 13
    show erik 5
    eri "Hmmm.... Sim, eu acho."
    show erik 3b
    show player 14
    player_name "E se trouxessemos alguém da escola e... nos divertissemos!"
    show player 33
    player_name "Esse lugar é perfeito para festas!"
    show player 14
    player_name "Acho que, nós podemos convidar uma garota, jogar poker, e ficarmos bêbados!"
    show player 13
    show erik 5
    eri "Não sei."
    eri "Minha mãe pode ficar puta se as coisas saírem do controle..."
    show erik 3b
    show player 12
    player_name "Vamos, {b}Erik{/b}... Esse lugar é perfeito!"
    show player 14
    player_name "Pense nas coisas que podemos fazer!"
    show player 33
    player_name "Podemos convidar garotas para jogar strip poker..."
    show player 18
    show erik 4 with hpunch
    eri "!!!"
    eri "Não sei, {b}[firstname]{/b}..."
    show erik 1
    show player 30
    player_name "Hmm..."
    pause
    show player 12
    player_name "E se trouxessemos algo que você sempre quis?"
    player_name "Você me deixaria convidar pessoas?"
    show player 14
    player_name "Estou ganhando dinheiro! Posso te ajudar com qualquer coisa..."
    show player 13
    eri "..."
    show erik 4
    eri "Bom, tem algo que eu sempre quis... mas isso é MUITO caro!"
    show erik 1
    show player 14
    player_name "É? E o que é?"
    show player 13
    show erik 4
    eri "Na {b}Cosmic Cumics{/b}, vi que eles estão vendo um Óculos de realidade virtual, {b}Virtual Saga X{/b}."
    show erik 1
    show player 17
    player_name "Entendi!"
    show player 13
    show erik 5
    eri "Sério?!"
    eri "Mas, espera! Eu... Eu quero um jogo dele também."
    show erik 4
    eri "Se chama... {b}World of Orcette{/b}."
    show erik 1
    show player 11
    player_name "..."
    show player 12
    player_name "É aquele daqueles jogos vulgares sobre-"
    show player 5
    show erik 5b
    eri "Uhh!!"
    show erik 5
    eri "Que seja!"
    show erik 4
    eri "Acho que eles fazer, eu acho!"
    eri "Você consegue comprar na {b}Cosmic Cumics{/b}, no shopping."
    show erik 1
    show player 14
    player_name "Certo."
    player_name "Trato feito!"
    hide player
    hide erik
    with dissolve
    $ erik.add_event(erik_vr)
    $ callScreen(location_count)

label erik_card_hunt:
    scene location_erik_basement01_closeup
    show player 13 at left
    show erik 4 at right
    with dissolve
    eri "Oi, {b}[firstname]{/b}."
    show erik 1
    show player 14
    player_name "Eae, {b}Erik{/b}."
    show player 2
    player_name "Pensei em parar e ver o que você está fazendo."
    show player 1
    show erik 5
    eri "Ah, só tô procurando pelas minhas cartas do {b}Magic the Fappening{/b}."
    eri "Preciso me preparar para o próximo torneio, mas não sei onde deixei..."
    show erik 1
    show player 14
    player_name "Ah é?"
    show player 13
    show erik 5
    eri "Geralmente deixo no porão, mas eles não estão aqui."
    show erik 1
    show player 12
    player_name "Hmm..."
    player_name "Posso te ajudar a achar. Eles não devem estar muito longe."
    show player 13
    show erik 5
    eri "Eles devem estar aqui."
    eri "Achei que a mãe tinha tirado eles daqui mas..."
    show erik 1
    show player 14
    player_name "Ah sim: Ela saiu."
    show player 17
    player_name "Ela disse que só voltaria no janta."
    show player 5
    show erik 5
    eri "Merda. Sinto falta dela."
    eri "Talvez eu tenha deixado lá em cima."
    eri "Você procura aqui em baixo, e eu procuro lá em cima, aceita?"
    show erik 1
    show player 14
    player_name "Claro."
    show player 5

    hide erik with dissolve
    show player 4
    player_name "( Estou pensando onde ele pode ter deixaod essas cartas. )"
    show player 12
    player_name "( Deve estar em algum lugar aqui em baixo... )"
    hide player with dissolve
    $ erik.add_event(erik_card_hunt)
    $ callScreen(location_count)

label erik_orcette:
    scene location_erik_basement01_closeup
    show erik 1 at right
    show player 14 at left
    with dissolve
    player_name "No porão de novo?"
    player_name "O que está fazendo?"
    show player 13
    show erik 5
    eri "Eae, {b}[firstname]{/b}!"
    eri "Tô pensando em vender a mesa de poker do papai..."
    show erik 1
    show player 23
    player_name "O quê?!"
    show player 30
    player_name "Por quê!"
    show player 12
    player_name "A mesa é tão legal!"
    show player 5
    show erik 3b
    eri "..."
    show player 10
    player_name "Quero dizer, essa coisa é feita de uma madeira boa! O seu pai não disse que ele tinha feito isso?"
    show player 11
    show erik 5
    eri "Sim... mas nós não usamos."
    eri "E eu poderia usar o dinheiro."
    show erik 3b
    show player 12
    player_name "Sim, mas sua mãe está de acordo com isso?"
    show player 11
    show erik 5
    eri "Provavelmente não, mas eu tenho que arrumar grana para... algo."
    show erik 3b
    show player 12
    player_name "Vai, {b}Erik{/b}. Achei que todas esssas coisas aqui faziam você lembrar do seu pai."
    player_name "O que é tão importante que está fazendo você pensar em vender isso?"
    show player 5
    show erik 3
    eri "Bom..."
    show erik 5
    eri "É um pouco pessoal."
    show erik 3b
    show player 26
    player_name "Ah, qual foi."
    pause
    show player 14
    player_name "Certo! Eu compro o item se você me contar."
    show player 30
    player_name "Aceita?"
    show player 5
    eri "..."
    show erik 4
    eri "Por que você faria isso?"
    show erik 1
    show player 43
    player_name "Tenho uns planos para o porão!"
    show player 14
    player_name "Acho que podemos passar um tempo aqui... E talvez... convidar pessoas!"
    show player 13
    show erik 4
    eri "Certo..."
    show erik 5
    eri "Mas prometa que você não vai me zoar?"
    show erik 3b
    show player 12
    player_name "Ehh... Claro?"
    show player 5
    eri "..."
    show erik 5
    eri "Vocẽ só pode comprar esssa coisa na internet..."
    eri "Então, se seu computador ainda estiver com problemas, você precisaá consertar primeiro."
    show erik 1
    show player 12
    player_name "O que eu tenho que comprar, {b}Erik{/b}?"
    show player 5
    eri "..."
    show erik 4
    eri "Já ouviu falar do {b}Orcette{/b}?"
    show erik 1
    pause
    show player 10
    player_name "O o quê?"
    show player 11
    show erik 5
    eri "É tipo um... um tubo... de borracha?"
    show erik 1
    show player 12
    player_name "O quê?"
    show player 11
    show erik 5
    eri "E é verde!"
    show erik 1
    show player 14
    player_name "Espera... É um brinquedo sexual?!"
    show player 13
    show erik 5
    eri "Ei, você prometeu!"
    show erik 3
    show player 17
    player_name "Certo. Certo."
    show player 26
    player_name "Então, você quer um desses, né?"
    show player 13
    show erik 5
    eri "Não sei, sempre quis, mas..."
    show erik 3
    show player 14
    player_name "Mas o quê?"
    show player 13
    show erik 5
    eri "Não posso deixar minha mãe ver essa encomenda..."
    eri "...Então você têm que entregar na sua casa!"
    show erik 1
    show player 12
    player_name "E se minha mã ver?"
    show player 10
    player_name "Ou minha irmã!"
    show player 11
    show erik 5
    eri "Você só precisa rastrear e ver quandovai chegar."
    show erik 1
    show player 12
    player_name "O quê?"
    show player 11
    show erik 5
    eri "Basta ver sua caixa postal assim que o correio chegar no dia da entrega."
    show erik 4
    eri "O pacote nunca entrará na sua casa!"
    show erik 1
    show player 12
    player_name "Certo. Vou ver o que posso fazer."
    show player 5
    show erik 4
    eri "Valeu, {b}[firstname]{/b}. Vocẽ é foda!"
    show erik 1
    show player 14
    player_name "Certo. Certo."

    hide erik with dissolve
    show player 12
    player_name "( Acho que deveria ir no meu computador para comprar o {b}Orcette{/b}... )"
    hide player with dissolve
    $ erik.add_event(erik_orcette)
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
