label classroom_dialogue:
    $ location_count = "French Classroom"
    if classroom_count == 0:
        scene classroom
        show player 1 at left with dissolve
        show teacher 2 at right with dissolve
        bis "Aí está você!"
        show player 2 at left
        show teacher 1 at right
        player_name "Oi, {b}Sra. Bissette{/b}!"
        show player 2 at left
        show teacher 5 at right
        bis "Escuta, {b}[firstname]{/b}, Eu sei que você teve alguns assuntos pessoais para cuidar, e é por isso que você esteve ausente ultimamente..."
        bis "...Mas está tudo bem?"
        show player 24 at left
        show teacher 4 at right
        player_name "Sim. Acho que está tudo bem..."
        show player 5 at left
        show teacher 6 at right
        bis "Suas notas estão baixas, mas vou dar-lhe um tempo extra para entregar sua {b}tarefa{/b}..."
        show teacher 5 at right
        show player 87 at left
        bis "Faça no seu {b}computador{/b}, e volte quando estiver completa!"
        show player 13 at left
        show teacher 1 at right
        player_name "Valeu, {b}Sra. Bissette{/b}!"
        player_name "Sua aula é a minha preferida! Farei o melhor!"
        show player 1 at left
        show teacher 3 at right
        bis "Sem problemas, {b}[firstname]{/b}!"
        bis "...E vá para a {b}biblioteca{/b} para pegar alguns {b}livros escolares{/b}, isso vai te ajudar a terminar a {b}tarefa{/b}! Toda pequena ajuda é boa!"
        hide player 1 at left with dissolve
        hide teacher 1 at right with dissolve

        $ inventory.items.append(homework)
        if quest01 not in completed_quests:
            $ quest_list.append(quest01)

        show unlock18 at truecenter
        $ renpy.pause()
        hide unlock18 with dissolve

        show unlock5 at truecenter
        $ renpy.pause()
        hide unlock5 with dissolve
        $ loc_library_unlocked = True

        show evedesk 1 at left with dissolve
        eve "Wow... Eu pensei que você estava morto!"
        show evedesk 2 at left
        player_name "O quê?... Como assim?"
        show evedesk 1 at left
        eve "Sei lá... Você desapareceu po meses, e as pessoas começaram a inventar rumores sobre como sua família havia sido assassinada ou algo assim..."
        show evedesk 3 at left
        player_name "Ugh... Não é nada disso!"
        show evedesk 4 at left
        eve "Imaginei. As pessoas gostam inventar coisas, e esta escola é uma grande piada."
        eve "Fice feliz que o último ano esteja quase terminando..."
        show evedesk 5 at left
        player_name "Sim, também."
        show evedesk 6 at left
        eve "Você deveria ir ao {b}parque{/b} às vezes... Ficar longe de todos esses idiotas em torno da escola e relaxe, você sabe?"
        show evedesk 5 at left
        eve "Tenha certeza de ir a {b}notie{/b}... é quando nós vamos lá."
        player_name "Ehh... acho que posso ir."
        show evedesk 6 at left
        eve "É só você querer. Faça o que quiser!"
        hide evedesk 6 at left with dissolve

        show unlock2 at truecenter
        $ renpy.pause()
        hide unlock2 with dissolve
        $ loc_park_unlocked = True

        $ classroom_count = 1
        $ stairs_count = 3
        $ left_hall_count = 0
        $ map_talk_count = 1
        $ unlock_ui()
        $ bed_locked = 1
        $ event_outside_school_count = 1
        $ erik_door_count = 1
        $ gTimer.tick()
        jump map_dialogue
    $ callScreen(location_count)

