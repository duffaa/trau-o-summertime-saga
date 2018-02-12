label garden_dialogue:
    default aunt_count = 0
    default in_garden = False
    default shed_dialogue = 0
    default aunt_dialogue_advance = False
    default after_minigame = False
    default drunk_dialogue = False
    default shed_unlocked = False
    default aunt_shed_scene = False
    default drank_milk = False
    default drink_milk_offer = False
    default pump_quest_active = False
    default aunt_drink_active = False
    default aunt_drink_made = False
    default aunt_extra_shot = False
    default aunt_drink_offered = False
    default garden_firsttime = False
    default infestation_done = False
    default aunt_masturbating_seen = False
    default seen_shed_locked = False
    default xray_toggle = False
    default xray = 0
    default aunt_had_sex = False
    default condom_on = True
    default shed_sex_angle = 0
    default shed_cow_outfit = True
    default cow_outfit = 0
    default shed_xray_toggle = False
    default shed_cum = False
    default shed_had_sex = False
    default shed_sex_count = 0
    default aunt_apology_seen = False
    default milking_unlocked = False
    default garden_done = 0
    default shed_sex_action = 0

    $ location_count = "Diane's Garden"
    $ tick_skip_active = True
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if not gTimer.is_dark():
        if aunt_shed_scene and not aunt.known(aunt_drunken_splur):
            scene location_garden_close_blur with None
            show player 11 at left
            show aunt 99 at right
            with dissolve
            dia "Uhuuuuum! Aí está o meu sobrinho!"
            show player 5
            dia "Como você está-{b}*hic*{/b} hoje?"
            dia "Veio até ao meu jardim com sua pá?"
            show aunt 95
            show player 12
            player_name "{b}Tia Diane{/b}? Você está bem?"
            show player 11
            show aunt 162 at Position (xpos = 973)
            dia "Quem, eu?"
            dia "Eu-{b}*hic*{/b}- estou bem."
            show aunt 161
            pause
            show aunt 162
            dia "Está meio quente aqui fora, então eu tive que fazer algo..."
            show aunt 161
            show player 22
            pause
            show player 10
            player_name "{b}Tia Diane{/b}, suas roupas... elas estão... escorregando."
            show player 11
            show aunt 162
            dia "Huh? O que você..."
            show aunt 163
            dia "Oh!!"
            show aunt 164
            dia "Hahaha!"
            show player 21
            show aunt 165
            player_name "Heh..."
            show player 13
            show aunt 166
            dia "Isso é o que acontece quando você começa a beber antes de se vestir."
            dia "E também não ajuda... ter esses melões indo de um lado para o outro!!"
            show aunt 164
            dia "Haha!"
            show aunt 165
            pause
            show player 11
            show aunt 163
            dia "Oops! Ainda está escapando!"
            show aunt 164
            dia "Haha!"
            show player 1
            show aunt 94 at right with fastdissolve
            dia "Pronto."
            show aunt 99
            dia "Já disse que você é meu sobrinho favorito?"
            show player 14
            show aunt 98
            player_name "Uh... algumas vezes..."
            show player 11
            show aunt 97
            dia "Digo, sua irmã é tão... puta, sabe?"
            show aunt 99
            show player 13
            dia "Mas eu gosto muito mais de você..."
            show aunt 98
            show player 11
            pause
            show aunt 94
            dia "Mas eu queria ter peitos igual o da sua irmã..."
            show aunt 95
            pause
            show aunt 99
            dia "O quê?"
            dia "Você não acha eles bonitos?"
            show aunt 98
            show player 24
            player_name "Eu... Uh..."
            show aunt 96
            show player 11
            dia "Vai dizer que você nunca olhou para eles?"
            show aunt 98
            show player 10
            player_name "Eu... não sei."
            show aunt 99
            show player 11
            dia "Aqui."
            show player 22
            show aunt 167 at Position (xpos = 973) with fastdissolve
            pause
            show aunt 169
            show player 11
            dia "Quer dizer, você não acha eles mais bonitos que os peitos antigos da sua {b}tia{/b}?"
            show aunt 167
            show player 21
            player_name "Não. Os seus são bonitos."
            show aunt 168
            show player 13
            dia "Awww!"
            dia "Você é tão querido..."
            dia "É por isso que você é meu sobrinho favorito!"
            show aunt 167
            pause
            show aunt 166 with fastdissolve
            show player 11
            dia "Me..."
            dia "Me... desculpa."
            dia "Eu não deveria falar essas coisas na sua frente."
            show player 21
            show aunt 165
            player_name "Está tudo bem..."
            show player 5
            show aunt 166
            dia "Você deve achar que sua {b}tia{/b} fica bêbada fácil."
            show aunt 165
            show player 21
            player_name "Não, não acho. É legal ver você assim... Quero dizer, você é ainda mais engraçada quando está bêbada."
            show player 13
            show aunt 166
            dia "Você é tão fofo, docinho, mas acho que vou me deitar um pouco."
            show aunt 97 at right with fastdissolve
            dia "Acho que bebi demais..."
            hide aunt with dissolve
            pause
            show player 35
            player_name "Cara, nem consigo me lembrar desde a última vez que a vi tão bêbada assim."
            player_name "Eu deveria ter certeza de que ela chegou até a cama."
            hide player with dissolve
            $ lock_ui()
            $ aunt.add_event(aunt_drunken_splur)

        elif quest09_3 and not aunt.known(aunt_mouse_attack):
            scene garden with None
            show player 1f with dissolve
            pause
            show player 32f at Position(xoffset=-69)
            player_name "Huh. Onde está a {b}tia Diane{/b}?"
            player_name "Ela geralmente está trabalhando no jardim..."
            show player 31 at Position(xoffset=68)
            pause
            show player 30
            player_name "Parece que ela também não está no seu galpão."
            show player 12
            player_name "Ela deve estar lá dentro. Está bem quente aqui fora hoje."
            show player 5
            player_name "..."
            show player 10
            player_name "Talvez eu devesse ir ver ela antes de trabalhar."
            hide player with dissolve
            $ lock_ui()
            $ aunt.add_event(aunt_mouse_attack)

        elif aunt_count == 0 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)

            if quest20 not in quest_list:
                scene garden
                show player 1 at left with dissolve
                show aunt 2 at right with dissolve
                dia "Olhe só se não é aquele garoto bonito..."
                show aunt 3 at right
                show player 13 at left
                dia "Você cresceu tanto, mal consigo te reconhecer!"
                show aunt 1 at right
                show player 17 at left
                player_name "Oi, {b}tia Diane{/b}!"
                show aunt 7 at right
                show player 2 at left
                player_name "Uau! Você é muito parecida com a {b}[mom_name]{/b}..."
                show aunt 6 at right
                show player 1 at left
                dia "Ah, ela sempre foi a irmã {b}gêmea{/b} mais bonita..."
                show aunt 7 at right
                show player 33 at left
                player_name "Acho que você está muito bonita, {b}tia Diane{/b}!"
                show aunt 12 at right
                show player 1 at left
                dia "Você sabe como tratar garotas..."
                show aunt 13 at right
                show player 11 at left
                dia "..."
                show aunt 5 at right
                dia "Bom, vamos falar do meu jardim!"
                show aunt 2 at right
                show player 1 at left
                dia "Acho que sua mãe disse que estava procurando jovem forte e forte para me ajudar a cuidar do meu jardim e que eu pagaria, certo?"
                show aunt 1 at right
                show player 2 at left
                player_name "Sim, eu poderia usar o dinheiro para a faculdade, que começa no outono, e ainda não tenho um emprego, então..."
                show aunt 2 at right
                show player 5 at left
                dia "Bem, eu estava esperando que você pudesse começar hoje, mas tenho algumas más notícias."
                show aunt 139 with dissolve
                dia "Minha pá bateu as botas hoje."
                show aunt 141
                show player 10
                player_name "Oh! Puts... Que droga."
                show aunt 140
                show player 1
                dia "Temos que esperar até eu comprar outra..."
                dia "Desculpa, {b}[firstname]{/b}."
                show aunt 141
                show player 2
                player_name "Está tudo bem, tia Diane."

                $ quest_list.append(quest20)
                if shovel not in inventory.items:
                    show player 2 at left
                    show aunt 1 at right
                    player_name "Algo mais que podemos fazer sem isso?"
                    show aunt 2
                    show player 1
                    dia "Nós precisamos cavar o jardim então... acho que não."
                    show aunt 8
                    show player 11
                    dia "A menos que..."
                    show player 10
                    show aunt 1
                    player_name "A menos que?"
                    show player 11
                    show aunt 2
                    dia "...Você não teria uma pá em casa?"
                    show player 4
                    show aunt 1
                    player_name "Hmm..."
                    show player 2
                    player_name "Talvez nós tenhamos uma {b}pá{/b} na nossa garagem!"
                    player_name "Vou lá ver e voltarei aqui se encontrar algo."
                    show player 203
                    show aunt 3
                    dia "Ótimo!"
                    show aunt 2
                    dia "Agradeço muito por você querer me ajudar! Volte quando você encontrar a ferramenta!"
                else:
                    show player 2 at left
                    show aunt 1 at right
                    player_name "Na verdade eu acho que eu tenho uma aqui na minha bolsa..."
                    label have_shovel:
                        show player 239_240
                        player_name "Hmm..."
                        show player 241
                        $ renpy.pause()
                        show player 242
                        $ renpy.pause()
                        show player 243
                        $ renpy.pause()
                        show player 244
                        player_name "Aqui!"
                        show player 243
                        show aunt 3
                        dia "Ohh! Ótimo!"
                        show aunt 2
                        dia "Eu sabia que você iria conseguir uma!"
                        dia "Certo! Antes de comer, tenho que te contar o que eu quero..."
                        show aunt 14 at right
                        show player 11 at left with dissolve
                        dia "Tenha certeza que você deixe {b}apenas{/b} vegetais que são {b}grandes{/b} e {b}duro{/b}!"
                        show aunt 14 at right
                        show player 11 at left
                        dia "Tire qualquer outra coisa que não seja isso... Especialmente esses ratos e insetos! ...Entendido?"
                        show aunt 1 at right
                        show player 14 at left
                        player_name "Entendido!!"
                        show aunt 2 at right
                        show player 1 at left
                        dia "Ah! ...E lembre-se de colocar todo o seu dinheiro no {b}banco{/b},quano você terminar!"
                        show aunt 1 at right
                        show player 4 at left
                        player_name "Umm... claro. Acho que posso fazer isso..."
                        show aunt 3 at right
                        show player 1 at left
                        dia "Obrigada pela ajuda, queirdo!"
                        hide aunt 3 at right
                        hide player 1 at left
                        show aunt 11 at left
                        player_name "..."
                        hide aunt 11 at left with dissolve
                        show unlock6 at truecenter
                        $ renpy.pause()
                        hide unlock6 with dissolve
                        $ loc_bank_unlocked = True
                        show expression "boxes/popup_garden.png" at truecenter with dissolve
                        $ renpy.pause()
                        hide expression "boxes/popup_garden.png" with dissolve
                        $ aunt_dialogue_advance = True
                        $ map_status_count = 3
                        $ completed_quests.append(quest20)
                        $ callScreen(location_count)

        elif aunt_count == 1 and quest21 not in completed_quests and garden_done >= 3:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)

            scene location_garden_blur
            if quest21 in quest_list:
                show player 203 at left
                show aunt 2 at right
                dia "Aqui está você!!"
                dia "Estava esperando você aparece."
                show player 14
                show aunt 1
                player_name "Oi, tia Diane."
                show player 203
                show aunt 8
                dia "Você acha que pode ajudar sua tia com o carrinho agora?"
                show player 14
                player_name "Sem problemas, tia Diane!"
                player_name "Deixa eu tentar!"
                show player 251 with dissolve
                player_name "Hmm..."
                show player 252
                player_name "Não deve ser tão pesado."
            else:

                show player 203 at left with dissolve
                show aunt 2 at right with dissolve
                dia "Aqui está você!!"
                dia "Estava esperando você aparece."
                show player 2
                show aunt 1
                player_name "Oi, tia Diane!"
                player_name "Tem algo errado?"
                show aunt 2
                show player 203
                dia "Está tudo ótimo! Você tem feito um bom trabalho, até agora..."
                dia "Na verdade, você está indo tão bem, que temos que jogar até alguns vegetais fora!"
                show aunt 1
                show player 17
                player_name "Desculpa por isso. Haha."
                show aunt 2
                show player 203
                dia "Estava tentando me livrar das sobras com o {b}carrinho de mão{/b}..."
                dia "Mas é muito pesado, e as dores da idade da sua tia são maiores!"
                dia "Você acha que poderia me ajudar?"
                show player 14
                show aunt 1
                player_name "Claro!"
                player_name "É para isso que estou aqui!"
                show player 10
                player_name "Mas... onde você quer que eu jogue isso?"
                show player 203
                show aunt 2
                dia "Estava pensando atrás da casa, perto da floresta."
                dia "Há uma pequena vala onde costumo colocar todo o lixo do jardim..."
                dia "Está um pouco longe, mas tenho certeza que você vai conseguir!"
                show player 2
                show aunt 1
                player_name "Sem problemas, tia Diane!"
                player_name "Vou fazer isso!"
                show player 251 with dissolve
                player_name "Hmm..."
                show player 252
                player_name "Não parece ser tão pesado."
                $ quest_list.append(quest21)

            if pStats.str() >= 2:
                show player 255 at left
                show aunt 1 at right
                player_name "Aqui vamos nós."
                player_name "Não é tão pesado!"
                show player 254
                show aunt 5
                dia "!!!" with hpunch
                dia "Wow... Você levantou isso como se não fosse nada!"
                show player 255
                player_name "Bom, eu tava treinando na academia..."
                show player 254
                show aunt 2
                dia "Ohh! Alguém está ficando muito forte!"
                show player 255
                show aunt 1
                player_name "Haha. Acho que sim."
                show player 254
                show aunt 8
                dia "Alongue esses músculos e me siga para trás da casa ... lindinho..."

                hide location_garden_blur
                hide player
                hide aunt
                scene location_garden_cutscene04
                show text "A vala atrás de sua casa estava tão longe!\n Quase não consegui; o carrinho de mão ficava escorregando das mãos. \n Fiquei feliz de mostrar para a tia Diane que eu era forte o suficiente para fazer isso..." at Position (xpos= 512, ypos = 700)
                with fade
                $ renpy.pause()
                hide text
                hide location_garden_cutscene04
                scene location_garden_blur
                show aunt 5 at right
                show player 18 at left
                with dissolve
                dia "Não acredito que você fez isso com tanta facilidade!"
                show player 17
                show aunt 1
                player_name "Foi bem difícil na verdade. Haha!"
                show player 203
                show aunt 2
                dia "Espero que você não me odeia por causa disso..."
                show player 2
                show aunt 1
                player_name "Está tudo bem."
                player_name "Tinha que ser feito, e não me importei com o exercício!"

                show player 203
                show aunt 8
                dia "Me diga..."
                dia "...como você ficou nessa forma?"
                show aunt 9
                show player 11
                player_name "..."
                show player 21
                player_name "Como assim?"
                show aunt 3
                show player 13
                dia "Ficando bonito e forte assim!"
                show aunt 6
                show player 11
                dia "Eu tento me mexer o tempo todo... Mas eu sempre sinto gorda."
                show aunt 1
                show player 10
                player_name "Gorda?"
                show aunt 7
                show player 29
                player_name "Acho que você está muito bem, {b}tia Diane{/b}."
                show aunt 12
                show player 13
                dia "Você diz isso assim, mas nunca me viu sem roupas..."
                show aunt 13
                show player 11
                player_name "..."
                show aunt 5
                dia "Err... Que seja!"
                show aunt 8
                dia "Qual seu segredo?"
                dia "Você esteve treinando?"
                show aunt 9
                show player 21
                player_name "Um pouco."
                show player 35
                player_name "Eu tento ir a academia as vezes."
                show aunt 2
                show player 13
                dia "Sério?!"
                dia "Que bacana!"
                show aunt 14
                dia "Sabe, há muitas boas vantagens para se manter em forma."
                show aunt 8
                show player 11
                dia "Mulheres adoram homens fortes, flexíveis e que tenham bastante... fôlego."
                show aunt 9
                player_name "..."
                show aunt 10
                dia "Me mostra seus abdômens!"
                show aunt 9
                show player 22
                player_name "!!!" with hpunch
                show player 21
                player_name "Você quer ver meu..."
                show aunt 10
                show player 11
                dia "Seus músculos! Sim."
                dia "Me mostra!"
                show aunt 9
                show player 10
                player_name "Ok..."
                show aunt 7
                show player 249
                show aunt 12
                dia "Wow!!"
                show aunt 10
                dia "Belo corpo!"
                show aunt 8
                dia "Você deve fazer sucesso com as mulheres da escola..."
                show aunt 9
                show player 250
                player_name "Na verdade não."

                show aunt 7
                show player 108f
                player_name "Tem caras muito mais fortes que eu na escola."
                player_name "E eu não sou aqueles caras descolados..."
                show player 109f
                show aunt 8
                dia "Não tem problema, sabe."
                show aunt 6
                show player 13
                dia "As garotas nem sempre querem os descolados."
                show aunt 5
                dia "Apenas tenha calma!"
                show aunt 4
                show player 17
                player_name "Valeu, {b}tia Diane{/b}."
                show aunt 2
                show player 203
                dia "Muito obrigada por me ajudar com o carrinho de mão!"
                dia "Agora podemos voltar a trabalhar no jardim!"
                show player 2
                show aunt 1
                player_name "Claro! Vou pegar as ferramentas e já começamos..."
                $ completed_quests.append(quest21)
                $ aunt_dialogue_advance = True
            else:

                show player 253 at left with dissolve
                $ renpy.pause()
                show player 256 at Position(xpos=0.0322,ypos=1.0000) with dissolve
                show aunt 1 at right
                player_name "[str_warn]Ughhh!!..."
                player_name "[str_warn]...Ghhh..."
                show player 27 with dissolve
                player_name "[str_warn]I... Não consigo fazer isso, {b}tia Diane{/b}..."
                player_name "[str_warn]Desculpa..."
                show player 3
                show aunt 2
                dia "Ah..."
                dia "Está tudo bem... tudo bem. Não sabia que estava tão pesado..."
                dia "Mas não se preocupe, vou achar alguém que consiga fazer isso para mim."
                show player 23
                player_name "Espere... Posso fazer isso!"
                show player 256 with dissolve
                dia "..."
                show player 10 with dissolve
                player_name "Acho que estou cansado, deve ser isso..."
                player_name "Vou descansar e recuperar minha {b}força{/b}. Vou voltar e fazer isso, prometo."
                show aunt 1
                show player 3
                dia "..."
                show aunt 3
                show player 5
                dia "Você é tão persistente!"
                show aunt 2
                show player
                dia "Certo. Vejo você em breve!"
                show player 2
                show aunt 1
                player_name "Valeu, tia Diane!"
                hide player with dissolve
                hide aunt with dissolve

        elif aunt_count == 2 and quest08 not in quest_list:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)
            scene garden
            show player 1 at left with dissolve
            show aunt 2 at right with dissolve
            dia "Hey!"
            show player 14 at left
            show aunt 1 at right
            player_name "Oi {b}tia Diane{/b}!"
            show aunt 3 at right
            show player 1 at left
            dia "Pronto para colher alguns vegetais?"
            show aunt 4 at right
            show player 17 at left
            player_name "Uhum!"
            show aunt 14 at right
            show player 1 at left
            dia "Oh! Antes de você começar..."
            show aunt 2 at right
            dia "Você poderia me fazer um favor e pegar a {b}bomba{/b} no {b}galpão{/b}?"
            show aunt 1 at right
            show player 12 at left
            player_name "Uma {b}bomba{/b}?"
            show aunt 2 at right
            show player 1 at left
            dia "Sim! Deve estar em algum lugar no galpão..."
            show aunt 1 at right
            show player 14 at left
            player_name "Uhh.. Ok, vou procurar."
            show aunt 3 at right
            show player 1 at left
            dia "Obrigada, {b}lindinho{/b}!"
            $ shed_unlocked = True
            $ quest_list.append(quest08)
            hide player 1 at left with dissolve
            hide aunt 3 at right with dissolve

        elif aunt_count == 3 and not aunt_dialogue_advance and quest09 not in quest_list:
            if not gTimer.is_weekend():
                if in_garden:
                    $ in_garden = False
                    $ callScreen(location_count)
                scene garden
                show player 106 at left with dissolve
                show aunt 2 at right with dissolve
                dia "Oh, {b}[firstname]{/b}!"
                show player 23
                dia "Estou tão feliz por você estar aqui..."
                show player 24
                player_name "Você precisa de algo?"
                show player 3
                dia "Sim!!"
                dia "Estou atrasada e preciso de um favor."
                show player 1
                player_name "Claro, {b}tia Diane{/b}! Qualquer coisa que você precisar!"
                show player 2
                dia "Ótimo!"
                dia "Quero que você faça uma {b}pequena entrega{/b} para mim."
                show player 3
                dia "O {b}pacote{/b} precisa ser entregue na {b}escola{/b}, hoje!"
                show player 1
                player_name "Espera. Você quer que eu entregue algo... na {b}minha{/b} escola?"
                show player 3
                dia "Sim! É {b}leite fresco{/b}!"
                show aunt 1
                player_name "..."
                player_name "Você... produz leite?"
                show aunt 6
                dia "Eu sei..."
                dia "Comecei não faz muito tempo."
                show aunt 108
                dia "Que seja, não tenho tempo para explicar. Aqui está o {b}recibo{/b}."
                show aunt 1
                player_name "Mas, {b}tia Diane{/b}, onde está o pacote? E onde eu entrego isso?"
                show aunt 22
                dia "Ah, certo! Desculpa..."
                show aunt 23
                dia "O pacote está no {b}galpão{/b}. Entregue na {b}cantina{/b}."
                show aunt 24
                player_name "Ok, farei isso."
                show aunt 2
                dia "Muito obrigada, {b}[firstname]{/b}."
                show aunt 14
                dia "Oh! E não demore muito! Não queremos que o leite estrague!."
                $ quest_list.append(quest09)
                $ lock_ui()
            else:

                scene garden
                show player 106 at left with dissolve
                show aunt 2 at right with dissolve
                dia "Oh, {b}[firstname]{/b}!"
                show player 23
                dia "Estou tão feliz por você estar aqui..."
                show player 24
                player_name "Precisa de algo?"
                show player 3
                dia "Sim!!"
                dia "Estou atrasada e preciso de um grande favor."
                show player 1
                player_name "Claro, {b}tia Diane{/b}! Qualquer coisa que você precisar!"
                show player 2
                dia "Ótimo!"
                dia "Quero que você faça uma {b}pequena entrega{/b} para mim."
                show player 3
                dia "O {b}pacote{/b} precisa ser entregue na {b}escola{/b}, então volte quando a escola estiver aberta."
                show player 1
                player_name "Ok."

        elif aunt_count == 4 and not aunt_dialogue_advance and quest10 not in quest_list:
            if quest10 in quest_list and quest10 not in completed_quests:
                scene garden_dead with None
            else:

                scene garden with None
            show player 11 at left with dissolve
            show aunt 106 at right with dissolve
            dia "{b}[firstname]!!!{/b}"
            show player 10
            show aunt 107
            player_name "{b}Tia Diane{/b}?"
            player_name "Está tudo bem??"
            show player 11
            show aunt 23
            dia "Meus vegetais!!"
            show player 23
            show aunt 22
            dia "Eles estão todos {b}destruídos{/b}!"
            show player 10
            player_name "O que você quis dizer? Como assim?"
            show player 11
            show aunt 106
            dia "Algum... {b}inceto{/b}... É uma infestação!"
            show player 22
            dia "Tomou conta de todo o jardim!!"
            show player 10
            show aunt 107
            player_name "O quê?!"
            show player 5
            show aunt 23
            dia "Tenho que fazer algo antes que eu perca tudo..."
            show player 10
            show aunt 24
            player_name "Posso te ajudar de alguma forma?"
            show player 5
            show aunt 2
            dia "Eu estava pensando, talvez você pudesse {b}dar uma olhada{/b} nesses insetos, primeiro..."
            show aunt 3
            dia "Odeio essas coisas! Não suporto nem chegar perto deles! Eles me dão medo!"
            show player 14
            show aunt 4
            player_name "Claro, {b}tia Diane{/b}, Posso dar uma olhada."
            show player 13
            show aunt 14
            dia "Oh! Você acha pode {b}achar algum veneno{/b} para usar neles?"
            show player 10
            show aunt 9
            player_name "Uhh... Não me importaria..."
            show player 12
            player_name "Mas não sei onde eu encontraria."
            show player 11
            show aunt 6
            dia "Você poderia tentar na {b}CONSUM-R{/b}, lá no shopping."
            show aunt 10
            dia "Peça ajuda {b}de alguém{/b} que trabalha lá. Descreva que tipo de insetos nós temos..."
            show player 10
            dia "Tenho certeza que ajudarão você a achar o que precisamos."
            show player 21
            show aunt 9
            player_name "Certo, vou ver o que consigo fazer!"
            show player 13
            show aunt 3
            dia "Muito obrigada!"
            show aunt 10
            dia "Eu não sei o que faria sem você..."
            hide player
            show aunt 11 at Position (xpos = 584, ypos = 768)
            with dissolve
            player_name "..."
            $ quest_list.append(quest10)

        elif aunt_count == 5 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)
            scene garden
            show player 127 with dissolve
            player_name "Onde está a {b}tia Diane{/b}?"
            show player 12
            player_name "Nessas horas, ela sempre está aqui fora..."
            show player 56
            player_name "Ela deve estar em algum lugar."
            hide player 56 with dissolve
            $ lock_ui()

        elif aunt_count == 6 and not aunt_dialogue_advance:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)
            scene garden
            show player 1 at left with dissolve
            show aunt 19 at right with dissolve
            dia "Oiiiii, botão!"
            show player 1 at left
            show aunt 17 at right
            player_name "Oi {b}tia Diane{/b}!"
            show player 11 at left
            player_name "..."
            show aunt 52 at right
            show player 21 at left
            player_name "Umm... Você não está usando uma camisa, {b}tia Diane{/b}..."
            show player 13 at left
            dia "Oh! É mesmo! Haha!"
            show aunt 19 at right
            dia "Não me lembro o que aconteceu!"
            show aunt 17 at right
            show player 21 at left
            player_name "...Você perdeu?"
            show aunt 19 at right
            show player 13 at left
            dia "Deve ter sido essas margaritas mexendo com minha cabeça!"
            show aunt 17 at right
            show player 17 at left
            player_name "Haha, percebo."
            show player 1 at left
            show aunt 18 at right
            dia "Quer saber?"
            dia "Acho que temos que tirar um dia de folga lá do jardim... E relaxar!"
            show aunt 19 at right
            show player 11 at left
            dia "O que você acha?"
            menu:
                "Claro!":
                    show player 17 at left
                    show aunt 17 at right
                    player_name "Claro! Acho que podemos..."
                    show aunt 18 at right
                    show player 1 at left
                    dia "Vamos curtiur o sol esta tarde!"
                    show aunt 19 at right
                    dia "Não há nada melhor do que um pouco de sol em um dia quente!"
                    show aunt 17 at right
                    show player 1 at left
                    player_name "Umm... Eu poderia pegar um bronzeado."
                    show aunt 20 at right
                    show player 11 at left
                    dia "Primeiro você tem que me...  ajudar com umas coisinhas!"
                    show aunt 21 at right
                    window hide
                    pause
                    show aunt 20 at right
                    window hide
                    pause
                    show aunt 21 at right
                    window hide
                    pause
                    show aunt 20 at right
                    window hide
                    pause
                    show player 21 at left
                    player_name "Você quer ajuda?... Com... o protetor solar?"
                    show aunt 19 at right
                    show player 13 at left
                    dia "Uhum, isso!"
                    show aunt 18 at right
                    dia "Quem mais poderia passar nas minhas costas?"
                    dia "Você não quer que sua tia fique queimada, né?"
                    show aunt 17 at right
                    show player 21 at left
                    player_name "Ok. Acho que posso te ajudar..."
                    show aunt 19 at right
                    show player 11 at left
                    dia "Deixe-me apenas pegar a cadeira... Você espera beeeem aqui!"
                    hide player
                    scene garden_close
                    show aunt 25
                    with dissolve
                    player_name "( Hmmm... Ok... )"
                    player_name "( Como eu vou fazer isso... )"
                    show aunt 26
                    player_name "( Essas alças estão encomodando... )"
                    player_name "( ...Talvez eu pudesse... )"
                    show aunt 27
                    player_name "( ...Tirar elas assim... )"
                    show aunt 28
                    player_name "( Aqui vamos nós! )"
                    player_name "( Agora, o crem... )"
                    show aunt 29
                    window hide
                    pause
                    show aunt 30
                    window hide
                    pause
                    show aunt 31
                    player_name "Woah..."
                    player_name "( Não acredito, estou tocando a {b}tia Diane{/b}'s pelada de costas... )"
                    show aunt 30
                    window hide
                    pause
                    show aunt 31
                    window hide
                    pause
                    show aunt 30
                    player_name "( É tão macia... e quente... )"
                    show aunt 31
                    window hide
                    pause
                    show aunt 30
                    window hide
                    pause
                    show aunt 32
                    player_name "..."
                    show aunt 32
                    window hide
                    pause
                    show aunt 33
                    window hide
                    pause
                    show aunt 34 with hpunch
                    player_name "( Mas que- )"
                    player_name "( Ela tirou a calça... )"
                    player_name "( Ela quer que eu vá mais pra baixo?? )"
                    player_name "..."
                    show aunt 35
                    window hide
                    pause
                    show aunt 36
                    window hide
                    pause
                    show aunt 35
                    window hide
                    pause
                    show aunt 36
                    player_name "( Talvez eu pudesse chegar... um pouco mais perto... no futuro... )"
                    show aunt 36
                    window hide
                    pause
                    show aunt 37
                    window hide
                    pause
                    show aunt 36
                    window hide
                    pause
                    show aunt 37 with hpunch
                    player_name "( Merda! Fui longe de mais! )"
                    show aunt 38
                    player_name "( Ela está acordando... )"
                    show aunt 39 at Position (xpos = 484, ypos = 768)
                    with dissolve
                    player_name "Desculpa, {b}tia Diane{/b}!!"
                    player_name "Eu sei, não devia ter feito!"
                    show aunt 40
                    dia "O que você está esperando?"
                    dia "Você fez um boooom trabalho..."
                    show aunt 41
                    dia "..."
                    show aunt 42
                    dia "Por que você não está olhando para mim?"
                    player_name "É que... Você está pelada, {b}tia Diane{/b}!"
                    show aunt 46
                    dia "E daí? ...Você nunca tinha visto uma mulher pelada antes?"
                    dia "...É completamente natural..."
                    show aunt 43
                    window hide
                    pause
                    show aunt 43
                    player_name "..."
                    show aunt 44
                    player_name "Uhh! Deixa eu pegar uma toalha!"
                    show aunt 45
                    dia "{b}Espera, só um segundo!!{/b}"
                    dia "Nós não estamos terminados ainda..."
                    dia "Você não vai me passar protetor na frente?"
                    show aunt 47
                    player_name "..."
                    show aunt 48
                    window hide
                    pause
                    show aunt 49 with hpunch
                    window hide
                    pause
                    show aunt 50
                    player_name "...Oh, merda! De novo não!"
                    dia "Oh! Wow!"
                    player_name "Desculpa! Tenho que ir!"
                    show aunt 51
                    with dissolve
                    dia "Hey, espere um segundo!"
                    hide aunt 51
                    with dissolve
                    $ drunk_dialogue = True
                    $ aunt_dialogue_advance = True
                    jump map_dialogue
                "Melhor não.":

                    show player 17 at left
                    show aunt 53 at right
                    player_name "Eu adoria, mas eu tenho que trabalhar no jardim..."
                    show player 1 at left
                    dia "Você tem que se divertir as vezes, sabe..."
                    show aunt 18 at right
                    dia "Mas eu compreendo..."
                    show aunt 17 at right
                    show player 14 at left
                    player_name "Talvez outra hora!"
                    hide aunt 17 at right with dissolve
                    hide player 14 at left with dissolve
                    $ callScreen(location_count)

        elif aunt_count == 6 and aunt_dialogue_advance and drunk_dialogue:
            scene townmap
            player_name "Eu deveria ir na {b}tia Diane{/b} outra hora..."
            jump map_dialogue

        elif aunt_count == 7 and not aunt_apology_seen:
            if in_garden:
                $ in_garden = False
                $ callScreen(location_count)

            if drunk_dialogue:
                scene garden
                show player 5 at left with dissolve
                show aunt 23 at right with dissolve
                dia "Hey {b}[firstname]{/b}..."
                show aunt 24 at right
                show player 10 at left
                player_name "Oi {b}tia Diane{/b}..."
                player_name "..."
                show player 24 at left
                player_name "Umm... Quero me desculpar sobre o outro dia..."
                show player 17 at left
                show aunt 23 at right
                show player 5 at left
                dia "Pare."
                dia "Eu quem tenho que me desculpar."
                show aunt 22 at right
                dia "Eu bebi demais... E... eu estava muito bêbada."
                show player 21 at left
                player_name "Está tudo bem, tia Diane..."
                show aunt 23 at right
                show player 13 at left
                dia "Podemos deixar isso em segredo?"
                show aunt 24 at right
                show player 29 at left
                player_name "Não se preocupe... Não vou contar a {b}[mom_name]{/b}."
                player_name "Não foi nada de mais."
                hide player
                show aunt 11 at left
                dia "Aw! Obrigada, querido. É por isso que você é meu sobrinho favorito!"
                hide aunt 11 at left
                $ aunt_apology_seen = True
                $ callScreen(location_count)
        else:

            if aunt_count < 8 and aunt_count != 5:
                if in_garden:
                    $ in_garden = False
                    $ callScreen(location_count)

                if quest10 in quest_list and quest10 not in completed_quests:
                    scene garden_dead
                else:

                    scene garden
                show player 1 at left with dissolve
                show aunt 5 at right with dissolve
                dia "Ei, lindinho! Você voltou para ajudar sua pobre tia a escolher os vegetais?"
                show player 14 at left
                show aunt 7 at right
                player_name "Você não é tão velha, {b}tia Diane{/b}."
                show player 1 at left
                show aunt 7 at right
                dia "Aw... Obrigada, seu fofo!"
                hide player 1
                show aunt 11 at left
                player_name "..."
                hide aunt 11 at left with dissolve
            $ callScreen(location_count)
    else:

        if quest09 in completed_quests and not aunt_shed_scene and aunt_count < 8:
            if quest10 in quest_list and quest10 not in completed_quests:
                scene garden_dead_night
            else:

                scene garden_night
            show player 12 with dissolve
            player_name "Estranho..."
            show player 30
            player_name "O galpão da Tia Diane {b}ainda está aberto{/b}..."
            hide player 30 with dissolve
        else:

            if aunt_count < 8:
                jump night_closed_garden
    $ callScreen(location_count)

