default MC_computer_broken = True
default cookies_taken = False
default first_mom_visit = False

label bedroom_dialogue:
    $ location_count = "Bedroom"
    if not M_player.is_set("just wokeup"):
        if M_mom.get_state() == S_mom_mrsj_visit and not gTimer.is_dark():
            jump home_front

        elif M_mom.get_state() == S_mom_car_fixed:
            jump home_front

        elif M_mom.get_state() == S_mom_bad_guys_revisit and not gTimer.is_dark():
            jump home_front

        elif M_mom.get_state() == S_mom_diane_visit and gTimer.is_evening():
            jump home_entrance

    if erik.completed(erik_bullying_2) and not erik.known(erik_bullying_3):
        jump erik_bullying_3

    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom{}"

    if M_player.get_state() == S_player_start and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        player_name "Ugh... Odeio acordar cedo."
        show player 9
        player_name "( Nenhuma mensagem do {b}Erik{/b}. Ele ainda deve estar dormindo. )"
        player_name "( Vou passar na casa dele antes de ir para a escola. )"
        hide player 9 with dissolve

    elif gTimer.is_morning() and not gTimer.is_weekend() and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        window hide
        pause
        show player 9
        player_name "( Tenho que me preparar para a escola... )"
        hide player with dissolve

    elif gTimer.is_morning() and gTimer.is_weekend() and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 8
        window hide
        pause
        show player 9
        player_name "( O que eu deveria fazer nesse fim de semana... )"
        hide player with dissolve

    if gTimer.gameDay() >= event_wait_till and not erik.known(erik_bullying):
        scene black with fade
        mom "Querido?"
        pause
        mom "Acorda, qurido."
        scene expression gTimer.image(tmp_image) with fade
        show mom 14f at left
        show player 101bf at right
        with dissolve
        player_name "Huh? {b}[mom_name]{/b}? Que horas são?"
        show player 100bf
        show mom 13f
        mom "{b}Sra. Johnson{/b} está na porta querendo falar com você."
        show mom 14f
        show player 101bf
        player_name "{b}Sra. Johnson{/b}? Comigo?"
        show player 100bf
        show mom 13f
        mom "Ela não disse muita coisa, mas queria falar com você antes de ir para a escola."
        show mom 14f
        show player 101bf
        player_name "Oh. Ok. Vou me vestir e já desco."
        show player 100bf
        show mom 13f
        mom "Ok..."
        show mom 14f
        pause
        show mom 13f
        mom "Tem algo que eu deveria saber, {b}[firstname]{/b}?"
        show mom 14f
        player_name "..."
        show player 101bf
        player_name "Não faço ideia do que ela quer, {b}[mom_name]{/b}."
        show player 100bf
        mom "..."
        show mom 13f
        mom "Ok, querido."
        hide mom
        hide player
        with dissolve
        $ lock_ui()
        $ erik.add_event(erik_bullying)

    elif M_mia.get_state() == S_mia_tattoo_help and M_mia.is_set('story delay'):
        scene expression gTimer.image(tmp_image)
        show player 35 with dissolve
        player_name "( Eu tenho que pensar em algo legal para a tatuagem dela. )"
        show player 34
        player_name "Hmm..."
        show player 35
        player_name "( Talvez eu pudesse usar {b}o cavalete da aula de artes{/b}! )"
        show player 33
        player_name "( Eu posso usar para criar um desenho legal para ela. )"
        show player 8 with dissolve
        pause
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 101 with dissolve
        player_name "Eu deveria dormir."
        hide player with dissolve
        show unlock53 at truecenter with dissolve
        pause
        hide unlock53 with dissolve
        $ M_mia.trigger(T_mia_tattoo_start)

    elif M_mia.get_state() == S_mia_strip_aftermath and M_mia.is_set('story delay'):
        scene expression gTimer.image(tmp_image)
        show player 24 with dissolve
        player_name "( Não acredito que nunca mais vou poder ver a {b}Mia{/b}. )"
        show player 25
        player_name "( A família dela não gosta de mim. )"
        show player 35
        player_name "( Talvez eu possa fazer com eles mudem de ideia de alguma forma... )"
        hide player with dissolve
        $ M_mia.trigger(T_mia_grounded)

    elif M_mia.get_state() == S_mia_strip_aftermath:
        scene expression gTimer.image(tmp_image)
        show player 4 with dissolve
        pause
        show player 30 at Position (xoffset=-6) with dissolve
        player_name "( Adoraria saber o que a {b}Mia{/b} está fazendo. )"
        show player 12 at Position (xoffset=-6)
        player_name "( Fazem dias e eu ainda não ouvi nada sobre ela... )"
        player_name "( ...Talvez eu devesse visitá-la... )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_urgent_message:
        scene expression gTimer.image(tmp_image)
        show player 12 with dissolve
        player_name "Huh?"
        show player 9 at Position (xoffset=40) with dissolve
        pause
        show player 14 with dissolve
        player_name "( Parece que eu tenho uma nova mensagem... )"
        hide player with dissolve
        $ lock_ui()
        if m_mia02 not in message_list:
            $ message_list.append(m_mia02)
            $ new_message = True

    elif M_mia.get_state() == S_mia_angelicas_impatience:
        scene expression gTimer.image(tmp_image)
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "( Talvez eu devesse ficar pronto para- )"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "Tem alguém aqui em baixo esperando você."
        show mom 1f
        show player 30f
        player_name "{b}Erik{/b}?"
        show player 11f
        show mom 2f
        mom "Não, querido. é uma mulher!"
        mom "Ela disse que vocês já falaram antes..."
        show mom 1f
        show player 10f
        player_name "O quê?"
        player_name "Mas quem-"
        show player 5f
        show mom 2f
        mom "Ela está esperando lá em baixo. Por que você não {b}se veste e vai até lá{/b}."
        hide mom with dissolve
        show player 12f player_name "Uma moça?!"
        show player 4f at Position (xoffset=-6) with dissolve
        player_name "Huh..."
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_home_visit:
        scene expression gTimer.image(tmp_image)
        show player 13f at right
        show mom 2f at left
        mom "Querido?"
        show mom 1f
        show player 17f
        player_name "Bom dia, {b}[mom_name]{/b}."
        show player 13f
        show mom 2f
        mom "Bom dia."
        mom "Aquela mesma mulher do outro dia está lá de novo."
        show mom 1f
        show player 11f
        player_name "..."
        show player 12f
        player_name "Quem?"
        show player 5f
        show mom 3f
        mom "Vamos, dorminhoco. A freira está aqui de novo."
        show mom 1f
        show player 22f
        player_name "!!!"
        mom "Vista-se e vá lá para baixo."
        hide mom with dissolve
        show player 10f
        player_name "O que ela quer agora?"
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_final_home_visit:
        scene expression gTimer.image(tmp_image) with fade
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "Eu deveria me preparar para a-"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "A freira está aqui de novo..."
        show mom 1f
        show player 30f
        player_name "De novo?"
        show player 24f
        pause
        show mom 13f
        mom "Desculpa perguntar mas..."
        mom "O que você está fazendo para a igreja?"
        show mom 14f
        show player 11f
        player_name "..."
        show mom 13f
        mom "Digo, estou supresa que você receba tantas visitas dessa freira..."
        show mom 14bf
        show player 29f at Position (xoffset=-35) with dissolve
        player_name "Eh, hum... está tudo... bem."
        player_name "Ela só está... me fazendo mandar recados."
        player_name "( Yeah, heh... heh... )"
        show player 3f at Position (xoffset=-35)
        show mom 14f
        mom "..."
        show mom 13f
        mom "Bem, pelo menos você está fazendo algo de bom para a comunidade..."
        show player 5f with dissolve
        show mom 2f
        mom "Acho que não deveria me preocupar."
        show mom 3f
        mom "Que mal pode vir de você ficar um tempo na igreja?"
        hide mom with dissolve
        show player 11f
        player_name "..."
        show player 37f at Position (xoffset=-41) with dissolve
        player_name "( Você não faz ideia... )"
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_impatience:
        scene expression gTimer.image(tmp_image)
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "Eu deveria me preparar para a-"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "Tem alguém te esperando lá em baixo."
        show mom 1f
        show player 30f
        player_name "{b}Erik{/b}?"
        show player 11f
        show mom 2f
        mom "Não, querido. É uma mulher!"
        mom "Ela disse que vocês já se falaram antes..."
        show mom 1f
        show player 10f
        player_name "Quê?"
        player_name "Mas quem-"
        show player 5f
        show mom 2f
        mom "Ela está te esperando lá em baixo. Por que você não {b}se veste e vem lá ver{/b}?"
        hide mom with dissolve
        show player 12f player_name "Uma moça?!"
        show player 4f at Position (xoffset=-6) with dissolve
        player_name "Huh..."
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_home_visit:
        scene expression gTimer.image(tmp_image) with fade
        show player 13f at right
        show mom 2f at left
        mom "Querido?"
        show mom 1f
        show player 17f
        player_name "Bom dia, {b}[mom_name]{/b}."
        show player 13f
        show mom 2f
        mom "Bom dia."
        mom "Aquela moça está lá em baixo de novo."
        show mom 1f
        show player 11f
        player_name "..."
        show player 12f
        player_name "Quem?"
        show player 5f
        show mom 3f
        mom "Vamos, dorminhoco. A freira está aqui de novo."
        show mom 1f
        show player 22f
        player_name "!!!"
        mom "Vista-se e venha vê-la."
        hide mom with dissolve
        show player 10f
        player_name "O que ela quer agora"
        hide player with dissolve
        $ lock_ui()

    elif M_mia.get_state() == S_mia_angelicas_final_home_visit:
        scene expression gTimer.image(tmp_image) with fade
        show player 55f at Position (xoffset=-12) with dissolve
        player_name "*Yawn*"
        show player 56f with dissolve
        player_name "Eu deveria me preparar para a-"
        show player 11f
        "*Knock knock*"
        show mom 2f at left
        show player 13f
        with dissolve
        mom "Hun?"
        mom "A freira está aqui de novo..."
        show mom 1f
        show player 30f
        player_name "De novo?"
        show player 24f
        pause
        show mom 13f
        mom "Desculpa perguntar mas..."
        mom "O que você está fazendo para a igreja?"
        show mom 14f
        show player 11f
        player_name "..."
        show mom 13f
        mom "Digo, estou supresa que você receba tantas visitas dessa freira..."
        show mom 14bf
        show player 29f at Position (xoffset=-27) with dissolve
        player_name "Eh, hum... está tudo... bem."
        player_name "Ela só está... me fazendo mandar recados."
        player_name "Yeah, heh... heh..."
        show player 3f at Position (xoffset=-35)
        show mom 14f
        mom "..."
        show mom 13f
        mom "Bem, pelo menos você está fazendo algo de bom para a comunidade..."
        show player 5f with dissolve
        show mom 2f
        mom "Acho que não deveria me preocupar."
        show mom 3f
        mom "Que mal pode vir de você ficar um tempo na igreja."
        hide mom with dissolve
        show player 11f
        player_name "..."
        show player 37f at Position (xoffset=-41) with dissolve
        player_name "Você não faz ideia..."
        hide player with dissolve
        $ lock_ui()

    if M_mom.get_state() == S_mom_overheard and gTimer.is_dark():
        scene expression gTimer.image(tmp_image)
        show player 34 with dissolve
        player_name "...{b}*voz distante*{/b}..."
        show player 35
        player_name "( É a {b}[mom_name]{/b} no telefone? )"
        show player 12
        player_name "( ...Parece que ela está brava... Ela está gritando? )"
        show player 10
        player_name "( Eu deveria ir checar se ela está bem. )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_check)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_doorbell:
        scene expression gTimer.image(tmp_image)
        show player 12 with dissolve
        player_name "( A campanhia está tocando, alguém está na porta. )"
        player_name "( Deve ser o {b}Erik{/b} ou algo do tipo... )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_check_door)
        $ lock_ui()

    elif M_mom.get_state() == S_mom_movie_afterthoughts:
        scene expression gTimer.image(tmp_image)
        show player 5
        player_name "Bem, isso foi super estranho!"
        player_name "Não tem como ela não ter notado..."
        player_name "Quero dizer, ela não disse nada."
        player_name "... mas ela ficou visivelmente desconfortável."
        show player 11
        player_name "Espero que {b}[mom_name]{/b} não fique triste comigo..."
        player_name "..."
        show player 24
        player_name "Ugh, vou me preocupar com isso amanhã. Agora preciso dormir um pouco."
        hide player with dissolve
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.get_state() == S_mom_movie_afterthoughts_two:
        scene location_bedroom_blur_night
        show player 13
        player_name "Isso foi excitante!"
        player_name "A buceta molhada da [mom_name] estava se esfregando em mim."
        player_name "... E os seios dela estavam muito bons!"
        show player 5
        player_name "..."
        player_name "Ela meio que ficou estranha lá no final."
        player_name "Talvez eu devesse me desculpar?"
        player_name "..."
        show player 13
        player_name "Sem sentido me preocupar com isso. Vou dormir."
        hide player with dissolve
        $ M_mom.trigger(T_mom_movie_night_finish)

    elif M_mom.get_state() == S_mom_note and gTimer.is_dark():
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 101 with dissolve
        player_name "Eu deveria ir dormir."
        hide player with dissolve

    elif M_mom.get_state() == S_mom_note and M_player.is_set("just wokeup"):
        scene expression gTimer.image(tmp_image)
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 11
        player_name "!!!"
        show player 10
        player_name "Alguém deixou um {b}recado{/b} na tela do meu computador?"
        hide player with dissolve
        $ M_player.set("just wokeup", False)
        $ lock_ui()

    if not gTimer.is_dark():
        if M_player.is_set("just wokeup"):
            if gTimer.is_morning() and not shower.occupied("sis", False) and (
                    sister.started(sis_webcam01) or
                    sister.started(sis_webcam02) or
                    sister.started(sis_webcam03) or
                    (sister.over(sis_webcam04) and not sis_lastwebcam_show_seen)
                    ):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "Hmm..."
                player_name "( O que será que a minha {b}irmã{/b} está fazendo agora? )"
                show player 1
                player_name "( Talvez eu pudesse ver pela {b}webcam{/b} que conectei no meu computador... )"
                hide player with dissolve

            elif sister.started(sis_telescope01) and (not shower.occupied("sis", False) and gTimer.is_morning()):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( O que será que o {b}Erik{/b} está fazendo agora? )"
                player_name "( I should use my {b}telescope{/b} and see what he's up to... )"
                hide player with dissolve

            elif sister.started(sis_telescope02) and (not shower.occupied("sis", False) and gTimer.is_morning()):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( O que será que a {b}Mia{/b} está fazendo agora? )"
                player_name "( Talvez eu pudesse usar meu {b}telescópio{/b} e espiar o que ela está fazendo... )"
                hide player with dissolve

            elif sister.started(sis_telescope03) and (not shower.occupied("sis", False) and gTimer.is_morning()):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( O que será que a {b}Sra. Johnson{/b} está fazendo agora? )"
                player_name "( Talvez eu pudesse usar meu {b}telescópio{/b} e espiar o que ela está fazendo... )"
                hide player with dissolve

            elif training_count == 1 and training_tier == 2 and sister.over(sis_shower_cuddle01) or training_count == 2 and training_tier == 3 and sister.over(sis_couch02) or training_count == 3 and training_tier == 4 and sister.over(sis_couch03):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( Será que o {b}Mestre Somrak{/b} está preparado para me treinar novamente? )"
                hide player with dissolve

            if M_mom.is_set("chores"):
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                if randomizer() < 50:
                    player_name "Será que {b}[mom_name]{/b} precisa de ajuda com algo na casa?"
                    player_name "Deveria ir perguntar para ela..."
                else:
                    player_name "Será que {b}[mom_name]{/b} precisa de ajuda com algo..."
                hide player with dissolve

            elif M_mom.get_state() == S_mom_search_panties:
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "( Não consigo parar de pensar em aplicar a loção na [mom_name] )"
                player_name "( As pernas tão mascias.. )"
                player_name "( E ela tão cheirosa.. )"
                show player 11
                player_name "( Pensando bem. A loção estava na gaveta da calcinha. )"
                player_name "( Estou morrendo de vontade de ver essas calcinhas... )"
                show player 13
                player_name "( Talvez agora seja uma boa hora. )"
                hide player with dissolve

            elif M_mom.get_state() == S_mom_kissing_practice:
                scene expression gTimer.image(tmp_image)
                show player 4 with dissolve
                player_name "Eu continuo tendo esses sonhos pervertidos com [mom_name]."
                player_name "Eles estão me enlouquecendo!"
                show player 5
                player_name "..."
                player_name "Eu provavelmente deveria {b}conversar com ela{/b} sobre isso..."
                hide player with dissolve
            $ M_player.set("just wokeup", False)

    elif gTimer.is_evening():
        if sister.started(sis_couch01):
            scene expression gTimer.image(tmp_image)
            show player 10 with dissolve
            player_name "( Ouvi alugém no corredor... Talvez a porta do quarto da minha {b}irmã{/b}? )"
            show player 4
            player_name "( Será que ela está fazendo algo? )"
            hide player with dissolve

        elif sister.started(sis_couch03):
            scene expression gTimer.image(tmp_image)
            show player 4 with dissolve
            player_name "( Será que eu não poderia assistir {b}novos filmes pornôs{/b} na TV hoje a noite? )"
            show player 26
            player_name "( Eu deveria tentar equanto está todo mundo dormindo... )"
            hide player with dissolve
    $ callScreen(location_count)

