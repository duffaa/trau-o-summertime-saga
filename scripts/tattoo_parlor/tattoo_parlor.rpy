default tattoo_interior_first_visit = True

label tattoo_parlor_dialogue:
    $ location_count = "Tattoo Parlor"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label tattoo_parlor_interior_dialogue:
    $ location_count = "Tattoo Parlor Interior"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if tattoo_interior_first_visit:
        $ tattoo_interior_first_visit = False
        scene tattoo_indoor_b
        show player 13 with dissolve
        player_name "( Nunca estive num estúdio de tatuagem antes. )"
        show player 34
        player_name "( Talvez eu devesse fazer uma tatuagem qualquer dia desses... )"
        hide player with dissolve

    if M_mia.get_state() == S_mia_get_tattoo and is_here("mia"):
        scene tattoo_indoor_b
        show mia 7f at Position (xpos=400)
        show player 13 at left
        show grace 2 at right
        with dissolve
        grace "Olá!"
        show grace 1
        show player 14
        player_name "Eae."
        show player 13
        show mia 10f
        mia "Oi!"
        show mia 7f
        show grace 4
        grace "Bem-vindos ao {b}Sugar Tats{/b}."
        show grace 2
        grace "Dêem uma olhada ao redor nas tatuagens..."
        grace "...E venham me ver se tiverem alguma dúvida!"
        hide grace with dissolve
        pause(.25)
        hide mia
        show mia 12 right
        with dissolve
        mia "Ela parece ocupada, deveríamos voltar outra hora?"
        show mia 8
        show player 12
        player_name "Ah, não."
        show player 10
        player_name "Você quer desistir agora?!"
        show player 5
        show mia 12
        mia "*suspiro*"
        mia "Tens razão."
        mia "Eu disse que iria fazer, então vamos fazer isso!"
        hide mia with dissolve
        show player 17
        player_name "Isso!"
        hide player with dissolve
        $ M_mia.trigger(T_mia_visit_tattoo_parlor)
    $ callScreen(location_count)

