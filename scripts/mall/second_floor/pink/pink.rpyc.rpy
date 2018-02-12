init python:
    class PinkItem:
        def __init__(self, item, name = "", image = "", popup = "", idle = "", hover = "", price = 0, category = "", purchased = False):
            self.name = name
            self.image = image
            self.popup = popup
            self.idle = idle
            self.hover = hover
            self.price = price
            self.category = category
            self.item = item
            self.purchased = purchased


    class PinkStore (object) :
        def __init__(self):
            self.items = []

label pink_dialogue:
    $ location_count = "Pink"
    default ivy_dialogue_count = 0
    default ivy_first_visit = True
    default ivy_xray_toggle = False
    default ivy_condom_on = True
    default xray_front = False
    default xray_needed = False
    default ivy_cum_inside = False

    if pink_count < 1:
        scene pink
        show player 23 with dissolve
        player_name "( Wow! )"
        show player 21
        player_name "( Isso é... Tem muitas coisas estranhas aqui. )"
        show player 29
        player_name "( Hmm... Talvez serão úteis um dia... )"
        hide player 29 with dissolve
        hide pink
        $ pink_count = 1

    if M_mia.get_state() == S_mia_helen_outfit_request and red_corset not in inventory.items:
        scene pink
        show player 12 with dissolve
        player_name "Eu deveria olhar nesse rack de roupas..."
        player_name "...Eles devem ter umas lingeries."
        hide player with dissolve

    elif M_mia.get_state() in [S_mia_angelicas_order, S_mia_angelicas_whip] and whip not in inventory.items:
        scene pink with fade
        show player 12 with dissolve
        player_name "Deve ter algo aqui que se pareça com um {b}chicote{/b}..."
        hide player with dissolve
    $ callScreen(location_count)

label ivy_button_dialogue:
    if ivy_dialogue_count == 0:
        scene location_pink_closeup
        $ ivy_dialogue_count = 1
        show player 1 at left with dissolve
        show ivy 2 at right with dissolve
        ivy "Oi!"
        ivy "Posso te ajudar com algo?"
        show player 29
        show ivy 1
        player_name "É minha primeira vez aqui. Eu... Umm..."
        show player 13
        show ivy 3
        ivy "Está tudo bem! Eu entendo! Todo mundo é tímido quando vem pela primeira vez..."
        show ivy 2
        ivy "Nós temos vários {b}brinquedo{/b} e {b}aparelhos sexuais{/b} que você pode ver ali na amostra."
        show player 11
        ivy "Nós também oferecemos... {b}sessões de mssagens{/b} nas nossas... salas privadas."
        ivy "Nosso massagista usa uma variedade de técnicas naturais de relaxamento corporal... Isso certamente irá satisfazer suas necessidades..."
        show player 12
        show ivy 1
        player_name "Oh... Não sabia que vocês faziam massagens aqui."
        show player 1
        show ivy 3
        ivy "É um dos nossos... serviços... não muito anunciados."
        show ivy 2
        ivy "Você gostaria de ver nosso {b}panfleto{/b} de massagens?"
        menu:
            "Sim.":
                show ivy 5
                show player 21
                player_name "Sim, quero dar uma olhada..."
                show player 13
                show ivy 4
                ivy "Claro! Olha!"
                hide ivy
                hide player
                with dissolve
                call screen pamphlet

            "Pacotes." if quest13 in quest_list and quest13 not in completed_quests and package not in inventory.items:
                show ivy 1
                show player 2
                player_name "Estou aqui para pegar um {b}pacote{/b}."
                show player 1
                show ivy 3
                ivy "Claro!"
                show ivy 2
                ivy "Está no nome de quem?"
                show ivy 1
                show player 12
                player_name "{b}Diane{/b}?"
                show player 1
                show ivy 11
                ivy "Deixa eu ver... Certo! Aqui!"
                show ivy 1
                show player 170
                player_name "Valeu!"
                show ivy 3
                show player 169
                ivy "É para sua {b}namorada{/b}?"
                show ivy 1
                show player 171
                player_name "!!!"
                show player 29
                player_name "Oh... Não! É para... Ummm... alguém que me pediu!"
                show ivy 2
                show player 13
                ivy "Bem, é um item muito bom da nossa coleção..."
                show ivy 3
                ivy "Tenho certeza que você vai gostar!"
                show player 21
                show ivy 4
                player_name "Valeu..."
                hide player 21
                hide ivy 4
                show unlock29 at truecenter
                with dissolve
                $ inventory.items.append(package)
                $ renpy.pause()
                hide unlock29 with dissolve
            "Só estou comprando.":

                show player 10
                show ivy 1
                player_name "Não, valeu."
                player_name "Só estou procurando algo para comprar..."
                show player 13
                show ivy 3
                ivy "Beleza então! Se precisar de algo, é só me chamar."
        $ callScreen(location_count)
    else:

        scene pink
        show player 1 at left with dissolve
        show ivy 2 at right with dissolve
        ivy "Oi!"
        ivy "Como posso te ajudar?"
        menu:
            "Pacote." if quest13 in quest_list and quest13 not in completed_quests and package not in inventory.items:
                show ivy 1
                show player 2
                player_name "Oi!"
                player_name "Estou aqui para pegar um {b}pacote{/b}."
                show player 1
                show ivy 3
                ivy "Claro!"
                show ivy 2
                ivy "Está no nome de quem?"
                show ivy 1
                show player 12
                player_name "{b}Diane{/b}?"
                show player 1
                show ivy 11
                ivy "Deixa eu ver... Certo! Aqui!"
                show ivy 1
                show player 170
                player_name "Valeu!"
                show ivy 3
                show player 169
                ivy "É para sua {b}namorada{/b}{/b}?"
                show ivy 1
                show player 171
                player_name "!!!"
                show player 29
                player_name "Não... Não! É para... Ummm... Alguém que me pediu!"
                show ivy 2
                show player 13
                ivy "Bem, é um item muito bom da nossa coleção..."
                show ivy 3
                ivy "Tenho certeza que você vai gostar!"
                show player 21
                show ivy 4
                player_name "Valeu..."
                hide player 21
                hide ivy 4
                show unlock29 at truecenter
                with dissolve
                $ inventory.items.append(package)
                $ renpy.pause()
                hide unlock29 with dissolve
            "Massagem.":

                show ivy 5
                show player 21
                player_name "Eu poderia... ver o planfeto de massagens?"
                show player 13
                show ivy 4
                ivy "Claro! Divirta-se!"
                player_name "Obrigado..."
                hide ivy
                hide player
                with dissolve
                call screen pamphlet
            "Só estou comprando.":

                show player 10
                show ivy 1
                player_name "Só vim para fazer umas compras..."
                show player 13
                show ivy 3
                ivy "Beleza então! Me chame se você precisar de algo."
        $ callScreen(location_count)