label june_bedroom_dialogue:
    $ gTimer.tick()
    $ june_hang_out = False
    if June.in_progress(june_cosplay):
        scene bedroom_sex2
        show player_sitting 2 zorder 1 at right
        show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
        with fastdissolve
        player_name "Então, o que vamos fazer?"
        show june_sitting 10
        show player_sitting 5
        june "Sua porta está fechada?"
        show june_sitting 11
        show player_sitting 2
        player_name "Uhh... Acho que sim? Por quê?"
        show june_sitting 12
        show player_sitting 5
        june "Bem, eu não quero que seus pais me vissem enquanto eu estou me vestindo!"
        show june_sitting 11
        show player_sitting 4
        player_name "Oh, você vai fazer isso... bem... aqui?"
        show june_sitting 10
        show player_sitting 5
        june "Claro, bobinho!"
        june "Talvez eu precise de sua ajuda para colocar isso..."
        june "E eu quero sua opinião!"
        show player_sitting 3
        june "Meu cosplay tem que parecer igual."
        show june_sitting 11
        show player_sitting 4
        player_name "Entendi."
        player_name "Então... Como começamos?"
        show june_sitting 10
        show player_sitting 5
        june "Eu deveria ficar pelada primeiro."
        show june_sitting 11
        player_name "..."
        show june_sitting 10
        june "Calma, vou tirar a roupa..."
        show june_sitting 14 at Position(xoffset=7) with fastdissolve
        pause
        show player_sitting 7
        show june_sitting 15 with fastdissolve
        pause
        show june_sitting 16 at Position(xpos=288) with fastdissolve
        show player_sitting 10 with hpunch
        pause
        show june_sitting 19
        show june_sitting_underwear zorder 2 at Position(xpos=268,ypos=595)
        with fastdissolve
        june "..."
        show june_sitting 20
        june "Ha ha!"
        show player_sitting 5 with fastdissolve
        june "Você não precisa fechar os olhos, bobinho!"
        show june_sitting 19
        show player_sitting 4
        player_name "Eu apenas... não quis-"
        show june_sitting 20
        show player_sitting 5
        june "Está tudo bem, quero que você veja."
        show june_sitting 19
        show player_sitting 4
        player_name "Okay..."
        show june_sitting 20
        show player_sitting 3
        june "Preciso tirar TODA minha roupa..."
        hide june_sitting_underwear
        show june_sitting 23
        with fastdissolve
        pause
        show june_sitting 24 with fastdissolve
        pause
        show june_sitting 25 at Position(xoffset=40) with fastdissolve
        june "... Se quisermos fazer o cosplay direito!"
        show june_sitting 19 with fastdissolve
        show player_sitting 4
        player_name "Você... Você está bem bonita!"
        show june_sitting 22b at Position(xoffset=18)
        show player_sitting 3
        june "Valeu."
        show june_sitting 20
        june "Agora, antes de colocar a roupa, preciso da sua ajuda com algo..."
        show june_sitting 19
        show player_sitting 4
        player_name "Como posso te ajudar?"
        show player_sitting 11
        show june_sitting 26 at Position(xoffset=24) with fastdissolve
        june "Preciso pintar o corpo... E tem alguns lugares que eu não consigo alcançar!"
        june "Aqui, pegue isso e ponha um pouco nos seus dedos..."
        show june_sitting 19
        show player_sitting 12
        with fastdissolve
        player_name "Onde começamos?"
        show june_sitting 22b at Position(xoffset=18)
        show player_sitting 13 with fastdissolve
        june "Deixe sua imaginação trabalhar!"
        show black zorder 3 with dissolve
        show june_sitting 29
        show player_sitting 1
        player_name "... Certeza que você quer pintar aqui também?"
        june "Não tenha medo, vai!"
        june "Aaah, isso faz cócegas..."
        hide black with dissolve
        june "Então?"
        june "Como estou?"
        show june_sitting 28
        show player_sitting 2
        player_name "Está bem... convincente!"
        player_name "Você realmente parece um orcette, de verdade..."
        show june_sitting 29
        show player_sitting 5
        june "Você se sentiu... atraido com meu novo visual?"
        show june_sitting 28
        show player_sitting 4
        player_name "Você quer dizer, eu-"
        show june_sitting 29
        show player_sitting 5
        june "Você ficou excitado... me olhando?"
        show june_sitting 28
        show player_sitting 3
        player_name "..."
        show player_sitting 4
        player_name "Acho que você ficou bem bonita... de verde..."
        show june_sitting 29
        show player_sitting 3
        june "Por que você não vem e me beija, capitão?"
        hide player_sitting
        show june_sitting 31 at center
        with fastdissolve
        pause
        label june_cosplay_sex:
            show junesex 2b
            hide june_sitting
            hide player_sitting
            with fade
            june "Eu quero esse... pauzão do capitão..."
            june "... deep inside me!"
            show junesex 3b with fastdissolve
            june "Ahh..."
            show junesex 4b with fastdissolve
            june "Isssoo!"
            june "Me bate, {b}[firstname]{/b}!!"
            $ anim_toggle = False
            $ xray = False
            $ M_june.set('sex speed', .3)

            label june_mcbedroom_cosplay_sex_loop:
                hide screen june_mcbedroom_cosplay_sex_options
                show screen xray_scr
                pause
                hide screen xray_scr
                if anim_toggle:
                    show junesex 4b_5b_6b_7b_8b
                    pause 8
                else:

                    $ animcounter = 0
                    while animcounter < 3:
                        show junesex 4b
                        pause
                        show junesex 5b
                        pause
                        show junesex 6b
                        pause
                        show junesex 7b
                        pause
                        show junesex 8b
                        pause
                        $ animcounter += 1

            show screen june_mcbedroom_cosplay_sex_options
            pause
            jump june_mcbedroom_cosplay_sex_loop

            label june_mcbedroom_cosplay_sex_cum_inside:
                hide screen june_mcbedroom_cosplay_sex_options
                show junesex 4b_5b_6b_7b_8b
                pause
                show junesex 9b with hpunch
                june "Ahh!!!"
                show white
                pause 0.3
                hide white with dissolve
                pause
                show junesex 14b with fastdissolve
                june "Eu... me sinto tão bem..."
                june "... seu pau de orc dentro de mim..."
                june "... meu capitão..."
                if June.over(june_cosplay):
                    jump june_aftercum_inside
                else:
                    jump june_aftercum_initial

            label june_mcbedroom_cosplay_sex_cum_outside:
                hide screen june_mcbedroom_cosplay_sex_options
                show junesex 4b_5b_6b_7b_8b
                pause
                show junesex 9b with hpunch
                player_name "Ahh!!!"
                show white
                pause 0.3
                show junesex 10b
                hide white with dissolve
                pause
                show junesex 11b with fastdissolve
                june "..."
                show junesex 12b
                june "Tanta... porra!"
                june "Eu estava esperando que você me abraçasse e gozasse dentro..."
                june "... com todo essa porra de orc..."
                june "Talvez na próxima vez?"
                if June.over(june_cosplay):
                    jump june_aftercum_outside

        label june_aftercum_initial:
        hide junesex
        scene black
        with fade
        scene bedroom_sex2
        show player_sitting 3 zorder 1 at right
        show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
        with fade
        june "Isso foi muito gostoso!"
        june "Está ficando muito tarde... Eu deveria ir para casa."
        show player_sitting 6
        show june_sitting 11
        player_name "Sim, minha mãe vai começar a suspeitar desse tempo que passamos aqui..."
        show june_sitting 10
        show player_sitting 3
        june "Ha ha."
        june "Acho que foi um tempo bem gasto!"
        show june_sitting 11
        show player_sitting 4
        player_name "Me diverti também."
        show june_sitting 10
        show player_sitting 3
        june "Talvez podemos fazer isso de novo?"
        show june_sitting 11
        show player_sitting 4
        player_name "Claro!"
        show player_sitting 6
        player_name "Eu adoraria."
        show june_sitting 10
        show player_sitting 3
        june "Ok, vejo você na escola então?"
        show june_sitting 11
        show player_sitting 4
        player_name "Claro!"
        $ June.complete_events(june_cosplay)
    else:

        scene bedroom_sex2
        if June.over(june_cosplay):
            show june_sitting 3 at Position(xpos=300,ypos=787)
            show player_sitting 1 at right
            with dissolve
            june "Belo quarto!"
            june "Adorei seus posters e figurinhas!"
            show june_sitting 4
            show player_sitting 2
            player_name "Ha ha, pois é, são legais."
            player_name "Tenho eles desde criança."
            player_name "Eles são bem... nerds, eu acho."
            show june_sitting 3
            show player_sitting 1
            june "Gostei muito deles!"
            show june_sitting 4
            show player_sitting 2
            player_name "Valeu."
            show june_sitting 3
            show player_sitting 1
            june "Então... o que vamos fazer?"
            show june_sitting 4
        else:

            show player_sitting 2 zorder 1 at right
            show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
            with fastdissolve
            player_name "Então, qual o plano?"
            show june_sitting 10
            show player_sitting 1
            june "Sua porta está trancada?"
            show player_sitting 2
            show june_sitting 11
            player_name "Claro. Acho que minha mãe não vai nos incomodar."
            show june_sitting 10
            june "Legal."
            show player_sitting 1
            show june_sitting 12
            june "Eu... eu gosto de estar no seu quarto..."
            show player_sitting 3
            june "É tão... aconchegante. Sinto que podemos fazer o que quiser em segredo..."
            show player_sitting 4
            show june_sitting 13
            player_name "Eu também gosto."
            show player_sitting 1
            show june_sitting 10
            june "Então, o que o meu... chefe que de mim hoje?"
            show june_sitting 11
        menu:
            "Sexo!" if June.over(june_cosplay):
                show player_sitting 2 zorder 1 at right
                show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
                player_name "Você quer... transar?"
                show player_sitting 1
                show june_sitting 10
                june "Eu deveria por meu cosplay?"
                show player_sitting 4
                show june_sitting 11
                player_name "Hummm, talvez outra hora?"
                show player_sitting 3
                show june_sitting 12
                june "Ok... Acho que podemos fazer assim."
                show player_sitting 4
                show june_sitting 13
                player_name "Você não sei importa?"
                show player_sitting 3
                show june_sitting 10
                june "Se fantasiar é divertido, mas claro, tudo bem..."
                show june_sitting 14 at Position(xoffset=7) with fastdissolve
                pause
                show june_sitting 15 with fastdissolve
                pause
                show june_sitting 16 at Position(xpos=288) with fastdissolve
                pause
                hide june_sitting_underwear
                show june_sitting 23
                with fastdissolve
                pause
                show june_sitting 24 with fastdissolve
                pause
                show june_sitting 25 at Position(xoffset=40) with fastdissolve
                june "Então? O que você está esperando? Estou aqui..."
                show june_sitting 30 at center
                hide player_sitting
                with fastdissolve
                pause
                jump june_normal_sex

            "Sexo com cosplay!" if June.over(june_cosplay):
                show player_sitting 6 at right
                show june_sitting 11 zorder 1 at Position(xpos=300,ypos=787)
                player_name "Posso te ajudar a se vestir igual da última vez... e ser seu chefe?"
                show player_sitting 3
                show june_sitting 10
                june "Eu estava esperando você sugerir isso!"
                june "Tudo o que eu queria era me fantasiar e ser sua orcette..."
                june "Ok, vou por a roupa..."
                show june_sitting 29
                with fade
                june "Por que você não vem mais perto... e me beija, chefe?"
                hide player_sitting
                show june_sitting 31 at center
                with fastdissolve
                pause
                jump june_cosplay_sex
            "Jogar.":

                if June.over(june_cosplay):
                    show june_sitting 11 at Position(xpos=300,ypos=787)
                    show player_sitting 2 at right
                    player_name "Você quer jogar?"
                    show june_sitting 10
                    show player_sitting 1
                    june "Claro, tem umas missões que ainda não terminamos no Orc Bork."
                    show june_sitting 11
                    show player_sitting 6
                    player_name "Então vamos lá!"
                    show player_sitting 2
                    player_name "Só mais uma coisa, poderia me lembrar como que joga mesmo?"
                    show june_sitting 10
                    show player_sitting 1
                    june "Ha ha."
                    june "Claro, chega mais perto e assim você pode ver a tela..."
                    show june_sitting 7 at center
                    hide player_sitting
                    with fastdissolve
                    june "Temos que jogar juntos e atacarmos juntos."
                    june "Quando a flecha estiver na área verde, ataque!"
                    show june_sitting 8
                    player_name "Oh, ok! Parece fácil."
                    show june_sitting 7
                    june "Vamos tentar!"
                else:

                    show june_sitting 4 at Position(xpos=300,ypos=787)
                    show player_sitting 2 at right
                    player_name "Pdemos tentar zerar o jogo."
                    show june_sitting 3
                    show player_sitting 1
                    june "Sério? Você quer?"
                    show june_sitting 4
                    show player_sitting 6
                    player_name "Claro!"
                    show player_sitting 2
                    player_name "Só uma coisa, poderia me ensinar a jogar?"
                    show june_sitting 3
                    show player_sitting 1
                    june "Ha ha."
                    june "Bom, é um jogo de caçar bichos."
                    june "Você vai por dungeons, mata monstros, pega itens..."
                    show player_sitting 5
                    june "... Mas aí está o chefão final que eu estou tentando matar há um bom tempo!!"
                    show player_sitting 1
                    june "Aqui, vem mais perto para que você possa ver a tela..."
                    show june_sitting 8 at center
                    hide player_sitting
                    with fastdissolve
                    player_name "Ok, e como matamos o chefão?"
                    show june_sitting 7
                    june "Temos que jogar juntos e atacarmos na mesma hora."
                    june "Quando a flecha chegar na área verde, nós atacamos!"
                    show june_sitting 8
                    player_name "Ah, ok! Parece bem fácil."
                    show june_sitting 7
                    june "Vamos tentar!"
                jump orc_battle_prep
            "Tenho que dormir.":

                show player_sitting 4 at right
                show june_sitting 6 at Position(xpos=300,ypos=787)
                player_name "Na verdade, tenho que ir pra cama..."
                show june_sitting 5
                show player_sitting 3
                june "Já?!"
                show june_sitting 6
                show player_sitting 4
                player_name "Sim... Minha mãe disse que eu tenho que acordar cedo amanhã."
                player_name "Desculpa, {b}June{/b}..."
                show june_sitting 5
                show player_sitting 3
                june "Tudo bem, eu acho."
                june "Talvez pudessemos sair outra hora?"
                show june_sitting 6
                show player_sitting 4
                player_name "Claro!"
                show june_sitting 4
                player_name "Eu adoraria."
                show june_sitting 3
                show player_sitting 3
                june "Ok, te vejo na escola então?"
                show june_sitting 4
                show player_sitting 4
                player_name "Claro!"
                hide june_sitting
                hide player_sitting
                with dissolve
                jump sleeping
    $ callScreen(location_count)

