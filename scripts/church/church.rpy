default church_first_time = True

label church_dialogue:
    $ location_count = "Church"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 3.9>audio/ambience_church.ogg"):
            $ playSound("<loop 3.9>audio/ambience_church.ogg")
    if church_first_time == True and not (gTimer.is_weekend() and gTimer.is_morning()):
        scene church_b with None
        show player 11 with dissolve
        player_name "( A igreja está vazia. )"
        player_name "( Parece que estou atrasado para a missa. )"
        hide player 11
        $ church_first_time = False

    if M_mia.get_state() == S_mia_church_plan and gTimer.is_weekend() and gTimer.is_morning():
        scene church_full02_b
        show player 32 at Position (xoffset=68) with dissolve
        player_name "( {b}Helen{/b} está sentada na frente. )"
        show player 12 with dissolve
        player_name "( Deve ter um jeito de falar com ela... )"
        player_name "(...Mas primeiro eu preciso mudar minha roupa. )"
        player_name "( Vamos ver se eu não consigo encontrar essas {b}roupas de padres{/b} em algum lugar da igreja... )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_convince_helen:
        scene church_cs01
        with fade
        show text "A missa ainda estava em andamento.\n{b}Helen{/b} foi até o confessionário...." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        hide church_cs01
        with dissolve

        scene church_cs02
        with fade
        show text "O padre saiu por um momento.\nAgora é a hora perfeita para me aproximar dela...\n...E seus pensamentos sobre {b}Harold{/b}." at Position (xpos= 512, ypos = 700) with dissolve
        with dissolve
        pause
        hide text
        hide church_cs02
        with dissolve

        scene church_full03_b
        show player 30 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "Preciso {b}entrar no confessionário{/b} pelo {b}lado direito{/b}..."
        hide player
        hide players robe
        with dissolve
        $ M_mia.trigger(T_helen_confessional)

    elif M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_full02_b
        show player 33 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "Perfeito!"
        show player 106 at Position (xoffset=-1)
        player_name "..."
        show player 14 at Position (xoffset=-1)
        player_name "( Eu deveria devolver essa roupa onde eu peguei... )"
        player_name "( ...antes que alguém perceba... )"
        hide player
        hide players robe
        with dissolve

    elif M_mia.get_state() == S_mia_nun_thoughts:
        scene church_b
        show player 10 with dissolve
        player_name "( Merda... Isso foi assustador! )"
        player_name "( Agora eu tenho que fazer coisas para essa freira... )"
        player_name "( ...Eu só espero que ela não conte para ninguém sobre o que eu fiz. )"
        hide player with dissolve
        $ unlock_ui()
        $ M_mia.trigger(T_mc_nun_thoughts)

    elif M_mia.get_state() == S_mia_church_night_visit and gTimer.is_dark():
        scene church_n_b
        show player 10 with dissolve
        player_name "( É tão silêncioso aqui pela noite. )"
        player_name "( Não tenho certeza de que pode ter pessoas aqui tão tarde. )"
        show player 12
        player_name "( Hora de ir ver a {b}Irmã Angelica{/b} e ver o que ela quer... )"
        hide player with dissolve
    $ callScreen(location_count)

