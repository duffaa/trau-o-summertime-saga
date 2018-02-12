default science_classroom_first_visit = True

label science_classroom_dialogue:
    $ location_count = "Science Classroom"
    if science_classroom_first_visit == True:
        scene science_classroom_c with None
        show okita 1 at right
        show player 5 at left
        with dissolve
        show okita 2
        okita "Ora, ora..."
        okita "Parece que alguém decidiu colocar o cérebro pra funcionar de novo."
        show okita 1
        show player 10
        player_name "Oi, {b}Sra. Okita{/b}."
        player_name "Não queria ficar todo esse tempo fora. Eu estava-"
        show okita 2
        show player 5
        okita "Sua vida pessoal é irrelevante pra mim."
        okita "O que me interessa é o estudo e os resultados."
        show okita 1
        show player 24
        player_name "Sim, {b}Sra. Okita{/b}."
        show player 10
        player_name "Vou estudar o dobro!"
        show okita 2
        show player 5
        okita "Mais uma coisa..."
        okita "Onde está seu {b}jaleco{/b}, {b}[firstname]{/b}?"
        show okita 1
        show player 35
        player_name "Oh, certo..."
        show player 29
        player_name "Não sei onde está, {b}Sra. Okita{/b}."
        show okita 2
        show player 3
        okita "Você não pode fazer os experimentos da aula sem ele!"
        okita "Encontre o seu {b}jaleco{/b}, e então poderemos começar os estudos."
        show okita 1
        show player 10
        player_name "Sim, {b}Sra. Okita{/b}..."
        hide okita
        hide player
        with dissolve
        $ science_classroom_first_visit = False

    elif M_mia.get_state() == S_mia_return_favor:
        scene school_science_c02
        show player 13 at left
        show mia 10 at right
        with dissolve
        mia "{b}[firstname]{/b}!"
        show mia 7
        show player 14
        player_name "Oi, {b}Mia{/b}."
        show player 12
        player_name "Como está sua...perna?"
        show player 13
        show mia 9
        mia "Ah, está bem... Só tá um pouco dolorido, ha ha."
        show mia 10
        mia "Mas já está melhor, e já removi o curativo!"
        show mia 7
        show player 17
        player_name "Legal! Como ficou?"
        show player 13
        show mia 10
        mia "Queria te mostrar, na verdade... E dar-lhe algo como um uma forma de agradecimento por me ajudar."
        show mia 7
        show player 10
        player_name "Aqui?"
        show player 11
        show mia 9
        mia "Aqui não, bobinho!"
        show mia 7
        show player 17
        player_name "Oh, ha ha."
        show player 13
        show mia 10
        mia "{b}Venha pro meu quarto de noite{/b} que eu te mostro."
        show mia 7
        show player 14
        player_name "Ok, vou ir!"
        show player 13
        show mia 10
        mia "Ótimo! Te vejo lá então!"
        hide player
        hide mia
        with dissolve
        $ M_mia.trigger(T_mia_night_invite)

    elif M_mia.get_state() == S_mia_strip_aftermath:
        scene school_science_c02
        show player 5 at left
        show mia 12 at right
        with dissolve
        mia "Oi, {b}[firstname]{/b}..."
        show mia 8
        show player 10
        player_name "{b}Mia{/b}!"
        player_name "Desculpa por ontem a noite."
        show player 12
        player_name "Está tudo bem na sua casa?"
        show player 5
        show mia 12
        mia "Na verdade, queria falar sobre isso."
        show mia 8
        show player 11
        player_name "..."
        show mia 12
        mia "Agora estou proibido passar um tempo com amigos... e especialmente você."
        mia "Minha mãe diz que eu tenho que estar em casa depois da escola e não falar com você..."
        show mia 8
        show player 10
        player_name "...Mas, {b}Mia{/b} I-"
        show player 11
        show mia 12
        mia "Não podemos conversar, desculpa..."
        hide mia with dissolve
        show player 24
        player_name "Não queria te causar problemas..."
        hide player with dissolve
        $ M_mia.trigger(T_mia_grounded)
    $ callScreen(location_count)

label okita_button_dialogue:
    scene science_classroom_c with None
    show okita 1 at right
    show player 5 at left
    with dissolve
    show player 10
    player_name "Oi, {b}Sra. Okita{/b}."
    show okita 2
    show player 5
    okita "O que foi, {b}[firstname]{/b}?"
    show okita 1
    show player 11
    menu:
        "Nada.":
            show player 29
            player_name "Nada, {b}Sra. Okita{/b}."
            player_name "Apenas me preparando para as próximas experiências do laboratório."
            show okita 2
            show player 3
            okita "Ótimo."
            okita "Se os meus números estiverem certos, o seu estudo deve aumentar em 400% nas próximas semanas."
            show player 22
            okita "Caso contrário, você ficará para trás, e eu REPROVAREI você."
            show okita 1
            show player 23
            player_name "!!!" with hpunch
            show player 10
            player_name "Entendido, {b}Sra. Okita{/b}."
    hide okita
    hide player
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