label june_normal_sex:
    show junesex 2
    hide june_sitting
    hide player_sitting
    with fade
    june "Quero esse seu pauzão..."
    june "... dentro de mim!"
    show junesex 3 with fastdissolve
    june "Ahh..."
    show junesex 4 with fastdissolve
    june "Siiim!"
    june "Me fode, {b}[firstname]{/b}!!"
    $ anim_toggle = False
    $ xray = False
    $ M_june.set('sex speed', .3)

    label june_mcbedroom_normal_sex_loop:
        hide screen june_mcbedroom_normal_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            show junesex 4_5_6_7_8
            pause 8
        else:

            $ animcounter = 0
            while animcounter < 3:
                show junesex 4
                pause
                show junesex 5
                pause
                show junesex 6
                pause
                show junesex 7
                pause
                show junesex 8
                pause
                $ animcounter += 1

    show screen june_mcbedroom_normal_sex_options
    pause
    jump june_mcbedroom_normal_sex_loop

    label june_mcbedroom_normal_sex_cum_inside:
        hide screen june_mcbedroom_normal_sex_options
        show junesex 4_5_6_7_8
        pause
        show junesex 9 with hpunch
        june "Ahh!!!"
        show white
        pause 0.3
        hide white with dissolve
        pause
        show junesex 14 with fastdissolve
        june "Eu... eu adoro isso..."
        june "... sua porra dentro de mim..."
        jump june_aftercum_inside

    label june_mcbedroom_normal_sex_cum_outside:
        hide screen june_mcbedroom_normal_sex_options
        show junesex 4_5_6_7_8
        pause
        show junesex 9 with hpunch
        player_name "Ahh!!!"
        show white
        pause 0.3
        show junesex 10
        hide white with dissolve
        pause
        show junesex 11 with fastdissolve
        june "..."
        show junesex 12
        june "Quanta..."
        june "Achei que você fosse gozar dentro de mim..."
        june "... com toda essa porra..."
        june "Talvez na próxima?"
        jump june_aftercum_outside

