label library_dialogue:
    $ location_count = "Library"
    if getPlayingSound("<loop 9 to 83>audio/ambience_library.ogg"):
        $ playSound("<loop 9 to 83>audio/ambience_library.ogg", 1.0)

    if aunt.started(aunt_breeding_guide):
        scene library with None
        show player 10 with dissolve
        player_name "( Talvez esse lugar tenha o livro que ajude a {b}tia Diane{/b} a produzir mais leite. )"
        show player 11
        pause
        show player 35
        player_name "( Onde eu deveria começar? )"
        show player 10
        player_name "( Acho que posso perguntar para a atendente primeiro. )"
        hide player with dissolve

    elif library_count == 0:
        scene library with None
        show player 1 at left
        show jane 2 at right
        with dissolve
        jan "Oi!"
        show player 14
        show jane 1
        player_name "Oh, oi!"
        player_name "Estou procurando por uns {b}livros{/b} da escola."
        show player 1
        show jane 2
        jan "Você já é membro?"
        show jane 1
        menu:
            "Não.":
                show player 10 at left
                show jane 1 at right
                player_name "Umm... Ainda não."
                show player 13
                show jane 3
                jan "Oh. Tudo bem!"
                show jane 2
                jan "Quer virar membro?"
                show jane 3
                show player 11
                jan "Inscreva-se por apenas {b}$20{/b}, você terá acesso a todos os livros!"
                show jane 1
                show player 2
                player_name "Uhh... Acho que não tenho outra escolha. Haha."
                show jane 3
                show player 13
                jan "Conhecimento nunca é caro de mais, certo?"
                show jane 2
                jan "Você quer se inscrever agora mesmo?"
                show jane 1
                menu:
                    "Claro." if inventory.money >= 20:
                        show player 4 at left
                        show jane 1 at right
                        player_name "Hmm..."
                        show player 174b at Position(xoffset=38) with fastdissolve
                        player_name "Certo. Aqui os {b}$20.{/b}"
                        play audio coins2
                        $ inventory.money -= 20
                        $ library_subscription = True
                        show player 1 with fastdissolve
                        show jane 3
                        jan "Obrigada!"
                        show jane 2
                        jan "Se você estiver procurando por um {b}livro{/b} específico, venha para a minha mesa."
                        jan "Eu vou procurar e achar para você!."
                        show jane 1
                        show player 2
                        player_name "Parece ótimo! Obrigado!"
                        hide player 2
                        hide jane 1
                        with dissolve
                        $ library_count = 1
                        $ callScreen(location_count)
                    "Nõa quero.":

                        show player 4 at left
                        show jane 1 at right
                        player_name "Hmm..."
                        show player 35
                        player_name "Na verdade, acho que não quero agora..."
                        show jane 2
                        show player 1
                        jan "Oh... tudo bem então."
                        show jane 1
                        show player 2
                        player_name "Talvz eu volte outra hora!"
                        show jane 2
                        show player 1
                        jan "Ok, tenha um bom dia!"
                        hide player 1
                        hide jane 2
                        with dissolve
                        $ library_count = 0
                        $ location_count = "Town Map"
                        $ callScreen(location_count)

    elif homework_count == 1 and not janice_thankyou:
        scene library with None
        show jane 6 at right
        show player 1 at left
        with dissolve
        jan "Ei!"
        jan "Só queria agradecer pela {b}nova webcam{/b}!"
        show jane 1
        show player 2
        player_name "De nada!"
        show jane 3
        show player 1
        jan "As pessoas estão amando..."
        jan "A resolução é fenomenal e a taxa de quadros também..."
        jan "...eles consegue ver tudo!"
        show jane 1
        show player 17
        player_name "Tenho que agradecer pelo {b}livro{/b} também!"
        show player 14
        player_name "Me ajudou muito. consegui terminar a {b}tarefa{/b}."
        show jane 3
        show player 1
        jan "Fico feliz que fizemos um acordo em que ambos saímos ganhando!"
        show jane 2
        jan "Vou estar na mesa se você quiser algo."
        $ janice_thankyou = True
        $ library_desk_count = 1
        hide player
        hide jane
    $ callScreen(location_count)

