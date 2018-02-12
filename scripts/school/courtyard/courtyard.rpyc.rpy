label gym_dialogue:
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ location_count = "School Courtyard"
    if player.started(intense_gymercise):
        scene gym with None
        show coach 3 at right
        show jersey 11 at left
        with dissolve
        bri "Olha só quem tá aí."
        bri "Como está o seu treino?"
        show jersey 10
        show coach 1
        player_name "Uhm... Tenho tentado ir a academia!"
        show jersey 11
        show coach 3
        bri "Tentado, huh?"
        bri "Vamos ver quantas flexões você pode fazer."
        show coach 2
        bri "Talvez você consgia bater seu record de... Quanto era mesmo, doi!?"
        show coach 4
        show jersey 22
        bri "Agora, para o chão e faça vinte!" with hpunch
        show coach 6
        show jersey 29
        with fastdissolve
        pause 0.5
        show jersey 30
        pause 0.5
        show jersey 29
        bri "Um!"
        show jersey 30
        pause 0.5
        show jersey 29
        bri "Dois!"
        show jersey 30
        pause 0.7
        show jersey 29
        bri "Três!"
        show jersey 30
        pause 0.9
        show jersey 29
        bri "Quatro!"
        show jersey 27
        show coach 2
        with fastdissolve
        bri "Parabéns, {b}[firstname]{/b}! Você melhorou de inútil a patético!"
        show coach 3
        bri "Continue treinando, inseto!"
        show coach 1
        show jersey 28
        player_name "Sim... {b}Treinador Bridget{/b}..."
        show coach 3
        show jersey 27
        bri "Agora saia do meu caminho!"
        bri "E é melhor você me mostrar alguma melhora na próxima vez!"
        show coach 1
        player_name "Desculpa, {b}Treinador Bridget{/b}!"
        hide coach
        hide jersey
        with dissolve
        $ intense_gymercise.finish()

    elif gym_count == 0:
        scene gym
        show jersey 13 at left with dissolve
        show coach 2 at right with dissolve
        bri "Olha quem apareceu!"
        show coach 1 at right
        show jersey 17 at left
        player_name "Oi, {b}Treinador Bridget{/b}!"
        show jersey 18 at left
        player_name "Eu sei que perdi algumas sessões de treino, mas garanto que estarei pronto para o Atletismo Regional Trim-"
        show coach 3 at right
        show jersey 22 at left
        bri "Cala a boca, inseto!" with hpunch
        bri "Você está um mês atrás de todos, {b}[firstname]{/b}, e eu não vou deixar você piorar o time com sua falta de compromisso!"
        bri "Se você não fizer as pontuações para a qualificação, você pode {b}esquecer se formar este ano.{/b}"
        show coach 7 at right
        show jersey 10 at left
        player_name "Não se preocupe, senhora! Tenho certeza que não será um problema!"
        show coach 3 at right
        show jersey 11 at left
        bri "...Ah é?"
        bri "Por que você não nos mostra suas \"habilidades atléticas de elite\" fazendo {b}20 flexões{/b} agora, seu inútil?!"
        show coach 5 at right
        show jersey 10 at left
        player_name "Mas-"
        show jersey 23 at left
        bri "{b}*APITO*{/b}"
        show coach 6 at right
        show jersey 29 at left
        player_name "Ghh..."
        show jersey 30 at left
        bri "Um..."
        show jersey 29 at left
        player_name "Ghhhh..."
        show jersey 30 at left
        bri "Dois..."
        show jersey 29 at left
        player_name "...Eu...Eu não..."
        show jersey 30 at left
        bri "Trê-"
        bri "... ... ..."
        show coach 3 at right
        bri "O quê?!! Só isso??"
        show jersey 27 at left
        bri "Você não consegue fazer nem 3 miseráveis flexões?!"
        show coach 7 at right
        player_name "Eu..."
        player_name "Me... desculpa... senhora..."
        show coach 3 at right
        bri "É melhor mover sua bunda para a {b}academia local{/b} agora, e começar a levantar peso, se você quiser ser aprovado..."
        show coach 4 at right
        bri "... vá para a {b}aula da Sra. Bissette{/b}, onde trabalho duro e boas notas não importam!"
        bri "Agora, {b}SAIA DA MINHA FRENTE!!!{/b}"
        hide coach 7 with dissolve

        show unlock3 at truecenter
        $ renpy.pause()
        hide unlock3 with dissolve
        $ loc_gym_unlocked = True
        if quest02 not in completed_quests:
            $ quest_list.append(quest02)

        show ronda 3 at right with dissolve
        ron "Você não vai conseguir passar..."
        ron "Por que você ainda se importa em vir pra essa aula?"
        show ronda 2 at right
        show jersey 28 at left
        player_name "Eu ainda consigo..."
        player_name "...E sabe...eu estava pensano, talvez você pudesse me ajudar a trei-"
        show ronda 4 at right
        show jersey 27 at left
        ron "Calma aí!"
        ron "Se você, por algum milagre, consiga {b}fazer a prova{/b}... volte a falar comigo. Caso contrário, pode parar de desperdiçar seu tempo."
        show ronda 1 at right
        show jersey 28 at left
        player_name "Ok!"
        player_name "Mas quando eu fizer, você terá que me mostrar seus truques!"
        show ronda 3 at right
        ron "Vou estar na {b}piscina{/b} nas próximas duas semana, treinando para a prova de 200m..."
        ron "Se você entrar na equipe, venha me ver."
        show ronda 1 at right
        show jersey 20 at left
        player_name "Feito!!"
        show ronda 3 at right
        show jersey 19 at left
        ron "Ugh... Patético..."
        hide ronda 2 at right with dissolve
        hide jersey 19 at left with dissolve
        show unlock4 at truecenter
        $ renpy.pause()
        hide unlock4 with dissolve
        hide gym
        $ loc_pool_unlocked = True
        $ gym_count = 1
        $ classroom_door_count = 2
        $ shower_door_count = 1
        $ stairs_count = 2
        $ left_hall_count = 2
        $ wearing_jersey_count = 1
    else:

        scene gym
        show jersey 11 at left with dissolve
        show coach 3 at right with dissolve
        bri "{b}[firstname]{/b}!"
        show jersey 31 at left
        bri "É melhor você estar treinando na {b}academia{/b}, ou eu vou chutar seu rabo!!"
        show jersey 32 at left
        show coach 7 at right
        player_name "Sim, senhora!!!"
        hide coach 7 at right with dissolve
        hide jersey 32 at left with dissolve
    $ callScreen(location_count)