label june_aftercum_outside:
    hide junesex
    scene black
    with fade
    scene bedroom_sex2
    show player_sitting 3 zorder 1 at right
    show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
    hide junesex
    with fade
    june "Foi ótimo!"
    june "Está ficando tarde... Tenho que ir."
    show player_sitting 6
    show june_sitting 11
    player_name "Sim, minha mãe vai suspeitar se ficarmos muito tempo aqui..."
    show june_sitting 10
    show player_sitting 3
    june "Ha ha."
    june "Acho que foi um tempo bem gasto!"
    show june_sitting 11
    show player_sitting 4
    player_name "Eu me diverti também."
    show june_sitting 10
    show player_sitting 3
    june "Talvez pudessemos fazer de novo outro dia?"
    show june_sitting 11
    show player_sitting 4
    player_name "Claro!"
    show player_sitting 6
    player_name "Eu adoraria."
    show june_sitting 10
    show player_sitting 3
    june "Ok, te vejo na escola então?"
    show june_sitting 11
    show player_sitting 4
    player_name "Claro!"
    $ callScreen(location_count)

label june_aftercum_inside:
    hide junesex
    scene black
    with fade
    scene bedroom_sex2
    show player_sitting 3 zorder 1 at right
    show june_sitting 10 zorder 1 at Position(xpos=300,ypos=787)
    hide junesex
    with fade
    june "Foi ótimo!"
    june "Está ficando tarde... Tenho que ir."
    show player_sitting 6
    show june_sitting 11
    player_name "Sim, minha mãe vai suspeitar se ficarmos muito tempo aqui..."
    show june_sitting 10
    show player_sitting 3
    june "Ha ha."
    june "Acho que foi um tempo bem gasto!"
    show june_sitting 11
    show player_sitting 4
    player_name "Me diverti também."
    show june_sitting 13
    show player_sitting 4
    player_name "Hey, uh, sobre fazer isso dentro..."
    show june_sitting 12
    show player_sitting 5
    june "Oh, não se preocupe, eu vou tomar uma pílula."
    show june_sitting 11
    show player_sitting 4
    player_name "Isso significa que podemos fazer?"
    show june_sitting 10
    show player_sitting 3
    june "Depende... Você quer?"
    show player_sitting 6
    show june_sitting 11
    player_name "Adoraria."
    show june_sitting 10
    show player_sitting 3
    june "Ok, te vejo na escola então?"
    show june_sitting 11
    show player_sitting 4
    player_name "Claro!"
    $ callScreen(location_count)

label bedroom_study01:
    if homework not in inventory.items and homework2 not in inventory.items and homework_done == False:
        scene expression gTimer.image(tmp_image)
        show player 1 with dissolve
        player_name "( Não tenho mais tarefa. )"
        hide player with dissolve
        $ callScreen(location_count)

    elif homework_done == True:
        scene expression gTimer.image(tmp_image)
        show player 1 with dissolve
        player_name "( Já fiz minha tarefa. )"
        hide player with dissolve
        $ callScreen(location_count)
    else:



        scene expression gTimer.image("bedroom{}")
        if not gTimer.is_dark():
            scene studybedroom01 with dissolve
            show text "Eu fiquei uma boa parte o dia lendo os livros para fazer a tarefa da {b}Sra. Bissette{/b}." at Position (xpos= 512, ypos = 700) with dissolve
        else:
            scene studybedroom02 with dissolve
            show text "Fiquei a noite toda lendo os livros para fazer a tarefa da {b}Sra. Bissette{/b}.\nAgora eu posso ir dormir..." at Position (xpos= 512, ypos = 700) with dissolve
        $ renpy.pause ()
        hide text with dissolve
        hide studybedroom01
        hide studybedroom02
        scene black
        with dissolve
        show unlock20 at truecenter with dissolve
        $ renpy.pause()
        hide unlock20 with dissolve
        if homework in inventory.items:
            $ inventory.items.remove(homework)
            $ inventory.items.append(homework1)
        elif homework2 in inventory.items:
            $ inventory.items.remove(homework2)
            $ inventory.items.append(homework1)
        $ homework_done = True
        $ gTimer.tick()
        $ callScreen(location_count)

label mia_midnight_text:
    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom"
    scene expression gTimer.image(tmp_image)
    show player 442 with dissolve
    player_name "{b}Mia{/b}!? Pedindo...por ajuda?"
    player_name "Por quê?"
    player_name "Ela está em perigo?"
    show player 443
    player_name "..."
    show player 442
    player_name "Talvez eu devesse {b}ir ver ela agora{/b}... Só pra ter certeza que ela esteja bem."
    hide player with dissolve
    $ unlock_ui()
    $ M_mia.trigger(T_mia_message)
    $ callScreen(location_count)

label mia_urgent_text:
    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom"
    scene expression gTimer.image(tmp_image)
    show player 10 with dissolve
    player_name "Ela não consegue achar o pai dela?"
    player_name "Melhor eu ir ver o que está acontecendo..."
    hide player with dissolve
    $ unlock_ui()
    $ M_mia.trigger(T_mia_message)
    $ callScreen(location_count)

label textbook_missing_dialogue:
    if MC_computer_broken:
        $ tmp_image = "bedroom_broken{}"
    else:
        $ tmp_image = "bedroom"
    scene expression gTimer.image(tmp_image)
    show player 73 with dissolve
    player_name "( Tenho que pegar os {b}livros{/b} antes de começar minha {b}tarefa{/b}... )"
    player_name "( Eu devo achar os livros na {b}biblioteca{/b}. )"
    hide player with dissolve
    $ callScreen(location_count)