label aunt_button_dialogue:
    if aunt_drink_made:
        $ aunt_drink_made = False
        $ aunt_drink_offered = False
        scene location_garden_close_blur
        if aunt_extra_shot:
            $ aunt_extra_shot = False
            show player 136 at left with dissolve
            show aunt 100 at right with dissolve
            player_name "Aqui está a sua {b}bebida{/b}!"
            show aunt 94
            show player 1
            dia "Minha bebida favorita!"
            show aunt 97
            show player 18
            dia "Você sabe como agradar sua {b}tia{/b}... E isso é muito fofo da sua parte..."
            show player 11
            show aunt 95
            dia "..."
            show player 13
            show aunt 94
            dia "Foi delicioso..."
            show player 33
            show aunt 98
            player_name "Fico feliz que você tenha gostado!"
            show player 11
            show aunt 96
            dia "Uau... É bem forte, haha!"
            dia "Estou me sentindo um pouco... {b}tonta{/b}!"
            show aunt 98
            show player 21
            player_name "Você está bem?"
            show player 13
            show aunt 97
            dia "Ah, eu estou bem..."
            show player 11
            show aunt 99
            dia "Apenas pegue minha {b}cadeira{/b}, para que eu deite um pouco..."
            hide player
            scene garden_close
            show aunt 65 at Position (xpos = 490, ypos = 768)
            with dissolve
            player_name "Está tudo certo?"
            show aunt 66
            dia "Oh, siiiim... Tudo maravilhoso!"
            show aunt 65
            player_name "Eu deveria... voltar ao trabalho?"
            show aunt 67
            dia "Acho que deveriamos nos divertir e relaxar..."
            show aunt 68
            player_name "Haha! Ok."
            show aunt 65
            player_name "Umm... O que faremos para nos divertir então?"
            show aunt 67
            dia "Eu acho que devemos continuar onde paramos."
            player_name "..."
            show aunt 65
            player_name "O qu-que você quer dizer?"
            show aunt 67
            dia "Você sabe bem, garoto..."
            show aunt 69
            show aunt 70
            show aunt 71 with hpunch
            player_name "!!!"
            show aunt 72
            dia "O que estamos esperando?"
            show aunt 73
            player_name "Não sei se deveriamos..."
            show aunt 72
            dia "Eu sei que você quer {b}sentir eles{/b} com suas mãos..."
            show aunt 74
            dia "Eles são gostosos e macios..."
            dia "É isso..."
            show aunt 75
            dia "Apenas sinta..."
            show aunt 77
            window hide
            pause
            show aunt 78
            window hide
            pause
            show aunt 75
            dia "Vá com calma..."
            dia "...e aperte eles bem de leve..."
            show aunt 77_78_76
            pause 4
            dia "..."
            show aunt 75
            dia "Você pode me levantar... lindinho?"
            show aunt 79 with hpunch
            player_name "!!!"
            dia "Como eu imaginava..."
            dia "Você gostosa de brincar com o corpo de sua {b}tia{/b}..."
            show aunt 80
            player_name "Eu... Eu não posso me controlar..."
            show aunt 81
            player_name "!!!"
            dia "Eu não vejo um pau tão duro assim há muito tempo..."
            dia "...E o seu é... Muito grande..."
            show aunt 83_82
            pause 4
            show aunt 81
            dia "Isso é bom?"
            show aunt 83_82
            pause 4
            show aunt 84 with hpunch
            player_name "Oh, merda!"
            show aunt 85
            dia "Bom... Isso não durou muito!"
            player_name "Desculpa, {b}tia Diane{/b}!"
            dia "Não precisa!"
            dia "Vamos limpar isso na {b}cozinha{/b}..."
            scene dianekitchen
            with dissolve
            show player 138 at left
            show aunt 86 at right
            with dissolve
            dia "Aqui, use isso!"
            show player 140
            show aunt 91
            player_name "Valeu..."
            show player 139
            show aunt 92
            dia "Ouça, {b}[firstname]{/b}."
            dia "Vamos ser honestos um com o outro..."
            show aunt 87
            dia "...Você óbviamente está desejando {b}meu corpo{/b}..."
            show aunt 92
            dia "...e sua {b}tia{/b} não tem atenção masculina fazem anos..."
            show aunt 89
            dia "...Então, por que não mantemos essa coisa apenas {b}ente nós dois{/b}?"
            show aunt 91
            show player 140
            player_name "Como assim?"
            show player 139
            show aunt 87
            dia "Bom... Apenas avise se você quiser \"algo a mais\" da sua {b}tia{/b}..."
            show aunt 89
            dia "...e não contamos a ninguém sobre isso!"
            show player 140
            show aunt 88
            player_name "Eu acho que... nós podemos fazer isso."
            show player 139
            show aunt 90
            dia "Sua mãe não pode ficar sabendo disso, ou ela me matará!!"
            show player 140
            show aunt 91
            player_name "Não se preocupe. Não vou contar."
            show player 139
            show aunt 90
            dia "Essa é o meu garoto!"
            show aunt 89
            dia "Teremos muita {b}diversão{/b} juntos..."
            hide player
            show aunt 93 at left
            with dissolve
            window hide
            pause
            $ unlock_ui()
            $ in_garden = True
            $ aunt_drink_active = False
            $ aunt_dialogue_advance = True
            jump garden_dialogue

    elif aunt_count < 8:
        scene location_garden_close_blur
        show player 1 at left with dissolve
        show aunt 5 at right with dissolve
        dia "Ei, querido! Você voltou para ajudar sua {b}tia{/b} a colher os vegetais?"
        show player 14 at left
        show aunt 7 at right
        player_name "Não acho que você é tão velha assim, {b}tia Diane{/b}."
        show player 1 at left
        show aunt 5 at right
        dia "Aw... Você é tão querido!"
        show aunt 10 at right
        dia "Existe mais alguma coisa que eu possa fazer por você antes de começarmos?"
        label dia_default_dialogue_options:
            menu:
                "Conversar.":
                    show aunt 1 at right
                    show player 17 at left
                    player_name "Eu só queria sentimos faltas das suas visitas em casa!"
                    show aunt 7
                    show player 10
                    player_name "Você costumava passar muito mais tempo e sair com a {b}[mom_name]{/b}..."
                    show aunt 22
                    show player 13
                    dia "Acho..."
                    show aunt 23
                    dia "Acho que a {b}tia{/b} gosta de ficar sozinha."
                    show aunt 24
                    show player 10
                    player_name "Está tudo bem?"
                    show aunt 3
                    show player 13
                    dia "Claro!"
                    show aunt 23
                    dia "Eu só..."
                    show aunt 6
                    dia "Bom... Depois do meu último divórcio..."
                    dia "Eu acho que... Não faz mais sentido conhecer novas pessoas."
                    show aunt 14
                    dia "Então eu não saio mais tanto!"
                    show aunt 1
                    show player 108f
                    player_name "Ah. Entendi..."
                    show aunt 14
                    show player 13
                    dia "Você talvez não sabia, mas eu costumava sair muito com a sua mãe!"
                    show aunt 8
                    show player 11
                    dia "Nós éramos conhecidas na cidade como {b}gêmeas siamesas{/b}..."
                    show aunt 3
                    dia "Nós íamos para festas o tempo todo!"
                    show aunt 4
                    show player 21
                    player_name "Sério?"
                    show aunt 2
                    show player 13
                    dia "Pode acreditar!"
                    show aunt 10
                    dia "Nós íamos para encontros e dançávamos a noite toda."
                    show aunt 6
                    show player 11
                    dia "Foi assim que sua mãe conheceu seu pai, e eu conheçi todos os idiotas dos meus ex."
                    show aunt 12
                    show player 5
                    dia "Isso é o que eu recebo por beber demais e tomar decisões erradas! Haha..."
                    show aunt 13
                    player_name "..."
                    show aunt 10
                    show player 11
                    dia "Mas você não é igual aos outros caras!"
                    dia "Você é gentil, bonito, jovem..."
                    show aunt 7
                    dia "..."
                    show aunt 22
                    dia "Por que estou dizendo isso? Você não precisa ouvir sobre os problemas da sua tia!"
                    show aunt 24
                    show player 21
                    player_name "Está tudo bem, não me importo em ouvir suas histórias."
                    show aunt 3
                    show player 13
                    dia "Você é tão bacana!"
                    show aunt 10
                    dia "Algo a mais que você queria conversar?"
                    jump dia_default_dialogue_options

                "Encontrei uma pá" if quest20 in quest_list and quest20 not in completed_quests and shovel in inventory.items:
                    show player 2 at left
                    show aunt 1 at right
                    player_name "Encontrei uma {b}pá{/b} na minha garagem!"
                    jump have_shovel

                "O jargim." if quest20 in completed_quests:
                    show aunt 1 at right
                    show player 29 at left
                    player_name "Sobre o jardim... O que você quer que eu faça mesmo?"
                    show aunt 2
                    show player 13
                    dia "Preciso de você limpe-o e remova todas as coisas indesejadas."
                    show aunt 14 at right
                    show player 11 at left
                    dia "Certifique-se de que deixe {b}apenas{/b} vegetais {b}longos{/b} e {b}duros{/b}!"
                    show aunt 14 at right
                    show player 11 at left
                    dia "Se não for isso, retire tudo... Especialmente aqueles ratos e insetos...! Você entendeu?"
                    show aunt 1 at right
                    show player 14 at left
                    player_name "Entendi!!"
                    show player 1
                    show aunt 2
                    dia "Algo a mais que você queira conversar?"
                    jump dia_default_dialogue_options

                "A bomba." if quest08 in quest_list and quest08 not in completed_quests:
                    show aunt 1
                    show player 29
                    player_name "Uhm... Sobre a bomba."
                    show aunt 2
                    show player 13
                    dia "Ah, certo. Você conseguiu encontrar?"
                    menu:
                        "Onde está?":
                            show aunt 1 at right
                            show player 14 at left
                            player_name "Onde você disse que estava mesmo?"
                            show aunt 2 at right
                            show player 1 at left
                            dia "Já te disse antes."
                            dia "Deve estar na {b}prateleira{/b}, no {b}galpão{/b}!"
                            show aunt 1 at right
                            show player 14 at left
                            player_name "Uhh... Ok. Vou procurar lá."
                            jump dia_default_dialogue_options
                        "Ainda não.":

                            show player 10 at left
                            show aunt 1 at right
                            player_name "Ainda não encontrei..."
                            show aunt 2 at right
                            show player 13 at left
                            dia "Tudo bem!"
                            show aunt 3 at right
                            dia "Apenas me traga quando você achar."
                            show aunt 1 at right
                            show player 17 at left
                            player_name "Trarei!"
                            hide player 17 at left with dissolve
                            hide aunt 1 at right with dissolve
                            jump dia_default_dialogue_options

                        "Achei!" if pump in inventory.items:
                            show player 17 at left
                            show aunt 1 at right
                            player_name "Sim, não foi muito difícil achar!"
                            show player 239_240
                            pause
                            show aunt 2 at right
                            show player 103 at left
                            player_name "Aqui..."
                            $ inventory.items.remove(pump)
                            show player 1 at left
                            show aunt 54 at right
                            dia "Obrigada!"
                            show player 21 at left
                            show aunt 1 at right
                            player_name "Queria perguntar uma coisa..."
                            show aunt 2 at right
                            show player 13 at left
                            dia "Claro! O quê?"
                            show aunt 7 at right
                            show player 35 at left
                            player_name "O que é aquela {b}coisa{/b} grande naquele {b}galpão{/b}? Tem todo tipo de correntes..."
                            player_name "...E alguns tubos estranhos..."
                            show aunt 5 at right
                            show player 13 at left
                            dia "Aquilo..."
                            dia "É um {b}ordenhador{/b}!"
                            show aunt 7 at right
                            show player 21 at left
                            player_name "Tipo... Para fazer leite?"
                            show aunt 6 at right
                            show player 13 at left
                            dia "Sim, eu... Umm... tinha uma vaca! Isso!"
                            show aunt 7 at right
                            show player 21 at left
                            player_name "No seu {b}galpão{/b}?"
                            show aunt 5 at right
                            show player 13 at left
                            dia "Hmm... Sim, eu não podia deixar ela comer meu jardim!"
                            show aunt 9 at right
                            show player 35 at left
                            player_name "Enteni..."
                            show player 17 at left
                            player_name "Que seja, tenho que voltar para o trabalho!"
                            $ quest_complete(quest08)
                            $ aunt_dialogue_advance = True
                            hide player 17 at left with dissolve
                            hide aunt 9 at right with dissolve

                "Entrega de leite." if quest09 in quest_list and quest09 not in completed_quests:
                    show aunt 1
                    show player 14
                    player_name "Sobre aqueles leites que você me pediu para entregar."
                    show aunt 3
                    show player 1
                    dia "Ah sim!"
                    show aunt 2
                    dia "Como está indo? Você levou para a escola?"
                    menu:
                        "Onde na escola?":
                            show aunt 1
                            show player 29
                            player_name "Onde eu tinha que entregar na escola mesmo? Eu esqueci..."
                            show aunt 2
                            show player 13
                            dia "Na {b}cantina{/b}!"
                            show aunt 3
                            dia "É onde toda entrega vai."
                            show aunt 1
                            show player 17
                            player_name "Entendi!"
                            show aunt 14
                            show player 11
                            dia "Apresse-se antes de ficar muito quente!"
                            show aunt 1
                            show player 17
                            player_name "Farei! Obrigado."
                            jump dia_default_dialogue_options
                        "Ainda não.":

                            show aunt 1
                            show player 29
                            player_name "Ainda tenho que ir para a escola para entregar."
                            show aunt 2
                            show player 13
                            dia "Sem problemas."
                            show aunt 14
                            show player 11
                            dia "Mas não demore muito! O leite vai ficar quente..."
                            show aunt 1
                            show player 17
                            player_name "Farei! Obrigado."
                            jump dia_default_dialogue_options

                        "Eu entrego!" if quest09_3 == True:
                            show aunt 1 at right
                            show player 2 at left
                            player_name "Tenho ótimas notícias, {b}tia Diane{/b}!"
                            player_name "Minha diretoa quer o dobro de encomendas!"
                            show player 13
                            show aunt 2
                            dia "O quê? Sério?"
                            show aunt 1
                            show player 17
                            player_name "Ela disse que as pessoas gostaram!"
                            show player 13
                            show aunt 6
                            dia "Ótimo, isso vai me deixar ocupada..."
                            show aunt 10
                            dia "Talvez eu precisa de uma ajudinha para ordenhar mais leite."
                            show aunt 8
                            dia "Só espero que eu consiga produzir o suficiente..."
                            show player 2
                            show aunt 9
                            player_name "Qualquer coisa que você precisar, posso ajudar!"
                            show player 1
                            show aunt 8
                            dia "Bom saber."
                            show aunt 9
                            pause
                            show aunt 10
                            dia "Ah, antes de você ir..."
                            dia "Acho que eu nunca te ofereci {b}leite fresco{/b} que eu fiz!"
                            show aunt 9
                            show player 11
                            player_name "..."
                            show aunt 55 with fastdissolve
                            dia "Quer provar?"
                            show aunt 56
                            show player 12
                            player_name "É fresco? Coletado essa manhã??"
                            show aunt 55
                            show player 11
                            dia "Claro!"
                            show aunt 56
                            show player 21
                            player_name "Você comprou uma vaca nova ou o quê?"
                            show aunt 55
                            show player 13
                            dia "Err.. Não. Eu... comprei do fazendeiro hoje mais cedo!"
                            dia "Eu apenas empacotei aqui."
                            show aunt 56
                            show player 17
                            player_name "Ah sim..."
                            show aunt 55
                            show player 11
                            dia "Então? Quer provar?"
                            show aunt 56
                            menu:
                                "Claro!":
                                    show player 17 at left
                                    show aunt 55 at right
                                    player_name "Claro! Vou experimentar..."
                                    show aunt 10 at right
                                    show player 105 at left
                                    dia "Tenho o tanto quanto você quiser!"
                                    show aunt 9 at right
                                    window hide
                                    pause
                                    show player 104 at left
                                    player_name "..."
                                    show player 34 at left
                                    show aunt 10 at right
                                    dia "Então? É bom?"
                                    show aunt 9 at right
                                    show player 35 at left
                                    player_name "É quente..."
                                    show player 30 at left
                                    player_name "...E um pouco.. cremoso?"
                                    show aunt 3 at right
                                    show player 11 at left
                                    dia "Haha!"
                                    show aunt 10 at right
                                    dia "Pelo menos você gostou disso?"
                                    show aunt 9 at right
                                    show player 21 at left
                                    player_name "...Sim, não é ruim!"
                                    show aunt 10 at right
                                    show player 13 at left
                                    dia "Ótimo, eu poderia te dar um pouco mais tarde..."
                                    show aunt 4 at right
                                    show player 21 at left
                                    player_name "Claro, {b}tia Diane{/b}! Obrigado!"
                                    $ drink_milk_offer = True
                                    $ drank_milk = True
                                    hide player 21 at left with dissolve
                                    hide aunt 4 at right with dissolve
                                "Não gosto de leite.":

                                    show aunt 4 at right
                                    show player 21 at left
                                    player_name "Não, valeu... Não sou um grande fã de leite..."
                                    show aunt 8 at right
                                    show player 13 at left
                                    dia "Sério?"
                                    show aunt 14 at right
                                    dia "Não é tão ruim... Você não sabe o que está perdendo!"
                                    show aunt 1 at right
                                    show player 26 at left
                                    player_name "Eu acredito..."
                                    show player 17 at left
                                    player_name "Que seja, tenho que voltar ao trabalho!"
                                    $ drink_milk_offer = True
                                    hide player 17 at left with dissolve
                                    hide aunt 1 at right with dissolve
                            $ gTimer.tick()
                            $ completed_quests.append(quest09)
                            $ aunt_dialogue_advance = True
                            $ quest09_3 = False

                "Infestação de insetos." if quest10 in quest_list and quest10 not in completed_quests:
                    show aunt 1
                    show player 14
                    player_name "Sobre os problemas de insetos no jardim..."
                    show player 1
                    show aunt 23
                    dia "Ah sim, esses malditos {b}insetos{/b}."
                    dia "Você {b}achou um jeito{/b} de se livrar deles?"
                    menu:
                        "O que eu deveria fazer?":
                            show aunt 24
                            show player 29
                            player_name "Não sei o que fazer para me livrar deles..."
                            show aunt 14
                            show player 13
                            dia "Se eu fosse você, tentaria algum {b}pesticida{/b}."
                            show aunt 6
                            dia "Talvez procurar na {b}loja{/b}? Eles {b}ajudarão{/b} você a comprar o correto."
                            show aunt 1
                            show player 21
                            player_name "Beleza, vou dar uma olhada no shopping. Valeu!"
                            show aunt 2
                            show player 13
                            dia "Até mais!"
                            jump dia_default_dialogue_options
                        "Ainda não.":

                            show aunt 24
                            show player 29
                            player_name "Ainda não consegui solucionar."
                            show player 21
                            player_name "Mas não se preocupe, tia Diane! Encontrarei algum jeito!"
                            show player 13
                            show aunt 3
                            dia "Haha."
                            dia "Sei que vai!"
                            show aunt 2
                            dia "Volte quando tiver algum progresso."
                            jump dia_default_dialogue_options

                        "Consegui dar um jeito neles!" if infestation_done == True:
                            show aunt 24
                            show player 33
                            player_name "Acho que me livrei deles!"
                            show aunt 7
                            show player 2
                            dia "Você conseguiu?!"
                            show player 162
                            player_name "Sim, apenas apliquei o {b}pesticida{/b} que comprei na loja!"
                            show aunt 1
                            show player 12
                            player_name "Demorou um pouco, mas eles te deixarão em paz por um tempo!"
                            show aunt 3
                            show player 2
                            dia "Ótimo!"
                            show aunt 10
                            show player 11
                            dia "Eu sou tão sortuda de ter um... {b}sobrinho tão bom{/b}..."
                            show aunt 9
                            show player 29
                            player_name "Não foi nada, fico feliz em ajudar!"
                            show aunt 23
                            show player 11
                            dia "Quanto foi o pesticida?"
                            dia "Eu deveria te pagar."
                            show aunt 24
                            show player 21
                            player_name "Não se preocupe com isso. Não foi muito caro."
                            show aunt 14
                            show player 11
                            dia "Se você não me deixar te pagar, vou te dar um aumento no meu jardim!"
                            show aunt 4
                            player_name "..."
                            show aunt 10
                            show player 13
                            dia "Sua tia também sabe jogar o jogo!"
                            show aunt 9
                            show player 21
                            player_name "Você tem certeza?"
                            show aunt 10
                            show player 13
                            dia "Claro! Você foi muito útil me ajudando aqui!"
                            show aunt 3
                            dia "Você merece!"
                            show aunt 4
                            show player 21
                            player_name "Heh... Valeu."
                            $ upgrade_garden()
                            $ aunt_dialogue_advance = True
                            $ completed_quests.append(quest10)

                "Fazer uma bebida." if aunt_count == 6 and not aunt_dialogue_advance or aunt_count == 7 and not aunt_dialogue_advance:
                    if pStats.chr() >= 5:
                        $ aunt_drink_offered = True
                        show aunt 1 at right
                        show player 14 at left
                        player_name "Ei, tive uma ideia!"
                        show player 17
                        show aunt 7
                        player_name "Vamos fazer uma {b}bebida{/b} referescante e gostosa!"
                        show player 1
                        show aunt 5
                        dia "Oh... Não sei se eu deveria! Haha!"
                        show player 17
                        show aunt 7
                        player_name "Acho que vai te fazer bem!"
                        show player 14
                        player_name "Você merece!"
                        show player 1
                        show aunt 12
                        dia "Acho que você tem razão... Tem sido um dia duro!"
                        show player 14
                        show aunt 13
                        player_name "Onde você deixa as suas margaritas?"
                        show player 1
                        show aunt 5
                        dia "Você pode fazer na {b}cozinha{/b}..."
                        show aunt 14
                        dia "...Vou me acomodar enquanto espero..."
                        show player 17
                        show aunt 9
                        player_name "Já volto!!"
                        hide player 17 with dissolve
                        $ aunt_drink_active = True
                    else:

                        show aunt 1 at right
                        show player 29 at left
                        player_name "[chr_warn]Hey, Eu umm..."
                        show aunt 7
                        player_name "[chr_warn]...Você gostaria de uma {b}bebida{/b}?"
                        show player 3
                        show aunt 5
                        dia "Oh... Não acho que agora seja uma boa hora."
                        show player 24
                        player_name "[chr_warn]Achei... Que você fosse gostar..."
                        show aunt 22
                        show player 13
                        dia "Eu... tomo más decisões quando bebo..."
                        show player 24
                        show aunt 24
                        player_name "[chr_warn]Entendi..."
                        show player 21
                        player_name "[chr_warn]Talvez outra hora."
                        hide player 21 with dissolve
                        hide aunt 24 with dissolve
                "Tenho que ir trabalhar.":

                    show aunt 1 at right
                    show player 17 at left
                    player_name "Vou lá cuidar do jardim..."
                    dia "Está querendo usar esses músculos, hein!"
                    show player 11
                    show aunt 10
                    dia "Vem e dê um bom {b}beijo{/b} na sua {b}tia{/b}!"
                    hide player 11
                    show aunt 11 at left
                    player_name "..."
                    hide aunt 11 at left with dissolve
        $ callScreen(location_count)

    elif aunt_count >= 8:
        scene location_diane_kitchen_closeup
        show player 1 at left with dissolve
        show aunt 89 at right with dissolve
        dia "Oi, docinho..."
        if not gTimer.is_weekend():
            dia "Passando na casa da sua {b}tia{/b} depois da escola?"
        else:

            dia "Entediado em casa e quis vim ver sua tia?"
        show aunt 88
        show player 29
        player_name "Está tudo... bem?"
        show aunt 90
        show player 13
        dia "Claro!"
        show aunt 89
        dia "Estava esperando que você viesse para casa em busca de uma {b}diversão secreta{/b}..."
        show aunt 88
        show player 21
        player_name "Você quer... Fazer algo?"
        show aunt 89
        show player 13
        dia "O que você quer fazer?"
        label dia_default_dialogue_options_kitchen:
            menu:
                "Conversar.":
                    show aunt 109 at Position (xpos=947)
                    show player 21
                    player_name "Eu só queria dizer o quanto eu tenho pensado em visitar você..."
                    show aunt 89 at right
                    show player 13
                    dia "Você estava sentindo falta da sua {b}tia{/b}?"
                    show aunt 89
                    show player 21
                    player_name "Uhum."
                    show aunt 87
                    show player 13
                    dia "Bom, eu também estava pensando nas suas visitas diárias... E olhar você trabalhando..."
                    show aunt 88
                    show player 29
                    player_name "Sério?"
                    show aunt 92
                    show player 5
                    dia "Faz tempo que não tenho uma companhia masculina... Há muito tempo."
                    show aunt 88
                    show player 2
                    player_name "Eu agradeço por tudo que você tem feito por mim, {b}tia Diane{/b}..."
                    player_name "Eu nunca tive esse tipo de... atenção, antes..."
                    show aunt 109 at Position (xpos=947)
                    show player 108f
                    player_name "...E você é tão bonita..."
                    show aunt 90 at right
                    show player 13
                    dia "Você é tão gentil!"
                    show aunt 88
                    show player 108f
                    player_name "E eu também gosto desses enconstros... secretos."
                    show aunt 89
                    show player 13
                    dia "Acho que tenha algo de emocionante sobre fazer coisas juntos, em segredo."
                    dia "Por isso você é o meu favorito. Posso confiar em manter isso só entre nós!"
                    show aunt 88
                    show player 17
                    player_name "Pois é... Não quero que isso acabe..."
                    show aunt 89
                    show player 13
                    dia "Sua {b}tia{/b} estará sempre aqui... Porta sempre abertas para você."
                    show aunt 88
                    show player 17
                    player_name "Valeu..."
                    show aunt 89
                    show player 1
                    dia "Você tem algo a mais em mente?"
                    jump dia_default_dialogue_options_kitchen
                "Falar sobre mamãe.":

                    show aunt 109 at Position (xpos=947)
                    show player 24
                    player_name "Estou preocupado sobre a {b}[mom_name]{/b}..."
                    show aunt 92 at right
                    show player 5
                    dia "Como assim?"
                    show aunt 91
                    show player 10
                    player_name "Ela está estressada depois de tudo o que aconteceu com o {b}papai{/b}..."
                    show aunt 92
                    show player 13
                    dia "Hmmm... Bom, minha {b}irmã{/b} é uma mulher forte, igual eu."
                    show aunt 87
                    dia "Ela ficará bem!"
                    show aunt 91
                    show player 24
                    player_name "Só quero proteger ela! Quero... segurá-la e fazer ela se sentir segura."
                    show aunt 109 at Position (xpos=947)
                    show player 13
                    dia "..."
                    show aunt 89 at right
                    show player 11
                    dia "Você... voê sente algo por sua mãe também?"
                    show aunt 88
                    show player 29
                    player_name "Bom... Eu amo minha maẽ, é claro."
                    show aunt 89
                    show player 3
                    dia "Você sabe o que eu quis dizer..."
                    dia "Você {b}fatasia{/b} coisas sobre ela também? Você quer fazer coisas com ela, igual você faz comigo?"
                    menu:
                        "Sim.":
                            show aunt 88
                            show player 24
                            player_name "Sim... Eu fantasio."
                            show player 21
                            player_name "Eu estive pensando nela e... E eu fiquei excitado quando eu a vi..."
                            show aunt 109 at Position (xpos=947)
                            show player 108f
                            player_name "Tipo quando eu vi ela no chuveiro, e espiei ela pelada..."
                            show aunt 110 at Position (xpos=950)
                            show player 13
                            dia "Ah, {b}uau{/b}..."
                            show aunt 89 at right
                            show player 11
                            dia "Ela sabe disso?"
                            show aunt 88
                            show player 10
                            player_name "Acho que não..."
                            show aunt 89
                            show player 11
                            dia "Você deve estar bastante excitado."
                            show aunt 109 at Position (xpos=947)
                            show player 29
                            player_name "Eu sei. Eu tenho esses desejos, e eu continuo pensanod em {b}[mom_name]{/b}... E {b}você{/b}."
                            show aunt 90 at right
                            show player 13
                            dia "Meu Deus! Você deve ter fetiches por gêmeas!"
                            show aunt 89
                            show player 11
                            dia "Você já tentou dar algumas {b}pistas{/b} pra ela?"
                            show aunt 87
                            dia "Nunca se sabe... Talvez ela goste."
                            show aunt 88
                            show player 21
                            player_name "Como assim?"
                            show aunt 89
                            show player 13
                            dia "Bom, ela está solitáro... Ela poderia gostar ter um homem ao redor."
                            show aunt 87
                            dia "Alguém que cuide dela, que faça ela se sentir segura... Sei lá!"
                            show aunt 88
                            show player 108f
                            player_name "Acho que..."
                            show aunt 89
                            show player 11
                            dia "Você deveria tentar."
                            dia "Ver o que ela vai fazer..."
                            show aunt 88
                            show player 21
                            player_name "Vou pensar sobre isso."
                            show aunt 89
                            show player 13
                            dia "Algo a mais que você queira falar?"
                            jump dia_default_dialogue_options_kitchen
                        "Não.":

                            show aunt 91
                            show player 24
                            player_name "Não... Na verdade não."
                            show player 10
                            player_name "Eu me importo muito com ela."
                            show aunt 89
                            show player 13
                            dia "Entendi..."
                            show aunt 87
                            dia "Bom, você está indo bem!"
                            show aunt 89
                            dia "E ela tem sorte de ter um {b}filho{/b} que se importa."
                            show aunt 88
                            show player 21
                            player_name "Obrigado..."
                            show aunt 89
                            show player 13
                            dia "Algo a mais que você queira falar?"
                            jump dia_default_dialogue_options_kitchen

                "Produção de leite." if not aunt.known(aunt_breeding_guide):
                    show aunt 91
                    show player 14
                    player_name "Como está indo o seu negócio de leite?"
                    show player 13
                    show aunt 90
                    dia "Maravilhoso!"
                    dia "O mercado está crescendo, e todo mundo está adorando o meu leite!"
                    show aunt 89
                    dia "A sua escola ter dobrado as encomendas me ajudou muito."
                    show aunt 88
                    show player 14
                    player_name "Isso é ótimo!"
                    show player 13
                    show aunt 89
                    dia "Sim."
                    show aunt 91
                    pause
                    show aunt 92
                    show player 11
                    dia "Infelizmente, minha {b}jarra térmica{/b} estragou."
                    dia "Eu não tenho como manter meu leite gelado."
                    show aunt 91
                    show player 4
                    pause
                    show player 17
                    player_name "Talvez eu pudesse comprar outro para você."
                    show player 18
                    pause
                    show aunt 110 at Position (xpos = 950)
                    dia "Você poderia?"
                    show aunt 92 at right
                    dia "Isso seria muito bom se você fizesse isso!"
                    show player 34
                    dia "Não sei onde você acharia um..."
                    show aunt 91
                    show player 35
                    player_name "Hmm... Posso procurar no {b}shopping{/b} por um."
                    show aunt 92
                    show player 13
                    dia "Claro, isso talvez desse certo."
                    dia "Mas essa é a parte fácil..."
                    show aunt 91
                    pause
                    show player 10
                    player_name "Algo a mais?"
                    show aunt 92
                    show player 11
                    dia "Não tneho certeza."
                    dia "Acho que estou chegando ao limite de produção de leite."
                    dia "Não acho que serei capaz de entregar as encomendas futuras."
                    dia "Eu preciso encontrar um jeito de aumenta a produção de leite."
                    show aunt 91
                    show player 10
                    player_name "Hum? Alguma ideia de como posso fazer isso?"
                    show player 11
                    show aunt 92
                    dia "Não consigo pensar em nada."
                    show aunt 87
                    dia "Não é como se eu pudesse comprar vacas!"
                    show player 17
                    show aunt 90
                    dia "Hahaha!"
                    pause
                    show aunt 88
                    show player 29
                    player_name "Talvez eu pudesse te ajudar com isso também!"
                    show aunt 89
                    show player 13 at left
                    dia "Sério?"
                    show aunt 88
                    show player 14
                    player_name "Sim. Podemos umar a {b}biblioteca{/b} para {b}pesquisa{/b}."
                    player_name "Talvez eu pudesse encontrar mais informações sobre {b}produção de leite{/b} lá."
                    show player 13
                    show aunt 90
                    dia "Meu deus, você é o melhor sobrinho do mundo!"
                    show aunt 87
                    dia "Me diga se você achar algo!"
                    show aunt 89
                    dia "Com certeza vou te dar uma boa {b}recompensa{/b}!"
                    hide aunt
                    hide player
                    with dissolve
                    $ quest_list.append(quest12)
                    $ aunt.add_event(aunt_breeding_guide)

                "O jarro de leite." if quest12 in quest_list and quest12 not in completed_quests and milkjug not in inventory.items:
                    show aunt 88
                    show player 10
                    player_name "O que deveria fazer para manter o leite gelado?"
                    show aunt 87
                    show player 5
                    dia "Talvez pudéssemos comprar uma {b}jarra térmica{/b} para manter o leite gelado."
                    show aunt 89
                    dia "Eles são feitos de {b}aço inoxidável, com tampa{/b}."
                    dia "Tenho certeza de que podemos encontrar algo assim no {b}shopping{/b}."
                    show aunt 88
                    show player 10
                    player_name "Ok, vou tentar achar algo."

                "O jarro de leite." if quest12 in quest_list and quest12 not in completed_quests and milkjug in inventory.items:
                    show player 239_240
                    pause
                    show aunt 88
                    show player 173
                    player_name "Encontrei um {b}jarro de leite{/b}!"
                    show aunt 90
                    show player 172
                    dia "Ah, isso é ótimo!"
                    show aunt 118
                    show player 1
                    dia "Obrigada, {b}[firstname]{/b}."
                    dia "Você me poupou muito trabalho!"
                    show aunt 88
                    show player 17
                    player_name "Não foi nada, {b}tia Diane!{/b}"
                    show player 14
                    player_name "Fico feliz por poder deixar todo esse leite gelado agora."
                    $ inventory.items.remove(milkjug)
                    $ completed_quests.append(quest12)

                "Livro de produção de leite." if aunt.known(aunt_breeding_guide) and breeding_guide in inventory.items and not aunt.known(aunt_breeding_bull):
                    $ inventory.items.remove(breeding_guide)
                    show player 239_240
                    pause
                    show player 369
                    player_name "Aqui, achei o {b}livro{/b} na {b}blibioteca{/b}!"
                    show player 14
                    show aunt 158 at Position(xpos=985)
                    with fastdissolve
                    player_name "Tem informações e ilustrações detalhadas sobre como aumentar a produção de leite..."
                    show aunt 159
                    show player 10
                    player_name "Isso é para... animais, mas acho que funcionaria."
                    show player 5
                    show aunt 157
                    dia "Huh?"
                    dia "Entendi..."
                    show aunt 159
                    player_name "..."
                    show aunt 160
                    dia "Hmm... Encontrar um touro?"
                    show aunt 159
                    dia "..."
                    show player 11
                    show aunt 160
                    dia "Encaixe o {b}touro{/b} com a {b}fêmea{/b} para... {b}reprodução{/b}?!"
                    show aunt 159
                    dia "..."
                    show aunt 160
                    dia "Assim que a vaca estiver {b}impregnando{/b}, as mamas se expandem para aumentar a produção de leite..."
                    show aunt 159

                    show player 5
                    player_name "..."
                    show aunt 158
                    show player 10
                    player_name "Então, o que você acha, {b}tia Diane{/b}?"
                    show player 5
                    show aunt 160
                    dia "Eu... não..."
                    show aunt 157
                    dia "Acho que estou um pouco surpresa."
                    show aunt 160
                    dia "Não era algo que eu estava pensando fazer."
                    dia "Digo, eu consegui produzir quantidades decentes de leite..."
                    show player 14
                    show aunt 159
                    player_name "Mas isso poderia dobrar sua oferta!"
                    show player 13
                    show aunt 158
                    dia "..."
                    show aunt 157
                    dia "Tenho que pensar nisso."
                    dia "Isso vai ter... consequências, sabe..."
                    show aunt 158
                    show player 21
                    player_name "Achei que isso pudesse acabar com seus problemas..."
                    show player 13
                    show aunt 160
                    dia "É ótimo! Agradeço pela sua ajuda."
                    show aunt 157
                    dia "Você tem sido muito legal ultimamente."
                    show aunt 158
                    show player 14
                    player_name "De nada, {b}tia Diane{/b}!"
                    show player 13
                    pause
                    show player 29
                    player_name "Acho que vou voltar para o jardim."
                    show player 1
                    show aunt 157
                    dia "Claro. Até mais tarde..."
                    show aunt 159
                    hide player with dissolve
                    dia "..."
                    show aunt 110 at Position(xpos=950)
                    dia "Ficar {b}grávida{/b}?"
                    dia "Fazem anos que pensei em ter um filho."
                    dia "Meus exs nunca quiseram..."
                    show aunt 91 at Position(xpos=1024)
                    dia "..."
                    show aunt 92
                    dia "Mas eu ainda não estou tão velha..."
                    show aunt 89
                    dia "Não posso acreditar que meu sobrinho está sugerindo manuais agrícolas..."
                    show aunt 88
                    pause
                    show aunt 92
                    dia "Mesmo que eu quisesse... {b}procriaria{/b} com quem?"
                    dia "{b}Reproduzir{/b}..."
                    show aunt 89
                    dia "Parece tão... primata! Tão... coisa de animais! Tão... safado!"
                    show aunt 88
                    dia "Hmm."
                    show aunt 87
                    dia "A única pessoa que consigo imaginar... é meu sobrinho."
                    show aunt 92
                    dia "Não! Não posso..."
                    show aunt 89
                    dia "... mas ele tem um pinto muito bom, igual a um {b}touro{/b}..."
                    show aunt 110 at Position(xpos=950)
                    dia "Céus, {b}Diane{/b}! Você está cogitando em dar para o seu sobrinho {b}sem camisinha{/b}!"
                    dia "O que eu diria para minha irmã se eu tivesse um filho dele?"
                    show aunt 91 at Position(xpos=1024)
                    dia "..."
                    show aunt 92
                    dia "Quem mais iria querer? Estou ficando velha..."
                    dia "Ele provavelmente nem quer fazer isso..."
                    show aunt 88
                    pause
                    show aunt 92
                    dia "Mas, eu tenho que fazer alguma coisa, se eu quiser expandir esse negócio de leite."
                    dia "Não fazer nada não vai ajudar."
                    show aunt 89
                    dia "Ele não fez nada além de me ajudar e... me satisfazer."
                    show aunt 88
                    pause
                    show aunt 87
                    dia "Céus, não consigo parar de pensar no pau dele!"
                    show aunt 89
                    dia "Eu amo sentir o pau dele dentro de mim."
                    show aunt 88
                    dia "..."
                    show aunt 89
                    dia "Eu... eu tenho que parar de pensar nisso."
                    show aunt 92
                    dia "Esta deve ser uma decisão meramente empresarial, {b}Diane{/b}."
                    hide aunt with dissolve
                    $ aunt.add_event(aunt_breeding_bull)
                    jump garden_dialogue

                "Procriação." if aunt.over(aunt_breeding_bull) and not aunt.known(aunt_breeding_help):
                    show player 10
                    player_name "Alguma novidado ao... achar um touro para reproduzir, {b}tia Diane{/b}?"
                    show player 5
                    show aunt 87
                    dia "Oh... Você me conhec..."
                    show aunt 92
                    dia "Eu mal saio de casa..."
                    dia "Eu tenho o jardim, e minhas vendas de leite para me deixar ocupada."
                    dia "É difícil se relacionar com pessoas, sabe?"
                    show aunt 91
                    show player 14
                    player_name "Creio que sim..."
                    show player 13
                    show aunt 89
                    dia "Por que pergunta? Você tem alguém em mente?"
                    show aunt 88
                    menu:
                        "Eu!" if pStats.chr() < 7:
                            show player 10
                            player_name "[chr_warn]Você se importaria... digo... você pensa..."
                            show player 24
                            show aunt 110 at Position (xpos = 950)
                            player_name "[chr_warn]Esqueça."
                            show player 5
                            show aunt 92 at right
                            dia "O que você iria dizer?"
                            show aunt 91
                            show player 10
                            player_name "[chr_warn]Não é nada. Eu só... hum..."
                            show player 24
                            player_name "[chr_warn]Eu prometo que continuarei... Digo, acharei um bom touro para você."
                            show player 5
                            show aunt 92
                            dia "Obrigada, querido!"
                            dia "Nunca tenha medo de falar sua ideia."
                            show aunt 91
                            show player 10
                            player_name "[chr_warn]Claro, {b}tia Diane{/b}."
                            show player 5
                            show aunt 92
                            dia "Algo a mais?"
                            show aunt 91
                            jump dia_default_dialogue_options_kitchen

                        "Eu!" if pStats.chr() >= 7:
                            show player 14
                            player_name "Bom... Por que não eu?"
                            show player 13
                            show aunt 109 at Position (xpos = 950)
                            dia "!!!" with hpunch
                            show aunt 110 at Position (xpos = 953)
                            dia "O quê? Sério?"
                            show player 17
                            show aunt 91 at Position(xpos=1027)
                            player_name "Sim! Sabe, a gente já... faz coisas juntos..."
                            show player 13
                            show aunt 87
                            dia "Sim... fazemo, mas..."
                            show aunt 89
                            dia "Você é filho da minha irmã!"
                            show aunt 88
                            show player 21
                            player_name "Desculpa, achei que você quisesse."
                            show player 5
                            show aunt 91
                            dia "..."
                            show player 11
                            show aunt 89
                            dia "Eu... eu quero!"
                            show aunt 92
                            dia "Achei que você pensaria que eu sou muito velha para você!"
                            show aunt 91
                            show player 33
                            player_name "Não acho que você seja tão velha!"
                            show player 1
                            pause
                            show aunt 89
                            dia "Eu amaria ter você se {b}procriando{/b} comigo."
                            show aunt 88
                            show player 11
                            player_name "!!!"
                            show player 1
                            show aunt 89
                            dia "Sabe, eu tinha pensado em você, mas achei que você nunca quisesse {b}procria{/b} {b}comigo{/b}."
                            show aunt 90
                            dia "Eu achava que você só gostava de enganar."
                            show aunt 88
                            show player 21
                            player_name "Não, Eu... Eu gosto de fazer essas coisas com você {b}tia Diane{/b}!"
                            player_name "Quando podemos começar? Estou pronto para fazer isso agora!"
                            show player 13
                            show aunt 90
                            dia "Não tão rápido, meu jovem, touro reprodutor!"
                            show aunt 89
                            dia "Temos que deixar algumas coisas claras aqui."
                            dia "Sua mãe nunca pode saber sobre isso, ok?"
                            show aunt 88
                            show player 14
                            player_name "Não direi nada, prometo!"
                            show player 13
                            show aunt 87
                            dia "Certo."
                            dia "Se você ainda quer fazer isso comigo..."
                            show aunt 89
                            dia "... encontre-me no galpão hoje a noite."
                            dia "Terei algumas coisas preparadas para nós..."
                            show aunt 88
                            show player 21
                            player_name "Te vejo lá, {b}tia Diane{/b}!"
                            hide player
                            hide aunt
                            with dissolve
                            $ aunt.add_event(aunt_breeding_help)
                        "Ainda não.":

                            show player 10
                            player_name "Não."
                            show player 14
                            player_name "Mas vou continuar procurando."
                            show player 13
                            show aunt 89
                            dia "Ótimo. Continue procurando por um candidato!"
                            show aunt 88
                            show player 14
                            player_name "Irei."
                            hide player
                            hide aunt
                            with dissolve
                "Se divertir.":

                    show aunt 109 at Position (xpos=947)
                    show player 29
                    player_name "Quer se divertir um pouco?"
                    show aunt 89 at right
                    show player 13
                    dia "Ahhh..."
                    dia "Alguém está querendo... atenção especial."
                    show aunt 88
                    show player 108f
                    player_name "S... sim."
                    show aunt 87
                    show player 11
                    dia "Muito bem... Vamos ficar confortáveis primeiro..."
                    scene dianekitchen_closeup
                    show auntsex 2 at Position(xpos = 702, ypos = 769)
                    show playersex 1 at Position(xpos = 260, ypos = 768)
                    with dissolve
                    dia "Agora..."
                    dia "Tire suas calças."
                    show auntsex 1
                    show playersex 1
                    window hide
                    pause
                    show playersex 2 at Position(xpos = 300, ypos = 768)
                    window hide
                    pause
                    show playersex 3 at Position(xpos = 350, ypos = 768)
                    show auntsex 2
                    dia "Muito bom..."
                    if not aunt_had_sex:
                        show playersex 4 with dissolve
                        show playersex 3 with dissolve
                        window hide
                        pause
                        show auntsex 7
                        window hide
                        pause
                        show playersex 4 with dissolve
                        show playersex 3 with dissolve
                        show auntsex 8
                        dia "Wow... Está ficando... duro..."
                        show auntsex 7
                        window hide
                        pause
                        show playersex 4
                        show playersex 3
                        show auntsex 2
                        dia "Quero comparar com meus vegetais!"
                        show auntsex 9
                        show playersex 3
                        player_name "..."
                        show auntsex 10 at Position(xpos = 698, ypos = 769)
                        show playersex 3
                        dia "Isso... é incrível!"
                        dia "Nenhum dos meus ex chegaram perto disso..."
                        show auntsex 2 at Position(xpos = 702, ypos = 769)
                        dia "Você se importa se eu tocar?"
                        show auntsex 1
                        player_name "Está... Está tudo bem."
                        hide playersex
                        show auntsex 11_12 at Position(xpos = 621, ypos = 769)
                        pause 4
                        show playersex 3 at Position(xpos = 350, ypos = 768)
                        show auntsex 2 at Position(xpos = 702, ypos = 769)
                        dia "Então..."
                        dia "Quer me ver pelada?"
                        menu:
                            "Sim.":
                                show auntsex 1
                                show playersex 3
                                player_name "Eu adoraria..."
                                show auntsex 2
                                dia "Okay. Minha vez então..."
                                show auntsex 3 at Position(xpos = 675, ypos = 769)
                                pause
                                show auntsex 4
                                pause
                                show auntsex 13 at Position(xpos = 709, ypos = 769)
                                player_name "Woa..."
                                show playersex 4
                                pause
                                show playersex 3
                                player_name "Você é tão bonita, tia Diane..."
                                show auntsex 15
                                dia "..."
                                show auntsex 14
                                dia "Se você continuar falando assim eu vou ter que te convidar para dormir aqui."
                                show auntsex 13
                                player_name "Eu posso... tocar?"
                                show auntsex 14
                                dia "Claro que pode..."
                                dia "Mas só um pouco..."
                                hide playersex
                                show auntsex 18 at Position(xpos = 626, ypos = 769)
                                dia "Tipo assim..."
                                show auntsex 19_20 at Position(xpos = 640, ypos = 769)
                                pause 4
                                show auntsex 21 at Position(xpos = 650, ypos = 769)
                                dia "Você gostou?"
                                show auntsex 20 at Position(xpos = 640, ypos = 769)
                                player_name "Sim..."
                                show auntsex 15 at Position(xpos = 709, ypos = 769)
                                show playersex 3 at Position(xpos = 350, ypos = 768)
                                player_name "Eu... quero mais..."
                                show auntsex 14
                                dia "O que mais você quer?"
                                label dia_sex_options:
                                    menu:
                                        "Você." if pStats.chr() < 7:
                                            show auntsex 15
                                            player_name "[chr_warn]Eu... Eu quero estar dentro de você, {b}tia Diane{/b}."
                                            dia "[chr_warn]..."
                                            show auntsex 14
                                            dia "[chr_warn]Alguém está excitado."
                                            show auntsex 16 at Position(xpos = 640, ypos = 769)
                                            dia "[chr_warn]Hmmm..."
                                            show auntsex 17
                                            dia "[chr_warn]Talvez seja muito cedo para isso."
                                            show auntsex 16
                                            player_name "[chr_warn]..."
                                            show auntsex 14 at Position(xpos = 709, ypos = 769)
                                            dia "[chr_warn]Mas talvez tenho algo que possamos fazer."
                                            jump dia_sex_options

                                        "Você." if pStats.chr() >= 7:
                                            show auntsex 15
                                            player_name "Eu... Eu quero estar dentro de você, tia Diane."
                                            dia "!!!"
                                            show auntsex 17 at Position(xpos = 640, ypos = 769)
                                            dia "Hmm... Não sei se deveriamos..."
                                            show auntsex 15 at Position(xpos = 709, ypos = 769)
                                            player_name "Eu sempre quis fazer isso contigo..."
                                            player_name "É a única coisa que eu penso!"
                                            show auntsex 16 at Position(xpos = 640, ypos = 769)
                                            dia "..."
                                            show auntsex 14 at Position(xpos = 709, ypos = 769)
                                            dia "Bem, eu não faço há anos..."
                                            show auntsex 17 at Position(xpos = 640, ypos = 769)
                                            dia "...Mas você é meu {b}sobrinho{/b}!"
                                            show auntsex 16
                                            player_name "..."
                                            dia "Hmm..."
                                            show auntsex 14 at Position(xpos = 709, ypos = 769)
                                            dia "Certo."
                                            show auntsex 22 at Position(xpos = 707, ypos = 769)
                                            dia "Mas temos que usar {b}camisinha{/b}!"
                                            hide playersex
                                            show auntsex 5 at Position(xpos = 522, ypos = 769)
                                            pause
                                            show auntsex 6
                                            window hide
                                            pause
                                            show playersex 3 at Position(xpos = 350, ypos = 768)
                                            show expression "characters/player/char_player_sex_05.png" at Position(xpos = 488, ypos = 601)
                                            show auntsex 14 at Position(xpos = 704, ypos = 769)
                                            dia "Tudo certo?"
                                            show auntsex 24 at Position(xpos = 707, ypos = 769) with dissolve
                                            dia "Agora, ponha lentamente..."
                                            hide playersex
                                            hide expression "characters/player/char_player_sex_05.png"
                                            show auntsex 29 at Position(xpos = 579, ypos = 769)
                                            dia "Lá vamos nós..."
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            dia "Mais fundo..."
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            dia "Isso! Assim..."
                                            $ M_aunt.set('sex speed', .4)
                                            $ xray = 0
                                            label aunt_sex_loop:
                                                show screen aunt_sex_xray_buttons
                                                pause
                                                if anim_toggle:
                                                    hide screen aunt_sex_xray
                                                    hide screen aunt_sex_xray_buttons
                                                    if xray_toggle:
                                                        hide auntsex
                                                        if condom_on:
                                                            show auntsex_xray 6_9 at Position(xpos = 686, ypos = 769)
                                                        else:

                                                            show auntsex_xray 6_7 at Position(xpos = 686, ypos = 769)
                                                    else:

                                                        hide auntsex_xray
                                                        show auntsex 30_31 at Position(xpos = 592, ypos = 769)
                                                    pause 8
                                                else:

                                                    show screen aunt_sex_xray
                                                    hide auntsex_xray
                                                    hide screen aunt_sex_xray_buttons
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                    pause
                                                    $ xray = 0
                                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                                    pause
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                    pause
                                                    $ xray = 0
                                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                                    pause
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                    pause
                                                    $ xray = 0
                                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                                    pause
                                                    $ xray = 1
                                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                                call screen aunt_sex_options

                                            label aunt_sex_cum_in:
                                                hide auntsex_xray
                                                show auntsex 28 at Position(xpos = 612, ypos = 769)
                                                if xray_toggle:
                                                    if condom_on:
                                                        show expression "characters/player/char_player_sex_10.png" at Position(xpos = 650, ypos = 610)
                                                    else:

                                                        show expression "characters/player/char_player_sex_08.png" at Position(xpos = 650, ypos = 610)
                                                with hpunch
                                                dia "AAahh!"
                                                hide expression "characters/player/char_player_sex_08.png"
                                                hide expression "characters/player/char_player_sex_10.png"
                                                show auntsex 24 at Position(xpos = 707, ypos = 769)
                                                show playersex 11 at Position(xpos = 275, ypos = 768)
                                                if condom_on:
                                                    show expression "characters/player/char_player_sex_12.png" at Position(xpos = 444, ypos = 617)
                                                else:

                                                    show expression "characters/player/char_player_sex_17.png" at Position(xpos = 570, ypos = 640)
                                                dia "..."
                                                show playersex 3
                                                if condom_on:
                                                    hide expression "characters/player/char_player_sex_12.png"
                                                    show expression "characters/player/char_player_sex_13.png" at Position(xpos = 418, ypos = 605)
                                                dia "Foi muita porra..."
                                                if condom_on:
                                                    dia "Ainda bem que usamos camisinha!"
                                                show auntsex 23
                                                player_name "Isso foi tão... Bom!"
                                                show auntsex 24
                                                dia "Vamos limpar isso..."
                                                $ aunt_had_sex = True
                                                jump aunt_sex_end

                                            label aunt_sex_cum_out:
                                                hide auntsex_xray
                                                show auntsex 24 at Position(xpos = 707, ypos = 769)
                                                show playersex 11 at Position(xpos = 275, ypos = 768)
                                                show expression "characters/player/char_player_sex_14.png" at Position(xpos = 525, ypos = 584)
                                                window hide
                                                pause
                                                hide expression "characters/player/char_player_sex_14.png"
                                                show expression "characters/player/char_player_sex_15.png" at Position(xpos = 531, ypos = 584)
                                                window hide
                                                pause
                                                hide expression "characters/player/char_player_sex_15.png"
                                                show expression "characters/player/char_player_sex_16.png" at Position(xpos = 534, ypos = 588)
                                                dia "..."
                                                dia "Adorei fazer isso..."
                                                dia "...Agora, vamos limpar."
                                                $ aunt_had_sex = True
                                                jump aunt_sex_end
                                        "Fazer mais.":

                                            show auntsex 13
                                            show playersex 3
                                            player_name "Podemos fazer mais?"
                                            show auntsex 16 at Position(xpos = 640, ypos = 769)
                                            dia "Hmmm..."
                                            show auntsex 35 at Position(xpos = 709, ypos = 769)
                                            dia "Aqui. Pegue isso..."
                                            show auntsex 24 at Position(xpos = 707, ypos = 769)
                                            show playersex 18
                                            with dissolve
                                            dia "Vai em frente..."
                                            hide playersex
                                            show auntsex 32_33 at Position(xpos = 535, ypos = 769)
                                            pause 2
                                            dia "Continue..."
                                            pause 2
                                            dia "Mais rápido!"
                                            window hide
                                            pause 2
                                            show auntsex 34 at Position(xpos = 670, ypos = 769)
                                            show playersex 18 at Position(xpos = 350, ypos = 768) with hpunch
                                            dia "!!!"
                                            player_name "..."
                                            player_name "Você está bem?"
                                            show auntsex 24 at Position(xpos = 707, ypos = 769)
                                            dia "{b}*Respirando ofegante*{/b}"
                                            dia "Foi ótimo... {b}[firstname]{/b}."
                    else:

                        show playersex 4 at Position(xpos = 350, ypos = 768)
                        pause
                        show playersex 3
                        pause
                        dia "Amei fazer isso..."
                        hide playersex
                        show auntsex 11_12 at Position(xpos = 621, ypos = 769)
                        pause 4
                        show playersex 3 at Position(xpos = 350, ypos = 768)
                        show auntsex 2 at Position(xpos = 702, ypos = 769)
                        dia "Minha vez."
                        show auntsex 3 at Position(xpos = 675, ypos = 769)
                        pause
                        show auntsex 4
                        pause
                        show auntsex 13 at Position(xpos = 709, ypos = 769)
                        player_name "Woa..."
                        show playersex 4
                        pause
                        show playersex 3
                        player_name "Você é tão gostosa, tia Diane..."
                        show auntsex 14
                        dia "Então, o que você gostaria de fazer agora??"
                        $ anim_toggle = False
                        $ xray_toggle = False
                        $ M_aunt.set('sex speed', .4)
                        label dia_sex_options_2:
                            menu:
                                "Brincar com o clitóris.":
                                    show auntsex 13
                                    player_name "Posso... te tocar?"
                                    show auntsex 14
                                    dia "Claro que pode..."
                                    dia "Mas só um pouco..."
                                    hide playersex
                                    show auntsex 18 at Position(xpos = 626, ypos = 769)
                                    dia "Assim..."
                                    show auntsex 19_20 at Position(xpos = 640, ypos = 769)
                                    pause 4
                                    show auntsex 21 at Position(xpos = 650, ypos = 769)
                                    dia "Gostou?"
                                    show auntsex 20 at Position(xpos = 640, ypos = 769)
                                    player_name "Yeah..."
                                    show auntsex 15 at Position(xpos = 709, ypos = 769)
                                    show playersex 3 at Position(xpos = 350, ypos = 768)
                                    player_name "Eu... quero mais..."
                                    show auntsex 14
                                    dia "O que você queria fazer agora?"
                                    jump dia_sex_options_2
                                "Brincar com os vegetais.":

                                    show playersex 3
                                    show auntsex 35 at Position(xpos = 709, ypos = 769)
                                    dia "Aqui. Pegue..."
                                    show auntsex 24 at Position(xpos = 707, ypos = 769)
                                    show playersex 18
                                    with dissolve
                                    dia "Vai em frente..."
                                    hide playersex
                                    show auntsex 32_33 at Position(xpos = 535, ypos = 769)
                                    pause 2
                                    dia "Continue..."
                                    pause 2
                                    dia "Mais rápido!"
                                    window hide
                                    pause 2
                                    show auntsex 34 at Position(xpos = 670, ypos = 769)
                                    show playersex 18 at Position(xpos = 350, ypos = 768) with hpunch
                                    dia "!!!"
                                    player_name "..."
                                    player_name "Você está bem?"
                                    show auntsex 24 at Position(xpos = 707, ypos = 769)
                                    dia "{b}*Ofegante*{/b}"
                                    dia "Isso foi muito bom... {b}[firstname]{/b}."
                                    dia "Quer fazer algo a mais?"
                                    jump dia_sex_options_2
                                "Foder sem camisinha.":

                                    $ condom_on = False
                                    show auntsex 13
                                    show playersex 3 at Position(xpos = 350, ypos = 768)
                                    player_name "Eu... Eu quero estar dentro de você, tia Diane."
                                    show auntsex 14
                                    dia "Certo."
                                    show auntsex 24 at Position(xpos = 707, ypos = 769)
                                    dia "Agora, ponha de vagar..."
                                    hide playersex
                                    show auntsex 25 at Position(xpos = 579, ypos = 769)
                                    dia "Aqui vamos nós..."
                                    show auntsex 26 at Position(xpos = 592, ypos = 769)
                                    dia "Mais fundo..."
                                    show auntsex 27 at Position(xpos = 608, ypos = 769)
                                    dia "Sim! Assim..."
                                    $ xray = 0
                                    label aunt_sex_loop_2:
                                        show screen aunt_sex_xray_buttons
                                        pause
                                        if anim_toggle:
                                            hide screen aunt_sex_xray
                                            hide screen aunt_sex_xray_buttons
                                            if xray_toggle:
                                                hide auntsex
                                                show auntsex_xray 6_7 at Position(xpos = 686, ypos = 769)
                                            else:

                                                hide auntsex_xray
                                                show auntsex 26_27 at Position(xpos = 592, ypos = 769)
                                            pause 8
                                        else:

                                            show screen aunt_sex_xray
                                            hide auntsex_xray
                                            hide screen aunt_sex_xray_buttons
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 26 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 26 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 26 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 27 at Position(xpos = 608, ypos = 769)
                                        call screen aunt_sex_options
                                "Foder com camisinha.":

                                    $ condom_on = True
                                    show auntsex 13
                                    player_name "Eu... Eu quero estar dentro de você, tia Diane."
                                    show auntsex 14
                                    dia "Certo."
                                    show auntsex 22 at Position(xpos = 707, ypos = 769)
                                    dia "Mas temos que usar {b}camisinha{/b}!"
                                    hide playersex
                                    show auntsex 5 at Position(xpos = 522, ypos = 769)
                                    pause
                                    show auntsex 6
                                    window hide
                                    pause
                                    show playersex 3 at Position(xpos = 350, ypos = 768)
                                    show expression "characters/player/char_player_sex_05.png" at Position(xpos = 488, ypos = 601)
                                    show auntsex 14 at Position(xpos = 704, ypos = 769)
                                    dia "Tudo certo?"
                                    show auntsex 24 at Position(xpos = 707, ypos = 769) with dissolve
                                    dia "Agora, enfie devagar..."
                                    hide playersex
                                    hide expression "characters/player/char_player_sex_05.png"
                                    show auntsex 29 at Position(xpos = 579, ypos = 769)
                                    dia "Isso..."
                                    show auntsex 30 at Position(xpos = 592, ypos = 769)
                                    dia "Mais fundo..."
                                    show auntsex 31 at Position(xpos = 608, ypos = 769)
                                    dia "Sim! Assim..."
                                    $ anim_toggle = False
                                    $ xray_toggle = False
                                    $ xray = 0
                                    label aunt_sex_loop_3:
                                        show screen aunt_sex_xray_buttons
                                        pause
                                        if anim_toggle:
                                            hide screen aunt_sex_xray
                                            hide screen aunt_sex_xray_buttons
                                            if xray_toggle == True:
                                                hide auntsex
                                                show auntsex_xray 6_9 at Position(xpos = 686, ypos = 769)
                                            else:

                                                hide auntsex_xray
                                                show auntsex 30_31 at Position(xpos = 592, ypos = 769)
                                            pause 8
                                        else:

                                            show screen aunt_sex_xray
                                            hide auntsex_xray
                                            hide screen aunt_sex_xray_buttons
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                            pause
                                            $ xray = 0
                                            show auntsex 30 at Position(xpos = 592, ypos = 769)
                                            pause
                                            $ xray = 1
                                            show auntsex 31 at Position(xpos = 608, ypos = 769)
                                        call screen aunt_sex_options

                    label aunt_sex_end:
                        scene blank with dissolve
                        if not aunt_had_sex:
                            scene dianekitchen with dissolve
                            show player 29 at left with dissolve
                            show aunt 88 at right with dissolve
                            player_name "Isso foi... muito bom!"
                            show player 13
                            show aunt 89
                            dia "Você gostou?"
                            show aunt 88
                            show player 21
                            player_name "Ah, sim..."
                            show player 29
                            player_name "Eu fiz certo?"
                            show aunt 87
                            show player 13
                            dia "Você está fazendo muito bem, jovem."
                            show aunt 89
                            dia "Espero que você volte logo..."
                            show player 11
                            dia "Especialmente após a escola, quando você precisa liberar todo esse estresse!"
                            show aunt 88
                            show player 17
                            player_name "Eu amaria."
                            show aunt 89
                            show player 13
                            dia "Está ficando tarde. Você deveria ir..."
                            show aunt 87
                            dia "Você não quer deixar sua mãe esperando!"
                            show aunt 88
                            show player 17
                            player_name "Sim."
                            show aunt 89
                            show player 11
                            dia "Lembre-se... É nosso segredinho."
                            show aunt 88
                            show player 21
                            player_name "Não se preocupe, {b}tia Diane{/b}, não vou contar para ninguém."
                            show player 13
                            show aunt 90
                            dia "Esse é o meu garoto!"
                            hide player
                            show aunt 111 at left
                            dia "Vamos nos {b}divertir{/b} muito juntos..."
                            $ gTimer.tick()
                            $ callScreen(location_count)
                            with dissolve
                        else:

                            scene dianekitchen with dissolve
                            show player 29 at left with dissolve
                            show aunt 88 at right with dissolve
                            player_name "Isso foi... muito bom!"
                            show player 13
                            show aunt 89
                            dia "Gostou?"
                            show aunt 88
                            show player 21
                            player_name "Uhum..."
                            show player 29
                            player_name "Fiz bem?"
                            show aunt 87
                            show player 13
                            dia "Você fez muito bem, querido."
                            show aunt 89
                            dia "Talvez você possa me ajudar a {b}ordenhar{/b} algu dia..."
                            show aunt 88
                            show player 17
                            player_name "Eu adoraria."
                            show aunt 89
                            show player 13
                            dia "Eu geralmente tiro leite {b}de noite{/b}, no {b}galpão{/b}."
                            dia "Você deveria vir me visitar. eu estarei esperando por você."
                            show aunt 88
                            show player 17
                            player_name "Beleza. Eu sempre quis saber como você fez todo esse leite!"
                            show aunt 89
                            show player 13
                            dia "Está ficando tarde. Você deveria ri..."
                            show aunt 87
                            dia "Você não quer deixar sua mãe esperando!"
                            show aunt 88
                            show player 17
                            player_name "Uhum."
                            show aunt 89
                            show player 11
                            dia "Lembre-se... É o nosso segredinho."
                            show aunt 88
                            show player 21
                            player_name "Não se preocupe, {b}tia Diane{/b}, não contarei a ninguém."
                            show player 13
                            show aunt 90
                            dia "Esse é o meu garoto!"
                            hide player
                            show aunt 111 at left
                            dia "Vamos nos {b}divertir{/b} muito juntos..."
                            if milking_unlocked == False:
                                show unlock28 at truecenter with dissolve
                                pause
                                hide unlock28 with dissolve
                                $ milking_unlocked = True
                            $ gTimer.tick()
                            $ callScreen(location_count)
                            with dissolve
                "Eu deveria ir.":

                    show aunt 88 at right
                    show player 21 at left
                    player_name "Eu adoraria ficar aqui com você..."
                    show aunt 91
                    show player 10
                    player_name "Mas eu tenho que ir cuidar do jardim..."
                    show aunt 92
                    show player 13
                    dia "Que pena."
                    dia "Eu estava querendo passar um tempo com você..."
                    show aunt 91
                    show player 10
                    player_name "Perdão, talvez outra hora."
                    show aunt 87
                    show player 11
                    dia "Qualquer hora. Sua {b}tia{/b} está sempre com vontade..."
                    show aunt 88
                    show player 17
                    player_name "Oh. Haha..."
                    show aunt 87
                    show player 13
                    dia "Vou ficar esperando!"
                    hide player 13 at left with dissolve
                    hide aunt 11 at right with dissolve
    $ callScreen(location_count)

