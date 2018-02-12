default park_count_night = 0
default anna_done = False

label park_dialogue:
    $ location_count = "Park"
    if gTimer.is_dark():
        if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
            $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")

    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if gTimer.is_dark() and park_count_night == 0:
        scene park_night
        show player 34 with dissolve
        player_name "..."
        show player 35
        player_name "( Consigo ouvir vozes vindo de longe... )"
        show player 14
        player_name "( Talvez eu devesse dar uma olhada! )"
        hide player 14 with dissolve
        $ park_count_night = 1
    $ callScreen(location_count)

label anna_button_dialogue:
    scene location_park_closeup
    if not Anna.known(anna_missing_pup):
        show player 11 at left with dissolve
        show anna 5 at right with dissolve
        anna "Oi, {b}[firstname]{/b}, você viu um {b}cachorrinho{/b} sem coleira??"
        show anna 4
        show player 10
        player_name "Acho que não..."
        show anna 5
        show player 11
        anna "Acho que ue perdi ele."
        anna "Eu estava correndo na trilha da {b}floresta{/b}, e quando fui ver, ele sumiu!!"
        show anna 4
        show player 10
        player_name "Você já olhou na trilha?"
        show anna 5
        show player 11
        anna "Claro! Procurei por todos os cantos!"
        anna "Mas eu não posso procurar na {b}floresta{/b} sozinha..."
        show anna 4
        show player 10
        player_name "Como ele se parece?"
        show player 11
        show anna 6 at Position(xpos=1002)
        anna "Ah, certo. Ele é um {b}pug{/b}!"
        show anna 5 at right
        anna "O nome dele é {b}Awesomo{/b}."
        anna "Ele está um pouco acima o peso, então não deve ter ido muito longe."
        anna "Por favor, me ajuda a encontrar ele?"
        show anna 4
        menu:
            "Sim":
                show anna 4
                show player 14
                player_name "Claro. Vou procurar por ele."
                player_name "Tem algo que eu deveria saber sobre ele?"
                player_name "Algo que pudesse me ajudar a encontrá-lo?"
                show player 1
                show anna 5
                anna "Bom... Ele ama comer {b}biscoitos{/b}."
                anna "Se você tiver alguns, ele sentirá o cheiro e virá até você..."
                show anna 11
                show player 14
                player_name "Ok! Volto aqui se encontrar algo!"
                show anna 12
                show player 1
                anna "Muito obrigada!"
                $ Anna.add_event(anna_missing_pup)
                show unlock42 at truecenter with dissolve
                $ loc_forest_unlocked = True
                pause
                hide unlock42 with dissolve
            "Não":

                show anna 4
                show player 10
                player_name "Adoraria procurar, mas tenho que fazer outras coisas..."
                show player 11
                show anna 5
                anna "Ah, perdão por inconomdar..."

    elif Anna.started(anna_missing_pup) and dog in inventory.items:
        scene location_park_closeup
        show player 247 at left with dissolve
        show anna 4 at right with dissolve
        player_name "Adivinha só quem eu encontrei?"
        show anna 5 with vpunch
        anna "!!!"
        show anna 12
        anna "{b}Awesomo{/b}!!!"
        show player 1
        show anna 9
        with dissolve
        anna "Onde vocẽ achou?!"
        show anna 8
        show player 14
        player_name "Ele estava nas proximidades da floresta, fora da trilha..."
        player_name "E você tem razão! Alguns biscoitos ajudaram."
        show anna 10
        show player 1
        anna "{b}Muito{/b} obrigada!"
        show anna 9
        anna "Ainda vou te pagar."
        show anna 7
        anna "Tenho que ir agora. Ele deve estar faminto depois disso."
        show anna 10
        anna "Vejo você por aí!"
        $ inventory.items.remove(dog)
        $ anna_missing_pup.finish()
    else:

        show player 11 at left with dissolve
        show anna 5 at right with dissolve
        anna "Você achou ele??"
        show anna 4
        show player 10
        player_name "Ainda não..."
        player_name "Poderia descrever ele pra mim de novo? E onde eu poderia encontrá-lo?"
        show player 11
        show anna 6 at Position(xpos=1002)
        anna "Ele é um {b}pug{/b}!"
        show anna 5 at right
        anna "Ele deve estar próximo à trilha da {b}floresta{/b}..."
        anna "...E ele adora {b}biscoitos{/b}!"
        anna "Talvez você pudesse usar uns {b}biscoitos{/b} para atraí-lo."
        show anna 11
        show player 14
        player_name "Ok! Voltarei se encontrar algo!"
    hide player
    hide anna
    with dissolve
    $ callScreen(location_count)

