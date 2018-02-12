label locker_room_dialogue:
    $ location_count = "Boy's Lockerroom"
    if not gTimer.is_dark():
        if player.over(intense_gymercise) and not roxxy.known(roxxy_shower):
            scene locker_empty_b with None
            show roxxy 17 at right
            show becca 1 at Position(xpos=315)
            show missy 1 at left
            with dissolve
            rox "E então eu fiquei tipo, \"sem chances que eu iria estudar para essas provas estúpidas!\""
            show roxxy 16
            show missy 2
            show becca 3
            missy "Entendo! Eu ODEIO estudar!"
            show roxxy 17
            show missy 1
            show becca 1
            rox "Ugh! Eu preciso encontrar uma maneira de fazer essas tarefas primeiro!"
            show roxxy 16
            show becca 2
            becca "Você ainda não fez?!"
            show roxxy 17
            show becca 1
            rox "Ah, cala a boca! Vou encontar uma forma de fazer!"
            rox "{b}Sra. Bissette{/b} estava me enchendo o saco por causa deles..."
            show roxxy 16
            show missy 2
            show becca 3
            missy "Sim, {b}Sra. Bissette{/b} é a mais chata."
            show missy 1
            show becca 2
            becca "Sim, pena que você não tem um pinto, {b}Roxxy{/b}. Ouvi dizer que ela adora um pinto em troca de boas notas."
            show roxxy 17
            show missy 3
            show becca 1
            rox "O problema são as provas."
            rox "Não posso tirar mais notas baixas."
            show roxxy 16
            show missy 2
            show becca 3
            missy "Seu namorado não pode te ajudar?"
            show roxxy 17
            show missy 3
            show becca 1
            rox "Tipo, ajudar como?! Única coisa que o {b}Dexter{/b} é bom, é no baquete e em levantar peso..."
            show roxxy 16
            show missy 1
            show becca 2
            becca "Talvez ele possa bater um dos nerds da escola, e pegar o que você quer?"
            show roxxy 17
            show becca 1
            rox "Quando ele não está fazendo isso..."
            show roxxy 16
            show missy 2
            show becca 3
            missy "Right."
            show roxxy 17
            show missy 1
            show becca 1
            rox "Eu não me dar mal nessas provas, ou eu vou parecer uma idiota na frente de todos!"
            rox "Preciso ter acesso às provas, de alguma forma..."
            show roxxy 16
            show becca 2
            becca "Como você planeja fazer isso?"
            show roxxy 17
            show missy 3
            show becca 1
            rox "Vou dar um jeito."
            show becca 2
            show roxxy 18 at Position(xoffset=-19) with fastdissolve
            becca "Espero que sim, eles estão chegando..."
            show becca 1
            show roxxy 19 at Position(xoffset=-49) with fastdissolve
            rox "Que seja!"
            show roxxy 20 at Position(xoffset=-69) with fastdissolve
            rox "Tenho que tomar banho."
            rox "Vocês fiquem de olho, para que ninguém entre aqui."
            show becca 2
            show roxxy 21 at Position(xoffset=-27) with fastdissolve
            becca "Quanto tempo você vai demorar?"
            show missy 2
            show becca 3
            missy "É, temos que ir para a aula daqui a pouco!"
            show missy 1
            show becca 1
            show roxxy 22 with fastdissolve
            rox "Cala a boca e cuidem do chuveiro!"
            show missy 3
            show roxxy 24 with fastdissolve
            rox "Eu não quero nenhum moleque entrando enquanto eu estiver lá."
            show roxxy 23
            becca "..."
            show missy 2
            missy "Claro, {b}Roxxy{/b}..."
            hide missy
            hide roxxy
            hide becca
            with dissolve
            pause
            show jersey 11 with dissolve
            player_name "( Parece que ninguém está aqui! )"
            show jersey 13
            player_name "( Como eu gosto... )"
            show jersey 18
            player_name "( Eu poderei tomar um banho quente antes que a água esfrie! )"
            hide jersey with dissolve
            $ roxxy.add_event(roxxy_shower)

        elif locker_room_count == 0:
            scene locker
            show combo 1 at left with dissolve
            player_name "Viu?"
            player_name "Não é tão ruim: Tem só umas pessoas aqui!"
            show combo 2 at left
            show annie 3 at right with dissolve
            ann "Espero que vocês dois se lembrem das regras em relação ao atraso!"
            ann "Se você não estiver com o uniforme e no pátio em um minuto-"
            show combo 3 at left
            show annie 1 at right
            player_name "Está tudo bem, {b}Annie{/b}... Já entendemos."
            player_name "Vamos sair daqui a pouco..."
            show combo 4 at left
            show annie 3 at right
            ann "Como o presidente da união estudantil e monitora oficial do corredor..."
            ann "...é meu {b}dever{/b} para anotar todas infrações de qualquer pessoa que quebre as diretrizes escolares!"
            show combo 5 at left
            show annie 1 at right
            player_name "Olha..."
            player_name "{b}Judith{/b} não se sente muito confortável com caras no banheiro."
            player_name "Ela precisa de um tempo a mais para ficar pronta, ok?"
            show combo 4 at left
            show annie 5 at right
            ann "É isso mesmo, {b}Judith{/b}?"
            show combo 6 at left
            show annie 6 at right
            jud "Bom..."
            jud "S...sim..."
            show combo 4 at left
            show annie 5 at right
            ann "Qual o problema?"
            ann "Sente-se insegura em relação aos homens?"
            ann "...Ou você está incitando desordem e desobedecendo às regras??"
            show combo 6 at left
            show annie 6 at right
            jud "Não estou..."
            jud "É que..."
            show combo 7 at left
            jud "...Não estou... usando sutiã!"
            show annie 5 at right
            ann "Ah, entendi... Inventando desculpas para falta à aula?"
            show combo 4 at left
            show annie 3 at right
            ann "Sua falta de obediência é alarmante, e não permitirei isso!"
            show annie 4 at right
            ann "Vista-se imediatamente, ou eu estou mandarei vocês dois para a detenção!!"
            show annie 6 at right
            show combo 8 at left
            window hide
            pause
            show combo 9 at left
            window hide
            pause
            show combo 10 at left
            window hide
            pause
            show combo 11 at left
            player_name "..."
            show combo 12 at left
            window hide
            pause
            show combo 13 at left
            window hide
            pause
            show annie 9 at right
            show combo 14 at left
            window hide
            pause
            show annie 10 at right
            show combo 15 at left
            window hide
            pause
            show annie 11 at right
            show combo 16 at left with hpunch
            player_name "Merda..."
            jud "Oh, meu..."
            show combo 18 at left
            show annie 8 at right
            ann "Isso..."
            ann "Isso é... impróprio... e vergonhoso!!"
            show combo 17 at left
            show annie 1 at right
            player_name "Me... desculpa..."
            show combo 18 at left
            show annie 2 at right with hpunch
            ann "Coloque seus uniformes e leve suas bundas para a aula, {b}AGORA{/b}!!!"
            show combo 19 at left
            show annie 7 at right
            ann "Terei que reportar esse incidente para a {b}Diretora Smith{/b}, juntamente com suas infracções por estarem atrasados..."
            show combo 20 at left
            ann "...Agora, andem!!"
            hide combo 20 at left with dissolve
            hide annie 7 at right with dissolve
            $ wearing_jersey_count = 2
            $ courtyard_door_count = 1
            $ locker_room_count = 1
            $ stairs_count = 1
            $ classroom_door_count = 1
    else:
        if webcam_quest:
            scene locker_night
            show player 14 at left with dissolve
            show erik 1 at right with dissolve
            player_name "Ok, é aqui!"
            show player 1
            show erik 5
            eri "Os vistiários??"
            show erik 1
            show player 35
            player_name "Sim... Mas preciso achar algum {b}lugar escondido{/b}..."
            player_name "...Deve ter um lugar nesta sala que eu possa {b}esconder{/b} algo pequeno..."
            hide erik 1
            hide player 35
    $ callScreen(location_count)