label job_done_dialogue:
    $ renpy.checkpoint()
    if quest10 in quest_list and quest10 not in completed_quests and annihilator in inventory.items:
        scene black with dissolve
        with Pause(0.5)

        show garden_event01 with dissolve
        show text "Comecei a pulverizar todo o lote com pesticida verde...\n Esvaziou toda a lata de veneno...\n Me certifiquei que nenhum inseto saisse vivo!" at Position (xpos= 512, ypos = 700) with dissolve
        $ inventory.items.remove(annihilator)
        if exterminator in inventory.items:
            $ inventory.items.remove(exterminator)

        if eradicator in inventory.items:
            $ inventory.items.remove(eradicator)
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        hide garden_event01
        scene black
        with Dissolve(0.5)
        show unlock27 at truecenter with dissolve
        $ renpy.pause()
        $ infestation_done = True
        hide unlock27 with dissolve
        hide black
        $ callScreen(location_count)

    if not garden_firsttime:
        scene black
        with Pause(0.5)

        show garden_firsttime_01 with dissolve
        show text "A tia Diane foi se deitar no quintal e comecei a limpar seu jardim.\n Estava tão quente lá fora ... E havia tantas ervas daninhas!\n Mas finalmente consegui fazer tudo, o que levou um bom tempo para fazer...\n Bom, eu estava segurando a pá do jeito certo!" at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show garden_firsttime_02 with dissolve
        show text "Percebi alguém me olhando enquanto trabalhava...\n Pude notar que tia Diane me olhava durante o processo todo!\n Ela não dizia nada e apenas olhava para mim de uma maneira estranha...\n Ela deve estar cansada ou algo do tipo." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        hide garden_firsttime_01
        hide garden_firsttime_02 with dissolve
        scene black with dissolve
        with Pause(0.5)
        $ garden_firsttime = True
    if quest10 in quest_list and quest10 not in completed_quests:
        scene garden_dead
    else:

        scene garden
    if earnings > 0:
        show player 1 at left with dissolve
        show aunt 2 at right with dissolve
        dia "Ah, uau! Meu jardim está maravilhoso, {b}[firstname]{/b}!"
        show player 1 at left
        show aunt 9 at right
        player_name "Uhum... Eu tive que me livrar de muitas coisas..."
        show aunt 15 at right
        show player 11 at left
        dia "Olha esses pepinos grandes e duros!"
        show aunt 16 at right
        player_name "..."
        show aunt 5 at right
        show player 13 at left
        dia "Obrigada, querido! Volte logo!"
        hide player 13 at left with dissolve
        hide aunt 5 at right with dissolve
    else:

        show player 5 at left with dissolve
        show aunt 23 at right with dissolve
        dia "Hmm... Dá para fazer melhor."
        show aunt 24 at right
        show player 24 at left
        player_name "Concordo... não fiz muito bem. Desculpa, {b}tia Diane{/b}!"
        show aunt 3 at right
        show player 13 at left
        dia "Está tudo bem... Você é novo nisso..."
        show aunt 2 at right
        dia "E tenho certeza que vai melhorar!"
        dia "Sua tia sempre precisa de legumes frescos..."
        show aunt 1 at right
        show player 10 at left
        player_name "Espero que sim..."
        show aunt 14 at right
        show player 11 at left
        dia "Apenas Certifique-se de que {b}apens{/b} tenha vegetais {b}grande{/b} e {b}duros{/b}!"
        show aunt 1 at right
        show player 13 at left
        player_name "Tentarei fazer melhor da próxima vez..."
        player_name "Obrigado, {b}tia Diane{/b}!"
        hide player 13 at left with dissolve
        hide aunt 1 at right with dissolve
    $ gTimer.tick()
    $ bad_garden_count = 0
    if earnings < 0:
        $ earnings = 0
    $ inventory.money += earnings
    $ after_minigame = True
    $ garden_done += 1
    show unlock7 at truecenter
    show text "{size=30}{b}[earnings]{/b}{/size}" at Position(xpos = 485,ypos = 413)
    with dissolve
    play audio coins1
    $ renpy.pause()
    hide text "{b}[earnings]{/b}"
    hide unlock7
    with dissolve
    $ in_garden = True
    jump garden_dialogue