label ivy_paizuri:
    scene pink
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Vou tentar o básico."
    ivy "Só testando, né?"
    show player 29
    player_name "Eu, ehh..."
    show ivy 3
    ivy "Heh, só estou brincando!"
    show ivy 12
    ivy "Me siga."
    scene massage_room_closeup
    with dissolve
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    if ivy_first_visit == True:
        show player 43 at left
        player_name "{b}*assobio*{/b} Bela sala."
        show player 1
        show ivy 3 at right with dissolve
        ivy "{b}*risada*{/b} Vai ficar aina mais legal quando começarmos."
        show ivy 2
        ivy "Agora, tira a roupa e deite-se na cama. Você pode colocar suas roupas na mesa."
        ivy "Vou te dar uns minutos para se preparar."
        ivy "Tenho que ter certeza que ninguém nos interrompa..."
        hide ivy 2 with dissolve
        show player 18
        player_name "( Phew! É menos estranho do que imaginava! )"
        scene blank with dissolve
        scene massage_room_closeup
        show player 175 at left
        with dissolve
        player_name "( Eu não esperava que fosse tão direto... )"
        show player 57
        player_name "( Já estou pronto para isso? )"
        player_name "( ...Não posso mais voltar. )"
        show player 175
        player_name "( Espero que eu goste. )"
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
        with dissolve
        ivy "{b}*Risada*{/b} Por que você ainda está usando isso?"
        ivy "Não precisamos de toalhas para esse tipo de massagem."
        player_name "Oh. Desculpa..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "Pronto! Muito melhor, não é?"
        player_name "Sim, bem melhor."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "Como você guarda isso?"
        ivy "De qualquer forma: me chamo Ivy."
        ivy "Agora, minha vez de me preparar..."
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Gosta do que vê?"
        player_name "Sim..."
        ivy "{b}*risadinha*{/b} Seu amiguinho falar por você."
        ivy "Acho que vou ter que tomar cuidado disso..."
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 7 at Position (xpos=518,ypos=725) with dissolve
        ivy "Antes de começar, quero te contar algo."
        ivy "Essa sala é à prova de som..."
        player_name "( Oh? )"
        ivy "...então você não precisa guardar nala."
        ivy "Agora, relaaaaxe..."
        $ ivy_first_visit = False
    else:

        show player 1
        ivy "Você sabe o procedimento. Volto em um minuto."
        hide ivy with dissolve
        pause 0.5
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        with dissolve
        pause 2
        show ivy 18 at Position (xpos=870,ypos=655) with dissolve
        ivy "Ok! Pronto!"
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Vamos fazer isso!"
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 6 at Position (xpos=516,ypos=724)
    $ ivy_sex_speed = 0.8
    $ ivy_paizuri_stage = 0
    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ xray_needed = False

    label ivy_paizuri_stage1:
        show playersex 19 zorder 1
        show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_paizuri_options
            hide screen ivy_sex_xray_button
            hide playersex 19
            hide ivysex 5
            show ivysex 6_5 at Position (xpos=513,ypos=728)
            pause 4
        else:

            hide screen ivy_paizuri_options
            hide screen ivy_sex_xray_button
            show ivysex 6 zorder 2 at Position (xpos=516,ypos=724)
            pause
            show ivysex 5 at Position (xpos=514,ypos=729)
            pause
            show ivysex 6 at Position (xpos=516,ypos=724)
            pause
            show ivysex 5 at Position (xpos=514,ypos=729)
            pause
            show ivysex 6 at Position (xpos=516,ypos=724)
            pause
            show ivysex 5 at Position (xpos=514,ypos=729)
            pause
            show ivysex 6 at Position (xpos=516,ypos=724)
            pause
        $ ivy_paizuri_stage += 1
        if ivy_paizuri_stage == 1:
            if anim_toggle:
                ivy "Aposto que isso não é tão bom quando você usa sua mão..."
                player_name "( Não chega nem perto! )"
                player_name "Mais rápido..."
                hide ivysex 6_5
                show playersex 19 zorder 1
                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
            else:

                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
                ivy "Aposto que isso não é tão bom quando você usa sua mão..."
                show ivysex 6 at Position (xpos=516,ypos=724)
                player_name "( Não chega perto! )"
                show ivysex 5 at Position (xpos=514,ypos=729)
                player_name "Mais rápido..."
                show ivysex 6 at Position (xpos=516,ypos=724)
            window hide

        elif ivy_paizuri_stage == 2:
            if anim_toggle:
                ivy "Você está-{b}*huff*{/b}-quase?"
                player_name "Sim..."
                ivy "Então vamos entrar em alta velocidade!"
                player_name "Aaah-vou..."
                hide ivysex 6_5
                show playersex 19 zorder 1
                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
            else:

                show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
                ivy "Você está-{b}*huff*{/b}-quase?"
                show ivysex 6 at Position (xpos=516,ypos=724)
                player_name "Sim..."
                ivy "Então vamos entrar em alta velocidade!"
                player_name "Aaah-vou..."
            window hide

        elif ivy_paizuri_stage == 3:
            hide ivysex 6_5
            show playersex 19 zorder 1
            show ivysex 5 zorder 2 at Position (xpos=514,ypos=729)
            player_name "...vou...GOZAR!"
            show ivysex 7 at Position (xpos=518,ypos=725)
            ivy "Goze!"
            window hide
            show white zorder 4 with dissolve
            hide white with dissolve
            show expression "characters/player/char_player_sex_25.png" zorder 3 at Position (xpos=498,ypos=400)
            with Dissolve(0.3)
            hide expression "characters/player/char_player_sex_25.png"
            show expression "characters/player/char_player_sex_26.png" zorder 3 at Position (xpos=498,ypos=400)
            with Dissolve(0.3)
            hide expression "characters/player/char_player_sex_26.png"
            show expression "characters/player/char_player_sex_27.png" zorder 3 at Position (xpos=500,ypos=434)
            with Dissolve(0.3)
            hide expression "characters/player/char_player_sex_27.png"
            show expression "characters/player/char_player_sex_28.png" zorder 3 at Position (xpos=503,ypos=434)
            with Dissolve(0.3)
            ivy "Wow.... quanto..."
            ivy "Você gostou?"
            player_name "Sim... você é ótima."
            ivy "{b}*risadinha*{/b} Eu sei."
            ivy "Quanta bagunça..."
            ivy "Vamos nos limpar."
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_paizuri_options
        jump ivy_paizuri_stage1

