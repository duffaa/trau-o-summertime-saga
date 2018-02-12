default move_list = []
default move_list_number = 4
default training_tier = 0
default training_skip_payment = False

label training_dialogue:
    $ location_count = "Gym"
    if training_count == 0:
        scene expression gTimer.image("training{}_b")
        pause 0.001
        show player 35 at left
        player_name "Uau..." with None
        show player 14
        player_name "Esse lugar tem tudo!"
        player_name "Até tem aquelas coisas de box!"
        show master 2 at right
        show player 11
        with dissolve
        mas "Isso não é uma academia de box, mas de {b}Muay Thai{/b}!"
        show master 1
        show player 17
        player_name "Ah. Entendi..."
        show master 3
        show player 11
        mas "Somente os alunos mais fortes e disciplinados aprendem meus ensinamentos!"
        show master 5
        show player 12
        player_name "Hmmm... Eu não posso levantar pesos e apenas ser o mais forte de toods?"
        show master 4
        show player 11
        mas "{b}NÃO!!!{/b}" with hpunch
        show master 3
        show player 1
        mas "Sem a disciplina mental e física do Muay Thai..."
        show master 4
        show player 11
        mas "...você não é nada além de um saco de pancadas!"
        show master 3
        mas "Ao aprender a usar as oito partes do nosso corpo para atacar, nos tornamos a arma mais poderosa!"
        show master 5
        show player 12
        player_name "Ah é? E se eu tivesse uma arma?"
        show master 4
        show player 11
        mas "Seu {b}IDIOTA{/b}!!!"
        show player 6
        show master 7
        window hide
        with vpunch
        pause
        show master 1
        show player 38
        player_name "Ouch!!"
        player_name "Isso machuca!"
        show master 4
        show player 11
        mas "Você é lento... e fraco! Uma arma será inútil para você!"
        show master 2
        mas "Isso não é bom, teremos que trabalhar na sua {b}Destreza{/b}."
        show master 5
        show player 12
        player_name "Tudo bem, então, quando começamos a treinar??"
        show master 4
        show player 11
        mas "Hah! Minhas lições não são gratuitas, jovem aprendiz."
        show master 3
        mas "Eu só aceito uma forma de pagamento..."
        mas "...e é..."
        show player 22
        mas "...um par de {b}calcinhas{/b}!"
        show player 21
        show master 6
        player_name "Um par de-"
        show master 4
        show player 11
        mas "Tenho que repetir, garoto?"
        show master 6
        show player 10
        player_name "Ahm, não... Vou ver o que posso fazer, senhor."
        show master 4
        show player 22
        mas "Você tem que se curvar antes de sair!"
        show master 1
        show player 40
        player_name "Sim, senhor!"
        show master 4
        show player 22
        mas "E me chame de, {b}Mestre Somrak{/b}!!!"
        show master 1
        show player 40
        player_name "Sim, {b}Mestre Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Isso! Agora vá!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        if quest07 not in completed_quests:
            $ quest_list.append(quest07)
        $ sis_door_locked_count = 1
        $ training_count = 1
        $ training_tier = 1
        $ sister.add_event(sis_panty01)

    elif training_count == 1 and training_tier == 2 and sister.over(sis_shower_cuddle01):
        scene expression gTimer.image("training{}_b")
        pause 0.001
        show player 14 at left
        show master 6 at right
        with dissolve
        player_name "{b}Mestr Somrak{/b}!"
        player_name "Estou pronto para aprender novas técnicas!"
        show player 1
        show master 2
        mas "Você está ansioso para aprender! Bom, muito bom!"
        show master 3
        mas "Mas minhas aulas não são gratuitas, jovem aprendiz."
        mas "A sua nova forma de pagamento será..."
        show player 11
        show master 9
        mas "...um par de calcinhas {b}usadas{/b}!"
        show master 1
        player_name "..."
        show master 3
        mas "E tenha certeza de que forma {b}usadas{/b}!"
        show master 5
        show player 12
        player_name "Usadas?"
        show player 11
        show master 3
        mas "Você tem que ver uma mulher tirando!"
        show master 9
        mas "Certifique-se de que eles foram usados ​​e absorveram seu cheiro!"
        show master 6
        show player 21
        player_name "Uh... Verei o que posso fazer, senhor."
        show master 4
        show player 5
        mas "Você tem que se curvar antes de sair, idiota!" with hpunch
        show master 6
        show player 40
        player_name "Sim, {b}Master Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Isso! Agora, vá!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        $ training_count = 2
        $ sister.add_event(sis_panty02)

    elif training_count == 2 and training_tier == 3 and sister.over(sis_couch02):
        scene expression gTimer.image("training{}_b")
        pause 0.001
        pause 0.001
        show player 14 at left
        show master 6 at right
        with dissolve
        player_name "{b}Mestre Somrak{/b}!"
        player_name "Estou pronto para aprender novas técnicas!"
        show player 1
        show master 2
        mas "Você está ansioso para aprender! Bom, muito bom!"
        show master 3
        mas "Mas minhas aulas não são gratuitas, jovem aprendiz."
        mas "A sua nova forma de pagamento será..."
        show player 11
        show master 9
        mas "...{b}calcinhas{/b} molhadas!"
        show master 1
        player_name "..."
        show master 3
        mas "Tenha certeza de que elas estejam {b}molhadas{/b}!"
        show master 5
        show player 12
        player_name "Molhadas?"
        show player 11
        show master 3
        mas "Você tem que ser testemunha!"
        show master 9
        mas "As {b}calcinhas{/b} devem estar {b}encharcadas{/b} naturalmente!"
        show master 3
        mas "Certifique-se de que eles foram usados ​​por uma mulher excitada!!"
        show master 6
        show player 21
        player_name "Uh... Verei o que posso fazer, senhor."
        show master 4
        show player 5
        mas "Você tem que se curvar antes de sair, idiota!"
        show master 6
        show player 40
        player_name "Sim, {b}Mestre Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Ótimo! Agora, vá!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        $ training_count = 3
        $ sister.add_event(sis_panty03)

    elif training_count == 3 and training_tier == 4 and sister.over(sis_couch03):
        scene expression gTimer.image("training{}_b")
        pause 0.001
        show player 14 at left
        show master 6 at right
        with dissolve
        player_name "{b}Mestre Somrak{/b}!"
        player_name "Estou pronto para aprender novas técnicas!"
        show player 1
        show master 2
        mas "Excelente!"
        show master 3
        mas "Mas minhas aulas não são gratuitas, jovem aprendiz."
        mas "O seu último pagamento será..."
        show player 11
        show master 9
        mas "...{b}calcinhas{/b} molhadas pelo {b}gozo feminino{/b}!!!"
        show master 1
        player_name "!!!"
        show master 3
        mas "Certifique-se de que elas foram {b}molhadas pelo gozo feminino{/b}!"
        show master 5
        show player 12
        player_name "Gozo feminino?"
        show master 4
        show player 22
        mas "Você é um homem ou um rato?!" with hpunch
        show master 5
        show player 5
        player_name "..."
        show player 11
        show master 3
        mas "Você tem que ser uma testemunha!"
        show master 9
        mas "Tenha certeza que elas foram {b}molhadas{/b} e {b}gozadas{/b} por uma mulher!!"
        show player 21
        show master 5
        player_name "Será difícil fazer..."
        show master 6
        player_name "...Mas verei o que posso fazer, senhor."
        show master 2
        show player 5
        mas "Você precisa se curvar, lembra?"
        show master 6
        show player 40
        player_name "Sim, {b}Mestre Somrak{/b}!!!"
        show master 2
        show player 1
        mas "Boa! Agora, vá!"
        hide player
        hide master
        with dissolve
        hide training_b
        hide training_n_b
        $ training_count = 4
        $ sister.add_event(sis_panty04)
    $ callScreen(location_count)

label cedric_dialogue:
    scene expression gTimer.image("training{}_b")
    show ced 1 at left
    show player 14f at right
    with dissolve
    player_name "Oi!"
    player_name "Você acha que poderia me ajudar?"
    show ced 2
    show player 1f
    ced "Uh..."
    show player 11f
    ced "Você já levantou peso alguma vez, mano?"
    show player 10f
    show ced 1
    player_name "Huh?"
    show ced 2
    show player 5f
    ced "Foi mal, não ajudo frangos."
    hide ced
    hide player
    with dissolve
    $ callScreen(location_count)

label tired_training_dialogue:
    scene expression gTimer.image("training{}_b")
    show player 5 with dissolve
    player_name "( Estou cansado, deveria ir para casa e dormir. )"
    hide player with dissolve
    $ callScreen(location_count)

label cant_solo_lift:
    scene expression gTimer.image("training{}_b")
    show player 11 at left with dissolve
    player_name "( Não posso levantar peso sozinho. )"
    player_name "( Preciso que alguém me ajude! )"
    hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
