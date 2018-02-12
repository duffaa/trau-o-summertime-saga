default dealership_first_time_visit = True
default plates = ["incezt", "dtfmom", "assman", "peni5", "viber8r", "yes269", "xesttub", "2grl1cp"]

label dealership_dialogue:
    $ location_count = "Dealership"
    $ callScreen(location_count)

label josephine_button_dialogue:
    scene location_dealership_indoor_closeup
    show joe 1 at Position(xpos=0.5474,ypos=0.7630)
    show xtra3 at right
    show player 24 at left
    with dissolve
    if dealership_first_time_visit == True:
        player_name "Bom dai."
        show player 109f
        pause
        pause
        show player 108f
        player_name "Olá?"
        show player 109f
        pause
        Josephine "{b}*suspiro*{/b}"
        pause
        show sato 2 behind xtra3 at Position(xpos=.7630,ypos=0.7299) with dissolve
        show player 11
        Mr. Sato "{b}Josephine{/b}!"
        show sato 1
        show joe 3 at Position(xpos=0.4976,ypos=1.0000) with fastdissolve
        Josephine "O quê?!"
        show joe 2
        show sato 2
        Mr. Sato "Não percebeu que temos um {b}cliente{/b}?!"
        show sato 1
        Josephine "{b}*suspiro*{/b}"
        show sato 4
        Mr. Sato "Perdão, senhor. Minha {b}filha{/b} ainda está aprendendo a ética do trabalho."
        show sato 2
        Mr. Sato "Agora, {b}Josephine{/b}! Por favor, saia desse celular e atenda o garoto."
        Mr. Sato "Lembre-se: Os clientes em primeiro lugar!"
        hide sato
        show joe 3 at Position(xpos=0.8294,ypos=1.0000)
        with dissolve
        Josephine "Ugh..."
        show joe 5
        Josephine "Odeio muito ele."
        Josephine "Está sempre me perseguindo..."
        show joe 4
        show player 10
        player_name "Você trabalha para o seu {b}pai{/b}?"
        show player 11
        show joe 5
        Josephine "Nunca quis trabalhar aqui. Ele só me faz trabalhar aqui para continuar me vigiando."
        Josephine "Eu gostaria que ele simplesmente me deixasse em paz!"
        show joe 4
        pause
        show joe 5
        Josephine "Que seja..."
        $ dealership_first_time_visit = False
    Josephine "O quê você quer?"
    show joe 4 at Position(xpos=0.8294,ypos=1.0000)
    menu dealership_options:
        "Comprar um carro.":
            show popup_unfinished at truecenter with dissolve
            $ renpy.pause()
            hide popup_unfinished with dissolve
            jump dealership_options

        "Utilizar o seguro" if M_mom.get_state() == S_mom_fix_car:
            show player 14
            player_name "Um... Eu queria falar com alguém para utilizar o seguro."
            show player 11
            show joe 5
            Josephine "Qual a placa do carro?"
            show joe 4
            show player 4
            label platemenu:
                player_name "Qual era a placa da {b}[mom_name]'s{/b} mesmo?"
                $ selected_plates = ["dtfmom"]
                $ counter = 0
                while (counter < 3):
                    $ random_plate = renpy.random.choice(plates)
                    while (random_plate in selected_plates):
                        $ random_plate = renpy.random.choice(plates)
                    $ selected_plates += [random_plate]
                    $ counter += 1
                menu:
                    "INCEZT" if "incezt" in selected_plates:
                        jump wrong_plate

                    "DTFM0M" if "dtfmom" in selected_plates:
                        show player 11
                        show joe 6
                        Josephine "Achei."
                        show joe 5
                        Josephine "Ainda vive na rua 240 Cookie?"
                        show joe 4
                        show player 17
                        player_name "Uhum!"
                        show player 11
                        show joe 5
                        Josephine "Ok... Com o que posso ajudar..."
                        show joe 4
                        show player 10
                        player_name "Bom, queria utilizar o seguro; o carro da minha mãe está quebrado."
                        show player 11
                        show joe 6
                        Josephine "Um minuto..."
                        pause
                        Josephine "..."
                        pause
                        show joe 5
                        Josephine "Umm... bom... Sua apólice de seguro foi cancelada por excesso de falta de pagamento."
                        show joe 4
                        show player 23
                        player_name "O quê!?"
                        show player 22
                        show joe 6
                        Josephine "Ainda falta pagar {b}$4,000{/b}."
                        Josephine "E precisam ser pagos {b}$5,000{/b} para que a seguradora cubra."
                        show joe 4
                        show player 23
                        player_name "!!!" with hpunch
                        show joe 5
                        Josephine "Então... você precisa de pelo menos {b}$9,000{/b} antes de cubrir qualquer coisa."
                        Josephine "O dano é muito grande?"
                        show joe 4
                        show player 22
                        player_name "Uh... Sim..."
                        show joe 5
                        Josephine "Ah. Se não fosse, sugeriria você a consertar sozinho."
                        show joe 4
                        pause
                        show player 10
                        player_name "Merda..."
                        show player 24
                        jump fix_car

                    "ASSMAN" if "assman" in selected_plates:
                        show player 11
                        show joe 5
                        Josephine "Você não é o {b}ASSMAN{/b}. O proctologista da cidade registrou essa placa."
                        show joe 4
                        show player 26
                        player_name "Oh. Sim..."
                        show player 4
                        jump platemenu

                    "I♥PEN15" if "peni5" in selected_plates:
                        jump wrong_plate

                    "VIBE R8R" if "viber8r" in selected_plates:
                        jump wrong_plate

                    "YES 269" if "yes269" in selected_plates:
                        jump wrong_plate

                    "XESTTUB" if "xesttub" in selected_plates:
                        jump wrong_plate

                    "2GRL 1CP" if "2grl1cp" in selected_plates:
                        jump wrong_plate
                    "Nenhuma dessas.":

                        jump platemenu
        "Nada":
            hide joe
            hide player
            hide xtra
            with dissolve
            $ callScreen(location_count)

