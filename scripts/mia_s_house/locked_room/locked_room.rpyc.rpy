label helens_locked_room:
    $ location_count = "Helen's Locked Room"
    if M_mia.get_state() == S_mia_locked_room:
        scene mia_house_locked_n
        show object_bed_11 at Position (xpos=527,ypos=765)
        show player 23 at left with dissolve
        player_name "{b}MIA{/b}!"
        player_name "Você está amarrada?!"
        show player 10
        player_name "Espera, deixa eu te ajudar..."
        hide player with dissolve
    $ callScreen(location_count)

label mia_tied_up:
    scene mia_house_cs01
    with fade
    show text "{b}Mia{/b} parece está amarrada, presa na cama.\nNão tenho tempo para pensar...\n...Preciso fazer algo!" at Position (xpos= 512, ypos = 700) with dissolve
    with dissolve
    pause
    hide text
    hide school_art_cs01
    with dissolve

    scene mia_house_locked_c
    show player 5 at left
    show mia 40f at right
    with dissolve
    pause
    show mia 41f with dissolve
    pause
    show mia 42f at Position (xoffset=-15) with dissolve
    mia "Ow..."
    show mia 43f at Position (xpos=500) with dissolve
    mia "{b}[firstname]{/b}!!!"
    show mia 44f
    show player 10
    player_name "{b}Mia{/b}! O que aconteceu?!"
    player_name "Eu vi sua mensagem no celular e-"
    show player 11
    show mia 43f
    mia "Tenho que ir, rápido!"
    show mia 44f
    show player 12
    player_name "Espera, {b}Mia{/b}, o quê está acontecendo?"
    show player 11
    show mia 43f
    mia "Minha mãe está ficando {b}MALUCA{/b}!!"
    mia "Ela está me trancando aqui e..."
    mia "...Me forçando a ler a bíblia e rezar, o dia todo..."
    show player 22
    mia "...AMARRADA NESSA CAMA!!!"
    show mia 44f
    show player 23
    player_name "O quê?! Que loucura!"
    show player 11
    show mia 43f
    mia "Não temos tempo para falar sobre isso agora."
    mia "Temos que sair!!!"
    show mia 44f
    show player 10
    player_name "Agora?!"
    show player 11
    show mia 46f
    mia "SIM!"
    show mia 45f
    show player 10
    player_name "Espera, pra onde?!"
    show player 5
    show mia 46f
    mia "Não me importo, não quero mais ficar-"
    hide player
    show player 22 at left
    show mia 45 at Position (xpos=420)
    show helen 6 at right
    with dissolve
    player_name "!!!"
    show helen 7 with dissolve
    helen "Como você se {b}ATREVE{/b} a voltar... {b}PRA MINHA CASA{/b}!"
    show helen 8
    show player 24
    show mia 47 at Position (xpos=465) with dissolve
    mia "{b}Mãe{/b}! {b}PARA{/b}!!!"
    show mia 48
    show helen 7
    helen "Não permitirei que esse malfeitor te tire de mim..."
    show helen 10 at Position (xpos=950) with dissolve
    helen "...{b}ESSA{/b} é a única coisa que importa..."
    show player 22
    helen "...eu vou {b}TE SALVAR{/b}!!!"
    show helen 11
    pause.5
    show helen 8 at Position (xpos=750)
    show harold 12 at right
    with dissolve
    harold "{b}Helen{/b}, por que todo esse escândalo?!"
    show harold 14
    show helen 7b
    helen "Vai lá para baixo, {b}Harold{/b}."
    show helen 8b
    show harold 13
    show player 11
    harold "Não, calma aí, {b}Helen{/b}!"
    harold "Isso é de mais, está ido muito longe!!"
    show harold 14
    show helen 7b
    show player 22
    helen "{b}QUIETO{/b}!"
    helen "Já tive o suficiente da sua péssima paternidade..."
    helen "...Você {b}NUNCA{/b} conseguiu controlar sua filha!"
    show helen 8
    show player 11
    hide mia
    show mia 46 at Position (xpos=425) with dissolve
    mia "{b}Pai{/b}!"
    show helen 8b
    hide mia
    show harold 15
    with dissolve
    mia "Faça ela parar!"
    harold "..."
    show helen 7b
    helen "Ela tem que ficar aqui."
    show helen 8b
    show harold 17
    harold "Não."
    show harold 16
    helen "..."
    show harold 17
    harold "Já deu!"
    pause
    show player 22
    harold "E você!"
    show harold 16
    show helen 8
    player_name "???"
    show harold 17
    harold "Você não deveria estar aqui."
    harold "Vai pra casa e me deixe cuidar disso!"
    show harold 16
    show player 10
    player_name "Certo, desculpa, eu... estou indo."
    hide player with dissolve
    show helen 7b
    helen "Nós temos que conversar, {b}Harold{/b}."
    show helen 8b
    show harold 17
    harold "Acho que não, {b}Helen{/b}."
    harold "Não tem mais o que conversar aqui."
    harold "{b}Mia{/b} vai para o quarto dela e nós resolvemos isso amanhã!"
    hide harold
    hide helen
    scene black
    with fade
    pause

    scene miahouse_night
    show player 12 with dissolve
    player_name "{b}Helen{/b} está ficando {b}LOUCA{/b}!!"
    player_name "Não pensava que os pais da {b}Mia{/b} erão tão chatos..."
    player_name "...Amarrar ela?! Isso é loucura!"
    show player 24
    player_name "{b}*suspiro*{/b}"
    player_name "Me sinto mal pela {b}Mia{/b}..."
    hide player with dissolve
    $ gTimer.tick(4)
    $ M_mia.trigger(T_mia_rescue)
    $ location_count = "Mia's House"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
