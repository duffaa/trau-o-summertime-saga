label backyard_dialogue:
    $ location_count = "Backyard"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_mom.get_state() == S_mom_midnight_search:
        jump mom_midnight_swim
    $ callScreen(location_count)

label backyard_chair_dialogue:
    $ callScreen(location_count)

label mom_pool_dialogue:
    if M_mom.get_state() == S_mom_fetch_towel and towel not in inventory.items:
        scene backyard_n_c
        show mom 204 at left
        show player 13f at right
        with dissolve
        mom "Você esqueceu de pegar uma {b}toalha no banheiro{/b}?"
        show mom 205
        show player 14f
        player_name "Desculpa! Já volto."
    else:

        scene home_diningroom_n_c
        show mom 207 at left
        show player 10f at right
        with dissolve
        player_name "!!!"
        show player 14f
        player_name "Você me assustou. Eu pensei que você ainda estivesse lá fora."
        show player 239_240f with dissolve
        pause
        show player 495f with dissolve
        player_name "Aqui, a toalha."
        show player 494f
        show mom 208
        mom "Sabe, acho que não preciso mais disso..."
        mom "Já me sinto mais quente e melhor aqui dentro."
        show player 11f with dissolve
        mom "É disso que você gosta?"
        show player 26f
        show mom 209_210 with dissolve
        mom "...Sempre percebi que você olhava para os meus peitos..."
        mom "Você..."
        mom "Você quer tocá-los?"
        show mom 207 with dissolve
        show player 11f
        player_name "{b}*Gulp*{/b}"
        show player 10f
        player_name "Eu... Uhhh-"
        show player 5f
        show mom 209_210 with dissolve
        mom "Qual é o problema? Eu sei que você não é tão tímido..."
        show mom 208 with dissolve
        mom "...Ou você quer algo mais da sua mãe?"
        show mom 207
        show player 11f
        player_name "!!!"
        show mom 208
        mom "Preciso te falar."
        mom "Preciso de algo a mais do que apenas suas mãos..."
        show mom 183bf with dissolve
        show player 434f
        show mom 184df with dissolve
        mom "Preciso de algo seu."
        show mom 184cf
        show player 435f
        player_name "I..."
        show player 434f
        show mom 184df
        mom "Seja um bom garoto."
        mom "Mamãe quer sentir seus dedos."
        hide player
        show mom 190f
        show player finger 193bf
        with dissolve
        player_name "Uhh... Ok..."
        show mom 191f
        mom "Ponha seus dedos aqui, querido."
        show mom 193f with dissolve
        mom "Mamãe quer seu dedos...lá dentro..."
        $ M_mom.set("sex speed", .225)
        $ M_mom.set("sex flip", True)
        $ M_mom.set("robe on", False)
        $ first_pass = True

        label mom_finger_loop:
            show screen sex_anim_buttons
            pause
            hide screen sex_anim_buttons
            hide player
            if anim_toggle:
                $ animcounter = 0

                while animcounter < 4:
                    if M_mom.is_set("sex flip"):
                        show mom 194f_195f_196f at left
                        if M_mom.is_set("robe on"):
                            show mom_robe 194bf_195bf_196bf
                    else:

                        show mom 194_195_196 at right
                        if M_mom.is_set("robe on"):
                            show mom_robe 194b_195b_196b
                    pause 4

                    if animcounter == 0:
                        if randomizer() <= 50:
                            mom "Ohh...{p=1}{nw}"
                            mom "Assim, querido.{p=2}{nw}"
                        else:

                            mom "Seus dedos são... tão bons...{p=2}{nw}"
                            mom "Você é um bom garoto...{p=2}{nw}"

                    if animcounter == 1:
                        if randomizer() <= 50:
                            mom "Oh, querido...{p=1}{nw}"
                        else:

                            mom "Como você ficou tão bom?{p=2}{nw}"

                    if M_mom.get_state() != S_mom_fetch_towel and first_pass and randomizer() <= 50 and animcounter == 2:
                        $ first_pass = False
                        player_name "Você está tão molhada, {b}[mom_name]{/b}.{p=2}{nw}"
                        player_name "No que você estava pensando antes de vir para a cozinha?{p=3}{nw}"
                        mom "...Você..."

                    elif M_mom.get_state() != S_mom_fetch_towel and first_pass and animcounter == 2:
                        $ first_pass = False
                        player_name "Você gosta de ter o dedo do seu filho enquanto você está no balcão da cozinha??{p=3}{nw}"
                        mom "Oh, querido...eu...eu...{p=2}{nw}"
                        mom "Eu gosto...{p=1}{nw}"
                        mom "Sua mamãe é uma gaortinha safada...{p=2}{nw}"

                    if animcounter == 3:
                        if randomizer() <= 50:
                            mom "Estou... Estou...quase!{p=2}{nw}"
                        else:

                            mom "Oh!!!{p=1}{nw}"
                            mom "É bem aí, querido!{p=2}{nw}"
                            mom "Ahh!!{p=1}{nw}"
                    pause 3

                    $ animcounter += 1
            else:

                $ animcounter = 0

                while animcounter < 4:
                    if M_mom.is_set("sex flip"):
                        show mom 194f at left
                        if M_mom.is_set("robe on"):
                            show mom_robe 194bf
                        pause
                        show mom 195f
                        if M_mom.is_set("robe on"):
                            show mom_robe 195bf
                        pause
                        show mom 196f
                        if M_mom.is_set("robe on"):
                            show mom_robe 196bf
                    else:

                        show mom 194 at right
                        if M_mom.is_set("robe on"):
                            show mom_robe 194b
                        pause
                        show mom 195
                        if M_mom.is_set("robe on"):
                            show mom_robe 195b
                        pause
                        show mom 196
                        if M_mom.is_set("robe on"):
                            show mom_robe 196b
                    pause

                    if animcounter == 0:
                        if randomizer() <= 50:
                            mom "Ohh..."
                            mom "Assim, querido."
                        else:

                            mom "Seus dedos... são tão bons..."
                            mom "Você é um ótimo garoto..."

                    if animcounter == 1:
                        if randomizer() <= 50:
                            mom "Oh, querido..."
                        else:

                            mom "Como você ficou tão bom?"

                    if M_mom.get_state() != S_mom_fetch_towel and first_pass and randomizer() <= 50 and animcounter == 2:
                        $ first_pass = False
                        player_name "Você está tão molhada, {b}[mom_name]{/b}."
                        player_name "No que você estava pensando antes de vir para a cozinha?"
                        mom "...Você..."

                    elif M_mom.get_state() != S_mom_fetch_towel and first_pass and animcounter == 2:
                        $ first_pass = False
                        player_name "Você gosta de sentir os dedos do seu filho em você enquanto está na mesa da cozinha?"
                        mom "Oh, querido...eu...eu..."
                        mom "Eu gosto..."
                        mom "Śua mãe é uma garotinha safadinha..."

                    if animcounter == 3:
                        if randomizer() <= 50:
                            mom "Eu... estou...quase!"
                        else:

                            mom "Oh!!!"
                            mom "Bem aí, querido!"
                            mom "Ahh!!"

                    $ animcounter += 1

            call screen mom_finger_options

        label mom_finger_cum:
            hide screen mom_finger_options
            if M_mom.get_state() == S_mom_fetch_towel:
                mom "Oh!"
                mom "Querido!"
            else:

                player_name "Pronto para eu parar de provocar você?"
                mom "Sim, seu safadinho!"
                mom "Eu quero gozar!"
                $ M_mom.set('sex speed', .100)
                if M_mom.is_set("sex flip"):
                    show mom 194f_195f_196f at left
                    if M_mom.is_set("robe on"):
                        show mom_robe 194bf_195bf_196bf
                else:

                    show mom 194_195_196 at right
                    if M_mom.is_set("robe on"):
                        show mom_robe 194b_195b_196b
                pause
                pause
                mom "Oh!!!!"
                mom "Sim!!!"

            if M_mom.is_set("sex flip"):
                show player finger 193bf zorder 3
                show mom 197f
                if M_mom.is_set("robe on"):
                    show mom_robe 197bf
            else:

                show player finger 193b zorder 3
                show mom 197
                if M_mom.is_set("robe on"):
                    show mom_robe 197b
            with flash
            mom "AHHH!"
            pause

            if M_mom.get_state() == S_mom_fetch_towel:
                show mom 197ff at left
                show player 11f at Position (xpos=600)
                with dissolve
                mom "Querido?"
                show mom 197cf
                show player 12f
                player_name "Sim-"
                show player 11f
                show mom 197df
                mom "Oh, não... não não nao... NÃO!"
                mom "O que eu estou fazendo..."
                show mom 197ff
                mom "O que eu fiz..."
                show mom 197cf
                show player 10f
                player_name "O que tem, {b}[mom_name]{/b}?"
                show player 11f
                show mom 197ff
                mom "Querido, me desculpa."
                show mom 197df
                mom "Eu... eu bebi demais."
                mom "Preciso ir para a cama."
                show mom 197ff
                mom "Desculpa."
                show mom 197df
                mom "Eu-"
                hide mom with fastdissolve
                show player 10 at center with dissolve
                player_name "{b}[mom_name]{/b}?"
                show player 10
                player_name "Eu estava tão perto..."
                show player 5
                pause
                show player 24
                player_name "Espero que ela esteja bem..."
                pause
                show player 25
                player_name "Eu deveria dormir e falar com ela amanhã."
                hide player with dissolve
                $ M_mom.trigger(T_mom_gave_towel)
                $ unlock_ui()
                $ location_count = "Dining Room"
            else:

                show player 13 zorder 0 at Position (xoffset=-118)
                show mom 184d
                if M_mom.is_set("robe on"):
                    show mom_robe 184f
                with dissolve

                if randomizer() <= 50:
                    mom "Oh, querido, isso foi ótimo."
                    show mom 184c
                    show player 14 at Position (xoffset=-118)
                    player_name "Valeu, {b}[mom_name]{/b}."
                else:

                    mom "Oh! Foi ótimo. Ainda tenho arrepios!"
                    mom "Aposto que seu pau está duro como uma pedra."
                    show mom 184c
                    show player 14 at Position (xoffset=-118)
                    player_name "Sim, foi gostoso te fazer gozar."
                show player 13 at Position (xoffset=-118)
                show mom 184d
                mom "Se você quiser que a mamãe cuide de você, me fale."
        $ gTimer.tick()
    hide player
    hide mom
    hide mom_robe
    with dissolve
    $ callScreen(location_count)