label park_dialogue01:
    if eve_park_dialogue == 0:
        scene park_bench
        show player 1 at left with dissolve
        show eve 2 at right with dissolve
        eve "Então você decidiu aparecer, hein?"
        show eve 1 at right
        show player 2 at left
        player_name "Você disse que eu devia..."
        show eve 6 at right
        show player 11 at left
        eve "Não é meio tarde para você?"
        eve "Você não tem um toque de recolher, ou algo assim?"
        show eve 1 at right
        show player 5 at left
        player_name "..."
        show eve 6 at right
        show player 11 at left
        eve "Estou brincando!!"
        show eve 1 at right
        show player 17 at left
        player_name "Oh. Haha..."
        show player 1 at left
        show eve 2 at right
        eve "Então, qual foi?"
        menu:
            "Você está bonita!":
                show player 21 at left
                show eve 1 at right
                player_name "Não sei se eu já disse isso pra você, mas eu gosto muito do seu cabelo!"
                show eve 4 at right
                show player 13 at left
                eve "Haha! Isso foi meio aleatório!"
                show player 29 at left
                player_name "Só quis falar... O azul fica bom em você."
                show eve 3 at right
                show player 13 at left
                eve "..."
                show eve 4 at right
                eve "Uhh... Valeu?"
                show eve 6 at right
                show player 11 at left
                eve "Hmm... Ei, você deveria ficar!"
                eve "Os caras vão começar uma {b}batalha de rap{/b} daqui a pouco."
                show eve 1 at right
                show player 2 at left
                player_name "Ah, sério? Tipo... Um zoando o outro no microfone?"
                show eve 6 at right
                show player 1 at left
                eve "Sim!"
                show eve 7 at right
                show player 11 at left
                eve "Acho que você deveria fazer isso."
                show eve 5 at right
                show player 23 at left with hpunch
                player_name "O quê?!"
                show eve 6 at right
                show player 5 at left
                eve "Por favor. Você não deve ser TÂO tímido?"
                eve "Just have fun with it!"
                show eve 5 at right
                show player 21 at left
                player_name "Acho que eu poderia tentar..."
                show player 13 at left
                show eve 6 at right
                eve "Então? Você vai fazer isso?"
                menu:
                    "Claro!":
                        show player 21 at left
                        show eve 5 at right
                        player_name "Tá, vamos lá!"
                        show player 13 at left
                        show eve 6 at right
                        eve "Sabia que você iria aceitar!"
                        show eve 8 at right
                        eve "Aqui, pena o microfone..."
                        show player 70
                        show eve 5 at right
                        player_name "Oh. Ok. Isso está ligado?"
                        show eve 6 at right
                        eve "Haha! Claro!"
                        show player 71 at left
                        show eve 5 at right
                        player_name "Quem eu vou enfrentar?"
                        show eve 6 at right
                        eve "Têm três: {b}Chico{/b}, {b}Tyrone{/b} e {b}Chad{/b}! "
                        show eve 5 at right
                        show player 70 at left
                        player_name "Hmmm... Quem eu deveria enfrentar?"
                        menu:
                            "Chico":
                                $ rap_opponent = "chico"
                                show player 70 at left
                                player_name "Vou primeiro contra o {b}Chico{/b}."
                                hide player 70 at left with dissolve
                                hide eve 5 at right with dissolve
                                jump chico_before_battle
                            "<>[chr_warn]Chad":

                                $ pass
                            "<>[chr_warn]Tyrone":

                                $ pass

                            "Pular Mini-Game (Trapaç)" if cheat_mode:
                                $ gTimer.tick()
                                $ pStats.increase("chr")
                                $ eve_park_dialogue = 1
                                show unlock23 at truecenter with dissolve
                                $ renpy.pause()
                                $ callScreen(location_count)
                    "Tenho que ir.":

                        show player 10 at left
                        show eve 1 at right
                        player_name "Tenho que ir. Tenho umas coisas pra fazer."
                        show eve 6 at right
                        show player 13 at left
                        eve "Eu acho que você realmente tem um toque de recolher..."
                        show eve 1 at right
                        show player 2 at left
                        player_name "Desculpa. Volto outra hora!"
                        show eve 7 at right
                        show player 13 at left
                        eve "Beleza então..."
                        hide player 13 at left with dissolve
                        hide eve 7 at right with dissolve
                        $ callScreen(location_count)
            "Eu deveria ir para casa.":

                show eve 1 at right
                show player 10 at left
                player_name "Ah, merda! Tenho que ir. Tenho que fazer coisas mais importantes."
                show eve 2 at right
                show player 13 at left
                eve "Eu acho que você realmente tem um toque de recolher..."
                show eve 1 at right
                show player 2 at left
                player_name "Desculpa. Volto outra hora!"
                show eve 7 at right
                show player 13 at left
                eve "Tá, que seja."
                hide player 13 at left with dissolve
                hide eve 7 at right with dissolve
                $ callScreen(location_count)
        $ eve_park_dialogue = 1
    else:

        scene park_bench
        show player 1 at left with dissolve
        show eve 6 at right with dissolve
        eve "Eae {b}[firstname]{/b}!"
        show eve 5 at right
        show player 14 at left
        player_name "Eae, {b}Eve{/b}!"
        show eve 6 at right
        show player 1 at left
        eve "Fico feliz por você ter aparecido!"
        show eve 3 at right
        show player 14 at left
        player_name "É bom te ver de novo..."
        show eve 4 at right
        show player 1 at left
        eve "Então?"
        menu:
            "Vamos batalhar.":
                show player 33 at left
                show eve 5 at right
                player_name "Quero fazer uma batalha de rap de novo!"
                show eve 6 at right
                show player 1 at left
                eve "Ah, sério??"
                show eve 5 at right
                show player 26 at left
                player_name "Sim! Acho que estou ficando bom."
                show eve 6 at right
                show player 1 at left
                eve "Ótimo!"
                show eve 8 at right
                eve "Ok. Aqui está seu microfone..."
                show eve 1 at right
                show player 70 at left
                player_name "Hmmm... Quem eu deveria enfrentar?"
                menu:
                    "Chico":
                        $ rap_opponent = "chico"
                        show player 71 at left
                        player_name "Vou conta o {b}Chico{/b} primeiro."
                        hide eve 1 at right with dissolve
                        jump chico_before_battle

                    "<>[chr_warn]Chad" if pStats.chr()< 4:
                        $ pass

                    "Chad" if pStats.chr() >= 4:
                        $ rap_opponent = "chad"
                        show player 71 at left
                        player_name "Vou contra o {b}Chad{/b}."
                        hide eve 1 at right with dissolve
                        jump chad_before_battle

                    "<>[chr_warn]Tyrone" if pStats.chr() < 7:
                        $ pass

                    "Tyrone" if pStats.chr() >= 7:
                        $ rap_opponent = "tyrone"
                        show player 71 at left
                        player_name "Vou contra o {b}Tyrone{/b}."
                        hide eve 1 at right with dissolve
                        jump tyrone_before_battle

                    "Pular Mini-Game (Trapaça)" if cheat_mode:
                        $ gTimer.tick()
                        $ pStats.increase("chr")
                        show unlock23 at truecenter with dissolve
                        $ renpy.pause()
                        $ callScreen(location_count)
            "Tenho que ir.":

                show player 10 at left
                show eve 1 at right
                player_name "Na verdade, tenho que ir. Tenho que fazer outras coisas."
                show player 13 at left
                show eve 6 at right
                eve "Mas você mal chegou..."
                show eve 1 at right
                show player 2 at left
                player_name "Foi mal. Volto outra hora!"
                show eve 7 at right
                show player 13 at left
                eve "Tá bom então..."
                hide player 13 at left with dissolve
                hide eve 7 at right with dissolve
                $ callScreen(location_count)