label ivy_blowjob:
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Sim. quero a clássica, por favor."
    ivy "Ah? Estave olhando meus lábios?"
    show player 29
    player_name "Eu ehh..."
    show ivy 3
    ivy "Calma, só estou brincando!"
    show ivy 12
    ivy "Me siga."
    scene massage_room_closeup
    show player 1 at left with dissolve
    show ivy 3 at right with dissolve
    ivy "Ok, vou me certificar que ninugém nos interrompa."
    if ivy_first_visit == True:
        show player 43 at left
        player_name "{b}*assobio*{/b} Bela sala."
        show player 1
        ivy "{b}*risada*{/b} Vai ficar aina mais legal quando começarmos."
        show ivy 2
        ivy "Agora, tira a roupa e deite-se na cama. Você pode colocar suas roupas na mesa."
        ivy "Vou te dar uns minutos para se preparar."
        ivy "Tenho que ter certeza que ninguém nos interrompa..."
        hide ivy 2 with dissolve
        show player 18
        player_name "( Phew! É menos estranho do que imaginava! )"
        show player 175 with dissolve
        player_name "( Eu não esperava que fosse tão direto... )"
        show player 57
        player_name "( Já estou pronto para isso? )"
        player_name "( ...Não posso mais voltar. )"
        show player 175
        player_name "( Espero que eu goste. )"
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        with dissolve
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
        ivy "{b}*Risada*{/b} Por que você ainda está usando isso?"
        ivy "Não precisamos de toalhas para esse tipo de massagem."
        player_name "Oh. Desculpa..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "Pronto! Muito melhor, não é?"
        player_name "Sim, bem melhor."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "Como você guarda isso?"
        ivy "De qualquer forma: me chamo Ivy."
        ivy "Agora, minha vez de me preparar..."
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Gosta do que vê?"
        player_name "Sim..."
        ivy "{b}*risadinha*{/b} Seu amiguinho falar por você."
        ivy "Acho que vou ter que tomar cuidado disso..."
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 2 at Position (xpos=515,ypos=723) with dissolve
        ivy "Antes de começar, quero te contar algo."
        ivy "Essa sala é à prova de som..."
        player_name "( Oh? )"
        ivy "...então você não precisa guardar nela."
        ivy "Ah, e me diga quando você estiver perto, tá?"
        player_name "Claro."
        ivy "Agora, deite aí e relaxe..."
        $ ivy_first_visit = False
    else:
        ivy "Você sabe o procedimento, já volto."
        hide ivy with dissolve
        pause 0.5
        hide player
        scene massage_room
        show playersex 19 zorder 1
        with dissolve
        pause 2
        show ivy 18 at Position (xpos=870,ypos=655) with dissolve
        ivy "Ok! Beleza!"
        show ivy 19 at Position (xpos=819,ypos=655) with dissolve
        pause 1
        show ivy 20 at Position (xpos=865,ypos=655) with dissolve
        ivy "Vamos fazer isso!"
        hide ivy
        show ivysex 1 zorder 2 at Position (xpos=546,ypos=728)
        with dissolve
        show ivysex 2 at Position (xpos=515,ypos=723)
    $ ivy_sex_speed = 0.8
    $ ivy_blowjob_stage = 0
    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ xray_needed = False

    label ivy_blowjob_stage1:
        show playersex 19 zorder 1
        show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_blowjob_options
            hide screen ivy_sex_xray_button
            hide playersex 19
            hide ivysex 3
            show ivysex 4_3 at Position (xpos=515,ypos=724)
            pause 4
        else:
            hide screen ivy_blowjob_options
            hide screen ivy_sex_xray_button
            show ivysex 4 zorder 2 at Position (xpos=515,ypos=723)
            pause
            show ivysex 3 at Position (xpos=515,ypos=724)
            pause
            show ivysex 4 at Position (xpos=515,ypos=723)
            pause
            show ivysex 3 at Position (xpos=515,ypos=724)
            pause
            show ivysex 4 at Position (xpos=515,ypos=723)
            pause
            show ivysex 3 at Position (xpos=515,ypos=724)
            pause
            show ivysex 4 at Position (xpos=515,ypos=723)
            pause
        $ ivy_blowjob_stage += 1
        if ivy_blowjob_stage == 1:
            if anim_toggle:
                player_name "( Cara, se a boca dela é tão boa, o sexo deve ser uma maravilha... )"
                player_name "Aaah... Mais rápido..."
                hide ivysex 4_3
                show playersex 19 zorder 1
                show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
            else:
                show ivysex 3 at Position (xpos=515,ypos=724)
                player_name "( Cara, se a boca dela é tão boa, o sexo deve ser uma maravilha... )"
                show ivysex 4 at Position (xpos=515,ypos=723)
                player_name "Aaah... Mais rápido..."
            window hide
        elif ivy_blowjob_stage == 2:
            if anim_toggle:
                player_name "( Merda, estou quase... )"
                player_name "Mais rápido."
                hide ivysex 4_3
                show playersex 19 zorder 1
                show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
            else:
                show ivysex 3 at Position (xpos=515,ypos=724)
                player_name "( Merda, estou quase... )"
                show ivysex 4 at Position (xpos=515,ypos=723)
                player_name "Mais rápido."
            window hide
        elif ivy_blowjob_stage == 3:
            hide ivysex 4_3
            show playersex 19 zorder 1
            show ivysex 3 zorder 2 at Position (xpos=515,ypos=724)
            player_name "( Tenho que avisar... )"
            show ivysex 4 at Position (xpos=515,ypos=723)
            player_name "Que tô quase-"
            show ivysex 3 at Position (xpos=515,ypos=724)
            player_name "MERDA!"
            show white zorder 4 with dissolve
            hide white
            show ivysex 24 at Position (xpos=515,ypos=750)
            with dissolve
            show ivysex 25 at Position (xpos=515,ypos=750) with dissolve
            player_name "Eu uhh..."
            show ivysex 26 at Position (xpos=548,ypos=730)
            ivy "{b}*tosse*{/b} {b}*tosse*{/b}"
            ivy "O que você não entendeu na parte do \"me avise\"?"
            player_name "Uhh, desculpa..."
            ivy "Você sabe, costumo cobrar extra por engolir."
            player_name "Eu..."
            player_name "( Merda, não devia ter feito isso. )"
            show ivysex 1
            ivy "{b}*risadinha*{/b} Cara, você tinha que ver seu rosto!"
            ivy "Não se preocupe, eu gostei! É da casa."
            player_name "*risada nervosa* Obrigado."
            player_name "Quero me desculpar de novo..."
            ivy "Está tudo bem, sério... Sabe, meus clientes geralmente não se {b}empolgam{/b} tanto."
            player_name "Oh, uh, valeu, eu acho."
            ivy "Agora, vamos nos limpar."
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_blowjob_options
        jump ivy_blowjob_stage1