label library_desk_dialogue:
    if library_desk_count == 0:
        scene librarydesk with None
        show jane 10
        show player 1f at right
        with dissolve
        jan "Oi! Como posso te ajudar?"
        show player 2f
        show jane 9
        player_name "Oi, estou procurando por um {b}livro{/b}."
        show player 1f
        show jane 10
        jan "Claro! Qual o nome?"
        show player 1f
        show jane 9
        menu:
            "Gramática Francesa - Volume 1" if textbook1 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Ah sim, Eu preciso do livro \"{b}Gramática Francesa - Volume 1{/b}\""
                show player 1f
                show jane 11
                jan "Oh, não temos ele..."
                jan "... mas posso comprar na internet."
                show player 14f
                show jane 9
                player_name "Ótimo, quanto tempo até chegar?"
                show player 11f
                show jane 11
                jan "Na verdade, não posso encomendar nada por enquanto."
                show player 12f
                show jane 9
                player_name "Por quê??"
                show player 5f
                show jane 11
                jan "Infelizmente, a biblioteca teve uma grande perda de verba ano passado..."
                jan "Não temos muito dinheiro para comprar livros..."
                show player 10f
                show jane 9
                player_name "Então... O que eu deveria fazer agora?"
                show player 5f
                show jane 10
                jan "Bom, você pode esperar até fazermos a encomenda numa outra hora?"
                show player 12f
                show jane 9
                player_name "Não posso! Tenho que terminar a {b}tarefa{/b} antes das {b}provas finais{/b}!"
                show player 11f
                show jane 10
                jan "Sinta-se livre para {b}procurar{/b} na biblioteca. Tenho certeza que terá edições passadas do {b}livro{/b} por aí."
                show jane 11
                jan "Ah! E tente evitar a {b}sala ali atrás{/b}... Eu preciso uh... limpar - ainda não está pronta."
                show player 12f
                show jane 9
                player_name "Ok..."
                hide player 12f
                hide jane 9
                with dissolve
                $ backroom_blocked_count = 1

            "Gramática Francesa - Volume 2" if textbook2 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Preciso do livro \"{b}Gramática Francesa - Volume 2{/b}\""
                show player 11f
                show jane 11
                jan "Ah, desculpa... O livro está fora do estoque por enquanto."
                show player 5f
                show jane 10
                jan "Volte outra hora para ver se já voltou..."
                show player 10f
                show jane 9
                player_name "Certo, valeu."
                hide player 10f
                hide jane 9
                with dissolve

            "Gramática Francesa - Volume 3" if textbook3 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Sim, preciso do livro \"{b}Gramática Francesa - Volume 3{/b}\""
                show player 11f
                show jane 11
                jan "Oh, desulpa... O livro está fora do estoque por enquanto."
                show player 5f
                show jane 10
                jan "Volte outra hora para ver se já voltou..."
                show player 10f
                show jane 9
                player_name "Certo, valeu."
                hide player 10f
                hide jane 9
                with dissolve
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished with dissolve

            "Livro de produção de leite." if aunt.started(aunt_breeding_guide):
                show jane 9 at left
                show player 14f at right
                player_name "Pode parecer um pouco estranho, mas você teria um livro sobre como aumentar a produção de leite?"
                show player 13f
                pause
                show jane 11
                jan "Um... O quê? Não acho que você poderá amamentar na sua vida."
                show jane 10
                jan "Oh! Whoops! Você estava falando de fazenda, certo?"
                show jane 9
                show player 10f
                player_name "Ummm... Na verdade, estou interessante em ambos os tópicos, eu acho..."
                show player 13f
                show jane 11
                jan "Cheque a prateleira bem ali. Devemos ter algo."
                show jane 9
                show player 14f
                player_name "Valeu!"
                show player 13f
                show jane 10
                jan "De nada!"
                hide player
                hide jane
                with dissolve
                $ aunt_breeding_guide.finish()

    elif library_desk_count == 1:
        scene librarydesk with None
        show jane 10
        show player 1f at right
        with dissolve
        jan "Oi! Como posso te ajudar?"
        show player 2f
        show jane 9
        player_name "Oi, estou procurando por um livro."
        show player 1f
        show jane 10
        jan "Claro, qual o nome dele?"
        show jane 9
        menu:
            "Gramática Francesa - Volume 1" if textbook1 not in inventory.items:
                show player 14f at right
                show jane 9
                player_name "Ah, preciso do \"{b}Gramática Francesa - Volume 1{/b}\""
                show player 1f
                show jane 11
                jan "Você me trouxe o que ue pedi?"
                show jane 9
                menu:
                    "Aqui está a webcam." if supersaga_webcam in inventory.items:
                        show player 12f at right
                        show jane 9
                        player_name "Sim... aqui está a {b}webcam{/b}."
                        show player 239_240f
                        pause
                        show player 54 at Position(xoffset=-38) with fastdissolve
                        pause
                        show player 1f with fastdissolve
                        $ inventory.items.remove(supersaga_webcam)
                        show jane 13
                        jan "Obrigada!"
                        show player 16f
                        show jane 9
                        player_name "..."
                        show player 12f
                        player_name "E o meu {b}livro{/b}?"
                        show player 11f
                        show jane 13
                        jan "Oh! Certo..."
                        show player 11f
                        jan "Chegou hoje de manhã, vou colocar na {b}prateleira{/b} ali."
                        jan "Vá lá e pegue."
                        $ completed_quests.append(quest06)
                        show player 1f
                        show jane 13
                        jan "Até a próxima!"
                        $ library_desk_count = 0
                        hide player 1f
                        hide jane 13 with dissolve
                    "Ainda não.":

                        show player 24f at right
                        show jane 9
                        player_name "Ainda não..."
                        show player 5f
                        show jane 10
                        jan "Não consigo comprar o {b}livro{/b} até você me trazer, você sabe."
                        jan "Volte quando você tiver a {b}webcam{/b}, e então conversaremos."
                        hide player 5f
                        hide jane 10
                        with dissolve

            "Gramática Francesa - Volume 2" if janice_thankyou:
                if not webcam_quest:
                    show player 14f at right
                    show jane 9
                    player_name "Preciso desse livro: {b}Gramática Francesa - Volume 2{/b}"
                    show player 1f
                    show jane 10
                    jan "Você sabe..."
                    jan "Ainda não posso fazer nenhuma compra."
                    show player 12f
                    show jane 9
                    player_name "Ainda não??"
                    show player 5f
                    show jane 11
                    jan "Eu adoraria conseguir... Mas a verba ainda está baixa."
                    show player 10f
                    show jane 9
                    player_name "Como assim? A nova {b}webcam{/b} não está ajudando??"
                    show player 5f
                    show jane 11
                    jan "Não me entenda mal: Está ajudando..."
                    jan "Mas as pessoas estão cansadas disso!"
                    show player 10f
                    show jane 9
                    player_name "Então... O que deveriamos fazer?"
                    show player 5f
                    show jane 11
                    jan "Nosso público quer coisas novas..."
                    show player 11f
                    show jane 13
                    jan "...e talvez você possa me ajudar com isso!"
                    show player 12f
                    show jane 9
                    player_name "Mas como?"
                    show player 11f
                    show jane 10
                    jan "Você vai pra escola?"
                    show player 12f
                    show jane 9
                    player_name "Sim?"
                    show player 11f
                    show jane 13
                    jan "Ótimo, esconda minha {b}webcams{/b} na escola!"
                    show jane 9
                    player_name "..."
                    show player 12f
                    player_name "Você está louca?!"
                    player_name "E se eu for pego!"
                    show jane 13
                    show player 90f
                    jan "Relaxe! Vá de noite, quando não estiver ninguém."
                    show player 37f
                    show jane 9
                    player_name "Ugh... Não acredito que vou ter que fazer isso..."
                    show jane 10
                    jan "Você quer esse livro, né?"
                    show player 24f
                    show jane 9
                    player_name "Vou ver o que consigo fazer..."
                    $ inventory.items.append(supersaga_webcam)
                    $ quest_list.append(quest11)
                    $ webcam_quest = True
                    hide jane
                    hide player
                else:

                    show player 14f at right
                    show jane 9
                    player_name "Preciso do livro: {b}Gramática Francesa - Volume 2{/b}"
                    show player 1f
                    show jane 11
                    jan "Bem? Você fez isso??"
                    menu:
                        "Eu coloquei." if webcam_planted:
                            show jane 9
                            show player 12f at right
                            player_name "Sim. Coloquei no {b}banheiro{/b}..."
                            player_name "Está no teto, na {b}ventilação de ar{/b}..."
                            show player 1f
                            show jane 13
                            jan "Valeu!"
                            show player 16f
                            show jane 9
                            player_name "..."
                            show player 12f
                            player_name "E o meu {b}livro{/b}?!"
                            show player 11f
                            show jane 13
                            jan "Oh! Certo..."
                            show player 11f
                            show jane 15
                            jan "Aqui está!"
                            $ inventory.items.append(textbook2)
                            show player 30f
                            show jane 9
                            player_name "Valeu!"
                            show player 1f
                            show jane 13
                            jan "Até a próxima!"
                            $ library_desk_count = 0
                            $ completed_quests.append(quest11)
                            hide player 1f
                            hide jane 13 with dissolve
                        "Ainda não.":

                            show player 24f at right
                            show jane 11
                            player_name "Ainda não fiz..."
                            show player 5f
                            show jane 10
                            jan "Não consigo comprar esse {b}livro{/b} para você então. Você sabe."
                            jan "Volte quando você colocar a {b}webcam{/b} na escola."
                            hide player 5f
                            hide jane 10
                            with dissolve

            "French Grammar - Volume 3" if quest11 in completed_quests:
                show popup_unfinished at truecenter with dissolve
                $ renpy.pause()
                hide popup_unfinished with dissolve
    $ callScreen(location_count)