label grace_dialogue:
    scene tattoo_indoor_c
    if M_mia.get_state() == S_mia_buy_tattoo and is_here("mia"):
        scene tattoo_indoor_c
        show mia 7f at Position (xpos=400)
        show player 13 at left
        show grace 2 at right
        show tattoo_desk at right
        with dissolve
        grace "Olá!"
        grace "Você está aqui para uma seção?"
    else:

        show player 13 at left
        show grace 2 at right
        show tattoo_desk at right
        with dissolve
        grace "Olá!"
        grace "Você está aqui para uma seção?"
    show grace 1
    menu grace_menu_dialogue:
        "Tatuagem." if M_mia.get_state() == S_mia_buy_tattoo and is_here("mia"):
            show mia 10f
            mia "Queria fazer uma tatuagem... agora."
            show mia 7f
            show grace 2
            grace "Agora? Entendi..."
            show grace 3
            grace "Você tem algo em mente?"
            show grace 1
            show mia 30f at Position (xoffset=64) with dissolve
            mia "Meu amigo aqui desenhou isso para mim, e eu gostarei que estivesse terminado hoje!"
            show mia 7f
            show grace 5
            with dissolve
            grace "Hmm..."
            show grace 6
            grace "Você tem certeza que quer isso?"
            grace "Tatuagens são permanentes, então eu tenho que ter certeza que os meus clientes saibam o que estão fazendo!"
            show grace 7
            show mia 10f
            mia "Eu venho pensando muito nisso e... sim, quero fazer."
            show mia 7f
            show grace 6
            grace "Certo, querida. Mas isso não é de graça!"
            show grace 7
            show player 14
            player_name "Quanto custa?"
            show player 13
            show grace 5
            grace "Com esse tamanhao... com cores... Cerca de {b}$400{/b}."
            show grace 7
            show player 22
            show mia 12f
            mia "!!!"
            mia "Caramba... Acho que só tenho {b}$200{/b}..."
            show mia 8f
            show player 11
            player_name "..."
            show player 10
            player_name "Você não tem o suficiente?"
            show player 5
            show mia 12 with dissolve
            mia "Não, isso foi tudo o que eu consegui economizar."
            mia "O que você acha que devemos fazer?"
            show mia 8
            menu:
                "Eu te ajudo." if inventory.money >= 200:
                    $ inventory.money -= 200
                    show player 14
                    player_name "Eu te ajudo a pagar o resto."
                    show player 13
                    show mia 12
                    mia "Sério?!"
                    show mia 7
                    show player 14
                    player_name "Porque não."
                    player_name "Eu estive trabalhando muito recentemente, então tenho dinheiro para gastar..."
                    show player 17
                    player_name "...E é por uma boa causa!"
                    show player 13
                    show mia 10
                    mia "É muito fofo da sua parte..."
                    mia "...E eu sei que vou te pagar de volta!"
                    show mia 7
                    show player 17
                    player_name "Está tudo bem, ha ha."
                    show player 13
                    show grace 6
                    grace "Então?"
                    show mia 7f with dissolve
                    grace "Pronta para começar?"
                    show grace 7
                    show mia 10f
                    mia "Estou pronta!"
                    hide player
                    hide mia
                    hide grace
                    hide tattoo_desk
                    with dissolve


                    scene tattoo_cs01
                    show text "Demorou um pouco até a {b}Grace{/b} terminar.\nEu estva bem preocupado pela {b}Mia{/b}...\n...Mas ela parecia bem tranquila o tempo todo!" at Position (xpos= 512, ypos = 700) with dissolve
                    with dissolve
                    pause
                    hide text
                    hide tattoo_cs01
                    with dissolve


                    scene tattoo_indoor_b
                    show mia 7f at Position (xpos=400)
                    show player 13 at left
                    show grace 2 at right
                    with dissolve
                    grace "Pronto!"
                    grace "Espero que vocês gostem."
                    show grace 1
                    show mia 10f
                    mia "Está ótimo! E não doeu tanto quando achei que iria doer..."
                    show mia 7f
                    show grace 2
                    grace "Certifique-se de deixar o curativo durante por uns dias."
                    show grace 1
                    show mia 10f
                    mia "Ok, obrigada!"
                    show mia 7f
                    show grace 2
                    grace "Tchau, pessoal."
                    hide grace with dissolve
                    pause(.25)
                    hide mia
                    show mia 7 right
                    with dissolve
                    show player 14
                    player_name "Como é?"
                    show player 13
                    show mia 12
                    mia "A tatuagem?"
                    show mia 7
                    show player 14
                    player_name "Sim."
                    show player 13
                    show mia 12
                    mia "É bom... Só que tem uma sensação de formigamento."
                    show mia 10
                    mia "E estou feliz por ter feito... posso dizer que fiz algo que eu sempre quis fazer."
                    show mia 7
                    show player 10
                    player_name "Você não está preocupada que sua mãe possa descobrir?"
                    show player 5
                    show mia 9
                    mia "Felizmente não, está em um lugar escondido, ha ha."
                    show mia 7
                    show player 17
                    player_name "Achei legal que você fez."
                    show player 18
                    show mia 10
                    mia "Valeu, {b}[firstname]{/b}. Estou feliz que você tenha vindo comigo."
                    show player 13
                    mia "Eu deveria ir embora. Antes que minha mãe comece a suspeitar de algo..."
                    show mia 7
                    show player 14
                    player_name "Ok, te vejo na escola!"
                    show player 13
                    show mia 10
                    mia "Tchau."
                    hide player
                    hide mia
                    with dissolve
                    $ gTimer.tick()
                    $ M_mia.trigger(T_mia_tattoo_done)
                "Voltar mais tarde.":

                    show player 10
                    player_name "Talvez devessemos voltar mais tarde?"
                    show player 5
                    mia "..."
                    show mia 12
                    mia "Acho que devemos."
                    show mia 8
                    show player 10
                    player_name "Está tudo bem. Podemos voltar outra hora."
                    show player 5
                    show mia 12
                    mia "Tens razão."
                    show mia 8
                    show player 10
                    player_name "Me desculpa por não podermos ter feito a tatuagem hoje..."
                    show player 5
                    show mia 12
                    mia "Está tudo bem. Tenho que ir para casa."
                    show mia 8
                    show player 10
                    player_name "Certo, te vejo mais tarde."
                    hide player
                    hide mia
                    hide grace
                    hide tattoo_desk
                    with dissolve

        "Você parece familiar." if not Grace.known(grace_intro) and not is_here("mia"):
            show player 10
            player_name "Sabe... acho que..."
            show player 12
            player_name "Uhh."
            show player 34
            show grace 3
            grace "Está tudo bem?"
            show grace 1
            show player 30
            player_name "Desculpa, mas você me parece... familiar."
            show player 5
            show grace 3
            grace "Huh?"
            show grace 2
            grace "Hmm... talvez você esteja me confundindo com minha irmã?"
            show grace 1
            show player 12
            player_name "Irmã?"
            show player 11
            show grace 3
            grace "Minha irmã mais nova? {b}Eve{/b}?"
            show grace 1
            show player 38 with dissolve
            player_name "Oh! Claro!"
            show player 14 with dissolve
            player_name "Eu vi a semelhança agora."
            show player 13
            show grace 4
            grace "Ha ha."
            show grace 2
            grace "Que seja, o que deseja?"
            $ Grace.add_event(grace_intro)
            $ grace_intro.finish()
            jump grace_menu_dialogue
        "Nada.":

            show player 14
            player_name "Só estou dando uma olhada."
            show player 13
            show grace 2
            grace "Ótimo! Continue olhando."
            grace "Eu faço todos os desenhos exibidos na minha loja!"
            grace "Apenas me avise se você quiser algo!"
            show grace 1
            show player 14
            player_name "Ok, valeu!"
            show player 13
            show grace 2
            grace "Até."
            hide grace
            hide mia
            hide player
            hide tattoo_desk
            with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