label bed_locked:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Ainda tenho que fazer algo antes de dormir... )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label bedroom_check_on_mom:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show player 10 with dissolve
    player_name "( Eu deveria ir dar uma olhada na {b}[mom_name]{/b}... )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label sleeping:
    if not gTimer.is_night() and (M_player.is_set("jerk mom") or M_player.is_set("jerk mia")):
        if MC_computer_broken:
            scene expression gTimer.image("backgrounds/location_bedroom_broken{}.jpg")
        else:
            scene expression gTimer.image("backgrounds/location_bedroom{}.jpg")
        menu:
            "Masturbar.":
                menu:
                    "Mamãe." if M_player.is_set("jerk mom"):
                        $ M_player.set("sex speed", .4)
                        scene expression gTimer.image("backgrounds/location_bedroom_jerk{}.jpg")
                        show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
                        pause
                        show player 496b
                        player_name "... Mamãe é tão bonita."
                        player_name "Não consigo parar de pensar nela."
                        player_name "... sobre ela."
                        player_name "Mmm, caralho, eu quero tanto ela!"
                        show player 496c
                        show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
                        pause
                        show momd 1 zorder 2 at Position(xpos=0.735, ypos=0.85) with dissolve
                        pause
                        show momd 2
                        mom "Bom, olá..."
                        show momd 1
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        show momd 2
                        mom "Oh, Deus... É pra mim?"
                        mom "... É tão grande!"
                        show momd 1
                        pause
                        show momd 2
                        mom "... e grosso."
                        show momd 3 with dissolve
                        mom "Mmm, você vai me dar isso?"
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        mom "Me dê, [firstname]!"
                        $ M_mom.set("sex speed", M_mom.get("sex speed") / 1)
                        show momd 4_5
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        pause
                        show player 496f
                        player_name "OH!"
                        show player 496g with flash
                        player_name "HHHNNNGGGG, HHuuuUUHH!!"
                        show player 496h
                        hide jerkbubble
                        hide momd
                        player_name "Haaaah... Haaaah..."
                        player_name "Uuuhh cara, estou todo sujo..."

                    "Mia." if M_player.is_set("jerk mia"):
                        $ M_player.set("sex speed", .4)
                        scene expression gTimer.image("backgrounds/location_bedroom_jerk{}.jpg")
                        show player 496 zorder 0 at Position(xpos=0.3375, ypos=0.875)
                        pause
                        show player 496b
                        player_name "Mia é tão fofa!"
                        player_name "Mal posso esperar pra ver ela de novo..."
                        pause
                        player_name "... Aquele corpo fofo dela."
                        player_name "Mmm..."
                        show player 496c
                        show jerkbubble zorder 1 at Position(xpos=0.6, ypos=1.0) with dissolve
                        pause
                        show miad 1 zorder 2 at Position(xpos=0.735, ypos=0.8) with dissolve
                        pause
                        show miad 2
                        mom "Eae, [firstname]!"
                        show miad 1
                        pause
                        show miad 2
                        mia "Wow, eu nunca tinha visto um desses antes!"
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        mia "Todos são assim tão grande?!"
                        show miad 1
                        pause
                        show miad 2
                        mia "Eu queria que você fosse o meu primeiro, [firstname]."
                        show miad 1
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        pause
                        show miad 2
                        mia "Você acha que cabe?"
                        mia "... na minha..."
                        show miad 1
                        $ M_player.set("sex speed", M_player.get("sex speed") / 2)
                        show player 496c_496d_496e_496d_496c
                        pause
                        show miad 2
                        mia "...na minha buceta?"
                        show player 496f
                        player_name "OH!"
                        show player 496g with flash
                        player_name "HHHNNNGGGG, HHuuuUUHH!!"
                        show player 496h
                        hide jerkbubble
                        hide miad
                        player_name "Haaaah... Haaaah..."
                        player_name "Uuuhh cara, estou todo sujo..."

                scene black with fade
                $ gTimer.tick()
                $ callScreen(location_count)
            "Dormir.":

                $ pass

    if M_mom.get_state() in [S_mom_movie_night, S_mom_movie_night_two]:
        if MC_computer_broken:
            scene expression gTimer.image("bedroom_broken{}")
        else:
            scene expression gTimer.image("bedroom{}")
        show player 101b with dissolve
        player_name "Acho que ouvi a {b}[mom_name]{/b} fazendo algo lá em baixo."
        hide player with dissolve
        $ gTimer.tick(3)
        $ lock_ui()
        $ callScreen(location_count)

    elif M_mom.get_state() == S_mom_sleepover:
        if MC_computer_broken:
            scene expression gTimer.image("bedroom_broken{}")
        else:
            scene expression gTimer.image("bedroom{}")
        show player 101b with dissolve
        player_name "Talvez eu devesse ir dormimr com a {b}[mom_name]{/b} hoje a noite."
        player_name "Ela disse que eu podia visitar ela se eu quisesse..."
        hide player with dissolve
        $ callScreen(location_count)

    elif M_mom.is_set("room sneak"):
        jump mom_sleepover

    if erik.over(erik_breastfeeding_2) and not erik.over(erik_thief) and randomizer() > 66:
        if erik.in_progress(erik_thief):
            $ erik_thief.unfinish()
            $ unlock_ui()
        else:

            if not erik.known(erik_thief):
                $ erik.add_event(erik_thief)
            scene location_bedroom_cutscene01 with fade
            pause
            "{b}*Thump*{/b}"
            scene bedroom_cs03 with dissolve
            "{b}*Thump Thump*{/b}"
            player_name "..."
            scene bedroom_cs04 with dissolve
            player_name "Que barulho é esse?"
            scene bedroom_night with fade
            show player 101bf
            player_name "( Parece que está vindo de fora. )"
            player_name "( ... Do quintal do {b}Erik{/b} talvez? )"
            show player 100bf
            menu:
                "Voltar a dormir.":
                    show player 101f
                    player_name "( Deve ser algum bicho. )"
                    player_name "( Preciso voltar a dormir... )"
                    hide player
                "Usar o telescópio.":

                    show player 101bf
                    player_name "( Eu deveria dar uma olhada. )"
                    show player 100f
                    player_name "Hmm..."
                    show player 101bf
                    player_name "( Vou dar uma rápida olhada no meu telescópio. )"
                    hide player

                    scene windowbackyardnight02a
                    player_name "!?!"
                    player_name "Mas que..."
                    scene windowbackyardnight02b
                    player_name "( Tem alguém no quintar do {b}Erik{/b}?! )"
                    player_name "( Esse é o {b}ladrão{/b} que eu vi no jornal! )"
                    scene windowbackyardnight02c
                    player_name "..."
                    player_name "( Ele está indo para a casa do {b}Erik{/b}?! )"

                    scene bedroom_night with fade
                    show player 101bf with dissolve
                    player_name "( Isso é ruim! )"
                    player_name "( E se {b}Erik{/b} e sua mãe estão em perigo? )"
                    player_name "( Eu deveria ir lá ver o que está acontecendo no quintal do {b}Erik{/b}. )"
                    hide player with dissolve
                    $ gTimer.tick(4)
                    $ erik_thief.finish()
                    $ lock_ui()
                    scene black with fade
                    jump erik_house_dialogue

    elif erik.started(erik_bullying_3):
        scene bedroom_night
        show player 12 with dissolve
        player_name "( Cara... Que dia. )"
        show player 17
        player_name "( Acho que o treino na academia está valendo a pena! )"
        pause
        show player 12
        player_name "( {b}Dexter{/b} nunca mais vai fazer isso. )"
        player_name "(... Preciso treinar muito! )"
        show player 8 with dissolve
        pause
        show player 7 with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 101 with dissolve
        player_name "( Eu deveria tirar um cochilo. )"
        hide player with dissolve
        $ erik_bullying_3.finish()

    elif M_mia.get_state() == S_mia_midnight_call:
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        "{b}Bzzt{/b}!"
        player_name "..."
        "{b}Bzzzzzzt{/b}!"
        scene bedroom_cs04 with dissolve
        player_name "Huh?"
        player_name "É meu celular?"
        scene black with fade
        pause
        scene bedroom_night
        show player 7 with dissolve
        pause
        show player 101
        player_name "Alguém está me mandando uma mensagem?"
        player_name "Eu deveria ver quem é..."
        hide player with dissolve
        $ lock_ui()
        $ gTimer.tick(4)
        if m_mia01 not in message_list:
            $ message_list.append(m_mia01)
            $ new_message = True
        $ callScreen(location_count)

    elif M_mom.get_state() == S_mom_solo_dream:
        scene dream_mom_04 with fade:
            ypos -707
            linear 4.0 ypos 0
        mom "Mmm..."
        mom "Oh, isso é maravilhoso, querido."
        player_name "..."
        player_name "Oh, {b}[mom_name]{/b}..."
        mom "Eu quero você, {b}[firstname]{/b}!"
        mom "Eu quero você todo dentro de mim!"
        player_name "*gulp*"
        player_name "Sério?"
        mom "Siiiim, por favor, querido. Ponha tudo dentro da mamãe..."
        mom "Eu preciso desse pauzão dentro de mim!"
        player_name "..."
        mom "Me beije, querido. Não aguento mais!!"
        scene dream_mom_05 with dissolve:
            ypos 0
        pause
        player_name "Hnnggg!!" with flash
        pause
        scene dream_mom_05 with flash:
            ypos 0
            linear 4.0 ypos -475
        player_name "... Oooooh..."
        pause

        scene location_bedroom_cutscene06 with fade
        pause
        scene location_bedroom_cutscene07
        player_name "..."
        scene location_bedroom_cutscene08
        player_name "Oh cara..."
        pause
        scene location_bedroom_cutscene09
        pause
        player_name "Fiz uma bagunça..."
        player_name ".. Mas caralho, isso foi intenso..."
        player_name "Parecia tão real!"
        player_name "Arrgghh!"
        player_name "Não consigo parar de pensar nela!"
        player_name "Eu quero falar isso pra ela e beijar ela..."
        player_name "Talvez eu devesse tentar {b}falar com a [mom_name] sobre beijo{/b}?"
        player_name "Ela parecia ter gostado quando eu beijei ela no shopping..."
        player_name "Hmm, é arriscado, mas acho que vale a tentativa!"
        player_name "Eu vou enlouquecer se não fizer nada..."
        player_name "... Tenho que me limpar antes de ir dormir."
        $ M_mom.trigger(T_mom_dream)

    elif M_mom.get_state() == S_mom_night_visit:
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        scene location_bedroom_cutscene02 with dissolve
        mom "..."
        mom "( Não consigo dormir. )"
        mom "( Desde que vi ela se masturbar... )"
        mom "( Não consigo para de pensar na- )"
        mom "( Eu só... )"
        mom "( Eu singo que estou muito perto dele... )"
        define fadehold = Fade(0.5, 1.0, 0.5)

        scene location_bedroom_sex01
        show moms 1
        with dissolve
        mom "( Meu bebê lindo. )"
        mom "( Sempre aqui para mim. )"
        mom "( ... Sempre nos meus pensamentos... )"
        show moms 2
        mom "..."
        mom "( Não consigo parar de pensar no seu... )"
        mom "( Corpo... e no jeito que ele me olha... )"
        show moms 3
        mom "( Eu só quero ver ele... )"
        show moms 4
        mom "Hmm..."
        show moms 5
        mom "( Aqui. Deve estar quente aí em baixo. )"
        show moms 6
        mom "( E isso... Acho que se eu tocar... )"
        show moms 7_8
        pause 4
        show moms 6
        mom "( Isso fica maior... )"
        show moms 7_8
        mom "( E mais duro! )"
        mom "..."
        mom "( Quero ver isso... )"
        show moms 9
        $ renpy.pause()
        show moms 10
        mom "( É tão apertado aqui... )"
        show moms 11
        mom "!!!"
        show moms 12
        mom "..."
        mom "( Esse negócio é tão... bonito... )"
        mom "( E grande! )"
        mom "( Não acredito o tanto que ele cresceu. )"
        mom "( ... )"
        mom "( Faz tanto tempo que não vejo um... )"
        mom "( E eu sinto muita falta... )"
        mom "( Deve estar tudo bem se eu tocar... )"
        mom "( Como sua mãe, tenho que chegar se está tudo...normal... )"
        show moms 13
        pause
        show moms 14
        pause
        mom "( É tão quente. )"
        mom "( E macio... )"
        show moms 13
        mom "..."
        show moms 13_14
        pause
        mom "( O que...estou fazendo...)"
        mom "..."
        mom "( Uma mãe não deveria desejar o pau do filho... )"
        mom "( Mas... )"
        mom "( Eu já deixei ele se masturbar pro meu corpo... )"
        pause
        mom "( Ele ficou tão tímido quando eu vi ele se mastrubando...o jeito que ele gozou...)"
        mom "..."
        mom "( Isso cabeira- )"
        show moms 12
        mom "( Controle-se... )"
        show moms 20
        mom "( Mas eu preciso isso...)"
        show moms 21
        mom "( Não. )"
        mom "( ...Eu preciso sair... )"
        show moms 22 at Position(xpos = 544, ypos = 768)
        player_name "Huh...?"
        show moms 23
        player_name "Hmm..."
        player_name "( O que foi? )"
        show moms 24 at Position(xpos = 512, ypos = 768)
        player_name "( Esqueça )"
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.get_state() == S_mom_night_visit_two:
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        scene location_bedroom_cutscene02 with dissolve
        pause
        scene location_bedroom_sex01
        show moms 1
        with dissolve
        mom "( Eu não devia estar aqui... )"
        mom "( ... Mas eu não consigo parar de pensar no pau dele! )"
        mom "( Meu bebê... )"
        show moms 2
        mom "..."
        mom "( Talvezl Diane esteja certa; Talvez eu devesse relaxar e deixa acontecer. )"
        mom "( O jeito que ele me olha com esses olhos famintos... )"
        mom "( Mmm, eu fico molhada só de pensar... )"
        show moms 3
        mom "( Tenho que ver isso! )"
        show moms 4
        mom "Hmm..."
        show moms 5
        mom "( Ooh, isso é errado... O que você está fazendo, [mom]? )"
        show moms 6
        mom "( É maior do que eu me lembro... )"
        show moms 7_8
        pause 4
        show moms 6
        mom "( Mmm e está ficando duro... )"
        show moms 7_8
        mom "( Tãããão {b}duro{/b}! )"
        mom "..."
        mom "( ... Talvez eu pudesse pegar um pouco... )"
        show moms 9
        $ renpy.pause()
        show moms 10
        mom "( ... Digo, isso pode ser desconfortável para ele. )"
        mom "( Só vou deixar ele relaxar... É isso. )"
        show moms 11
        mom "!!!"
        show moms 12
        mom "..."
        mom "( Oh meu deus! )"
        mom "( Oooh! )"
        show moms 13
        mom "( É tão macio e quente... )"
        mom "( E é tão bom sentir na minha mão... )"
        show moms 13_14
        mom "( Tão grosso... )"
        mom "( ... e excitante. )"
        mom "..."
        mom "( Faz muito tempo... )"
        mom "( E eu quero... )"
        mom "( Eu quero experimentar isso. )"
        show moms 15
        mom "( Eu {b}PRECISO{/b} provar isso! )"
        mom "( Só por um segundo! Isso não vai doer, né? )"
        show moms 16_17
        mom "( Hmmmm!! )"
        mom "( Oh meu Deus, eu senti tanta falta isso! )"
        mom "( Mmm, estou tão molhada... )"
        show moms 18
        player_name "{b}*Moan*{/b}"
        show moms 19
        mom "!!!" with hpunch
        mom "( Oh merda! Ele está acordando... )"
        mom "..."
        show moms 20
        mom "( O que eu fiz! )"
        mom "( Ele não pode me ver assim! )"
        show moms 21
        mom "( Tenho que sair daqui! )"
        show moms 22 at Position(xpos = 544, ypos = 768)
        player_name "Huh...?"
        show moms 23
        player_name "Hmm..."
        player_name "( O que é isso? )"
        show moms 24 at Position(xpos = 512, ypos = 768)
        player_name "( ... )"
        player_name "( Acho que não é nada... )"
        $ M_mom.trigger(T_mom_midnight_fun)

    elif M_mom.get_state() == S_mom_midnight_noises:
        scene bedroom_cs01 with fade
        "Ha ha ha..."
        "{b}*SPLASH*{/b}"
        scene bedroom_cs03 with dissolve
        player_name "..."
        scene bedroom_cs04
        player_name "Quem está fazeno tanto barulho assim?"
        scene bedroom_cs03
        player_name "..."
        player_name "......"
        scene bedroom_cs01 with dissolve
        pause
        "{b}*SPLASH*{/b}"
        scene bedroom_cs04 with dissolve
        player_name "O que está acontecendo?"

        scene bedroom_night
        show player 101b
        with dissolve
        player_name "Talvez, eu deveria ver o que está acontecendo."
        player_name "Parece que quem está lá fora não vai parar."
        show player 8 with dissolve
        $ M_mom.trigger(T_mom_midnight_wakeup)
        $ gTimer.tick(4)
        $ lock_ui()
        $ callScreen(location_count)

    elif M_mom.get_state() == S_mom_night_visit_three:
        $ M_mom.set('sex speed', .175 / .75)
        scene location_bedroom_cutscene01 with dissolve
        player_name "Zzz..."
        scene location_bedroom_cutscene02 with dissolve
        pause
        scene location_bedroom_sex01
        show moms 1
        with dissolve
        mom "( Oh... )"
        mom "( Estou aqui... )"
        show moms 3
        mom "( O que estou fazendo! )"
        show moms 4
        mom "( O QUE ESTOU FAZENDO!!! )"
        show moms 5
        mom "( Mmm! )"
        mom "( Aí está! )"
        show moms 6
        mom "( Ooh, eu quero tanto isso... )"
        show moms 7_8
        mom "( Fique duro pra mim, querido... )"
        mom "( Fique duro para sua {b}mamãe{/b}. )"
        show moms 6
        pause
        show moms 9
        pause
        show moms 10
        mom "( ... )"
        show moms 11
        mom "!!!"
        show moms 12
        mom "..."
        mom "( Oh, estou louca de tesão... preciso isso!!! )"
        show moms 15
        mom "( Mmm. )"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / .75)
        show moms 16_17
        mom "( Oh! )"
        mom "( É tão gostoso! )"
        player_name "( Mmm )"
        mom "*slurp*"
        show moms 19
        player_name "Hmm?"
        show moms 20b
        player_name "O que- ?"
        show moms 20c at Position(xpos=0.53, ypos=1.0) with dissolve
        player_name "... {b}[mom_name]{/b}?"
        show moms 20d
        mom "Está tudo bem, {b}[firstname]{/b}, sou eu."
        show moms 20c
        player_name "... Ok."
        player_name "Mas o que está-"
        show moms 20d
        mom "Shhh..."
        show moms 20c
        player_name "{b}[mom_name]{/b}? O que você-"
        show moms 20e with dissolve
        mom "Silêncio, querido, relaxe..."
        player_name "..."


        mom "Oh, eu preciso disso, {b}[firstname]{/b}!"
        mom "Eu preciso disso dentro de mim!!!"
        show moms 20f at Position(xpos=0.5, ypos=1.0) with dissolve
        player_name "*gulp*"
        mom "Eu tentei..."
        mom "Eu tentei me conter."
        mom "... mas não pude!"
        show moms 20g with dissolve
        mom "Por favor, não me leve a mal..."
        pause
        show moms 20h with hpunch

        player_name "... Ooohh!!"
        mom "Haaaaaaaah!"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / 1.75)
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "Oh Deus!!"
        pause
        mom "Oh, é mais gostoso do que eu imaginava!"
        player_name "Oh, {b}[mom_name]{/b} this feels so good!"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / 2)
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "Haah! [firstname]! Oh, [firstname]!"
        mom "Eu vou gozar!"
        show moms 20h with flash
        mom "AAHHH!!"

        player_name "Você está bem, {b}[mom_name]{/b}?"
        mom "Haaah... Haaaah..."
        mom "... Não se preocupe, querido."
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "Continue! Caralho, isso é tão bom!"
        player_name "..."
        mom "Continua!!"
        $ M_mom.set('sex speed', M_mom.get('sex speed') / 1.5)
        show moms 20h_20i_20j_20k_20l_20m_20n_20o
        mom "OOOHH!!!"
        mom "Isso, querido!!"
        mom "Deixe a mamãe cavalgar nesse pauzão!!"
        $ keep_going = 0
        $ M_mom.set("change angle", False)
        label night_visit_loop:
            menu:
                "Continuar." if keep_going < 2:
                    $ keep_going += 1
                    if M_mom.get("change angle"):
                        show moms 170_171_172_173_174_175_176_177
                    else:

                        show moms 20h_20i_20j_20k_20l_20m_20n_20o
                    pause
                    jump night_visit_loop

                "Mudar de posição." if keep_going < 2:
                    $ keep_going += 1
                    if not M_mom.get("change angle"):
                        $ M_mom.set('sex speed', .15)
                        $ M_mom.set("change angle", True)
                        hide moms
                        scene bedroom_sex_05
                        show moms 170_171_172_173_174_175_176_177
                        with fade
                    else:

                        $ M_mom.set('sex speed', ((.175 / .75) / 3) / 1.5)
                        $ M_mom.set("change angle", False)
                        hide moms
                        scene location_bedroom_sex01
                        show moms 20h_20i_20j_20k_20l_20m_20n_20o
                        with fade
                    pause
                    jump night_visit_loop
                "Gozar.":

                    player_name "Oh, {b}[mom_name]{/b}... Eu sou..."
                    player_name "... I'm gonna!!"
                    mom "Não pare!! Não-"
                    $ M_mom.set('sex speed', M_mom.get('sex speed') / .075)
                    scene location_bedroom_sex01
                    show moms 20p_20q
                    with flash
                    player_name "HHNNGGG!!!!!"

                    mom "AAAAAAAAHHHH!!!"
                    pause
                    show moms 20h

                    player_name "*panting*"

                    mom "Mmm..."
                    show moms 20r with dissolve
                    mom "..."
                    show moms 20s with dissolve
                    mom "Oh céus..."
                    show moms 20t
                    player_name "Isso foi incrível!"
                    show moms 20s
                    mom "Hehe, foi mesmo..."
                    mom "..."
                    mom "Desculpa, querido!"
                    mom "Eu não devia ter feito isso..."
                    show moms 20t
                    player_name "O quê!? Não, não diga isso!"
                    mom "..."
                    player_name "Eu quis também!"
                    show moms 20s
                    mom "... Sério?"
                    show moms 20t
                    player_name "Você não tem noção! É praticamente tudo sobre o que eu pensava!"
                    show moms 20s
                    mom "... Sério?"
                    show moms 20t
                    player_name "Sim!"
                    player_name "Eu te amo, {b}[mom_name]{/b}!"
                    show moms 20s
                    mom "... Eu também te amo, Sweetie!"
                    mom "..."
                    mom "Eu nunca tive um orgasmo assim!!!"
                    show moms 20t
                    player_name "Sério?!"
                    show moms 20s
                    mom "Hehe, acho que sim..."
                    show moms 20t
                    player_name "Desculpa, eu não durei muito..."
                    show moms 20s
                    mom "Não, você foi bem, querido! Especialmente por ser sua primeira vez!"
                    show moms 20t
                    player_name "... Primeira vez?"
                    mom "..."
                    player_name "Podemos fazer isso de novo, {b}[mom_name]{/b}?"
                    show moms 20s
                    mom "Ah querido, tem certeza que você quer isso?"
                    show moms 20t
                    player_name "Claro!!!"
                    player_name "[mom_name], eu não quero nada mais!"
                    show moms 20s
                    mom "Oh céus..."
                    mom "Eu não queria admitir mas eu sinto o mesmo!"
                    mom "..."
                    mom "Certo, querido..."
                    mom "... Mas só podemos ser safadinhos assim quando não tiver ninugém por perto!"
                    mom "Você não pode contar pra {b}NINGUÉM{/b}! Principalmente pra sua {b}irmã{/b}!"
                    mom "Entendido?!"
                    show moms 20t
                    player_name "Sim."
                    show moms 20s
                    mom "[firstname], é sério! Você não pode contar pra ninguém!"
                    show moms 20t
                    player_name "Não vou, {b}[mom_name]{/b}. Prometo."
                    show moms 20s
                    mom "Bom garoto."
                    mom "*yawn*"
                    mom "Ah, estou exausta agora."
                    show moms 20t
                    player_name "Eu também."
                    show moms 20s
                    mom "Mmm, eu poderia dormir aqui mesmo."
                    show moms 20t
                    player_name "Você pode, [mom_name]."
                    show moms 20s
                    mom "Acho que está tudo bem. Contanto que eu acorde antes que a sua [sis]."



                    scene location_bedroom_cutscene_sleep
                    with fade
                    show text "[mom_name] e eu finalmente dormimos juntos." at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    show text "Isso foi ótimo! Todas as nossas ansiedades reprimidas evaporaram em um instante!" at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    show text "Ela dormiu nos meus braços nessa noite..." at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    show text "... E eu acordei no outro dia me sentindo ótimo como nunca." at Position (xpos= 512, ypos= 700) with dissolve
                    pause
                    hide text
                    with dissolve


                    if M_player.is_set("pet cat"):
                        scene location_sleeping4 with fade
                    else:
                        scene location_sleeping2 with fade
                    show unlock11 at truecenter with dissolve
                    $ renpy.pause()
                    hide unlock11


                    scene location_bedroom_sex04
                    show moms 20u
                    pause
                    show moms 20v
                    player_name "[mom_name]?"
                    show moms 20u
                    player_name "..."
                    show moms 20v
                    player_name "[mom_name], acorda."
                    show moms 20u
                    mom "Hmm?"
                    show moms 20x
                    mom "*yawn* Já é de manhã?"
                    show moms 20w
                    player_name "Infelizmente."
                    show moms 20x
                    mom "Oh, dormi como um bebê..."
                    show moms 20w
                    player_name "Heh, é, eu também."
                    show moms 20x
                    mom "Hmm, certo. Acho que é bom sairmos antes da sua {b}irmã{/b} acorde."
                    show moms 20w
                    player_name "Certeza que não quer ficar um pouco mais?"
                    show moms 20x
                    mom "Hehe, não me provoque, querido. Esse seu pau é tão bom pra dizer não."
                    show moms 20w
                    player_name "Nunca vou ficar cansado de ouvir isso!"
                    show moms 20x
                    mom "Venha me ver mais tarde, ok?"
                    $ M_mom.trigger(T_mom_midnight_fun)
                    $ Sleep()
                    $ callScreen(location_count)
    else:
        if MC_computer_broken:
            show expression gTimer.image("bedroom_broken{}")
        else:
            show expression gTimer.image("bedroom{}")

    if M_player.is_set("pet cat"):
        scene location_sleeping3 with fade
    else:
        scene location_sleeping with fade
    show unlock11 at truecenter with dissolve
    $ renpy.pause()
    $ Sleep()
    hide unlock11
    hide bedroom
    hide bedroom_broken
    hide bedroom_night
    hide bedroom_broken_night
    scene black with fade
    hide sleeping with fade


    if M_mom.get_state() == S_mom_smith_dream:
        scene dreammom 1 at Position(ypos=1475) with fade
        mom "Oi, querido."
        mom "É a {b}mamãe{/b}..."
        player_name "{b}[mom_name]{/b}?"
        player_name "Onde estamos?"
        mom "Tudo bem, querido. Tudo ficará bem..."
        mom "{b}Mamãe{/b} vai cuidar e você..."
        scene dreammom 1_2:
            linear 5.0 ypos -707
        player_name "{b}[mom_name]{/b}..."
        player_name "O que você está fazendo..."
        mom "Tudo bem... {b}Mamãe{/b} quer que você se sinta bem..."
        player_name "{b}[mom_name]{/b}... Você está fazendo muito rápido..."
        scene dreammom 3
        player_name "!!!" with hpunch
        smi "{b}[firstname]{/b}!!!"
        scene dreammom 3:
            ypos -707
            linear 1.0 ypos 0
        smi "O que você está fazendo aqui???"
        smi "Você está... DORMINDO?!"

        smi "Vai para a aula AGORA ou eu te mando para a {b}DETENÇÃO{/b}!"
        scene black with fade
        pause .2
        if MC_computer_broken:
            scene bedroom_broken
        else:
            scene bedroom
        show player 264
        with dissolve
        player_name "{b}*Yawn*{/b}"
        show player 265 with dissolve
        player_name "!!!"
        show player 266
        player_name "( Eu estou tendo sonhos estranhos sobre a {b}[mom_name]{/b}! )"
        player_name "( Estamos fazendo coisas, e ela estava pelada! )"
        player_name "( Comigo! )"
        show player 267 with hpunch
        player_name "!!!"
        show player 268
        player_name "Isso é normal?!"
        player_name "( Eu nunca tive esses sonhos com a {b}[mom_name]{/b} antes... )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_dream)
    jump bedroom_dialogue