screen locker_room:

    if not gTimer.is_dark():
        if roxxy.started(roxxy_shower):
            add "backgrounds/location_locker_room_empty.jpg"
        else:
            add "backgrounds/location_locker_room.jpg"
    else:
        add "backgrounds/location_locker_room_night.jpg"

    if roxxy.started(roxxy_shower):
        if not gTimer.is_dark():
            imagebutton:
                focus_mask True
                pos (25,274)
                idle "images/objects/object_door_17_girls.png"
                hover "images/objects/object_door_17b_girls.png"
                action Hide("locker_room"), Jump("roxxy_shower_dialogue")

    else:
        imagebutton:
            focus_mask True
            pos (25,274)
            idle gTimer.image("objects/object_door_17{}.png")
            hover gTimer.image("objects/object_door_17b{}.png")
            if not gTimer.is_dark():
                action If(
                    shower_door_count == 0,
                    [Hide("locker_room"), Jump("door17_locked_dialogue")],
                    [Hide("locker_room"), Jump("lockershowers_dialogue")]
                )
            else:
                action Hide("locker_room"), Jump("denied_access_locker")

    if gTimer.is_evening() and quest11 in quest_list and not webcam_planted:
        imagebutton:
            focus_mask True
            pos (520,160)
            idle "objects/object_airvent_01.png"
            hover "objects/object_airvent_01b.png"
            action Hide("locker_room"), Jump("airvent_webcam_quest")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_02.png"
        hover "boxes/auto_option_02b.png"
        action Hide("locker_room"), Jump("left_hall_dialogue")