label mom_midnight_swim:
    scene home_diningroom_cs01 with fade
    show text "Quando me aproximei da porta, pude sentir meu coração batendo no meu peito...\nEstava pensando no que estava acontecendo lá fora a essas horas da noite...\nEu abri a porta do pátio...\n...e olhei para o nosso quintal iluminado pela lua." at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide home_diningroom_cs01
    with dissolve

    scene home_backyard_pool_c
    show mom 214
    mom "Ha ha ha! O que você está fazendo?"
    show mom 212
    dia "O que? você é muito velha para abraçar sua irmã?"
    show mom 214
    dia "Ha ha ha!"
    mom "Ha ha ha!"
    show mom 211
    dia "Sabe, as vezes eu me esqueço que seus peitos são tão grandes quando os meus!"
    show mom 213
    mom "Eu acho que não! Eu acho que o seu é maior!"
    mom "Embora que, provavelmente, seja por causa desse seu novo ramo."
    show mom 212
    dia "Talvez vocẽ devesse tentar..."
    show mom 215
    dia "A solidão desaparece..."
    show mom 213
    mom "Ah, você é tão safadinha!"
    show mom 211
    dia "Ah, e vocẽ não é?"
    show mom 214
    mom "Ha ha ha!"
    dia "Ha ha ha!"
    show mom 212b_215b
    pause
    pause
    show mom 213
    mom "Deixa eu ir!"
    mom "Antes que eu me mije!"
    mom "Você está me fazendo cócegas!"
    show mom 212
    dia "E daí? Estamos na água!"
    show mom 213
    mom "Sim, mas é na minha piscina!"
    show mom 212
    dia "Que seja."
    show mom 200
    show aunt 170
    with dissolve
    pause
    show aunt 171
    dia "Isso é divertido."
    dia "Eu não nadava nua há muitos anos."
    show aunt 176
    dia "Não desde que marcamos um encontro com seu marido e meu primeiro marido em Pebble Beach."
    show aunt 175
    show mom 201
    mom "Oh, aquilo foi divertido..."
    show mom 198
    show aunt 170
    pause
    show mom 199
    mom "Merda, sinto falta de sexo..."
    show mom 198
    show aunt 173
    dia "Fale mais."
    show aunt 172
    dia "Nenhum dos meus brinquedinhos se comparam à sensação de um pau de verdade."
    show aunt 174
    dia "Mas não se preocupe. Agora que você está solteira, talvez possamos sair juntas de novo?"
    show aunt 175
    show mom 199
    mom "Não sei, {b}Diane{/b}..."
    show mom 198
    show aunt 176
    dia "Ah, não se prenda."
    dia "Lembra dos tempos selvagens e estranhos que costumávamos ter?"
    show aunt 175
    show mom 199
    mom "Sim..."
    mom "Mas..."
    show mom 198
    show aunt 176
    dia "Mas o quê?"
    show aunt 175
    pause
    show mom 199
    mom "Eu... Eu talvez tenha feito algo errado..."
    show mom 198
    show aunt 171
    dia "O que houve?!"
    show aunt 170
    show mom 199
    mom "É um...tabu..."
    show mom 198
    show aunt 171
    dia "Me diga! Me diga!"
    show aunt 170
    show mom 199
    mom "Não posso! É muuuito errado!"
    show mom 198
    show aunt 171
    dia "Você tem que me contar!"
    show aunt 170
    mom "..."
    show aunt 174
    dia "Vai, irmã. Você me conhece."
    show aunt 170
    show mom 201
    mom "Eu sei, tenho certeza que você estaria de acordo com isso."
    show mom 199
    mom "Mas eu não."
    show mom 201
    mom "Não completamente..."
    show mom 198
    pause
    show aunt 171
    dia "Apenas uma parte então!"
    show aunt 170
    pause
    show mom 199
    mom "Talvez eu fiz algo de errado com..."
    mom "...Com o {b}[firstname]{/b}."
    show mom 198
    show aunt 171
    dia "Não!"
    dia "Tipo o quê?"
    show aunt 170
    show mom 199
    mom "Não sei..."
    mom "Eu acho que eu quero..."
    show mom 198
    show aunt 176
    dia "!!!"
    show aunt 175
    show mom 199
    mom "Digo...é tudo o que eu penso ultimamente."
    show mom 198
    show aunt 176
    dia "Você é bem safadinha...e eu gosto disso."
    dia "Eu acho que você deveria fazer isso."
    show aunt 175
    show mom 201
    mom "Claro que você acha."
    mom "Mas não é seu filho."
    show mom 199
    mom "Eu sou a mãe dele."
    mom "Não é algo que uma boa mãe deveria fazer.."
    show mom 198
    show aunt 174
    dia "Para."
    dia "Você é uma boa mãe."
    dia "E vocês dois são adultos."
    show aunt 176
    dia "Apenas me diga todos os detalhes depois que vocês fizerem..."
    show aunt 175
    show mom 201
    mom "Não seja tão safada."
    mom "Merda, tô tão excitada agora."
    show mom 200
    show aunt 173
    dia "Você e eu..."
    show aunt 175
    show mom 201
    mom "Não olhe o meu garoto agora."
    show mom 200
    show aunt 176
    dia "E você não esconda ele!"
    show aunt 175
    pause
    show mom 199
    mom "Não acredito que eu te contei..."
    show mom 201
    mom "Você e seus vinhos..."
    show mom 200
    show aunt 172
    dia "Ha ha ha..."
    dia "Não culpe o vinho, garota."
    show aunt 170
    pause
    show aunt 173
    dia "Estou tão bêbada..."
    dia "...E eu tenho muito trabalho para fazer amanhã!!"
    show aunt 174
    dia "Eu deveria ir..."
    show aunt 170
    show mom 199
    mom "Fique um pouco mais!"
    show mom 198
    show aunt 176
    dia "Não vou cair nos seus truques."
    show mom 200
    dia "Além disso, você não deveria ver seu filho?"
    show aunt 173
    dia "Sabe... Se ele não estiver dormindo, você poderia-"
    show aunt 175
    show mom 201
    mom "Ah, pare e leve essa sua bunda para sua casa."
    mom "Eu sabia que não deveria ter te contado isso."
    show mom 200
    show aunt 172
    dia "Ha ha ha!"
    show aunt 171
    dia "Foi divertido. Deveriamos fazer isso de novo!"
    show aunt 177 with dissolve
    pause
    show mom 201
    mom "Foi mesmo! Boa noite, {b}Diane{/b}."
    show mom 202
    show aunt 178
    with dissolve
    dia "Woah!"
    dia "Eu estou... um pouco... bêbada!"
    mom "Cuide-se!"
    dia "Você que tem que ter mais cuidado!"
    dia "Olha quem tem as duas toalhas!"
    show aunt 179 with dissolve
    dia "Boa noite, irmã! Divirta-se andando pelada!"
    mom "Hey! {b}Diane{/b}!"
    hide aunt with dissolve
    pause
    show mom 199 with dissolve
    mom "Isso não faz sentido..."
    mom "Não sou eu que moro no outro lado da cidade..."
    show mom 198
    pause
    show mom 199
    mom "Eu deveria voltar lá pra dentro..."
    mom "Está ficando frio e ela saiu com as minhas toalhas."
    scene black with fade
    hide mom
    pause 1

    scene home_diningroom_n_c
    show player 26f with dissolve
    player_name "Eu deveria ver se a {b}[mom_name]{/b} precisa de toalhas."
    hide player with dissolve

    scene backyard_n_c with fade
    show mom 208f at left
    show player 434f at right
    with dissolve
    mom "Aquela loucas. Não acredito que ela me deixou-"
    show player 435f
    player_name "{b}[mom_name]{/b}?"
    show player 434f
    show mom 203 with dissolve
    mom "!!!"
    show player 13f
    show mom 204
    mom "Querido!"
    mom "O qu...o que você está fazendo aqui?"
    show mom 205
    show player 14f
    player_name "Ouvi uns barulhos estranhos no fundo."
    player_name "E pensei em vir dar uma olhada."
    show player 13f
    show mom 204
    mom "Oh... Desuclpa por ter te acordado."
    show mom 205
    show player 26f
    player_name "Não, sem problemas."
    show player 14f
    player_name "Só achei que alguém estava tentando nos roubar."
    show player 13f
    show mom 204
    mom "Não, era sua tia e eu...relaxando."
    show mom 206
    mom "Você não-"
    show mom 205
    show player 29f with dissolve
    player_name "Não vi ela. Acabei de chegar."
    show player 13f with dissolve
    show mom 204
    mom "...Ótimo..."
    show mom 205
    pause
    show player 434f
    show mom 206
    mom "{b}*Brrr*{/b}"
    mom "Eu...eu estou com frio."
    show mom 205
    show player 14f
    player_name "Quer que eu busque algo?"
    show player 13f
    show mom 204
    mom "Você poderia trazer uma {b}toalha do banheiro{/b} para sua mãe?"
    mom "Estou meio...molhada..."
    show mom 205
    show player 14f
    player_name "Claro! Já volto!"
    show player 10f
    player_name "Não... Não saia daqui!"
    hide player
    hide mom
    with dissolve
    $ M_mom.trigger(T_mom_midnight_swim)
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