label teacher_button_dialogue:
    scene location_classroom_closeup
    show player 1 at left with dissolve
    show teacher 2 at right with dissolve
    bis "Oi, {b}[firstname]{/b}!"
    show player 17 at left
    show teacher 1 at right
    player_name "Oi, {b}Mrs. Bissette{/b}!"
    show player 1 at left
    show teacher 2 at right
    bis "Você conseguiu acompanhar seus estudos??"
    bis "Espero que esteja a recuperar os seus estudos!"
    bis "Agora, há algo sobre o que você queria falar?"
    show teacher 1
    menu:
        "Não.":
            show player 14
            player_name "Não. Só queria dizer oi."
            show teacher 2
            show player 13
            bis "Bom, sente-se. A aula já vai começar!"
            show teacher 3
            bis "Eu tenho uma aula emocionante planejada para hoje!"
            show teacher 1
            show player 2
            player_name "Parece legal, {b}Sra. Bissette{/b}."

        "Estou pronto!" if homework1 in inventory.items or homework_handed:
            if homework_handed:
                show player 14 at left
                show teacher 1 at right
                player_name "Agora que eu entreguei minha {b}tarefa{/b}, tem algo que eu devesse fazer?"
                show teacher 3
                show player 1
                bis "Eu corrijo durante a aula e te entrego depois!"
                show teacher 2
                bis "Sente-se, e {b}fique para a aula{/b}. Te vejo mais tarde..."
                hide teacher 2 at right with dissolve
                hide player 1 at left with dissolve
            else:

                show player 17 at left
                show teacher 1 at right
                player_name "Terminei sua primeira {b}tarefa{/b}!"
                show player 239_240
                pause
                show player 86 at left
                player_name "Aqui!"
                show teacher 6 at right
                show player 13 at left
                bis "Já? Foi rápido! Geralmente demoram bem mais!"
                show teacher 3 at right
                show player 29 at left
                player_name "Eu te disse, eu gosto das suas aulas!!"
                bis "Você é tão fofo!"
                show teacher 2 at right
                bis "...Se eu tivesse mais alunos como você..."
                show teacher 11 at right
                show player 13 at left
                bis "Hmm..."
                show teacher 12 at right
                show player 11 at left
                bis "Por que você não fica {b}para depois da aula{/b}? Eu te devolvo a {b}tarefa{/b} corrigida!"
                show teacher 13 at right
                show player 14 at left
                player_name "Uhm... Claro, {b}Sra. Bissette{/b}!"
                show teacher 12 at right
                show player 1 at left
                bis "Sente-se e {b}fique para a aula{/b}. Te vejo mais tarde..."
                $ inventory.items.remove(homework1)
                $ homework_handed = True
                hide teacher 12 at right with dissolve
                hide player 1 at left with dissolve
        "Trabalhando nisso.":

            show player 10 at left
            show teacher 12 at right
            player_name "Ainda não terminei, estou trabalhando nisso!"
            show player 5 at left
            show teacher 2 at right
            bis "Tudo bem, demore o quanto você quiser..."
            show teacher 3 at right
            show player 13 at left
            bis "...E lembre-se de visitar a {b}biblioteca{/b}!"
            bis "Você pode achar {b}livros{/b} úteis lá!"
            show teacher 1 at right
            show player 2 at left
            player_name "Obrigado, {b}Sra. Bissette{/b}!"
            hide teacher 1 at right with dissolve
            hide player 2 at left with dissolve
        "Conversar.":

            show player 29 at left
            show teacher 1 at right
            player_name "{b}Sra. Bissette{/b}, eu só queria dizer que eu agradeço a sua ajuda com o atraso da minha tarefa!"
            show player 13 at left
            show teacher 3 at right
            bis "O prazer é todo meu! Tudo o que quero é garantir que você esteja pronto e motivado..."
            show teacher 12 at right
            bis "...E eu amo recompensar meus bons alunos!"
            show teacher 13 at right
            show player 10 at left
            player_name "Farei o que for possível. Eu quero ir para uma boa faculdade..."
            show teacher 2 at right
            show player 13 at left
            bis "Isso que eu gosto de ouvir!"
            bis "Posso corrigir sua {b}tarefa{/b} com você quando tiver pronto, se quiser!"
            show teacher 1 at right
            show player 17 at left
            player_name "Parece ótimo, {b}Sra. Bissette{/b}! Obrigado!"
            hide teacher 1 at right with dissolve
            hide player 17 at left with dissolve
    $ callScreen(location_count)