label ivy_reverse_cowgirl:
    $ xray_front = False
    show player 174 at left
    show ivy 5 at right
    with dissolve
    player_name "Ah, quero o premium, por favor."
    ivy "Ohoh, bem ousado para a sua idade!"
    show player 29
    player_name "Eu uhh..."
    show ivy 3
    ivy "{b}*risada*{/b} gosto de homens assim!"
    show ivy 2
    ivy "Me siga."
    scene massage_room_closeup
    with dissolve
    show ivy 2 at right with dissolve
    show player 43 at left with dissolve
    ivy "Certo, vou garantir que ninugém nos interrompa."
    if ivy_first_visit == True:
        player_name "{b}*assobio*{/b} Bela sala."
        show player 1
        show ivy 3 at right
        ivy "{b}*risada*{/b} Vai ficar aina mais legal quando começarmos."
        show ivy 2
        ivy "Agora, tira a roupa e deite-se na cama. Você pode colocar suas roupas na mesa."
        ivy "Vou te dar uns minutos para se preparar."
        ivy "Tenho que ter certeza que ninguém nos interrompa."
        hide ivy 2 with dissolve
        show player 18
        player_name "( Phew! É menos estranho do que imaginava! )"
        show player 175 with dissolve
        player_name "( Eu não esperava que fosse tão direto... )"
        show player 57
        player_name "( Já estou pronto para isso? )"
        player_name "( ...Não posso mais voltar. )"
        show player 175
        player_name "( Espero que eu goste. )"
        hide player with dissolve
        scene massage_room
        show playersex 19 zorder 1
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        with dissolve
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655) with dissolve
        ivy "{b}*Risada*{/b} Por que você ainda está usando isso?"
        ivy "Não precisamos de toalhas para esse tipo de massagem."
        player_name "Oh. Desculpa..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "Pronto! Muito melhor, não é?"
        player_name "Sim, bem melhor."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "Como você guarda isso?"
        ivy "De qualquer forma: me chamo Ivy."
        ivy "Agora, minha vez de me preparar..."
    hide player
    scene massage_room
    show playersex 19 zorder 1
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "Vamos ter que usar camisinha pra isso."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Aww, cara..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "Oh, não se preocupe! você nem vai sentir. Confie em mim."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "Pronto, vamos lá..."
    $ ivy_first_visit = False
    hide player
    scene massage_room
    show playersex 19 zorder 1
    if ivy_condom_on == True:
        show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 15 zorder 2 at Position (xpos=510,ypos=715)
    with dissolve
    pause
    show ivysex 16 zorder 2 at Position (xpos=520,ypos=720) with dissolve
    pause
    show ivysex 17 zorder 2 at Position (xpos=530,ypos=720) with dissolve
    ivy "{b}*risada*{/b} Me pergunto se vou conseguir..."
    ivy "Você está pronto para ir para o céu?"
    player_name "{b}*Glup*{/b} Sim."
    ivy "Aqui vamos nós..."
    show playersex 22
    show ivysex 18 zorder 2 at Position (xpos=538,ypos=726) with dissolve
    show ivysex 19 zorder 2 at Position (xpos=538,ypos=707) with dissolve
    player_name "Haaah-"
    show ivysex 20 zorder 2 at Position (xpos=538,ypos=724)
    ivy "Está tudo bem aí?"
    player_name "Sim, continue..."
    $ ivy_sex_speed = 0.8
    $ ivy_rcowgirl_stage = 0
    $ xray = 1
    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ ivy_cum_inside = False
    $ xray_front = False
    $ xray_needed = True

    label ivy_rcgirl_stage1:
        show playersex 22 zorder 1
        show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
        show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
        show screen ivy_sex_xray
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_rcowgirl_options
            hide screen ivy_sex_xray
            hide screen ivy_sex_xray_button
            hide playersex 22
            hide expression "characters/player/char_player_sex_29.png"
            hide ivysex 19
            if ivy_xray_toggle == True:
                show ivysex_xray 39_40 at Position (xpos=515,ypos=724)
            else:
                show ivysex 18_19 at Position (xpos=515,ypos=724)
            pause 4
        else:
            hide screen ivy_rcowgirl_options
            hide screen ivy_sex_xray_button
            $ xray = 0
            show ivysex 18 zorder 2 at Position (xpos=538,ypos=726)
            pause
            $ xray = 1
            show ivysex 19 at Position (xpos=538,ypos=707)
            pause
            $ xray = 0
            show ivysex 18 at Position (xpos=538,ypos=726)
            pause
            $ xray = 1
            show ivysex 19 at Position (xpos=538,ypos=707)
            pause
            $ xray = 0
            show ivysex 18 at Position (xpos=538,ypos=726)
            pause
            $ xray = 1
            show ivysex 19 at Position (xpos=538,ypos=707)
            pause
            $ xray = 0
            show ivysex 18 at Position (xpos=538,ypos=726)
            pause
        $ ivy_rcowgirl_stage += 1
        if ivy_rcowgirl_stage == 1:
            if anim_toggle:
                player_name "( Puta merda, isso é muito bom! )"
                player_name "Pode ir mais forte. Eu consigo aguentar..."
                ivy "Ok. Você pediu por isso!"
                hide ivysex 18_19
                hide ivysex_xray 39_40
                show playersex 22 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
                show screen ivy_sex_xray
            else:
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                player_name "( Caralho, isso é muito bom! )"
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                player_name "Pode ir mais rápido... Acho que aguento..."
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                ivy "Ok. Você pediu por isso!"
            window hide
        elif ivy_rcowgirl_stage == 2:
            if anim_toggle:
                player_name "( Só vou aguentar mais um pouco... )"
                ivy "Haah-Tenho que dizer..."
                ivy "...você pode ser só um adolescente..."
                ivy "...mas você-aaahh-é melhor que muitos clientes!"
                player_name "( Isso aumentou meu ego. )"
                player_name "( Eu me pergunto como ela reagiria... )"
                hide ivysex 18_19
                hide ivysex_xray 39_40
                show playersex 22 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
                show screen ivy_sex_xray
            else:
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                player_name "( Tenho que aguentar um pouco mais... )"
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                ivy "Haah-Tenho que dizer..."
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                ivy "...você pode ser um adolescente..."
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                ivy "...mas você-aah-deixa alguns dos meus clientes no chão!"
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
                player_name "( Essa é uma maneira de aumentar meu ego. )"
                $ xray = 0
                show ivysex 18 at Position (xpos=538,ypos=726)
                player_name "( Me pergunto como ela reagiria se... )"
                $ xray = 1
                show ivysex 19 at Position (xpos=538,ypos=707)
            window hide
        elif ivy_rcowgirl_stage == 3:
            $ xray = 1
            if not anim_toggle:
                hide ivysex 18_19
                hide ivysex_xray 39_40
                show playersex 22 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 19 zorder 2 at Position (xpos=538,ypos=707)
            player_name "( Merda, estou no meu limite! )"
            player_name "( Ela é muito boa nisso! )"
            player_name "Vou gozar!"

            label ivy_rcowgirl_cum_options_menu:
            show screen ivy_rcowgirl_cum_options
            pause
            jump ivy_rcowgirl_cum_options_menu
            label ivy_rcowgirl_cum_inside:
                hide screen ivy_rcowgirl_cum_options
                ivy "Haah- pode gozar!"
                hide screen ivy_sex_xray
                $ ivy_cum_inside = True
                jump ivy_rcowgirl_cum_end
            label ivy_rcowgirl_cum_outside:
                hide screen ivy_rcowgirl_cum_options
                ivy "Haah- pode gozar!"
                hide screen ivy_sex_xray
                $ ivy_cum_inside = False
                jump ivy_rcowgirl_cum_end
            label ivy_rcowgirl_cum_end:
            hide ivysex_xray
            if ivy_cum_inside == True:
                show playersex 22
                show ivysex 19 zorder 2 at Position (xpos=538,ypos=708)
            else:
                hide expression "characters/player/char_player_sex_29.png"
                show playersex 19
                show ivysex 16 zorder 2 at Position (xpos=521,ypos=718)
                show expression "characters/player/char_player_sex_25.png" zorder 3 at Position (xpos=494,ypos=415)
            show white zorder 3 with hpunch
            if ivy_cum_inside == True:
                show screen ivy_sex_xray
            hide white
            with dissolve
            ivy "Haaa..."
            hide expression "characters/player/char_player_sex_25.png"
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_51.png" zorder 3 at Position (xpos=490,ypos=338)
            ivy "Haah... você aguentou por um bom tempo... por ser um adolescente."
            if ivy_cum_inside == True:
                hide screen ivy_sex_xray

            hide expression "characters/player/char_player_sex_29.png"
            if ivy_cum_inside == True:
                show playersex 19
                show ivysex 16 zorder 2 at Position (xpos=521,ypos=718)
                show expression "characters/player/char_player_sex_35.png" zorder 3 at Position (xpos=523,ypos=500)
            player_name "Valeu. Você é incrível..."
            hide expression "characters/player/char_player_sex_35.png"
            hide expression "characters/player/char_player_sex_51.png"
            show playersex 19
            show ivysex 15 zorder 2 at Position (xpos=510,ypos=710)
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_52.png" zorder 3 at Position (xpos=511,ypos=275)
            else:
                show expression "characters/player/char_player_sex_31.png" zorder 3 at Position (xpos=513,ypos=526)
            window hide
            pause
            ivy "Vamos nos limpar..."
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_rcowgirl_options
        jump ivy_rcgirl_stage1