label chico_before_battle:
    if chico_battle_count == 0:
        scene park_bench
        show douche 1 at right with dissolve
        show player 77 at left with dissolve
        player_name "Eae, caras!"
        hide douche 1 at right
        show douche 2 at right
        show chico 3
        hide player 77
        show player 77 at left
        with dissolve
        chi "Quem é você?!"
        show player 74 at left
        show chico 1
        show player 71 at left
        player_name "Ah, oi! Me chamo {b}[firstname]{/b}!"
        player_name "E eu acho que você é o... {b}Chico{/b}?"
        show chico 2
        show player 74 at left
        chi "Você não me conhece, otário!"
        show chico 1
        show player 71 at left
        player_name "{b}Eve{/b} me contou seu nome-"
        show chico 3 with hpunch
        show player 74 at left
        chi "{b}AE{/b}! Cala a {b}porra{/b} {b}DA SUA BOCA{/b}!"
        show player 75 at left
        show chico 1
        player_name "..."
        show chico 4
        show player 74 at left
        chi "Eu começo, {b}se prepare{/b}!"
        hide player 74
        hide chico 4
        hide douche
        with dissolve
        $ chico_battle_count = 1
        jump rapbattle_listing
    else:

        scene park_bench
        show douche 1 at right with dissolve
        show player 77 at left with dissolve
        player_name "Eae, caras!"
        hide douche 1 at right
        show douche 2 at right with dissolve
        show chico 3
        hide player
        show player 74 at left
        with dissolve
        chi "Você voltou para mais?"
        show chico 1
        show player 71 at left
        player_name "Eae, {b}Chico{/b}!"
        player_name "Sim, vamos começar!"
        show chico 4
        show player 74 at left
        chi "Eu começo. {b}Se prepare{/b}!"
        hide player 74 at left with dissolve
        hide chico 4 with dissolve
        jump rapbattle_listing