label class_started:
    scene classroom
    show player 12 with dissolve
    player_name "( A aula já começou! Tem mais algumas horas restantes... )"
    show player 35
    player_name "( Eu deveria me sentar na aula pela manhã para que eu possa entender tudo! )"
    hide player 35 with dissolve
    $ callScreen(location_count)

label school_closing_dialogue:
    scene classroom
    show player 1 with dissolve
    player_name "( Deveria ir para casa, a escola já vai fechar. )"
    hide player
    $ callScreen(location_count)

label class_study01:
    if class_study_count == 0:
        show studyclass01 with dissolve
        show text "Foi bom estar de volta à aula depois de um mês de folga." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass02 with dissolve
        show text "Passei o dia inteiro tentando recuperar meu estudos..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass03 with dissolve
        show text "...até que o sino soou." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass04 with dissolve
        show text "É difícil manter o foco quando eu dormi pouco." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass05
        show text "Mas eu sempre posso contar com meus colegas de classe para me manter acordado..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass06
        show text "Eles estão me perseguindo ultimamente...\nProvavelmente porque acabei de voltar e agora sou o centro das atenções..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass07
        show text "Não me entenda mal. Posso me virar..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass08 with hpunch
        show text "...mas acho que é assim que a escola funciona.\nBem, pelo menos o dia acabou e eu posso ir para casa agora..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        $ class_study_count = 1

        hide studyclass01
        hide studyclass02
        hide studyclass03
        hide studyclass04
        hide studyclass05
        hide studyclass06
        hide studyclass07
        hide studyclass08 with dissolve

        if homework_handed == True:
            jump homework_handed_dialogue
        scene black with dissolve
        show unlock21 at truecenter with dissolve
        $ renpy.pause()
        hide unlock21 with dissolve
        $ gTimer.tick()
        $ pStats.increase("int")
        if gTimer.is_evening():
            jump night_closed_school
        $ callScreen(location_count)
    else:

        show studyclass01 with dissolve
        show text "Eu me sento na minha mesa e comecei outro dia da aula..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass02 with dissolve
        show text "Passei o dia inteiro tentando voltar aos estudos..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text
        show studyclass03 with dissolve
        show text "...até que o sinal soou." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        scene black with dissolve
        with Pause(0.5)

        show studyclass04 with dissolve
        show text "É difícil manter o foco quando eu dormi pouco.\nPelo menos o dia acabou e eu posso ir para casa agora..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve

        if homework_handed == True:
            jump homework_handed_dialogue

        hide studyclass01
        hide studyclass02
        hide studyclass03
        hide studyclass04 with dissolve
        scene black with dissolve
        with Pause(0.5)
        $ pStats.increase("int")
        $ gTimer.tick()
        if gTimer.is_dark():
            jump night_closed_school
        $ callScreen(location_count)