label night_closed_garden:
    if quest10 in quest_list and quest10 not in completed_quests:
        scene garden_dead_night
    else:

        scene garden_night
    show player 10 with dissolve
    if aunt_had_sex and not gTimer.is_night():
        player_name "{b}Tia Diane{/b} disse que ia estar no {b}celeiro{/b}."
    else:

        player_name "{b}Tia Diane{/b} deve estar dormindo... Acho que não posso trabalhar no jardim agora."
    hide player 2 with dissolve
    $ callScreen(location_count)

screen garden_minigame:
    timer 0.01 repeat True action If(
        time_count > 0,
        true=SetVariable("time_count", time_count - 0.01),
        false=[Hide("garden_minigame"), Jump("job_done_dialogue")]
    )
    add "backgrounds/minigame01_bg01.jpg"
    $ pos_index = 0
    for Good in t_list:
        $ pic = Good.image
        $ i_passive = Good.passive
        if not Good.passive:
            imagebutton:
                idle pic
                hover pic
                pos valid_pos[pos_index]
                action [If(
                    not Good.status,
                    SetVariable("earnings", earnings + Good.price),
                    [If(
                        earnings - Good.price < 0,
                        SetVariable("earnings", 0),
                        SetVariable("earnings", earnings - Good.price)
                    )]
                 ),
                        Play("audio", "audio/sfx_splat.ogg"),
                        Function(Good.change_passive),
                        If(
                            Good in bad_list or Good in rotten_t_list,
                            SetVariable("bad_garden_count", bad_garden_count + 1),
                            NullAction()
                        ),
                        If(
                            bad_garden_count == bad_garden_number,
                            Jump("job_done_dialogue"),
                            NullAction()
                        )
                ]
        else:
            add Good.passive_pic pos valid_pos[pos_index]
        $ pos_index += 1
    text "[bad_garden_count]"
    text "{b}[earnings]{/b}" pos 155,672 size 35 xalign 0.5
    bar value time_count range timer_range pos 260,685 xmaximum 513 ymaximum 33 style "time_bar"

