label computer_lab_dialogue:
    $ location_count = "Computer Lab"
    $ callScreen(location_count)

label june_dialogue:
    scene school_computer_b
    if June.completed(june_mc_help):
        show player 14 at left
        show june 5 at right
        player_name "Oi, {b}June{/b}!"
        show player 1
        show june 6
        june "Oi, {b}[firstname]{/b}!"
        june "Então?"
        show june 5
    else:

        if is_here("erik"):
            show erik 1b at Position (xpos=700)
        show june 1 at right
        show player 14 at left
        with dissolve
        player_name "Oi!"
        show june 3
        show player 1
        june "Oh, uh, oi?"
        june "Então?"
        show june 2
    menu:
        "Nada.":
            show june 2 at right
            show player 14
            player_name "Ah, nada!"
            player_name "Só falando oi."
            show player 1
            show june 4
            june "Oh, beleza..."
            show june 1
            show player 29 at Position(xoffset=8)
            player_name "Err... Até mais tarde!"

        "Sair." if June.completed(june_mc_help) and not june_hang_out:
            show player 14 at left
            player_name "Você não quer sair pra minha casa?"
            show player 1
            show june 6
            june "Claro!"
            june "Depois da escola?"
            show player 14
            show june 5
            player_name "Uhum."
            show player 1
            show june 6
            june "Para seu quarto?"
            show player 10
            show june 5
            player_name "Meu quarto?"
            show player 11
            show june 6
            june "Sim! Tenho que ter um lugar calmo e tranquilo para jogar."
            show player 14
            show june 5
            player_name "Heh, ok!"
            show player 1
            show june 6
            june "Legal!"
            june "A aula já está começando, eu deveria ir."
            june "Te vejo depois da escola, {b}[firstname]{/b}!"
            if not June.known(june_mc_help_2):
                $ June.add_event(june_mc_help_2)
            $ june_hang_out = True

        "Cosplay." if June.started(june_cosplay) and orcette_cosplay not in inventory.items:
            show player 14 at left
            show june 2 at right
            player_name "Que cosplay você está querendo fazer?"
            show player 1
            show june 3
            june "Ah, é um cosplay de orcette."
            june "Preciso do dente, colar e a cinta!"
            show player 14
            show june 2
            player_name "Certo!"
            player_name "Acho que sei um lugar no {b}shopping{/b} que tem a roupa..."
            show player 1
            show june 6
            june "Sério?"
            show player 14
            show june 5
            player_name "Eu deveria ir lá dar uma olhada!"
            show player 1
            show june 6
            june "Ótimo! Até mais."
            hide june
            hide player
            with dissolve

        "Cosplay." if June.started(june_cosplay) and orcette_cosplay in inventory.items:
            show player 17 at left
            show june 2 at right
            player_name "Acho que achei algo que você possa gostar!"
            show player 1
            show june 3
            june "Huh?"
            show june 6
            june "O que?"
            show june 5
            show player 423 with fastdissolve
            player_name "É uma roupa de orcette!!"
            show player 422
            show june 6
            june "Pro meu cosplay?!"
            show player 1
            show june 7
            with fastdissolve
            pause
            show player 13
            show june 8
            june "Oh meu deus!!"
            june "Tem todas as peças que eu precisava!"
            june "Até parece ser dentes reais!"
            show player 17
            show june 5 with fastdissolve
            player_name "Fico feliz que você tenha gostado."
            show player 14
            player_name "Vai ficar lindo em você!"
            show player 1
            show june 6
            june "Muito obrigada, {b}[firstname]{/b}."
            show player 14
            show june 5
            player_name "Fico feliz que você tenha um bom cosplay para a comic con."
            show player 11
            show june 6
            june "Eu vou atrair muita atenção do pública, tenho certeza!"
            show player 10
            show june 5
            player_name "Você quer dizer, tipo caras?"
            show player 11
            show june 6
            june "Sim, acho que sim..."
            show june 5
            player_name "..."
            show june 6
            june "Mas sabe?"
            june "Acho que eu deveria testar o cosplay antes de usar!"
            june "Talvez colocar... na frente de um amigo?"
            show june 5
            show player 10
            player_name "Tipo quem?"
            show player 11
            show june 6
            june "Você!! Bobinho..."
            show player 17
            show june 5
            player_name "Oh, ha ha!"
            show player 14
            player_name "Claro, eu poderia emm... dar um feedback!"
            show player 1
            show june 6
            june "Ótimo! Que tal na sua casa... igual da última vez?"
            show player 14
            show june 5
            player_name "Ok, te vejo depois da escola então!"
            show player 1
            show june 6
            june "Até mais!"
            hide player
            hide june
            with dissolve
            $ june_hang_out = True
            $ inventory.items.remove(orcette_cosplay)
            $ june_cosplay.finish()

        "Perguntar sobre turma." if June.completed(june_intro) and (not June.known(june_erik_help) and not June.known(june_mc_help)):
            if not June.known(june_intro_2):
                $ June.add_event(june_intro_2)
            $ june_intro_2.finish()
            show player 14
            show june 2
            player_name "Ei, em qual turma você está?"
            player_name "Eu não te vejo muito na escola."
            show player 1
            show june 3
            june "Ah, eu não faço a aula de educação física."
            june "Prefiro ficar por aqui..."
            show player 14
            show june 2
            player_name "O que você faz aqui?"
            show player 1
            show june 3
            june "Você sabe, coisas... tipo navegar na internet..."
            june "... indo para fóruns, vendo transmissões e jogando."
            show june 2
            show player 14
            player_name "Jogos, huh?"
            show player 1
            show june 3
            june "Sim."
            show june 1
            show player 14
            player_name "Tipo esse que você está segurando?"
            show player 1
            show june 3
            june "Oh, esse? É só um jogo bobo..."
            show player 14
            show june 2
            player_name "Como se chama?"
            show player 1
            show june 3
            june "É Orc Bork."
            show player 14
            show june 2
            player_name "Um jogo sobre orcs?"
            show player 1
            show june 3
            june "Sim."
            show june 4
            june "É bem difícil."
            show player 11
            june "Tenho tentado zerar fazem meses..."
            show player 14
            show june 2
            player_name "É tão difícil assim?"
            show player 1
            show june 3
            june "É mais fácil quando você joga em duas pessoas."
            show june 4
            june "Não achei alguém que jogasse esse tipo de jogo na escola..."
            show june 3
            june "A menos que... você conhece alguém?"
            show june 1
            $ config.skipping = None
            show popup_warning at truecenter with dissolve
            $ renpy.pause(3, hard=True)
            pause
            hide popup_warning with dissolve
            menu june_route_split:
                "Meu amigo {b}Erik{/b}!":
                    hide screen save
                    show player 14 at left
                    show june 2 at right
                    player_name "Na verdade sim!"
                    player_name "Meu amigo {b}Erik{/b} ADORA jogos que tenham orcs!"
                    player_name "Especialmente... os orcettes."
                    player_name "Acho que vocês deveriam jogar juntos!"
                    show player 1
                    show june 3
                    june "{b}Erik{/b}?"
                    show player 11
                    june "Acho que não conheço..."
                    show player 10
                    show june 1
                    player_name "Ele disse que já tem emprestou um lápis uma vez."
                    show player 1
                    show june 4
                    june "Huh..."
                    show player 14
                    show june 5
                    player_name "Ele fica muito tempo no quarto dele... jogando..."
                    show player 1
                    show june 6
                    june "Sério?"
                    show player 14
                    show june 5
                    player_name "Acho que ele poderia te ajudar a zerar o jogo."
                    show player 1
                    show june 6
                    june "Seria incrível."
                    june "Me diga se ele também quiser!"
                    show player 17
                    show june 5
                    player_name "Claro!!"
                    show player 14
                    player_name "Vou falar pra ele."
                    $ June.add_event(june_erik_help)
                "Eu jogo!":

                    hide screen save
                    show player 14
                    show june 2
                    player_name "Eu não sou muito bom nesses jogos... Mas eu posso tentar!"
                    show player 1
                    show june 4
                    june "Você... quer jogar comigo?"
                    june "Tem certeza que você gostaria?"
                    show player 14
                    show june 2
                    player_name "Claro, por que não?"
                    show player 11
                    show june 3
                    june "É que ninguém me convidou antes..."
                    show player 17
                    show june 2
                    player_name "Fico feliz que serei o primeiro!"
                    show player 21
                    show june 5
                    player_name "Err... Digo... não tipo-"
                    show player 11
                    show june 6
                    june "Ha ha, você é tão engraçado."
                    show june 5
                    player_name "..."
                    show player 14
                    player_name "Então... quer jogar aogra?"
                    show player 11
                    show june 6
                    june "Umm... Vamos jogar em outro lugar?"
                    june "Não aguento mais ficar nesse laboratório..."
                    show player 14
                    show june 5
                    player_name "Ok, onde então?"
                    show player 10
                    player_name "Se jogarmos no corredor, {b}Annie{/b} vai nos mandar para a detenção..."
                    show player 11
                    show june 6
                    june "Hmm... e se jogassemos na sua casa?"
                    show player 12
                    show june 5
                    player_name "Minha... minha casa?!"
                    show player 11
                    show june 6
                    june "Sim!"
                    june "Depois da escola?"
                    show player 10
                    show june 5
                    player_name "Uhh... acho que podemos."
                    show player 11
                    show june 6
                    june "Ótimo!"
                    june "Agradeço por querer jogar comigo..."
                    show player 13
                    june "É bem... gentil vindo de você!"
                    show player 14
                    show june 5
                    player_name "Oh, ha ha. Não é nada..."
                    show player 1
                    show june 6
                    june "Venha me chamar quando você quiser jogar!"
                    june "Vou estar aqui."
                    show player 17
                    show june 5
                    player_name "Claro!"
                    $ June.add_event(june_mc_help)
                "Save Menu.":

                    show screen save
                    pause
                    hide screen save
                    jump june_route_split
    hide june
    hide player
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