label angelica_dialogue:
    if M_mia.is_set('helen dialogue change'):
        scene church_c with fade
        show player 10 at left
        show ang 1 at right
        with dissolve
        player_name "Olá, {b}Sister Angelica{/b}."
        show player 5
        show ang 2
        ang "Você de novo."
        ang "O que você quer?"
        show ang 1
        menu:
            "Conversar.":
                show player 10
                player_name "Só quero conversar."
                show player 5
                show ang 2
                ang "Silêncio."
                show ang 1
                show player 24
                player_name "Ah..."
                show ang 2
                ang "Se você quiser conversar, venha me visitar de noite..."
                show ang 1
                show player 25
                player_name "Ok, desculpa."
                hide player
                hide ang
                with dissolve
            "Cemitério.":

                show player 10
                player_name "Como vou ao cemitério?"
                show player 5
                show ang 2
                ang "Está inacessível."
                ang "Mesmo estando fechado, alguns pestinhas ainda encontram maneiras de se {b}esgueirar pelas cercas{/b}."
                show ang 1
                show player 12
                player_name "Mas meu pai está enterrado lá."
                show player 5
                ang "..."
                show ang 2
                ang "Tenho certeza que está."
                show ang 1
                show player 12
                player_name "Mas-"
                show player 16
                show ang 2
                ang "Vá. Você está desperdiçando o meu tempo."
                hide ang
                hide player
                show player 16
                with dissolve
                player_name "..."
                show player 12
                player_name "Talvez eu possa encontrar {b}um jeito de me esgueirar pela cerva{/b} também."
                hide player with dissolve
            "Nada.":

                show player 10
                player_name "Esqueça. Tenho que ir."
                show player 5
                ang "..."
                show ang 2
                ang "Não desperdice meu tempo assim novamente."
                show ang 1
                show player 25
                player_name "Tens razão, desculpa..."
                hide player
                hide ang
                with dissolve
    else:

        scene church_c
        show ang 2 at right
        show player 1 at left
        with dissolve
        ang "Você é da paróquia, garoto?"
        show ang 1
        show player 14
        player_name "Oi, eu nã-"
        show ang 2
        show player 11
        ang "Você é da paróquia, jovem??"
        show ang 1
        show player 14
        player_name "Huum... Não."
        show ang 2
        show player 11
        ang "Você acredita em Deus?"
        show ang 1
        show player 10
        player_name "Bom..."
        show ang 2
        show player 11
        ang "Perdão."
        ang "Só posso ajudar aqueles que compartilham a fé em Deus!"
        hide player
        hide ang
        with dissolve
    $ callScreen(location_count)

label confessional_left:
    if M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_full02_b
        show player 10 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "( Preciso devolver este manto antes que alguém me veja. )"
        hide player
        hide players robe
        with dissolve

    elif M_mia.get_state() == S_mia_priest_act:
        scene church_full02_b
        show player 10 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "( Eu não posso ir nesse lado. )"
        player_name "( Tenho que usar a porta do {b}lado esquerdo{/b} do confessionário... )"
        hide player
        hide players robe
        with dissolve
    else:

        scene church_confession
        show player 283 at Position(xpos=280)
        with dissolve
        player_name "Abençoe-me, pai, porque eu pequei."
        show player 278
        player_name "..."
        show player 284
        player_name "......"
        show player 280
        player_name "Pai?"
        player_name "( Não há ninguém aqui? )"
        show player 10
        player_name "( Eu acho que não há nenhum padre por aqui agora... )"
        hide player
        hide church_confession
    $ callScreen(location_count)