label airvent_webcam_quest:
    scene locker_night
    show player 34 at left with dissolve
    show erik 1 at right with dissolve
    player_name "Hmm..."
    show player 43
    show erik 13
    player_name "Aqui em cima!"
    show erik 14
    eri "Na ventilação de ar?"
    show erik 1
    show player 14
    player_name "Sim! É perfeito!"
    player_name "Tem visão para a sala toda..."
    player_name "...apenas fique bem aqui em baixo."
    show player 17
    player_name "Vou subir nos seus ombros e aí eu alcanço!"
    show player 1
    show erik 3
    eri "Ok..."
    hide erik
    show player 128 at center
    with dissolve
    player_name "Certo, fique parado!"
    hide player
    hide erik
    scene locker_closeup
    show player 129
    with dissolve
    player_name "Fique parado!"
    show player 130
    player_name "Estou quase pronto..."
    show player 131
    player_name "..."
    player_name "Aqui!"
    hide player
    $ inventory.items.remove(supersaga_webcam)
    scene locker_night
    show player 43 at left
    show erik 1 at right
    with dissolve
    player_name "Cert! Vamos dar o fora daqui..."
    show player 11
    show erik 5
    eri "Eu poderia saber sobre o que se trata?"
    $ erik_helped_with_camera = True
    menu:
        "Não posso contar.":
            show erik 3 at right
            show player 10 at left
            player_name "Provavelmente será melhor se você não souber..."
            player_name "...Não é tão mal também..."
            show player 21
            player_name "...E isso vai me ajudar com a {b}tarefa{/b}!!"
            show player 13
            eri "Ok então..."
            show erik 5
            eri "...Podemos sair agora?"
            show erik 1
            show player 14
            player_name "Claro, vamos."
            hide erik 1 with dissolve
            hide player 14 with dissolve
        "Uma webcam escondida.":

            show player 24 at left
            show erik 1 at right
            player_name "{b}*suspiro*{/b}..."
            player_name "É a {b}biblioteca.{/b}"
            show player 25
            player_name "Ela não consegue comprar os {b}livros{/b} que preciso..."
            player_name "...A menos que eu fizesse isso pra eles."
            show player 5
            show erik 5
            eri "O quê? Por quê?"
            show erik 1
            show player 10
            player_name "Parece que a {b}biblioteca{/b} ficou sem dinheiro para comprar mais livros."
            player_name "Que seja, já está feito. Vamos indo..."
            show player 13
            show erik 4
            eri "Ok. Obrigado por me falar sobre isso."
            hide player 13 with dissolve
            hide erik 1 with dissolve
    $ gTimer.tick()
    $ webcam_planted = True
    $ unlock_ui()
    jump map_dialogue