label homework_handed_dialogue:
    if homework_count == 0:
        scene classroom_night
        show desk 1 at Position (xpos = 400, ypos = 768) with dissolve
        show teacher 7 at right with dissolve
        bis "Obrigada por ter ficado até mais tarde!"
        show teacher 8 at right
        show desk 2
        bis "Só queria entregar sua {b}tarefa{/b}, e falar sobre o seu progresso..."
        show teacher 9 at right
        show desk 4
        player_name "Fui mal?"
        show desk 3
        $ inventory.items.append(homework2)
        $ homework_done = False
        player_name "..."
        show desk 6
        player_name "Tirei um {b}C+{/b}..."
        show desk 5
        show teacher 10 at right
        bis "Não se preocupe!"
        bis "Você foi bem se levarmos em consideração que você está atrasado!"
        show teacher 9 at right
        show desk 6
        player_name "Naõ sei se consigo fazer isso {b}Sra. Bissette{/b}..."
        show teacher 10 at right
        show desk 5
        bis "Não diga isso!"
        hide teacher
        show desk 7 at Position (xpos = 450, ypos = 768)
        bis "Você tem que continuar tentando."
        show desk 8 at Position (xpos = 371, ypos = 768)
        bis "...você é um estudante tão forte..."
        player_name "..."
        show desk 9 at Position (xpos = 373, ypos = 768)
        bis "...Não tem nada que eu goste mais..."
        show desk 10
        bis "...do que {b}motivar{/b} meus alunos..."
        bis "...E eu sou muito boa nisso..."
        show desk 11
        player_name "...Hum..."
        show desk 8 at Position (xpos = 371, ypos = 768)
        bis "Muito bem!"
        show desk 12 at Position (xpos = 450, ypos = 768)
        bis "Agora termine sua {b}tarefa{/b} em casa e volte quando você tiver terminado..."
        bis "...Sei que você consegue mais do que um {b}C+{/b}!"
        show desk 13
        player_name "S... Sim! {b}Sra. Bissette{/b}!"
        show desk 12
        bis "Bom garoto..."
        $ gTimer.tick(3)
        $ homework_handed = False
        $ homework_count = 1
        $ M_mia.trigger(T_mc_homework)
        hide desk 12 with dissolve

    elif homework_count == 1:
        scene classroom_night
        show desk 1 at Position (xpos = 400, ypos = 768) with dissolve
        show teacher 7 at right with dissolve
        bis "Obrigado por ficar depois da aula comigo novamente..."
        show teacher 8 at right
        show desk 2
        bis "Só queria te entregar a {b}tarefa{/b} e falar sobre o seu progresso..."
        show teacher 9 at right
        show desk 4
        player_name "Como eu fui agora?"
        show desk 21
        $ inventory.items.append(homework3)
        player_name "..."
        show desk 22
        player_name "Um {b}B+{/b}!"
        hide teacher
        show desk 7 at Position (xpos = 450, ypos = 768)
        bis "Exato!"
        show desk 12
        bis "Foi melhor que a média da sala!"
        show desk 13
        player_name "Wow... Isso é uma ótima notícia,{b}Sra. Bissette{/b}!"
        show desk 12
        bis "Sim!"
        bis "E..."
        show desk 14 at Position (xpos = 458, ypos = 768)
        bis "Estou muito orgulhosa de você, {b}[firstname]{/b}."
        bis "Você está mostrando melhoras..."
        show desk 15
        player_name "...Ah, é?"
        show desk 16
        bis "Sim!"
        bis "E... Eu sempre estou disposta a..."
        show desk 17 at Position (xpos = 457, ypos = 768)
        bis "...{b}recompensar{/b}..."
        show desk 18 at Position (xpos = 458, ypos = 768)
        bis "...quem tira {b}A{/b}'s."
        player_name "!!!"
        show desk 16
        bis "Apenas..."
        bis "Continue me mostrando seu desejo de melhorar..."
        show desk 19
        bis "And..."
        show desk 20
        bis "Eu vou ter certeza de devolver o favor..."
        player_name "..."
        show desk 12 at Position (xpos = 450, ypos = 768)
        bis "Você gostaria disso?"
        show desk 13
        player_name "S... Sim! {b}Sra. Bissette{/b}!"
        show desk 12
        bis "Bom garoto..."
        hide desk with dissolve
        $ gTimer.tick(3)
        $ homework_handed = False
        $ homework_count = 2
    else:

        scene classroom_night
        show popup_unfinished at truecenter with dissolve
        $ renpy.pause()
        hide popup_unfinished with dissolve
        $ callScreen(location_count)
    jump night_closed_school
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
