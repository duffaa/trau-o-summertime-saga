label hospital_dialogue:
    $ location_count = "Hospital"
    $ callScreen(location_count)

label roz_dialogue:
    scene hospital_desk
    show roz 1 at left
    if datetime.date.today().month == 12 and (datetime.date.today().day >= 15 and datetime.date.today().day <= 30):
        show xtra 35 zorder 2 at Position(xalign = 0.1, yalign = 0.251)
    show roz_desk at left
    show player 14f at right
    with dissolve
    player_name "Oi!"
    show player 13f
    show roz 2
    roz "Sim?"
    roz "O que eu posso fazer por você?"
    show roz 1
    if not Roz.known(roz_intro):
        $ Roz.add_event(roz_intro)
        $ roz_intro.finish()
    menu roz_dialogue_repeat:
        "Primeiro andar?":
            show player 12f
            player_name "Como posso ir para o primeiro andar?"
            show player 5f
            roz "..."
            show roz 2
            roz "É a recepção."
            show roz 1
            show player 10f
            player_name "Oh... Tem algo a mais?"
            show player 5f
            show roz 3 with dissolve
            roz "Você vê algo a mais?"
            show roz 1 with dissolve
            show player 24f
            player_name "Acho que não..."
            show player 25f
            show roz 2
            roz "Algo mais que eu possa fazer?"
            show roz 1
            show player 13f
            jump roz_dialogue_repeat
        "Segundo andar?":

            show player 12f
            player_name "O que eu encontro no segundo andar?"
            show player 5f
            show roz 2
            roz "Temos quartos de enfermagem e uma sala de armazenamento no 2º andar."
            show roz 1
            show player 12f
            player_name "Ah. Entendi."
            show player 5f
            show roz 2
            roz "Algo mais?"
            show roz 1
            show player 13f
            jump roz_dialogue_repeat
        "Horários.":

            show player 12f
            player_name "Sempre tem gente na recepção??"
            show player 5f
            show roz 2
            roz "Sim."
            roz "Estou sempre aqui."
            show roz 1
            show player 12f
            player_name "Você nunca deixa a sua mesa?"
            show player 5f
            show roz 2
            roz "Por que pergunta?"
            show roz 1
            show player 10f
            player_name "Err... Apenas me perguntando?"
            show player 5f
            show roz 2
            roz "Eu só sai da minha mesa em caso de emergência."
            show player 11f
            roz "Se eu não receber um {b}telefonema{/b}, eu não saio."
            show roz 1 with dissolve
            show player 14f
            player_name "Entendi."
            show player 13f
            show roz 2
            roz "Algo mais?"
            show roz 1
            jump roz_dialogue_repeat

        "Ascendência." if M_aqua.get_state() == S_aqua_boatsmith_search and M_roz.get_state() == S_roz_start:
            show player 14f
            show roz 1
            player_name "Roz! Preciso perguntar algo."
            show player 11f
            show roz 2
            roz "Hmm, pois não?"
            show roz 1
            show player 10f
            player_name "Estou tentando encontrar o túmulo de alguém que morreu nesta cidade, há muito tempo."
            show player 29f
            player_name "Eu acho que ele era dono de um barco."
            player_name "Você tem idéias sobre o que fazer para encontrá-lo?"
            show player 3f
            show roz 2
            roz "Talvez eu tenha uma ideia."
            show roz 1
            roz "..."
            show player 11f
            player_name "..."
            show player 12f
            player_name "Poderia me dizar?"
            show player 11f
            show roz 2
            roz "... Acho que poderia."
            show roz 1
            roz "..."
            show player 16f
            player_name "..."
            show player 30f
            player_name "*suspiro* Poderia me dizer?"
            show player 16f
            show roz 2
            roz "Qual é o nome desse cara?"
            show player 29f
            show roz 1
            player_name "... Aí está, eu não sei o nome dele."
            show player 11f
            show roz 2
            roz "Hmm..."
            roz "Bem, isso dificulta as coisas, não é?"
            show player 25f
            show roz 1
            player_name "... Uhum."

            show player 24f
            show roz 2
            roz "Hmm..."
            roz "É possível que você possa encontrá-lo no antigo {b}registro de obituário{/b}."
            show player 11f
            roz "Lembro que algumas pessoas tinham suas profissões listadas lá."
            show player 10f
            show roz 1
            player_name "Sério?! Parece bom!"
            show player 11f
            show roz 2
            roz "O problema é, vai ser um grande incômodo. Eu mexendo nessa coisa antigas."
            show player 29f
            show roz 1
            player_name "Hum?"
            show player 3f
            show roz 2
            roz "Talvez você possa fazer algo para que compense esse tempo perdido..."
            show player 29f
            show roz 1
            player_name "C-claro!"
            show player 2f
            player_name "Você me deixa dar uma olhada nesses registros e farei o que você quiser!"
            show player 1f
            show roz 2
            roz "Hmm... Qualquer coisa?"
            show player 2f
            show roz 1
            player_name "Qualquer coisa!"
            show player 1f
            roz "..."
            show roz 2
            roz "Bem. Vou te contar. Leve essa chave para a {b}sala de armazenamento no segundo andar{/b}."
            roz "Você encontrará uma caixa um pouco acabada na prateleira, é fácil de achar, você achará facilmente."
            show player 2f
            show roz 1
            player_name "Caixa acabada, entendido."
            show player 1f
            show roz 2
            roz "Você vai me trazer aquela caixa enquanto eu procuro pelos registros."
            show player 2f
            show roz 1
            player_name "Parece fácil! Estarei de volta rapidamente!"
            hide player with dissolve

            show roz 2
            roz "Heh, com certeza você vai. Com certeza."
            hide roz
            hide roz_desk
            with dissolve
            $ M_roz.trigger(T_roz_favour)
            $ M_roz.set("fun time", True)

        "Intervalo." if M_roz.get_state() == S_roz_end and not M_roz.is_set("fun time"):
            show player 14f
            show roz 1
            player_name "Eu tava pensando aqui... sabe, não quer fazer um intervalo?"
            show player 13f
            show roz 2
            roz "Ahh..."
            roz "Ainda não foi o suficiente, hein, rapaz?"
            show roz 1
            player_name "..."
            show roz 2
            roz "Não se preocupe, já entendi."
            roz "Vá para a sala de armazem que eu vou daqui a pouco..."
            roz "...só preciso de um tempo."
            show roz 1
            player_name "..."
            show player 14f
            player_name "C-claro, estarei lá te esperando."
            show player 13f
            hide player with dissolve
            show roz 2
            roz "Bom garoto..."
            hide player
            hide roz
            hide roz_desk
            with dissolve
            $ M_roz.set("fun time", True)
        "Nada.":

            show player 14f
            player_name "Não, acho que é tudo!"
            show player 13f
            show roz 2
            roz "Tchau."
            hide player
            hide roz
            hide roz_desk
            with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
