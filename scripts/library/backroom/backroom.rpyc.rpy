label backroom_blocked_dialogue:
    scene library
    show player 35 with dissolve
    player_name "Hmm... Não tenho certeza de onde os {b}livros{/b} da escola estão..."
    player_name "Talvez eu devesser perguntara para a {b}bibliotecária{/b} na {b}mesa{/b} primeiro."
    hide player 35 with dissolve
    $ callScreen(location_count)

label backroom_dialogue:
    $ location_count = "Library Backroom"
    if backroom_count == 0:
        scene backroom01
        show library 1_2 at Position(xpos = 486, ypos = 707) with dissolve
        player_name "( PUTA MERDA!!! )"
        player_name "..."
        player_name "( As pessoas estão transando aqui... )"
        pause 4
        player_name "..."
        player_name "( Tem uma webcam na prateleira? )"
        player_name "( Acho que estão filmando... Eles sabem que isso está lá? )"
        player_name "( Eu deveria contar para a {b}bibliotecária{/b}? )"
        call screen backroom_couple_sex01

    elif backroom_count == 2:
        scene backroom01
        show jane 8 at right
        show player 23 at left
        with dissolve
        jan "Que merda!"
        show player 22
        jan "Eu não disse para você não voltar aqui?!"
        jan "Eu disse que eu tenho que limpar primeiro!!"
        show jane 12
        show player 10
        player_name "Sim, mas eu vi-"
        show jane 8
        show player 11
        jan "EU SEI!!!" with hpunch
        show jane 7
        jan "Ugh..."
        jan "Foi por isso que eu falei pra você não voltar aqui..."
        show jane 12
        show player 12
        player_name "Você sabia que as pessoas estavam fazendo isso aqui?!"
        show jane 8
        show player 11
        jan "Eu... Eu não tenho escolhas, ok?"
        show jane 7
        jan "De que outra forma eu matenria este lugar aberto?"
        show jane 12
        show player 12
        player_name "Espera, você está fazendo {b}dinheiro{/b} com isso??"
        show jane 8
        show player 11
        jan "Claro, idiota!"
        jan "Estou sendo paga para transmitir isso."
        show jane 4
        jan "É a única força que eu consigo dixar isso {b}aberto{/b}, ok?"
        show jane 5
        jan "Eu não tenho escolhas..."
        show player 30
        show jane 1
        player_name "Mas... E as pessoas que estão sendo filmadas?"
        player_name "Eles sabem?"
        show jane 4
        show player 11
        jan "Claro que não... Mas quem se importa? Essa sala é conhecida pelos casais."
        show jane 2
        jan "As pessoas amam fazer isso aqui e eu não vou proibir!"
        jan "Mantenha isso em segredo se você quiser aqueles livros..."
        show jane 1
        show player 12
        player_name "Certo! Não vou contar para ninguém..."
        show player 4
        player_name "..."
        show player 12
        player_name "Mas quando posso esperar que meu {b}livro{/b} chegue?"
        show player 1
        show jane 2
        jan "Eu faço um trato... Se você me comprar a {b}Supersaga Digital Webcam{/b}, eu trago o livro agora!"
        show jane 1
        show player 34
        player_name "..."
        show player 35
        player_name "Elas não são muito caras?"
        show jane 7
        show player 11
        jan "Olha, você quer seu {b}livro{/b} ou não?"
        show jane 2
        show player 12
        player_name "Sim... Vou ver o que posso fazer."
        show jane 8
        show player 11
        jan "Ótimo, agora sai daqui! Estou esperando mais casais virem aqui..."
        hide jane 8
        hide player 11
        with dissolve
        if quest06 not in completed_quests:
            $ quest_list.append(quest06)
        $ library_desk_count = 1
        $ backroom_count = 3
        $ unlock_ui()
    $ callScreen(location_count)

label backroom_couple_finish01:
    scene backroom01
    show library 1_2 at Position(xpos = 486, ypos = 707)
    pause 4
    hide library 1_2
    pause .2
    show library 3 at Position(xpos = 486, ypos = 707) with dissolve
    window hide
    pause
    show library 4
    window hide
    pause
    player_name "( Merda! )"
    player_name "( Ouvi alguém vindo!! )"
    show library 5 at Position(xpos = 512, ypos = 707) with hpunch
    window hide
    pause
    hide library 5 with dissolve
    $ backroom_count = 2
    jump backroom_dialogue
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