label mom_sleepover:
    $ M_mom.set('sex speed', .175)
    scene location_bedroom_sex01 with fade
    show moms 1
    player_name "( ... )"
    mom "Querido?"
    mom "Aww, você pegou no sono me esperando?"
    player_name "( ... )"
    show moms 3
    pause
    show moms 4
    pause
    show moms 5
    pause
    show moms 6
    mom "... Acorde, querido."
    $ M_mom.set('sex speed', M_mom.get('sex speed') / .75)
    show moms 7_8
    mom "Mmm..."
    show moms 6
    pause
    show moms 9
    pause
    show moms 10
    mom "( ... )"
    show moms 11
    mom "!!!"
    show moms 12
    pause
    show moms 20b
    mom "[firstname]?"
    player_name "... Hmm?"
    show moms 20c at Position(xpos=0.53, ypos=1.0) with dissolve
    player_name "... [mom_name]?"
    player_name "Merda, eu peguei no sono, não?"
    show moms 20d
    mom "Hehe, tudo bem, querido."
    show moms 20c
    player_name "Você ainda- ?"
    show moms 20e with dissolve
    mom "Não tão alto! Não queremos acordar {b}[sis]{/b}!"
    player_name "Oh! ... Sim, desculpa."
    show moms 20f at Position(xpos=0.5, ypos=1.0) with dissolve
    mom "Hehe..."
    mom "Tudo bem, você está animado. Mamãe também está!"
    mom "Mal posso esperar para que a {b}[sis]{/b} vá para cama."
    show moms 20g with dissolve
    player_name "Oh wow, {b}[mom_name]{/b}, você está ensopada!"
    mom "Eu disse que eu estava animada."
    show moms 20h with dissolve
    mom "Mmm..."
    mom "Agora, não vamos perder tempo... Dê isso para a mamãe!"
    $ M_mom.set('sex speed', M_mom.get('sex speed') / 3)
    show moms 20h_20i_20j_20k_20l_20m_20n_20o
    if randomizer() < 33:
        mom "Ahh!!!"
        mom "Oh {b}[firstname]{/b}, é tão fundo!"
        mom "Você gosta quando mamãe aperta você com sua buceta?"
        player_name "Oh céus, sim!"
        mom "Sim, querido!"
    elif randomizer() < 66:
        mom "Oh sim!!!"
        mom "Isso, querido! Come a buceta da mamaẽ!"
        mom "Mmm, você gosta?"
        player_name "Oh sim, {b}[mom_name]{/b}!"
        mom "Mais rápido, querido!"
    elif randomizer() < 100:
        mom "Oh céus, isso é ótimo!"
        mom "Quem é o menino safadinho da mamãe?"
        player_name "Mmm, Eu..."
        mom "Isso, querido! Come a mamãe com força!"
        player_name "Uuhh!! Você gosta desse pau duro, {b}[mom_name]{/b}?"
        mom "Aaahh!! Sim! Siiiiim! SIIIIIIM!!"
        mom "De esse paaaaau!"
    $ M_mom.set('sex speed', M_mom.get('sex speed') / 1.5)
    show moms 20h_20i_20j_20k_20l_20m_20n_20o
    pause
    $ M_mom.set("change angle", False)
    label mom_sleepover_options:
        menu:
            "Continuar.":
                if M_mom.get("change angle"):
                    show moms 170_171_172_173_174_175_176_177
                else:

                    show moms 20h_20i_20j_20k_20l_20m_20n_20o
                pause
                jump mom_sleepover_options
            "Mudar posição.":

                if not M_mom.get("change angle"):
                    $ M_mom.set('sex speed', .15)
                    $ M_mom.set("change angle", True)
                    hide moms
                    scene bedroom_sex_05
                    show moms 170_171_172_173_174_175_176_177
                    with fade
                else:

                    $ M_mom.set('sex speed', ((.175 / .75) / 3) / 1.5)
                    $ M_mom.set("change angle", False)
                    hide moms
                    scene location_bedroom_sex01
                    show moms 20h_20i_20j_20k_20l_20m_20n_20o
                    with fade
                pause
                jump mom_sleepover_options
            "Gozar.":

                player_name "... Oh!"
                player_name "[mom_name], eu vou..."
                mom "Vai, querido! Goza dentro de mim!"
                $ M_mom.set('sex speed', M_mom.get('sex speed') / .075)
                scene location_bedroom_sex01
                show moms 20p_20q
                with flash
                player_name "Uhhhuh!!!"
                mom "Hnnngg!!"
                mom "AAAAHHhh!!!"
                player_name "Shh! Você vai acordar a {b}[sis_name]{/b}!"
                player_name "..."
                show moms 20h with dissolve
                mom "Huhhh, huhhh, huhhh..."
                show moms 20r with dissolve
                pause
                show moms 20s with dissolve
                mom "Oh {b}[firstname]{/b}... Isso foi..."
                show moms 20t
                player_name "Surpreendente?"
                show moms 20s
                mom "Phew... Sim!"
                mom "Mmm, não consigo sentir minhas pernas."
                pause
                mom "Mmm... Amo você, {b}[firstname].{/b}"
                show moms 20t
                player_name "Também te amo, [mom_name]. Você é o melhor!"
                show moms 20s
                mom "Hah, valeu, querido."

    if M_player.is_set("pet cat"):
        scene location_sleeping4 with fade
    else:
        scene location_sleeping2 with fade
    show unlock11 at truecenter with dissolve
    $ renpy.pause()
    $ Sleep()
    hide unlock11
    $ M_player.set("just wokeup", False)

    if randomizer() < 70 and M_mom.get_state() != S_mom_note:
        scene location_bedroom_sex04
        show moms 20u
        pause
        show moms 20v
        player_name "Acorde, [mom_name]."
        show moms 20u
        mom "Mmm..."
        show moms 20w
        player_name "Já amanheceu."
        show moms 20x
        mom "Bom dia, querido."
        show moms 20w
        player_name "Você dormiu bem?"
        show moms 20x
        mom "... Você está brincando? Depois de ser comdia assim, eu dormi como nunca!"
        show moms 20w
        player_name "Heh, eu também..."
        mom "..."
        show moms 20x
        mom "Tenho que ir antes que a {b}[sis]{/b} acorde."
        show moms 20w
        player_name "Sim..."
        show moms 20x
        mom "Agradeço pela noite, {b}[firstname]{/b}! Eu te amo!"
        show moms 20w
        player_name "Também te amo, {b}[mom_name]{/b}!"
        hide moms with dissolve
    else:

        scene location_bedroom_blur
        show player 7
        pause
        show player 8
        pause
        show player 1
        player_name "..."
        show player 2
        player_name "Hmm, {b}[mom_name]{/b} deve ter me acordado antes de mim e saiu..."
        player_name "Phew, que noite! Eu dormi igual eu bebê..."
        if not M_mom.is_set("basement sex"):
            show player 10
            player_name "Hmm, o que é esse bilhete no meu computador?"
            player_name "... A [mom_name] deixou isso?"
            $ M_mom.trigger(T_mom_delay)
        hide player with dissolve
    $ callScreen(location_count)