label chad_before_battle:
    show player 1 at left
    show chad 2 at right
    with dissolve
    chad "Então, você acha que consegue vencer do Chico."
    chad "Não sei por que você está querendo me enfrentar, a menos que você pense que você pode me vencer de alguma forma."
    show chad 1
    show player 2
    player_name "É nisso que estou pensando."
    show chad 4
    show player 1
    chad "Olha só! O rebeldezinho tem coragem!"
    chad "Vou jogar seu jogo, saiba que você não está saindo da mesma maneira que você chegou."
    jump rapbattle_listing

label tyrone_before_battle:
    show tyrone 2 at right
    show player 1 at left
    with dissolve
    tyrone "Quem é esse trouxa?"
    show tyrone 1
    show player 2
    player_name "Eae, eu sou-"
    show player 3
    show tyrone 3
    tyrone "Eu estava perguntando pra você?"
    show player 12
    show tyrone 1
    player_name "Não, mas eu pensei que-"
    show tyrone 2
    tyrone "Pensou errado!"
    tyrone "Agora você quer se humilhado, ou só veio pra gastar meu tempo?"
    show tyrone 4
    show player 12
    player_name "Nenhum."
    show player 1
    show tyrone 3
    tyrone "Mano, só te dou duas opções, e você fará apenas uma!"
    show tyrone 2
    tyrone "Bora, vou acabar com você!"
    jump rapbattle_listing

label eve_after_win:
    scene park_bench
    show player 76 at left
    show eve 4 at right with dissolve
    eve "Wow! Isso foi demais!"
    show player 77 at left
    show eve 5 at right
    player_name "Valeu!"
    show eve 7 at right
    show player 76 at left
    eve "Tem certeza que foi a primeira vez??"
    show eve 5 at right
    show player 71 at left
    player_name "Sim!"
    show eve 6 at right
    show player 76 at left
    eve "Estou feliz que você tentou. Você deveria voltar!"
    show eve 5 at right
    show player 77 at left
    player_name "Claro! Acho que vou!"
    show eve 6 at right
    show player 76 at left
    player_name "Tenho que ir pra casa agora! Até a próxima!"
    show eve 5 at right
    show player 77 at left
    eve "Beleza. Boa noite!"
    hide player 77 at left with dissolve
    hide eve 5 at right with dissolve
    $ eve_park_dialogue = 1
    $ callScreen(location_count)

label eve_after_lose:
    scene park_bench
    show player 71 at left
    show eve 1 at right with dissolve
    player_name "Isso foi, horrível..."
    show eve 6 at right
    show player 76 at left
    eve "Haha! Sim..."
    show eve 7 at right
    eve "Mas está tudo bem; você vai melhorar."
    show eve 1 at right
    show player 71 at left
    player_name "Eu não sei se estou pronto pra isso..."
    show eve 6 at right
    show player 76 at left
    eve "Não diga isso!"
    show eve 7 at right
    eve "Os caras vão te conhecer, então não será tão ruim."
    show eve 1 at right
    show player 71 at left
    player_name "É. Talvez..."
    show eve 6 at right
    show player 76 at left
    eve "Tenho que ir agora, mas acho que você deveria voltar!"
    show eve 1 at right
    show player 77 at left
    player_name "Beleza. Boa noite!"
    show eve 6 at right
    show player 76 at left
    eve "See ya!"
    hide player 76 at left with dissolve
    hide eve 6 at right with dissolve
    $ eve_park_dialogue = 1
    $ callScreen(location_count)

label fountain_dialogue:
    $ location_count = "Park Fountain"
    scene expression gTimer.image("park_fountain{}")
    if weird_coin not in inventory.items:
        show expression "private/objects/object_coin_01.png" at Position(xalign = 0.44, yalign = 0.81)
    player_name "( Vejo muitas moedas aqui. )"
    $ callScreen(location_count, False, False)

label coin_dialogue:
    hide expression "private/objects/object_coin_01.png"
    show expression "private/objects/closeup_coin_01.png" at Position(xalign = 0.5, yalign = 1.0)
    with dissolve
    player_name "Huh?"
    player_name "Parece ser uma moeda bem antiga."
    player_name "Olha esses {b}símbolos{/b} antigos!"
    player_name "Eu deveria ficar com isso. Talvez tenha algum valor."
    show popup_item_coin1 at truecenter with dissolve
    $ inventory.items.append(weird_coin)
    pause
    hide popup_item_coin1 with dissolve
    hide expression "private/objects/closeup_coin_01.png" with dissolve
    $ callScreen(location_count, False, False)

label park_night_closed:
    scene park_night
    show player 10 with dissolve
    player_name "( Está ficando tarde, deveria ir para casa. )"
    hide player
    hide park_night
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