label ivy_slap_ass:
    hide screen ivy_sex_xray_button
    show playersex 23
    show ivysex 20 at Position (xpos=538,ypos=724)
    pause 0.2
    if ivy_xray_toggle == True:
        hide screen ivy_sex_xray
        show expression "characters/player/char_player_sex_40b.png" zorder 3 at Position (xpos=517,ypos=581)
    show ivysex 21 at Position (xpos=537,ypos=724)
    show playersex 24 with vpunch
    pause 0.2
    ivy "{b}*risada*{/b} Ficando muito excitado?"
    ivy "Mais rápido então!"
    hide expression "characters/player/char_player_sex_40b.png"
    show playersex 22
    $ ivy_sex_speed -= 0.25
    jump ivy_rcgirl_stage1

label ivy_cowgirl:
    show ivy 5 at right
    show player 174 at left
    with dissolve
    player_name "Hum, quero a ultimate, por favor."
    ivy "{b}*risada*{/b} Você quer tudo, não quer?"
    show player 29
    player_name "Eu uhh..."
    show ivy 3
    ivy "Eu gosto de homens corajosos."
    show ivy 2
    ivy "Me siga."
    scene massage_room_closeup
    with dissolve
    show ivy 2 at right with dissolve
    show player 43 at left with dissolve
    ivy "Certo, quero garantir que ninguém nos interrompa."
    if ivy_first_visit == True:
        player_name "{b}*assobio*{/b} sala legal."
        show player 1
        show ivy 3
        ivy "{b}*risada*{/b} Vai ficar mais legal quando começarmos."
        show ivy 2
        ivy "Agora, tire sua roupa e deite-se. Você pode colocar a roupa na mesa."
        ivy "Vou dar alguns minutos para você se preparar."
        hide ivy 2
        scene blank with dissolve
        scene massage_room_closeup
        show player 175 at left
        with dissolve
        player_name "( Phew! É menos estranho do que imaginava! )"
        player_name "( Eu não esperava que fosse tão direto... )"
        player_name "( Talvez eu ainda não esteja preparado pra isso... )"
        player_name "( ...Não posso mais voltar. )"
        player_name "( Espero que eu goste. )"
        scene massage_room
        hide player
        show playersex 19
        show expression "characters/ivy/char_ivy_13.png" zorder 2 at Position (xpos=500,ypos=691)
        show ivy 18 zorder 3 at Position (xpos=870,ypos=655)
        with dissolve
        ivy "{b}*risada*{/b} Por que você ainda tá usando isso?"
        ivy "Não precisamos de toalhas para esse tipo de massagem."
        player_name "Ah, desculpa..."
        show ivy 14 at Position (xpos=780,ypos=655) with dissolve
        pause 0.5
        hide expression "characters/ivy/char_ivy_13.png"
        show ivy 15 at Position (xpos=804,ypos=655) with vpunch
        ivy "Pronto! Muito melhor, não é?"
        player_name "Yeah, it is."
        show ivy 16 at Position (xpos=870,ypos=658)
        pause 1
        show ivy 17 at Position (xpos=870,ypos=655)
        pause 1
        show ivy 18 at Position (xpos=870,ypos=655)
        ivy "Como você guarda isso?"
        ivy "De qualquer forma: me chamo Ivy."
        ivy "Agora, minha vez de me preparar..."
        $ ivy_first_visit = False
    scene massage_room
    hide player
    show playersex 19
    show ivy 7 zorder 2 at Position (xpos=800,ypos=656)
    with dissolve
    ivy "Vamos usar camisinha pra isso."
    show ivy 6 at Position (xpos=799,ypos=655)
    player_name "Aww, cara..."
    show ivy 7 at Position (xpos=800,ypos=656)
    ivy "Calma, você nem vai perceber. Confia em mim."
    show ivy 9 at Position (xpos=730,ypos=674) with dissolve
    pause
    show ivy 10 at Position (xpos=730,ypos=697) with dissolve
    pause
    show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
    show ivy 18 at Position (xpos=870,ypos=655)
    ivy "E para finalizar..."
    show ivy 19 at Position (xpos=819,ypos=655) with dissolve
    pause 1
    show ivy 20 at Position (xpos=865,ypos=655) with dissolve
    pause
    hide ivy
    show ivysex 8 zorder 2 at Position (xpos=496,ypos=750)
    with dissolve
    pause
    show ivysex 9 zorder 2 at Position (xpos=482,ypos=768) with dissolve
    pause
    show playersex 20
    show ivysex 10 zorder 2 at Position (xpos=532,ypos=770) with dissolve
    ivy "{b}*risada*{/b} Me pergunto se consigo colocar tudo..."
    show playersex 20
    ivy "Pronto para ir para o céu?"
    player_name "{b}*gulp*{/b} Sim."
    ivy "Aqui vamos nós..."
    show playersex 21
    show ivysex 11 zorder 2 at Position (xpos=535,ypos=766)
    player_name "Haaah-"
    show playersex 20
    show ivysex 10 zorder 2 at Position (xpos=532,ypos=770)
    ivy "Você está bem?"
    player_name "Sim, continue..."
    $ ivy_sex_speed = 0.8
    $ ivy_cowgirl_stage = 0

    $ anim_toggle = False
    $ ivy_xray_toggle = False
    $ ivy_cum_inside = False
    $ xray_front = True
    $ xray_needed = True

    label ivy_cowgirl_stage1:
        $ xray = 1
        show playersex 21 zorder 1
        show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
        show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
        show screen ivy_sex_xray
        show screen ivy_sex_xray_button
        pause
        if anim_toggle:
            hide screen ivy_cowgirl_options
            hide screen ivy_sex_xray
            hide screen ivy_sex_xray_button
            hide playersex 21
            hide expression "characters/player/char_player_sex_29.png"
            hide ivysex 11
            if ivy_xray_toggle == True:
                show ivysex_xray 36_37 at Position (xpos=515,ypos=724)
            else:
                show ivysex 10_11 at Position (xpos=515,ypos=724)
            pause 4
        else:
            hide screen ivy_cowgirl_options
            hide screen ivy_sex_xray_button
            $ xray = 0
            show playersex 20
            show ivysex 10 at Position (xpos=532,ypos=770)
            pause
            $ xray = 1
            show playersex 21
            show ivysex 11 at Position (xpos=533,ypos=766)
            pause
            $ xray = 0
            show playersex 20
            show ivysex 10 at Position (xpos=532,ypos=770)
            pause
            $ xray = 1
            show playersex 21
            show ivysex 11 at Position (xpos=533,ypos=766)
            pause
            $ xray = 0
            show playersex 20
            show ivysex 10 at Position (xpos=532,ypos=770)
            pause
            $ xray = 1
            show playersex 21
            show ivysex 11 at Position (xpos=533,ypos=766)
            pause
        $ ivy_cowgirl_stage += 1
        if ivy_cowgirl_stage == 1:
            if anim_toggle:
                player_name "( Puta merda, isso é muito bom! )"
                player_name "Pode ir mais rápido... Acho que aguento..."
                ivy "Ok, você pediu por isso!"
                hide ivysex 10_11
                hide ivysex_xray 36_37
                show playersex 21 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
                show screen ivy_sex_xray
            else:
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                player_name "( Puta merda, isso é muito bom! )"
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                player_name "Pode ir mais rápido... Acho que aguento..."
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                ivy "Ok, você pediu por isso!"
            window hide
        elif ivy_cowgirl_stage == 2:
            if anim_toggle:
                player_name "( Só vou aguentar mais um pouco... )"
                ivy "Haah-Tenho que confessar..."
                ivy "...você pode ser um adolescente..."
                ivy "...mas você-aah-põe alguns clientes no chão!"
                player_name "( Isso foi um jeito de aumentar meu ego. )"
                player_name "( Me pergunto como ela reagiria se eu... )"
                hide ivysex 10_11
                hide ivysex_xray 36_37
                show playersex 21 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
                show screen ivy_sex_xray
            else:
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                player_name "( Só vou aguentar mais um pouco... )"
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                ivy "Haah-Tenho que confessar..."
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                ivy "...você pode ser um adolescente..."
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                ivy "...mas você-aah-põe alguns clientes no chão!"
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
                player_name "( Isso foi um jeito de aumentar meu ego. )"
                $ xray = 1
                show playersex 21
                show ivysex 11 at Position (xpos=533,ypos=766)
                player_name "( Me pergunto como ela reagiria se eu... )"
                $ xray = 0
                show playersex 20
                show ivysex 10 at Position (xpos=532,ypos=770)
            window hide
        elif ivy_cowgirl_stage == 3:
            $ xray = 1
            if not anim_toggle:
                hide ivysex 10_11
                hide ivysex_xray 36_37
                show playersex 21 zorder 1
                show expression "characters/player/char_player_sex_29.png" zorder 2 at Position (xpos=522,ypos=572)
                show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
            player_name "( Merda, cheguei no meu limite! )"
            player_name "( Ela é muito boa nisso! )"
            player_name "Vou gozar!"

            label ivy_cowgirl_cum_options_menu:
            show screen ivy_cowgirl_cum_options
            pause
            jump ivy_cowgirl_cum_options_menu
            label ivy_cowgirl_cum_inside:
                hide screen ivy_cowgirl_cum_options
                ivy "Haah-vai!"
                hide screen ivy_sex_xray
                $ ivy_cum_inside = True
                jump ivy_cowgirl_cum_end
            label ivy_cowgirl_cum_outside:
                hide screen ivy_cowgirl_cum_options
                ivy "Haah-vai!"
                hide screen ivy_sex_xray
                $ ivy_cum_inside = False
                jump ivy_cowgirl_cum_end
            label ivy_cowgirl_cum_end:
            hide ivysex_xray
            if ivy_cum_inside == True:
                show playersex 21
                show ivysex 11 zorder 2 at Position (xpos=533,ypos=766)
            else:
                hide expression "characters/player/char_player_sex_29.png"
                show playersex 20
                show ivysex 13 zorder 2 at Position (xpos=533,ypos=770)
                show expression "characters/player/char_player_sex_32.png" zorder 3 at Position (xpos=485,ypos=423)
            show white zorder 3 with hpunch
            if ivy_cum_inside == True:
                show screen ivy_sex_xray
            hide white
            with dissolve
            ivy "Haaa..."
            hide expression "characters/player/char_player_sex_32.png"
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_33.png" zorder 3 at Position (xpos=460,ypos=405)
            ivy "Haah... Você durou muito para... um adolescente."
            hide expression "characters/player/char_player_sex_33.png"
            if ivy_cum_inside == False:
                show expression "characters/player/char_player_sex_34.png" zorder 3 at Position (xpos=442,ypos=401)
            player_name "Valeu... Você é ótima..."
            if ivy_cum_inside == True:
                hide screen ivy_sex_xray

            hide expression "characters/player/char_player_sex_34.png"
            hide expression "characters/player/char_player_sex_29.png"
            show playersex 19
            show ivysex 9 zorder 2 at Position (xpos=483,ypos=769)
            if ivy_cum_inside == True:
                show expression "characters/player/char_player_sex_30.png" zorder 3 at Position (xpos=522,ypos=510)
                with dissolve
            pause
            hide expression "characters/player/char_player_sex_30.png"
            show ivysex 8 zorder 2 at Position (xpos=499,ypos=750)
            if ivy_cum_inside == True:
                show expression "characters/player/char_player_sex_31.png" zorder 3 at Position (xpos=514,ypos=524)
                with dissolve
            window hide
            pause
            ivy "Vamos nos limpar..."
            hide expression "characters/player/char_player_sex_31.png"
            hide playersex
            hide ivysex
            scene blank
            with dissolve
            $ callScreen(location_count)
        window hide
        call screen ivy_cowgirl_options
        jump ivy_cowgirl_stage1

label ivy_no_money:
    show player 13 at left
    show ivy 4 at right
    with dissolve
    player_name "( Puts, não posso pagar isso. )"
    player_name "Pensadno bem, talvez outra hora."
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