label sleeping_locked:
    if MC_computer_broken:
        scene bedroom_broken
    else:
        scene bedroom
    show player 35 at left
    if not erik.over(erik_intro):
        player_name "( Não posso dormir agora. Tenho que ir para a escola antes que eu me atrase. )"
    $ callScreen(location_count)

label tired_bedroom_dialogue:
    if MC_computer_broken:
        scene bedroom_broken_night
    else:
        scene bedroom_night
    show player 55 with dissolve
    player_name "{b}*yawn*{/b}"
    show player 56
    player_name "( Muito cansado por isso... )"
    hide player 56
    $ callScreen(location_count)

label M6_note:
    if MC_computer_broken:
        scene bedroom_broken
    else:
        scene bedroom
    show momnote at Position (ypos=650) with dissolve
    pause
    hide momnote with dissolve
    show player 11 with dissolve
    player_name "( {b}[mom_name]{/b} quer ajuda com as roupas? )"
    player_name "( Deveria dar uma olhada no que ela quer. )"
    hide player with dissolve
    $ M_mom.trigger(T_mom_read_note)
    $ callScreen(location_count)

label player_room_lock:
    if MC_computer_broken:
        scene bedroom_broken
    else:
        scene bedroom
    show player 10 with dissolve
    player_name "( Deveria dar uma olhada o que tem está escrito no {b}bilhete{/b}. )"
    hide player 10 with dissolve
    $ callScreen(location_count)

