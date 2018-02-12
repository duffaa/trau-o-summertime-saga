default music_classroom_first_visit = True

label music_classroom_dialogue:
    $ location_count = "Music Classroom"
    if music_classroom_first_visit == True:
        scene music_classroom_c with None
        show dewitt 1 at left
        show player 1f at right
        with dissolve
        show player 2f
        player_name "Oi, {b}Sra. Dewitt{/b}!"
        show dewitt 2
        show player 1f
        dewitt "Meu Deus!"
        dewitt "Estava pensando que você tinha ido para outra escola!"
        show dewitt 1
        show player 10f
        player_name "Desculpa, {b}Sra. Dewitt{/b}..."
        player_name "Sei que estou atrasado agora, mas eu consigo me recuperar."
        show dewitt 2
        show player 5f
        dewitt "Oh, tudo bem, querido. Não se preocupe."
        dewitt "Você só precisa voltar ao ritmo!!"
        show dewitt 3
        show player 11f
        pause
        show dewitt 2
        dewitt "Pegue um instrumento e sente-se!"
        dewitt "Nós vamos recuperar o tempo perdido!"
        show dewitt 1
        show player 2f
        player_name "Valeu, {b}Sra. Dewitt{/b}..."
        hide dewitt
        hide player
        with dissolve
        $ music_classroom_first_visit = False
    $ callScreen(location_count)

label dewitt_button_dialogue:
    scene music_classroom_c with None
    show dewitt 1 at left
    show player 2f at right
    player_name "Oi, {b}Sra. Dewitt{/b}."
    show dewitt 2
    show player 1f
    dewitt "Olá, {b}[firstname]{/b}!"
    dewitt "Pronto pra estudar hoje?"
    show dewitt 1
    show player 33f
    player_name "Claro!"
    show dewitt 2
    show player 13f
    dewitt "Algo a mais que você queira conversar?"
    show dewitt 1
    show player 34f
    menu:
        "Não.":
            show player 10f
            player_name "Não..."
            player_name "Apenas esperando que eu possa começar."
            show dewitt 2
            show player 5f
            dewitt "Oh, querido. Você ficará beeeem!"
            show player 13f
            dewitt "Pegue um instrumento e sente-se!"
            dewitt "Vamos recuperar o tempo perdido..."
            show dewitt 1
            show player 14f
            player_name "Valeu, {b}Sra. Dewitt{/b}..."
        "Que instrumento?":

            show player 29f
            player_name "Só estava me perguntando que {b}instrumento{/b} eu deveria usar..."
            show dewitt 2
            show player 3f
            dewitt "Hmm..."
            dewitt "Bem, eu sei que você usou uma bateria antes..."
            dewitt "Mas eu realmente acho que você deveria tentar algo mais ... Delicado, desta vez."
            show dewitt 1
            show player 12f
            player_name "Ah, é?"
            show dewitt 2
            show player 5f
            dewitt "Sim!"
            dewitt "Por que você não usa uma {b}flauta{/b}, por exemplo?"
            show dewitt 1
            show player 4f
            player_name "Hmm..."
            show player 10f
            player_name "Não sei-"
            show dewitt 2
            show player 5f
            dewitt "Tente, querido!!"
            dewitt "Não tem por que ter medo!"
            show dewitt 1
            show player 10f
            player_name "Aco que sim... Gosto de aprender novas coisas..."
            show dewitt 2
            show player 11f
            dewitt "Eu gosto de ensinar a flauta..."
            show dewitt 1
            show player 17f
            player_name "Haha. Certo."
    hide dewitt
    hide player
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