label roxxy_shower_dialogue:
    scene locker_empty_b with None
    show jersey 11 at left
    show becca 2f at Position(xpos=715)
    show missy 1f at right
    with dissolve
    becca "Uhmm... O que você está fazendo?"
    show becca 3f
    show missy 2f
    missy "Ninguém está permitido a entrar aqui."
    show missy 1f
    show becca 1f
    show jersey 10
    player_name "Estava na academia! Eu PRECISO tomar banho."
    show becca 2f
    show jersey 11
    becca "Uhmm... Não. Você não precisa."
    show becca 1f
    show jersey 12
    player_name "Sim, Preciso! Tenho aula daqui a pouco, e estou todo suado!"
    player_name "Esse é o vestiário masculino!"
    show missy 2f
    show becca 3f
    show jersey 11
    missy "Tipo, está ocupado."
    show missy 1f
    show becca 2f
    becca "Não percebreu?"
    show missy 3f
    show becca 1f
    show jersey 12
    player_name "Estou surpreso que você saiba o que significa \"ocupado.\""
    show becca 4f
    show missy 1f
    show jersey 13
    becca "Haha!"
    show jersey 11
    show missy 4f
    show becca 3f
    missy "Não ria de mim, sua puta burra!"
    show missy 1f
    player_name "..."
    show becca 2f
    becca "Você ainda está aqui?"
    show missy 2f
    show becca 1f
    missy "O que você quer?"
    show missy 1f
    $ unlock_ui()
    menu:
        "Nada.":
            show becca 1f
            show missy 1f
            show jersey 12
            player_name "Certo!!"
            player_name "Vou tomar banho em casa..."
            show becca 2f
            show missy 3f
            show jersey 11
            becca "Vai chorar no corredor seu viado!"
            becca "Nenhum dos outros nerds se importará se você feder mesmo!"
            becca "Você ficará bem com eles!"
            show becca 1f
            player_name "..."
            show jersey 12
            player_name "Você não devia falar com as pessoas assim."
            show becca 3f
            show missy 2f
            show jersey 11
            missy "Que seja, perdedor."
            show becca 2f
            show missy 1f
            becca "Só saia."
            hide missy
            hide becca
            hide jersey
            with dissolve

        "Por favor?" if pStats.chr() < 5:
            show becca 1f
            show missy 1f
            show jersey 10
            player_name "[chr_warn]... Por favro?"
            show jersey 13
            pause
            show missy 2f
            show becca 3f
            show jersey 11
            missy "[chr_warn]Tipo, isso foi patético!"
            show missy 3f
            show becca 2f
            becca "[chr_warn]Sim, você não vai passar."
            show missy 1f
            show becca 1f
            show jersey 10
            player_name "[chr_warn]Mas eu preciso mesmo tomar banho!"
            show missy 3f
            show becca 2f
            show jersey 12
            becca "[chr_warn]Vá lavar na fonte de água!"
            show missy 1f
            show becca 1f
            show jersey 12
            player_name "[chr_warn]Não é uma fonte de água, é um bebedouro!"
            show missy 3f
            show becca 2f
            show jersey 11
            becca "[chr_warn]Foda-se, fedorento!!"
            show missy 2f
            show becca 3f
            missy "[chr_warn]Saia daqui! Tipo, agora!"
            show missy 1f
            show becca 1f
            show jersey 10
            player_name "[chr_warn]Ah, vamos! Por favor, estou fedendo muito!"
            show missy 3f
            show becca 2f
            show jersey 11
            becca "[chr_warn]Haha! Eu sei! Você sempre estará!"
            show missy 2f
            show becca 1f
            missy "[chr_warn]Saia..."
            hide missy
            hide becca
            hide jersey
            with dissolve

        "Por favor?" if pStats.chr() >= 5:
            show becca 1f
            show missy 1f
            show jersey 10 at Position (xpos=200) with fastdissolve
            player_name "Por favor! Eu estou tão fedido..."
            show becca 2f
            show jersey 11
            becca "Eew! nem se aproxime!"
            show becca 1f
            show missy 2f
            missy "Tipo, fique longe!"
            show becca 2f
            show missy 3f
            becca "Nós não queremos que seu fedor nos contamine!"
            show becca 1f
            show missy 1f
            show jersey 12
            player_name "Então eu acho que você pudesse me deixar tomar banho!"
            show becca 2f
            show missy 3f
            show jersey 11
            becca "Não podemos! {b}Roxxy{/b} está lá!"
            show missy 1f
            show becca 1f
            show jersey 12
            player_name "Se você não me deixar entrar, Vou chamar a {b}Annie{/b} e vocês conversarão com a {b}Sra. Smith{/b} então..."
            show missy 2f
            show becca 3f
            show jersey 13
            missy "Não! Não faça isso!"
            show becca 2f
            show missy 3f
            becca "Eu... Não aguento mais o cheiro!"
            becca "Vamos, tipo, dar o fora daqui!"
            hide becca
            hide missy
            with dissolve
            show jersey 17
            player_name "Ótimo..."
            player_name "Hora de um bom banho!"
            hide jersey with dissolve
            scene lockershowers with fade
            player_name "..."
            show jersey 11 at left
            show roxxy 25 at right
            with dissolve
            rox "!!!"
            show roxxy 26
            show jersey 22
            rox "Mas o que você está fazendo aqui?!" with hpunch
            show roxxy 25
            show jersey 23
            player_name "Uhh..."
            show roxxy 26
            show jersey 11
            rox "Cai fora!"
            show roxxy 25
            show jersey 10
            player_name "Não vou demorar!! Só preciso-"
            show roxxy 26
            show jersey 22
            rox "NÃO!! Da o FORA daqui!" with hpunch
            show roxxy 25
            hide jersey with fastdissolve
            pause
            show roxxy 26
            rox "Não acredito que elas deixaram você entrar!"
            rox "Ughh!!!"
            rox "{b}[firstname]{/b}, você está tããããão fodido!"
            scene locker_empty_b with None
            show player 11 with dissolve
            player_name "( Wow... )"
            player_name "( Não acredito que vi a {b}Roxxy{/b} pelada!! )"
            show player 13
            player_name "( Ela tem um corpo muito bom. )"
            show player 11
            player_name "( Espero que o {b}Dexter{/b} não descubra sobre isso... )"
            hide player with dissolve
            $ roxxy_shower.finish()
            $ roxxy_shower_lock = True
            $ location_count = "School Left Hallway"
    $ callScreen(location_count)

label denied_access_locker:
    scene locker_night
    show erik 1f at Position (xpos = 550, ypos = 768)
    show player 34 at Position (xpos = 370, ypos = 768)
    player_name "Hmm..."
    show player 113
    player_name "( Deveríamos achar {b}outro caminho{/b}. )"
    hide player 113
    hide erik 1f
    $ callScreen(location_count)

label door17_locked_dialogue:
    scene locker
    show jersey 10 at left
    player_name "( Eu deveria ir para o {b}campo{/b} para minha aula de {b}educação física{/b}... )"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
