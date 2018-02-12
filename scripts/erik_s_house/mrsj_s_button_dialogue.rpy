label mrsj_button_dialogue:
    if location_count == "Erik's House Entrance":
        scene expression gTimer.image("erik_entrance{}_c")
    elif location_count == "Mrs Johnson's Room":
        if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
            scene erik_upstairs_night_c
            show erikmom 42 at right
            show player 11 zorder 2 at left
            show erik 1f zorder 1 at Position(xpos=300)
            with dissolve
            erimom "Olá, meninos..."
            show erikmom 41
            show player 21
            player_name "O-olá, {b}Sra. Johnson{/b}!"
            show player 13
            show erik 4f
            eri "Você está... muito bonita, mãe."
            show erik 1f
            show erikmom 40b with fastdissolve
            erimom "Vão continuar olhando pra mim ou querem me perguntar algo??"
            show erikmom 39
            jump mrsj_button_dialogue_repeat

        elif gTimer.is_dark() and erik.over(erik_gf):
            scene erik_upstairs_night_c2
            show erikmom 54 at Position(xpos=734,ypos=650)
            show player 433 zorder 2 at left
            with dissolve
            erimom "Olá, {b}[firstname]{/b}..."
            show erikmom 53
            player_name "!!!"
            show erikmom 54
            erimom "Tem algo de errado?"
            show player 435
            show erikmom 53
            player_name "Sabe.. você está pelada, {b}Sra. Johnson{/b}."
            show player 434
            show erikmom 54
            erimom "Eu gosto de me sentir... confortável no meu quarto..."
            erimom "Você não queria me perguntar algo?"
            show erikmom 53
            jump mrsj_button_dialogue_repeat
        scene erik_house_upstairs_n_c01
    show player 14 at left
    show erikmom 14 at right
    with dissolve
    player_name "Oi, {b}Sra. Johnson{/b}!"
    show player 1
    show erikmom 17
    erimom "Eai, {b}[firstname]{/b}!"
    erimom "Como você está?"
    show player 14
    show erikmom 14
    player_name "Estou bem, valeu!"
    show player 1
    show erikmom 17
    erimom "Tem algo que eu possa fazer por você?"
    show erikmom 14
    menu mrsj_button_dialogue_repeat:
        "Sobre o {b}Erik{/b}." if erik.started(erik_path_split):
            $ callScreen("Route Warning", False, False)
            show player 14 at left
            show erikmom 14 at right
            player_name "Quero falar sobre o {b}Erik{/b}..."
            show player 1
            show erikmom 19
            erimom "Ah, ele está bem?"
            show player 14
            show erikmom 19c
            player_name "Sim, ele está bem."
            player_name "Eu estava falando com ele sobre o que aconteceu na outra noite..."
            show player 11
            show erikmom 19
            erimom "Ele está chateado?"
            show player 14
            show erikmom 19c
            player_name "Não, nem um pouco."
            show player 10
            player_name "Ele só não tem certeza do que ele quer..."
            show player 11
            show erikmom 19
            erimom "Como assim?"
            show player 10
            show erikmom 19c
            player_name "Eu acho que ele desistiu de falar com outras meninas."
            player_name "Eu poderia tentar ajudá-lo a encontrar uma namorada, mas acho que ele gosta mais de você..."
            show player 13
            show erikmom 19
            erimom "Oh meu..."
            show erikmom 20
            erimom "Eu protegi ele demais?"
            show erikmom 19
            erimom "O que eu deveria fazer?"
            show erikmom 19c
            menu mrsj_route_split:
                "Educação sexual.":
                    show player 14 at left
                    show erikmom 19c at right
                    player_name "Eu acho melhor se você lhe der a atenção que ele precisa..."
                    show erikmom 19
                    show player 1
                    erimom "Você acha?"
                    show erikmom 19c
                    show player 14
                    player_name "Não que ele queira outras mulheres..."
                    player_name "... E ele gosta muito de você!"
                    show erikmom 19
                    show player 1
                    erimom "Ele sempre foi muito próximo a mim..."
                    show erikmom 19c
                    show player 14
                    player_name "Foi muito bom na outra noite!"
                    player_name "Eu nunca tinha visto o {b}Erik{/b} tão feliz."
                    show erikmom 19
                    show player 11
                    erimom "Você acha... que vocês, garotos, gostariam de mais desse tipo de... atenção?"
                    show erikmom 19c
                    show player 21
                    player_name "Eu...Eu acho que sim!"
                    show erikmom 20
                    show player 13
                    erimom "Se nenhuma das meninas da escola darem a atenção que ele precisa..."
                    show erikmom 19
                    erimom "...Eu devesse ser a única?"
                    show erikmom 14
                    show player 14
                    player_name "Acho que ele gostaria."
                    show erikmom 49
                    show player 11
                    erimom "E se eu der uma...educação sexual especial para vocês?"
                    show erikmom 50
                    player_name "!!!" with vpunch
                    show erikmom 49
                    erimom "É apenas para fins educativos, é claro..."
                    show erikmom 50
                    show player 29
                    player_name "Oh, Eu emm... Eu não me importaria!"
                    show erikmom 49
                    show player 13
                    erimom "Eu teria que pensar sobre isso primeiro, no entanto."
                    show erikmom 50
                    show player 14
                    player_name "Sem problemas, {b}Sra. Johnson{/b}!"
                    show erikmom 14
                    show player 1
                    $ erik_path_split.finish()
                    $ erik.add_event(erik_sex_ed)
                    jump mrsj_button_dialogue_repeat
                "Arranjar uma namorada.":

                    show player 14 at left
                    show erikmom 19c
                    player_name "Acho que devemos arranjar uma namorada para ele."
                    show player 1
                    show erikmom 19
                    erimom "Você acha?"
                    show player 14
                    show erikmom 19c
                    player_name "Acho que ele ficará mais feliz..."
                    player_name "... e isso aumentaria sua confiança!"
                    show player 1
                    show erikmom 20
                    erimom "Ele precisa sair mais mesmo..."
                    show player 10
                    show erikmom 19c
                    player_name "Não me entenda mal, nos divertimos muito na outra noite..."
                    show player 14
                    player_name "... Mas acho que {b}Erik{/b} precisa encontrar outras mulheres."
                    show player 13
                    show erikmom 20
                    erimom "Tem razão..."
                    show player 11
                    show erikmom 19
                    erimom "Mas e... eu?"
                    show player 10
                    show erikmom 19c
                    player_name "Como assim?"
                    show player 11
                    show erikmom 19
                    erimom "Bom..."
                    erimom "Se o {b}Erik{/b} achar uma namorada... O que eu farei?"
                    show erikmom 20
                    erimom "Não terei ninguém me dando atenção..."
                    show player 21
                    show erikmom 19c
                    player_name "Hummm, tenho certeza que você encontrará alguém {b}Sra. Johnson{/b}!"
                    show erikmom 14
                    player_name "Você é muito... bonita, e gostosa!"
                    show player 13
                    show erikmom 17
                    erimom "Aww, obrigada."
                    show erikmom 50
                    erimom "Hmm..."
                    show erikmom 49
                    show player 1
                    erimom "Tenho uma ideia!"
                    erimom "E se você me der essa atenção..."
                    show player 11
                    erimom "... e eu dê para {b}você{/b}?"
                    show erikmom 50
                    player_name "!!!" with vpunch
                    show erikmom 49
                    erimom "O quê foi?"
                    erimom "Só se você quisesse, quer dizer..."
                    show player 21
                    show erikmom 50
                    player_name "E-eu não me importaria!"
                    player_name "Mas, só se {b}Erik{/b} concordasse com isso."
                    show player 1
                    show erikmom 49
                    erimom "Pergunte a ele!"
                    erimom "Tenho certeza que ele concordará..."
                    show player 13
                    erimom "... Ainda mais se ele estiver muito ocupado 'brincando' com a outra garota. Ha ha."
                    show player 29
                    show erikmom 50
                    player_name "Acho que sim, ha ha."
                    show player 14
                    player_name "Vou tentar achar alguém para ele..."
                    show player 13
                    show erikmom 49
                    erimom "Volte e me avise o que aconteceu."
                    show player 17
                    show erikmom 50
                    player_name "Beleza, {b}Sra. Johnson{/b}!"
                    show erikmom 14
                    show player 1
                    $ erik_path_split.finish()
                    $ June.add_event(june_intro)
                    jump mrsj_button_dialogue_repeat

        "Educação sexual." if mrsj.started(mrsj_sex_ed):
            show erikmom 14 at right
            show player 10 at left
            player_name "Como podemos ajudá-la a se preparar para a educação sexual?"
            show player 5
            show erikmom 17
            erimom "Preciso de um bom livro, tipo o {b}Kama Sutra{/b}."
            erimom "E algumas {b}pílulas anticoncepcional{/b}!"
            show erikmom 49
            erimom "Cuidado nunca é de mais..."
            show erikmom 50
            show player 14
            player_name "Beleza."
            player_name "Vou tentar achar..."
            hide player
            hide erikmom
            with dissolve

        "Educação sexual." if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
            jump mrsj_3some

        "Aula de yoga privado." if gTimer.is_dark() and erik.over(erik_gf):
            jump mrsj_private_yoga

        "Namorada." if erik.started(erik_gf):
            show player 14
            player_name "Acho que consegui uma namorada para o {b}Erik{/b} na escola!"
            show player 1
            show erikmom 17
            erimom "Sério?!"
            show player 14
            show erikmom 14
            player_name "Uhum!"
            player_name "Eles têm muito em comum, seriam perfeitos um para o outro!"
            show erikmom 17
            show player 17
            player_name "Eu acho que vai funcionar, com certeza!"
            show player 1
            show erikmom 18
            erimom "Isso é ótimo!!"
            show erikmom 17
            erimom "Não acreditar que você tenha sido tão legal com meu filho."
            show erikmom 49
            erimom "Acho que é hora de você ter uma recompensa..."
            show player 21
            show erikmom 50
            player_name "Uma... Uma recompensa?"
            show player 11
            show erikmom 49
            erimom "E se eu te der uma... aula {b}privada{/b} de yoga..."
            erimom "Aquelas que você não vê na academia."
            show erikmom 50
            show player 21
            player_name "Seria ótimo, {b}Sra. Johnson{/b}!"
            show player 13
            show erikmom 49
            erimom "Venha me ver de noite no meu quarto... tenha certeza de que você esteja descansado!"
            show player 11
            erimom "Isso pode ser... meio cansativo."
            show player 21
            show erikmom 50
            player_name "S-sim, {b}Sra. Johnson{/b}."
            show player 13
            show erikmom 49
            erimom "Até mais tarde, vou estar esperando!"
            hide player
            hide erikmom
            with dissolve
            $ erik_gf.finish()
            jump erik_house_dialogue

        "Namorada." if erik.in_progress(erik_gf_stolen):
            show erikmom 19c at right
            show player 10 at left
            player_name "Eu não acho que vai funcionar com June..."
            show player 11
            show erikmom 19
            erimom "A garota da escola?"
            show player 10
            show erikmom 19c
            player_name "É."
            show player 5
            show erikmom 19
            erimom "Que pena..."
            erimom "O que houve?"
            show player 10
            show erikmom 19c
            player_name "Ela não está interessada, e..."
            show erikmom 51
            player_name "... ela pode está vindo para minha casa mais tarde para passar um tempo comigo."
            show player 5
            show erikmom 52
            erimom "Meu deus..."
            erimom "Erik está bem?"
            show player 10
            show erikmom 51
            player_name "Não sei... Provavelmente não."
            show player 5
            show erikmom 52
            erimom "Tenho que falar... Estou bem desapontada com você, {b}[firstname]{/b}."
            show erikmom 51
            player_name "..."
            show erikmom 52
            erimom "Você sabia que o {b}Erik{/b} gostava dela..."
            erimom "... Eu pensei que ele fosse seu amigo!"
            show player 10
            show erikmom 51
            player_name "Desculpa, {b}Sra. Johnson{/b}."
            player_name "Vou para casa agora."
            hide erikmom
            hide player
            jump erik_house_dialogue

        "Namorada." if June.started(june_intro_2):
            show player 14
            player_name "Tem essa garota na escola que eu acho o {b}Erik{/b} gostsa."
            show player 1
            show erikmom 17
            erimom "Sério?"
            show erikmom 18
            erimom "Isso é muito bom!"
            show erikmom 17
            erimom "Você conhece ela? Como ela é?!"
            show erikmom 14
            show player 14
            player_name "Não, Ainda não falei com ela."
            player_name "Ela é de outra turma, eu acho."
            show erikmom 17
            show player 1
            erimom "Ah, entendi."
            show player 11
            erimom "O {b}Erik{/b} fala com ela?"
            show erikmom 14
            show player 10
            player_name "Acho que não... Ele diz que é muito tímido."
            player_name "Eu disse a ele que iria descobrir mais sobre ela e falaria pra ele."
            show erikmom 18
            show player 13
            erimom "Você é tão bom!!"
            show erikmom 17
            erimom "Ele tem muita sorte de ter você como amigo..."
            show erikmom 14
            show player 14
            player_name "Tenho certeza que ele faria o mesmo por mim!"
            show erikmom 49
            show player 1
            erimom "Agora vá e me conte o que vai acontecer..."
            show player 11
            erimom "Se você arranjar uma namorada para o {b}Erik{/b}, você vai ter uma recompensa bem especial..."
            show erikmom 50
            player_name "..."
            show player 21
            player_name "Beleza, {b}Sra. Johnson{/b}!"
            show player 1
            show erikmom 14
            $ june_intro_2.finish()
            jump mrsj_button_dialogue_repeat

        "Amamentação." if erik.over(erik_breastfeeding_2) and (not erik.known(erik_sex_ed) and not mrsj.known(mrsj_sex_ed) and not June.known(june_intro)):
            show erikmom 38 at right
            show player 12 at left
            player_name "Então, há quanto tempo você está... amamentando o {b}Erik{/b}?"
            show player 5
            show erikmom 52
            erimom "Ah..."
            erimom "Escute, não é o que você está pensando."
            erimom "Eu sempre o amei assim."
            show erikmom 38
            show player 11
            erimom "..."
            show erikmom 52
            erimom "Sabe, ele não recebe muita atenção das garotas da escola."
            erimom "Fico muito triste por ele!"
            erimom "Eu só queria que meu bebê vivesse as mulheres inteiras!"
            show erikmom 20
            erimom "Mas talvez eu... tenha exagerado..."
            show erikmom 19c
            show player 5
            player_name "..."
            show player 12
            player_name "É ótimo que se importe tanto e lhe dê atenção!"
            show erikmom 14
            show player 10
            player_name "Acho que ele é muito sortudo..."
            show player 11
            show erikmom 18
            erimom "Oh, ha ha!"
            show erikmom 17
            erimom "Obrigada..."
            erimom "Acho que garotos como vocês, precisam de toda a atenção do mundo..."
            show erikmom 14
            show player 13
            player_name "..."
            show erikmom 49
            erimom "Quero dizer, obrigado pela compreensão, [firstname]."
            show erikmom 52
            erimom "Mas...lembre-se de manter isso entre nós, ok?"
            show erikmom 14
            show player 14
            player_name "Sim, {b}Sra. Johnson{/b}."
            hide player
            hide erikmom
            with dissolve

        "O que você queria que eu fizesse mesmo?" if mrsj.started(mrsj_yoga_help):
            show player 10
            player_name "O que você queria que eu fizesse mesmo?"
            show player 5
            show erikmom 19
            erimom "Preciso que alguém vá e {b}dê aula de yoga para minha hoje a noite{/b}."
            show erikmom 49
            erimom "Você acha que pode ajudar sua... vizinha favorita??"
            show erikmom 50
            show player 14
            player_name "Claro!"
            show player 13
            show erikmom 17
            erimom "Lembre-se de {b}estudar os movimentos de yoga da lista{/b} que eu dei!"

        "Onde está o {b}Erik{/b}?" if not gTimer.is_dark():
            show player 14
            if gTimer.is_morning() and not gTimer.is_weekend():
                player_name "Você sabe onde eu encontraria o {b}Erik{/b}?"
                show player 1
                show erikmom 17
                erimom "Ele deve estar na {b}escola{/b} agora."
            else:

                show erikmom 14
                player_name "Você sabe onde eu encontraria o {b}Erik{/b}?"
                show player 1
                show erikmom 17
                erimom "Acho que vi ele indo para o {b}porão{/b}."
                erimom "Você deveria ver se ele está lá!"
                show erikmom 14
                show player 17
                player_name "Valeu, {b}Sra. Johnson{/b}!"
            show erikmom 14
            jump mrsj_button_dialogue_repeat

        "Você está em uma ótima forma!" if not gTimer.is_dark():
            show erikmom 14 at right
            show player 29 at left
            player_name "Sabe, {b}Mrs. Johnson{/b}, você está em uma ótima forma!"
            player_name "Você faz muitos exercícios?"
            show erikmom 18 at right
            show player 13 at left
            erimom "Aw... Você é tão legal!"
            show erikmom 17 at right
            erimom "Eu tento ir a academia sempre que posso..."
            erimom "...Eu também faço corridas! E também faço yoga no meu quarto durante a noite...."
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
            erimom "...E meus {b}peitos{/b} não são como comstumavam ser..."
            player_name "..."
            show player 28 at left
            show erikmom 19 at right
            player_name "*glup*"
            show player 1 at left
            show erikmom 18 at right
            erimom "Queria falar algo?"
            jump mrsj_button_dialogue_repeat

        "Convidar para jogar poker." if mrsj.known(mrsj_poker_night) and not gTimer.is_night():
            show player 14 at left

            if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                show erikmom 39 at right
            elif gTimer.is_dark() and erik.over(erik_gf):
                show erikmom 53
            else:
                show erikmom 14 at right

            if gTimer.is_morning() and not gTimer.is_weekend():
                player_name "Você poderia nos ensinar a jogar poker?"
                show player 11
                show erikmom 19
                erimom "Você não deveia estar na escola??"
                erimom "O Erik já foi!"
                show player 29
                show erikmom 14
                player_name "Puts! Tens razão..."
                player_name "Talvez mais tarde!"

            elif pStats.chr() >= 5 and poker_bot02 == "" and not gTimer.is_morning():
                if mrsj.completed(mrsj_poker_night_2):
                    show player 14 at left
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 39
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 53
                    else:
                        show erikmom 14 at right
                    player_name "Gostaria de jogar poker com a gente de novo?"
                    show player 1
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 17
                    erimom "Ainda está à procura de amigos para jogar?."
                    show player 14
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 39
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 53
                    else:
                        show erikmom 14
                    player_name "É que-"
                    show player 1
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 18
                    erimom "Está tudo bem!!"
                    show player 1
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 17
                    erimom "Vou jogar com vocês..."
                    show player 14
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 39
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 53
                    else:
                        show erikmom 14
                    player_name "Sério?"
                    show player 1
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40b
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 20
                    erimom "Na última vez passou um pouco dos limites..."
                    show player 13
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 18
                    erimom "Mas, por que não?"
                    show player 14
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 39
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 53
                    else:
                        show erikmom 14
                    player_name "Beleza."
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 17
                    erimom "Quando vamos jogar?"
                    show player 14
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 39
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 53
                    else:
                        show erikmom 14
                    player_name "Hoje a noite, depois do jantar."
                    player_name "{b}Erik{/b} e eu vamos preparar o jogo."
                    show player 1
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40b
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 18
                    erimom "Haha, beleza."
                    if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                        show erikmom 40
                    elif gTimer.is_dark() and erik.over(erik_gf):
                        show erikmom 54
                    else:
                        show erikmom 17
                    erimom "Até mais!"
                else:

                    player_name "Gostaria de jogar poker com o Erik e eu?"
                    show player 1
                    show erikmom 17
                    erimom "Agora?"
                    show player 14
                    show erikmom 14
                    player_name "Sim... Digo, você não é obrigada!"
                    player_name "{b}Erik{/b} e eu estamos procurando por um terceiro jogador..."
                    show player 1
                    show erikmom 17
                    erimom "Ele está esperando lá em baixo?"
                    show player 14
                    show erikmom 14
                    player_name "Sim, ele queria jogar agora, você poderia?"
                    show player 1
                    erimom "Hmm..."
                    show erikmom 17
                    erimom "Acho que posso jogar um ou dois jogos."
                    show erikmom 18
                    show player 13
                    erimom "Beleza, vejo vocês dois lá em baixo!"
                    show player 18
                    show erikmom 14
                    player_name "Legal! Valeu, {b}Sra. Johnson{/b}!"
                $ poker_bot02 = "erik_mom"
                $ poker_sayer02 = erimom
            else:

                if pStats.chr() < 5 and not gTimer.is_morning():
                    $ stat_warn = chr_warn
                else:
                    $ stat_warn = ""
                player_name "[stat_warn]Você poderia nos ensinar a jogar poker?"
                show erikmom 17
                show player 1
                erimom "[stat_warn]O jogo de cartas?"
                show erikmom 14
                show player 14
                player_name "[stat_warn]Sim, Erik e eu estamos procurando alguém para jogar."
                show erikmom 17
                show player 14
                erimom "[stat_warn]Eu adoraria."
                show player 19
                erimom "[stat_warn]Mas eu não tenho tempo agora, desculpe..."
                show erikmom 14
                show player 14
                player_name "[stat_warn]Belza, Talvez outra hora."
        "Tenho que ir!":

            if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                show erikmom 39
                show player 14 at left
                player_name "Tenho que ir, mas volto outra hora!"
            else:
                if gTimer.is_dark() and erik.over(erik_gf):
                    show erikmom 53
                else:
                    show erikmom 14 at right
                show player 14 at left
                player_name "Vou procurar pelo {b}Erik{/b}!"
            if gTimer.is_dark() and (mrsj.over(mrsj_sex_ed) or erik.over(erik_gf)):
                if mrsj.over(mrsj_sex_ed):
                    show erikmom 40
                elif erik.over(erik_gf):
                    show erikmom 54
                show player 1 at left
                erimom "Mesmo?"
                erimom "Volte logo!"
            else:
                show erikmom 18 at right
                show player 1 at left
                erimom "Beleza!"
            if gTimer.is_dark() and mrsj.over(mrsj_sex_ed):
                show erikmom 39
            elif gTimer.is_dark() and erik.over(erik_gf):
                show erikmom 53
            else:
                show erikmom 14 at right
            show player 17 at left
            player_name "Tchau, {b}Sra. Johnson{/b}!"
    hide player
    hide erik
    hide erikmom
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