label library_bookshelf:
    $ location_count = "Library BookShelf"
    $ callScreen(location_count, ui = False)

label kamasutra:
    scene libraryshelf with None
    show book_02_c at truecenter with dissolve
    player_name "Woa..."
    player_name "Esse livro tem todos os tipos de...posições?"
    player_name "Deve ser esse que ela estava querendo..."
    hide book_02_c with dissolve
    $ inventory.items.append(kamasutra)
    $ callScreen(location_count, ui = False)

label library_old_book:
    scene libraryshelf with None
    show closeup_book_03 at truecenter with dissolve
    player_name "Esse livro parece ser útil para decodificar algo."
    player_name "..."
    if weird_coin not in inventory.items:
        player_name "Heh. Talvez algum tipo de {b}tesouro pirata escondido{/b}."
        player_name "Mas isso é apenas uma {b}ilusão{/b}."
    else:
        player_name "Acho que aquela {b}moeda pirata{/b} tem o número quatro nela."
        player_name "Eu deveria olhar para ela novamente."
    show popup_item_book6 at truecenter with dissolve
    $ inventory.items.append(old_book)
    hide popup_item_book6 with dissolve
    hide closeup_book_03 with dissolve
    $ callScreen(location_count, ui = False)

label breeding_guide:
    scene libraryshelf with None
    player_name "( Esse livro deve estar am algum lugar... )"
    show book_01_c at truecenter with dissolve
    player_name "( Acho que é esse! )"
    player_name "Hmm..."
    player_name "( Parece ser bem simples. )"
    player_name "( Deve funcionar com a {b}tia Diane{/b} também. )"
    player_name "( Só não tenho certeza que ela quer ficar {b}grávida{/b}. )"
    player_name "( Vamos ver o que ela vai dizer... )"
    hide book_01_c with dissolve
    $ inventory.items.append(breeding_guide)
    $ callScreen(location_count, ui = False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