label player_message_lock:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    if not gTimer.is_dark():
        show player 12 with dissolve
    else:
        show player 101 with dissolve
    player_name "Eu deveria ver minhas mensagens."
    $ callScreen(location_count)

label pet_cat:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show cat 14 with dissolve
    player_name "Oi, [cat]!"
    show cat 12
    if randomizer() < 33:
        cat "Meow"
    elif randomizer() < 66:
        cat "Prrrr"
    else:
        cat "Brrrep"
    show cat 15 at Position(xoffset = -7)
    pause
    show cat 14
    if randomizer() < 15:
        player_name "Quem é o melhor gatinho?!"
    elif randomizer() < 30:
        player_name "Você dorme o dia todo?"
    elif randomizer() < 45:
        player_name "O que você fez hoje, huh?"
    elif randomizer() < 60:
        player_name "Sua pequena bola de pelo."
    elif randomizer() < 75:
        player_name "Aww, carinho para o gatinho!"
    elif randomizer() < 85:
        player_name "Hey, cuidado com essas garras!"
    elif randomizer() < 93:
        player_name "Eu deveria te comprar um brinquedo, huh?"
    else:
        player_name "Eu adoro acariciar meu gato..."
    show cat 16
    pause
    hide cat with dissolve
    $ callScreen(location_count)

label cookies:
    if MC_computer_broken:
        scene expression gTimer.image("bedroom_broken{}")
    else:
        scene expression gTimer.image("bedroom{}")
    show expression "objects/closeup_cookies.png" at left with dissolve
    player_name "( Uma caixa dos meus biscoitos favoritos! )"
    player_name "( Eu deveria levar junto no caso de eu ficar com fome. )"
    hide expression "objects/closeup_cookies.png" with dissolve
    show expression "boxes/popup_cookies.png" at truecenter with dissolve
    $ renpy.pause()
    hide expression "boxes/popup_cookies.png" with dissolve
    $ callScreen(location_count)

label june_mcbedroom_normal_faster_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') - 0.1)
    jump june_mcbedroom_normal_sex_loop

label june_mcbedroom_normal_slower_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') + 0.1)
    jump june_mcbedroom_normal_sex_loop

label june_mcbedroom_cosplay_faster_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') - 0.1)
    jump june_mcbedroom_cosplay_sex_loop

label june_mcbedroom_cosplay_slower_sex:
    $ M_june.set('sex speed', M_june.get('sex speed') + 0.1)
    jump june_mcbedroom_cosplay_sex_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