label wrong_plate:
    show player 11
    show joe 6
    pause
    show joe 5
    if randomizer() < 50:
        Josephine "Não há nenhuma conta que coincida com essa placa."
    else:
        Josephine "Isso seria estranho, mas infelizmente não está no sistema."
    Josephine "Certeza que não é outra placa?"
    show joe 4
    show player 4
    jump platemenu

label fix_car:
    player_name "O quê eu deveria fazer agora?"
    menu:
        "Pagar a dívida.":
            if inventory.money < 9000:
                show player 24
                player_name "[chr_warn]I... Uhm... Você poderia?"
                show joe 5
                Josephine "Poderia... o quê?"
            else:

                show player 14
                player_name "Eu devo ter o suficiente para cobrir o custo."
                show player 12
                player_name "Você aceita em dinheiro?"
                show player 5
                show joe 5
                Josephine "Sim."
                show joe 4
                show player 14
                player_name "Toma."
                show player 41 at Position (xoffset=38) with dissolve
                show joe 5
                Josephine "Obrigada."
                show player 5
                show joe 6
                Josephine "Você trouxe o carro?"
                show joe 4
                show player 12
                player_name "Não... Ele está quebrado."
                player_name "Ainda está na nossa casa."
                show player 5
                show joe 6
                Josephine "Oh... Certo, vamos mandar um mecânico para lá."
                show joe 5
                Josephine "Quando você gostaria que ele fosse?"
                show joe 4
                show player 14
                player_name "Hoje seria ótimo."
                show player 12
                player_name "É o nosso único carro e demorou muito para que eu chegasse aqui."
                show player 5
                show joe 5
                Josephine "Umm... Normalmente, temos reservas por uma semana..."
                show joe 6
                Josephine "Deixa eu ver."
                Josephine "Hoje é seu dia de sorte."
                show joe 5
                Josephine "Eu posso enviar um mecânico esta tarde."
                show joe 4
                show player 14
                player_name "Ótimo!"
                player_name "Muito obrigado."
                show player 13
                show joe 5
                Josephine "De nada."
                show joe 4
                show player 10
                player_name "Algo a mais?"
                show player 5
                show joe 5
                Josephine "Não, era só isso."
                show joe 4
                show player 14
                player_name "Obrigado novamente!"
                show player 106
                show joe 1 at Position(xpos=0.5474,ypos=0.7630) with dissolve
                Josephine "Uh huh."
                $ M_mom.trigger(T_mom_renew_insurance)
                $ gTimer.tick()
        "Convencer ela.":

            if pStats.chr() >= 7:
                show player 12
                player_name "Seria possível pagar mais tarde?"
                show player 10
                player_name "Está um pouco difícil lá em casa..."
                player_name "Minha mãe precisa do carro para o trabalho, caso contrário, não poderemos pagar o seguro."
                show player 11
                show joe 5
                Josephine "Não acho que posso-"
                show joe 4
                show player 24
                player_name "E meu {b}pai{/b} morreu recentemente! Estamos lutando para voltar ao normal!"
                show player 25
                player_name "Não há nada que você possa fazer para nos ajudar?"
                pause
                show joe 6
                Josephine "Olha..."
                show joe 5
                Josephine "Vou te ajudar apenas {b}UMA{/b} vez!"
                show joe 6
                Josephine "Meu {b}pai{/b} jamais aprovaria isso, então não conte para ninguém."
                show joe 4
                show player 14
                player_name "Claro."
                show player 13
                show joe 5
                Josephine "Ele ficaria muito puto comigo, mas não seria a primeira vez!"
                show joe 6
                Josephine "Vou acabar com a sua dívida e diminuir a sua franquia ao mesmo tempo."
                Josephine "Vou enviar um guincho para a sua casa para pegar o carro. Provavelmente estará pronto antes mesmo de você chegar em casa!"
                show joe 4
                show player 10
                player_name "Sério?"
                Josephine "..."
                show player 14
                player_name "Digo, muito obrigado!"
                show player 13
                show joe 5
                Josephine "Você me {b}deve{/b} uma!"
                show joe 4
                show player 17
                player_name "Com certeza! Qualquer coisa!"
                $ M_mom.trigger(T_mom_renew_insurance)
                $ gTimer.tick()
            else:

                show player 24
                player_name "[chr_warn]Eu... Uhm... Você poderia?"
                show joe 5
                Josephine "Podeia... o quê?"
                show joe 4
                show player 37
                player_name "[chr_warn]Um... Esqueça."
                pause
                show player 24
                player_name "[chr_warn]Desculpa por encomodar."
                show joe 5
                Josephine "Espero que você consiga consertar o carro."
                show joe 4
                show player 25
                player_name "Uhum, valeu..."
                show player 24
                player_name "( Vamos lá, {b}[firstname]{/b}! Tudo o quê você precisa fazer é pedir ajuda. )"
                player_name "{b}*suspiro*{/b}"
                player_name "( Eu estava nervoso... )"
        "Desistir":

            show player 10
            player_name "Provavelmente devo falar com a minha mãe sobre isso."
            show player 2
            player_name "Obrigado!"
            show player 1
            show joe 5
            Josephine "De nada."
    hide joe
    hide player
    hide xtra
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