label confessional_right:
    if M_mia.get_state() == S_mia_return_priest_outfit:
        scene church_full02_b
        show player 10 at Position (xoffset=-1)
        show players robe
        with dissolve
        player_name "( Preciso devolver este manto antes que alguém me veja. )"
        hide player
        hide players robe
        with dissolve

    elif M_mia.get_state() == S_mia_priest_act:
        scene church_confession
        show player 5f at Position (xpos=795)
        show players robe f at Position (xpos=794)
        show helen 16 at Position (xpos=300)
        with dissolve
        helen "Perdoe minha família, {b}Pai{/b}, porque eles pecaram. Fazem 7 dias desde a minha última confissão."
        show helen 15
        helen "..."
        show helen 13
        helen "{b}Pai{/b}? você está aí?"
        show helen 12
        show player 23f
        player_name "*toce*"
        show player 10f
        player_name "Sim... Eu ehhh... Estou ouvindo..."
        show player 5f
        show helen 16
        helen "Oh, {b}Senhor{/b}, Estou profundamente mal pela maneira pela qual a minha família o ofendeu..."
        helen "...Por meu marido desistir do nosso casamento... E o comportamento pecaminoso da minha filha..."
        helen "Eu tentei febrilmente fazê-los verem seus erros."
        helen "Eu os disse que eles iriam para o inferno se não mudassem."
        helen "...Mas parece que perderam o caminho sagrado e sucumbiram à escuridão."
        show helen 14
        helen "O que eu deveria fazer, {b}Pai{/b}?"
        show helen 15
        menu:
            "Rezar?" if pStats.chr() < 3:
                show player 10f
                player_name "[chr_warn]Talvez você pudesse... Hum... Rezar?"
                show player 22f
                show helen 12
                helen "[chr_warn]..."
                show helen 13
                helen "[chr_warn]Rezar?"
                show helen 12
                show player 10f
                player_name "[chr_warn]Claro!"
                show player 22f
                show helen 13
                helen "[chr_warn]Não vejo bem como isso ajudaria minha família, {b}Pai{/b}."
                helen "[chr_warn]Algo deve ser feito! Algo deve mudar para que eles reconheçam seu comportamento pecaminoso e vil."
                show helen 12
                show player 21f
                player_name "[chr_warn]Huuum... O {b}Senhor{/b} escreve certo por linhas tortas!"
                show player 22f
                helen "[chr_warn]..."
                show helen 14
                helen "[chr_warn]Ok... Farei o que for possível, {b}Pai{/b}."
                show helen 16
                helen "[chr_warn]Por favor, peça ao {b}Senhor{/b} para perdoá-los e você poderia orar por eles também?"
                show helen 15
                show player 10f
                player_name "[chr_warn]Claro! Sem problemas!"
                show player 5f
                show helen 12
                helen "[chr_warn]..."
                show helen 14
                helen "[chr_warn]E, querido {b}Pai{/b}, o que seu cervo fiel fará como castigo no lugar da minha família??"
                show helen 12
                show player 10f
                player_name "[chr_warn]Err... Ummm... duas rezas serã o suficiente?"
                show player 5f
                helen "[chr_warn]..."
                show helen 13
                helen "[chr_warn]Obrigada..."
                hide helen with dissolve
                show player 24f
                player_name "[chr_warn]Merda, fiquei muito nervoso..."
                player_name "[chr_warn]... Preciso tentar de novo outra hora, com mais confiança."
                hide players robe
                show player 444f
                with dissolve
                pause
                hide player with dissolve
                $ unlock_ui()
                $ M_mia.trigger(T_helen_convince_fail)

            "Mudar." if pStats.chr() >= 3:
                show player 12f
                player_name "Talvez seja {b}você{/b} que precise mudar, para que eles voltem ao caminho sagrado..."
                show player 5f
                show helen 14
                helen "Eu?! ...Mas eu fiz tudo certo. Eu..."
                show helen 12
                show player 12f
                player_name "Sim, você fez um bom trabalho apontando as falhas de seus familiares, mas e sobre você?"
                player_name "Eu preciso que você me diga as suas falhas. Você não pode ser perfeita."
                show player 5f
                show helen 15
                helen "..."
                show helen 14
                helen "*suspira*"
                show helen 16
                helen "Talvez você esteja certo, {b}Pai{/b}."
                helen "Talvez... eu tenha... ido longe de mais..."
                show helen 14
                helen "É que eles parecem não entender o perigo que estão correndo.... como eu entendo..."
                helen "Eu faço isso, porque os amos..."
                show helen 15
                show player 10f
                player_name "Você ainda pode se redimir!"
                show player 5f
                show helen 14
                helen "Redimir? O que eu deveria fazer?"
                show helen 15
                show player 12f
                player_name "Talvez você possa tentar ser mais receptível a seu marido..."
                player_name "...E dê a sua filha liberdade para crescer!"
                show player 10f
                player_name "Eles não precisam ser sufocados pelas leis de {b}Deus{/b}, Em vez disso, mostre-lhes o quanto você os ama, igual {b}Deus{/b} ama todo mundo."
                player_name "Você não pode controlar a todos... Mas você pode mudar."
                show player 5f
                show helen 14
                helen "Tens razão... Farei o que for possível, {b}Pai{/b}."
                show helen 15
                show player 14f
                player_name "Agora, vá e mostre compaixão e perdão, assim como o {b}Senhor{/b} perdoa você."
                show player 13f
                show helen 16
                helen "Obrigado pela sua visão... e por me perdoar..."
                show helen 15
                show player 17f
                player_name "Sem problemas!"
                show helen 12
                helen "..."
                show player 21f
                player_name "Err... Umm... tenha um dia abençoado."
                show player 13f
                show helen 16
                helen "O que você quer que eu faça como castigo, {b}Pai{/b}?"
                show helen 15
                show player 12f
                player_name "Duas rezas será o suficiente como seu castigo."
                show player 22f
                show helen 12
                pause
                show helen 16
                show player 13f
                helen "Obrigada..."
                hide helen
                hide player
                hide players robe
                with dissolve
                $ M_mia.trigger(T_helen_convince_change)
                jump church_dialogue
    else:

        scene church_confession
        show player 43f at Position(xpos=760)
        with dissolve
        player_name "( Massa! )"
        player_name "( Eu nunca estive nesse lado do confessionário. )"
        show player 4f
        player_name "Hmm..."
        show player 14f
        player_name "( Parece com o outro lado... )"
        player_name "( Eu deveria dar o fora daqui... )"
        hide player
        hide church_confession
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