label coach_button_dialogue:
    scene location_gym_closeup
    show jersey 11 at left with dissolve
    show coach 3 at right with dissolve
    bri "{b}[firstname]{/b}!"
    show jersey 13 at left
    bri "É melhor você estar treinando na {b}academia{/b}, ou eu vou chutar seu raboass!!"
    show jersey 32 at left
    show coach 7 at right
    player_name "Sim, senhora!!!"
    show jersey 31 at left
    show coach 3 at right
    bri "Alguma pergunta?!"
    menu:
        "Onde eu posso treinar?":
            show jersey 10 at left
            show coach 1 at right
            player_name "Eu... Hmmm, onde posso treinar?"
            show coach 7 at right
            show jersey 13 at left
            bri "..."
            show jersey 22 at left
            show coach 3 at right
            bri "Eu já te disse!"
            show coach 4 at right
            bri "Na {b}ACADEMIA{/b}!!!"
            show jersey 10 at left
            show coach 7 at right
            player_name "Mas... o que eu deveria treinar?"
            show jersey 11 at left
            show coach 3 at right
            bri "Você tem que aumentar sua {b}força{/b} e {b}destreza{/b} se você quiser ser aprovado!"
            bri "Você vai competir nos {b}110m com obstáculos{/b} para as qualificatórias da {b}escola{/b} e entrar no {b}campeonato estadual{/b}!"
            show jersey 10 at left
            show coach 7 at right
            player_name "Isso é... muita pressão."
            show jersey 23 at left
            show coach 3 at right
            bri "...E é melhor você não me decepcionar!"
            show jersey 32 at left
            show coach 7 at right
            player_name "Sim, senhora!!!"
            hide coach 7 at right with dissolve
            hide jersey 32 at left with dissolve
        "Não.":

            show jersey 10 at left
            show coach 1 at right
            player_name "Acho que não..."
            show jersey 11 at left
            show coach 3 at right
            bri "{b}ÓTIMO{/b}!"
            show jersey 22 at left
            show coach 4 at right
            bri "Entõ vá {b}TREINAR{/b}!!"
            show jersey 32 at left
            show coach 7 at right
            player_name "Sim, senhora!!!"
            hide coach 7 at right with dissolve
            hide jersey 32 at left with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