label garden_listing:
    $ bad_garden_count = 0
    if quest10 in quest_list and quest10 not in completed_quests and not infestation_done:
        $ renpy.random.shuffle(rotten_list)
        $ t_list=[earwig01, earwig02, earwig03, rotten_list[0], rotten_list[1], rotten_list[3]]
        $ bad_garden_number = 5
        $ renpy.random.shuffle(t_list)
        $ renpy.random.shuffle(valid_pos)
        $ time_count = 3
        $ timer_range = 3
        $ style.time_bar.left_bar = "buttons/bar_full.png"
        $ style.time_bar.right_bar = "buttons/bar_empty.png"
        $ rotten_good_reset()
        $ earwig01.passive = False
        $ earwig02.passive = False
        $ earwig03.passive = False
        $ earnings = 0
        call screen garden_minigame
    else:

        $ t_list=item_list[:]
        $ renpy.random.shuffle(t_list)
        $ renpy.random.shuffle(valid_pos)
        $ bad_garden_number = len(bad_list) - 1
        $ time_count = 3
        $ timer_range = 3
        $ style.time_bar.left_bar = "buttons/bar_full.png"
        $ style.time_bar.right_bar = "buttons/bar_empty.png"
        $ good_reset()
        $ earnings = 0
        call screen garden_minigame

