label erik_button_dialogue:
    if not erik.known(erik_card_hunt):
        jump erik_card_hunt
    if erik.over(erik_crown_card) and not erik.known(erik_orcette):
        jump erik_orcette
    if is_here("june"):
        scene expression "backgrounds/location_erik_house_bedroom_bed_june.jpg" with hpunch
        player_name "!!!"
        $ location_count = "Erik's House Entrance"
        $ erik_funky = True
        jump erik_funky_block
    if location_count == "Erik's Basement":
        scene location_erik_basement01_closeup
    elif location_count == "Erik's Room":
        if erik.started(erik_gf):
            scene expression gTimer.image("erik_house_bedroom{}_b")
            show player 14
            with dissolve
            player_name "Ele parece tão feliz agora."
            show player 17
            player_name "Eu deveria contar as boas notícias para a {b}Sra. Johnson{/b}!"
            hide player with dissolve
            $ callScreen(location_count)

        elif erik.in_progress(erik_gf_stolen):
            scene expression gTimer.image("erik_house_bedroom{}_b")
            show player 10
            with dissolve
            player_name "Ele não está muito feliz..."
            player_name "Falo com ele amanhã."
            hide player with dissolve
            $ callScreen(location_count)
        scene expression gTimer.image("eriks_room{}_c")
    show player 2 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Eai {b}Erik{/b}!"
    show player 1 at left
    show erik 5 at right
    eri "Eai {b}[firstname]{/b}! O que quer?"
    label erik_talk:
        menu:
            "Cartas." if erik.started(erik_card_hunt):
                jump erik_cards

            "Cock Crown of Thorns." if erik.started(erik_crown_card):
                jump erik_crown_card

            "A encomenda." if erik.started(erik_orcette) or erik.started(erik_orcette_2):
                jump erik_package

            "Óculos VR." if erik.started(erik_vr):
                jump erik_vr_game

            "Educação sexual." if mrsj.started(mrsj_sex_ed):
                show erik 1 at right
                show player 12 at left
                player_name "O que sua mãe queria que fizéssemos??"
                show player 5
                show erik 5
                eri "Hmm... Eu acho que ela quer que nós compremos {b}pílulas anticoncepcionais{/b}."
                eri "E aquele livro... Aquele sobre posições sexuais..."
                show erik 1
                show player 35
                player_name "Ah sim, um livro tipo o {b}Kama Sutra{/b}?"
                show player 34
                show erik 5
                eri "Acho que sim."
                show erik 1
                show player 14
                player_name "Beleza."
                hide player
                hide erik
                with dissolve

            "Namorada." if June.completed(june_erik_help) and not erik.known(erik_gf):
                show player 14
                player_name "Cara, tenho ótimas notícias!"
                show player 1
                show erik 5
                eri "Huh?"
                show player 14
                show erik 1
                player_name "Então, falei com a {b}June{/b}..."
                show erik 4
                eri "Sério?"
                show player 14
                show erik 1
                player_name "Parece que ela gosta de jogar um jogo chamado Orc Bork..."
                player_name "... e ela procura alguém para jogar com ela!"
                show player 1
                show erik 4
                eri "Sério?"
                show player 17
                show erik 1
                player_name "Uhum!"
                show player 14
                player_name "Eu falei sobre você para ela!"
                player_name "Falei que você poderia ajudá-la a zerar o jogo que ela joga."
                show player 1
                show erik 4
                eri "Woah..."
                show erik 1
                show player 17
                player_name "Você devia ir para a escola e conversar com ela!"
                show player 1
                show erik 4
                eri "Sim... Eu deveria!"
                show player 14
                show erik 1
                player_name "De qualquer forma, vai dar tudo certo, pode apostar!"
                show player 1
                show erik 4
                eri "Valeu, [firstname]."
                show player 14
                show erik 1
                player_name "Até mais."
                hide player
                hide erik
                $ erik.add_event(erik_gf)

            "Namorada." if June.completed(june_mc_help) and not erik.known(erik_gf_stolen):
                show erik 1 at right
                show player 10 at left
                player_name "{b}Erik{/b}, sobre a {b}June{/b}..."
                show player 5
                show erik 5
                eri "O quê?"
                show player 10
                show erik 2
                player_name "Não acho que vá funcionar..."
                show player 5
                show erik 3b
                eri "Por quê? O que houve?"
                show player 10
                show erik 3c
                player_name "A gente conversou um pouco..."
                show player 5
                show erik 3
                eri "E?"
                show player 10
                show erik 3c
                player_name "E ela não parece estar interessada..."
                show player 5
                show erik 3
                eri "Oh..."
                show erik 3b
                eri "Está tudo bem."
                eri "Eu sabia que ela não iria querer mesmo..."
                show player 10
                show erik 3b
                player_name "Ela, uh... ela vai ir para minha casa mais tarde."
                show player 5
                show erik 5
                eri "O quê?!"
                show player 10
                show erik 3c
                player_name "Foi mal!"
                player_name "Enquanto eu estava falando com ela, um coisa levou a outra..."
                player_name "Nós vamos sair..."
                show player 5
                eri "..."
                player_name "..."
                show player 10
                player_name "Eu, humm, falo com você mais tarde, Erik."
                hide player
                hide erik
                with dissolve
                $ erik.add_event(erik_gf_stolen)
                $ erik_gf_stolen.finish()

            "Namorada." if June.completed(june_intro) and not June.known(june_intro_2):
                show player 14 at left
                show erik 1 at right
                player_name "Ei, quem é mesmo a menina que você gostava?"
                show erik 4
                show player 1
                eri "{b}June{/b}?"
                show player 14
                show erik 1
                player_name "Isso, por onde ela fica?"
                show player 1
                show erik 4
                eri "Geralmente ela fica na {b}escola{/b} na {b}sala de informática{/b} no segundo andar..."
                show player 14
                show erik 1
                player_name "Ah, entendi!"
                player_name "Vou ver o que consigo fazer."
                show player 1
                $ June.add_event(june_intro_2)
                jump erik_talk

            "Um recado do seu pai." if erik.started(erik_father_forgive):
                show erik 52 at right
                show player 10 at left
                player_name "Eu estava na delegacia..."
                show player 5
                show erik 5
                eri "Ah, sério?"
                show erik 52
                show player 10
                player_name "Vi seu pai."
                show player 11
                show erik 3b
                eri "Ugh. Não quero falar sobre ele..."
                show erik 52
                show player 10
                player_name "Ele ainda está preso, e ele me viu enquanto eu estava lá..."
                show player 5
                show erik 53
                eri "Sério? Ele falou algo pra você?"
                show erik 52
                show player 10
                player_name "Ele quer que você saiba que ele está arrependido de tudo..."
                player_name "...E, espero que você vai perdoá-lo e vocês voltem a se verem algum dia."
                show player 11
                show erik 2
                eri "..."
                show erik 3
                show player 5
                eri "Entendi..."
                show erik 3b
                show player 13
                eri "Valeu por me conta isso, {b}[firstname]{/b}."
                show erik 52
                show player 14
                player_name "Sem problemas, {b}Erik{/b}."
                hide player
                hide erik
                with dissolve
                $ erik_father_forgive.finish()

            "Sua mãe." if erik.over(erik_breastfeeding_2) and not erik.completed(erik_path_split):
                if mrsj.completed(mrsj_poker_night_2) and not erik.known(erik_path_split):
                    show player 14 at left
                    show erik 1 at right
                    player_name "Ei, lembra daquilo que fizemos com sua mãe depois do poker?"
                    show erik 3
                    show player 11
                    eri "Ah, sim..."
                    show erik 3b
                    eri "Espero que você não pense que minha mãe está louca ou qualquer coisa..."
                    show erik 1
                    show player 14
                    player_name "Não, claro que não!"
                    show player 17
                    player_name "Eu acho ela foda!"
                    show player 14
                    player_name "Mas... Eu só queria ter certeza de que você estava de boa em relação a isso, sabe?"
                    show erik 7
                    show player 1
                    eri "Tá de boa, sério."
                    show erik 5
                    eri "Ela sempre foi bem próxima a mim."
                    eri "Eu nunca fui muito próximo de outras garotas."
                    show player 4
                    eri "Eu acho que ela faz isso porque ela se sente mal por mim estar sozinho o tempo todo..."
                    show erik 1
                    show player 14
                    player_name "Que tal uma namroada?"
                    show erik 3
                    show player 11
                    eri "Quem iria namorar comigo?"
                    show erik 3b
                    eri "Sou muito ruim em conversar com as garotas..."
                    show erik 2
                    show player 5
                    eri "*suspiro*"
                    show player 14
                    player_name "Talvez alguém da escola tenha coisas em comum ou algo do tipo?"
                    show erik 3b
                    show player 1
                    eri "Acho que..."
                    show erik 1
                    show player 14
                    player_name "Ou você prefere fazer coisas com sua mãe??"
                    show erik 5
                    show player 1
                    eri "Tipo o quê?"
                    show erik 1
                    show player 14
                    player_name "Tipo... sexo? Você já pensou nisso?"
                    show erik 5
                    show player 1
                    eri "Acho que é mais fácil... ela sempre me deu muita atenção."
                    show erik 1
                    show player 14
                    player_name "Ah, é? Como assim?"
                    show erik 5
                    show player 11
                    eri "Tipo me tocar... Deixar eu tocar nela..."
                    eri "Tipo as coisas que fizemos depois do jogo de poker."
                    show erik 1
                    show player 10
                    player_name "Eu sabia que você estava mamando neal, mas eu não sabia ia além disso."
                    show erik 4
                    show player 11
                    eri "Acho que ela gosta."
                    show erik 1
                    show player 14
                    player_name "Você acha que ela faria mais coisas com a gente??"
                    show erik 5
                    show player 4
                    eri "Não sei... Talvez?"
                    show erik 1
                    show player 14
                    player_name "Podemos falar com sua mãe sobre isso?"
                    show erik 5
                    show player 1
                    eri "Acho que não..."
                    show erik 1
                    show player 14
                    player_name "Por quê não?"
                    player_name "Talvez ela queira..."
                    show erik 5
                    show player 1
                    eri "Talvez?"
                    show erik 1
                    show player 4
                    player_name "Hmm..."
                    show erik 4
                    show player 1
                    eri "Você acha que poderia falar com ela?"
                    show erik 1
                    show player 23
                    player_name "Eu?!"
                    show erik 4
                    show player 11
                    eri "Uhum!"
                    eri "É muito estranho que eu pergunte, sabe?"
                    show erik 1
                    show player 29
                    player_name "Vou ver o que ela vai dizer..."
                    show player 1
                    $ erik.add_event(erik_path_split)
                    jump erik_talk

                elif erik.started(erik_path_split):
                    show player 14 at left
                    show erik 1 at right
                    player_name "O que devo perguntar para a sua mãe mesmo?"
                    show erik 5
                    show player 1
                    eri "Descobrir se ela quer fazer mais coisas com a gente."
                    show player 14 at left
                    show erik 1
                    player_name "Ah, sim."
                    player_name "Vou te contar depois que conversar com ela."
                    show player 1
                    show erik 1
                    jump erik_talk
                else:

                    show erik 1 at right
                    show player 10 at left
                    player_name "Eu não sabia que você e sua mãe era assim... tão perto."
                    show player 5
                    show erik 3
                    eri "É estranho, eu sei..."
                    show erik 2 with dissolve
                    show player 12
                    player_name "Não, nem tanto!"
                    show player 10
                    player_name "Eu... eu acho legal!"
                    show player 13
                    show erik 3b with dissolve
                    eri "..."
                    show player 29 with dissolve
                    player_name "Tipo, sua mãe é... muito gostosa!"
                    player_name "Acho que você é um sortudo..."
                    show player 13 with dissolve
                    show erik 3
                    eri "Acho que sim."
                    show player 12
                    player_name "Você fazem... qualquer coisa juntos?"
                    show player 11
                    show erik 5
                    eri "...NÃO!!"
                    show erik 3
                    eri "Ela só me deixa, sabe, tocar ela..."
                    show erik 3b
                    show player 23
                    player_name "Sério?!"
                    player_name "Tipo... o corpo dela todo?"
                    show player 14
                    show erik 5
                    eri "Tipo isso."
                    show erik 50
                    show player 12
                    player_name "Você não gostsa?"
                    show player 13
                    show erik 5
                    eri "Claro que gosto!"
                    eri "Mas é que... é minha mãe, sabe?"
                    show erik 50
                    show player 33
                    player_name "Acho que sim."
                    show player 13
                    show erik 5
                    eri "Por favor...não conte para ninguém, ok?"
                    show erik 50
                    show player 14
                    player_name "{b}Erik{/b}, você é meu melhor amigo."
                    player_name "Vou manter isso só entre nós."
                    player_name "Eu só tava um pouco... surpreso, sabe?"
                    show player 13
                    show erik 5
                    eri "Valeu, {b}[firstname]{/b}. Você é um bom amigo."
                    hide player
                    hide erik
                    with dissolve

            "Comprei o jogo!" if erik.completed(erik_favor) and game in inventory.items and not erik.known(erik_favor_2):
                show erik 1 at right
                show player 17 at left
                player_name "Comprei o jogo!"
                show erik 4 at right
                show player 1 at left
                eri "Sério?"
                show erik 1 at right
                show player 33 at left
                player_name "Aqui, {b}Sea Dogs SAGA{/b}!"
                show player 239_240
                pause
                show erik 4 at right
                show player 72 at left
                eri "Nem fodendo!"
                show erik 8 at right
                show player 1 at left
                eri "Valeu, {b}[firstname]{/b}!"
                show erik 9 at right
                show player 14 at left
                player_name "Então... Você vai falar com o Kevin?"
                show erik 10 at right
                show player 1 at left
                eri "Sim. Vou tomar conta da cantina."
                show erik 9 at right
                show player 36 at left
                player_name "Ótimo! Valeu, {b}Erik{/b}!"
                $ inventory.items.remove(game)
                $ erik.add_event(erik_favor_2)
                jump erik_talk

            "Preciso de um favor." if erik.started(erik_favor):
                show erik 1 at right
                show player 29 at left
                player_name "Preciso de um favor!"
                show erik 5 at right
                show player 13 at left
                eri "Ah?"
                eri "Qual?"
                show erik 1 at right
                show player 14 at left
                player_name "Sabe o {b}Kevin{/b} da {b}escola{/b}?"
                show erik 5 at right
                show player 1 at left
                eri "Sei..."
                show erik 1 at right
                show player 17 at left
                player_name "OK, bem. Ele estará cuidando da cantina por mais dois meses..."
                player_name "...E ele precisa de um substituto."
                show erik 2 at right
                show player 11 at left
                eri "Ugh. Eu {b}ODEIO{/b} trabalhar na cantina..."
                show erik 3 at right
                show player 10 at left
                player_name "Você não precisa fazer isso..."
                show player 14 at left
                player_name "...Mas se você fizer, farei qualquer coisa que você quiser!"
                player_name "Você quer algo?"
                show erik 1 at right
                show player 1 at left
                eri "Hmm..."
                show erik 4 at right
                show player 11 at left
                eri "Você poderia me comprar esse novo jogo que acabou de sair..."
                show erik 1 at right
                show player 2 at left
                player_name "Qual o nome?"
                show erik 4 at right
                show player 1 at left
                eri "O nome é: {b}Sea Dogs SAGA{/b}"
                eri "...vende na {b}COSMIC CUMICS{/b}..."
                show erik 1 at right
                show player 18 at left
                player_name "Beleza! Se eu comprar, você faria isso pra mim?"
                show erik 3 at right
                show player 2 at left
                eri "Sim... Eu acho."
                show erik 1 at right
                show player 14 at left
                player_name "Valeu!!!"
                $ erik_favor.finish()
                jump erik_talk
            "Onde sua mãe está?":

                show erik 1 at right
                show player 35 at left
                player_name "Onde sua mãe está?"
                show erik 5 at right
                show player 34 at left
                eri "Minha mãe? ...Eh, está em casa, exceto durante a tarde.."
                show player 1 at left
                show erik 1 at right
                show player 14 at left
                player_name "Ah, entendi."
                jump erik_talk
            "Nada.":

                show erik 1 at right
                show player 2 at left
                player_name "Ah, nada."
                show player 17 at left
                player_name "Apenas passando pra dizer oi!"
                show erik 5 at right
                show player 1 at left
                eri "Tá tudo certo na sua casa com a sua família?"
                show erik 1 at right
                show player 10 at left
                player_name "{b}[mom_name]'s{/b} está recebendo {b}ligações estranhas{/b} mas ela diz que está tudo bem, então..."
                show player 24 at left
                player_name "Acho que ficaremos bem..."
                show erik 5 at right
                show player 13 at left
                eri "Isso é estranho..."
                show erik 5 at right
                show player 24 at left
                player_name "É, eu sei..."
                show player 36 at left
                player_name "Que seja, vou indo."
                show erik 7 at right
                eri "Beleza, até mais!"
                hide player 36 at left with dissolve
                hide erik 7 at right with dissolve
                hide erik_indoors

            "Preciso da sua ajuda." if webcam_quest and not erik_helped_with_camera:
                show player 29 at left
                show erik 1 at right
                player_name "Preciso de uma ajudinha hoje a noite..."
                show erik 5
                eri "Ah é? Qual?"
                show player 21
                show erik 1
                player_name "Vai parecer um pouco estranho, mas eu preciso de ajuda para entrar na escola esta noite..."
                show player 13
                show erik 5
                eri "O quê?"
                eri "...Mas por quê?"
                show player 10
                show erik 1
                player_name "Tudo o que você precisa saber é que você me ajude a entrar na escola..."
                show player 108f
                player_name "...E não pode dar errado, eu preciso muito fazer isso."
                show player 5
                show erik 3
                eri "Hmm..."
                eri "Sei lá... Parece encrenca."
                show player 10
                show erik 1
                player_name "Por favor!"
                show player 13
                show erik 5
                eri "Acho que posso ajudar..."
                show player 17
                show erik 1
                player_name "Valeu!!!"
                show player 14
                player_name "Certo, me encontre na escola hoje a noite!"
                show player 1
                show erik 4
                eri "Ok."
                $ webcam_erik_help = True
                hide erik
                hide player
        $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