label drink_offered:
    scene garden
    if aunt_drink_made:
        show player 137 with dissolve
    else:

        show player 12 with dissolve
    player_name "I should give {b}Aunt Diane{/b} her {b}drink{/b} before I get back to work..."
    $ callScreen(location_count)

label aunt_masturbate:
    if not aunt_masturbating_seen:
        show aunt_masturbate 1_2
        player_name "!!!"
        player_name "( ...Tia Diane... O que ela está... )"
        window hide
        pause 2
        player_name "( WOW... )"
        player_name "( Ela está se masturbando com os vegetais... )"
        player_name "( Um pepino inteiro! )"
        player_name "( ... )"
        player_name "( ...Eu deveria sair antes que ela me visse. )"
        scene garden
        with dissolve
        show player 113 with dissolve
        player_name "Não acredito no que eu acabei de ver..."
        show player 114
        player_name "( Não pensei que a tia Diane fosse assim... tão safada... )"
        show player 113
        player_name "É pra isso que ela quer esses vegetais?"
        show player 109f
        player_name "Hmm..."
        show player 108f
        player_name "Acho que ela esteve sozinha ultimamente..."
        player_name "Eu deveria voltar ao trabalho e fingir que não vi nada..."
        $ unlock_ui()
        $ aunt_masturbating_seen = True
        hide player 108f with dissolve
    $ aunt_dialogue_advance = True
    $ callScreen(location_count)

label before_masturbation:
    scene garden
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "Eu deveria saber se a tia Diane está em casa primeiro."
    $ callScreen(location_count)

label after_masturbation:
    scene garden
    show player 34 with dissolve
    player_name "Hmmm..."
    show player 12
    player_name "Acho que não agora."
    $ callScreen(location_count)

label aunt_kitchen_faster_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') - 0.1)
    if not aunt_had_sex:
        jump aunt_sex_loop
    elif aunt_had_sex and not condom_on:
        jump aunt_sex_loop_2
    elif aunt_had_sex and condom_on:
        jump aunt_sex_loop_3

label aunt_kitchen_slower_sex:
    $ M_aunt.set('sex speed', M_aunt.get('sex speed') + 0.1)
    if not aunt_had_sex:
        jump aunt_sex_loop
    elif aunt_had_sex and not condom_on:
        jump aunt_sex_loop_2
    elif aunt_had_sex and condom_on:
        jump aunt_sex_loop_3
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
