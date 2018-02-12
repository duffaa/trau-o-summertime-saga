label erik_backyard_dialogue:
    $ location_count = "Erik's Backyard"
    if erik.in_progress(erik_thief):
        scene eriks_backyard_n
        show door_thief_night at Position (xpos=882,ypos=655)
        player_name "( Ele está...tentando entrar na porta dos fundos da {b}Sra. Johnson{/b}? )"
        player_name "( Deve ser o ladrão que ouvi nos noticiários. )"
        player_name "( Eu deveria me aproximar e ver... )"
    $ callScreen(location_count)

label erik_thief_block2:
    scene eriks_backyard_n
    show door_thief_night at Position (xpos=882,ypos=655)
    player_name "( Ainda não posso sair. )"
    player_name "( E se ele estiver tentando roubar?! )"
    player_name "( Tenho que me certificar que nada de ruim aconteça... )"
    $ callScreen(location_count)

label erik_thief:
    $ unlock_ui()
    scene eriks_backyard_c
    show larry 1 at Position (xpos=800) with dissolve
    show player 12 at left with dissolve
    player_name "...Uhm!"
    player_name "Com licença!"
    show player 16
    show larry 2 at right with dissolve
    thief "!!!" with hpunch
    show player 12
    player_name "O que você está fazendo?"
    show player 16
    show larry 3 with dissolve
    thief "Ah, merd-"
    hide larry with dissolve
    show player 15
    player_name "HEY!"
    player_name "Fique aí parado!!"
    hide player with dissolve

    scene erik_house_cs03 with fade
    show text "Eu estava prestes a confrontá-lo enquanto estava tentando arrombar...\n...Mas ele foi correndo para o muro.\nEu estava me aproximando dele, então..." at Position (xpos= 512, ypos = 700) with dissolve
    pause
    hide text

    if pStats.dex() >= 5:
        scene erik_house_cs05 with fade
        show text "...Ele correu para o muro e tentou pular...\n...Mas eu estava lá para agarrá-lo e puxar para baixo..." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text
    else:

        scene erik_house_cs04 with fade
        show text "...Ele correu para o muro e pulou rapidamente!!\nEu não fui ágil o suficiente para pegar ele..." at Position (xpos= 512, ypos = 700) with dissolve
        pause
        hide text

        scene eriks_backyard_c with None
        show player 25 with dissolve
        player_name "[dex_warn]Merda..."
        player_name "[dex_warn]Não acredito que ele pulou tão alto, e deixei ele escapar!"
        player_name "[dex_warn]Preciso treinar mais caso queira pegar ele."
        show player 24
        player_name "[dex_warn]Ugh."
        player_name "[dex_warn]Eu deveria voltar para a cama..."
        hide player with dissolve
        scene black with fade
        jump sleeping

    scene eriks_backyard_c
    show larry 4 at left
    with dissolve
    player_name "Ei!"
    show larry 5
    pause
    show larry 4
    player_name "O que você estava fazendo?!"
    player_name "Parece de se mexer!"
    player_name "Você não vai pra lugar algum."
    show larry 7
    show erik 52 at Position (xpos=750)
    show erikmom 52 at right
    erimom "O que está fazendo tanto barulho aqui atrás?"
    erimom "Quem está aí?"
    show erikmom 38
    show erik 53
    eri "{b}[firstname]{/b}?"
    show erik 52
    show larry 6
    player_name "Desculpa, {b}Sra. Johnson{/b}. Não quis te acordar..."
    show larry 4
    player_name "...Mas peguei esse cara tentando invadir sua casa!"
    show larry 7
    show erik 51
    show erikmom 19
    erimom "!!!"
    show erikmom 52
    erimom "O quê? O que aconteceu?"
    show erikmom 38
    show erik 52
    show larry 6
    player_name "Bom, eu ouvi alguns barulhos no meu quarto, e vi esse cara aqui atrás."
    player_name "Eu fui para fora para ver onde ele foi e achei ele na sua porta tentando entrar!"
    show larry 4
    player_name "Ele tentou corre, mas eu consegui pegar ele..."
    show larry 7
    show erikmom 19
    erimom "Oh meu deus!"
    show erikmom 38
    show larry 5
    erimom "Vamos ver quem está por trás dessa máscara..."
    hide erikmom
    hide larry
    show larry 8 at left
    with dissolve
    pause
    show larry 9
    show erikmom 61 at right
    with dissolve
    show erik 51
    erimom "!!!" with hpunch
    show erik 53
    eri "{b}Papai{/b}?!"
    show erik 3b
    player_name "!!!"
    show erikmom 51 with dissolve
    show larry 10
    larry "Desculpa..."
    show larry 11
    show erikmom 52
    erimom "{b}Larry{/b}! O que você está fazendo na cidade?? Achei que você estava em outro estado?"
    show erikmom 51
    show erik 52
    show larry 10
    larry "Eu... Eu sei... é que..."
    larry "...Alguns anos atrás, minha banda faliu."
    larry "Tive problemas com dinheiro e... eu precisava voltar."
    show larry 9
    show erikmom 52
    erimom "Você está de volta há alguns anos?!"
    show erikmom 51
    show larry 11
    larry "..."
    show erikmom 52
    erimom "Explique-se, {b}Larry{/b}!"
    show erikmom 51
    show larry 10
    larry "Eu... Eu não tive a coragem de te ver depois que te deixei..."
    show larry 9
    show erikmom 19
    erimom "E você achou que seria bom começar a roubar?"
    show erikmom 19c
    show larry 11
    larry "..."
    show larry 10
    larry "Não consegui achar um emprego!"
    larry "E... todo mundo me conhece aqui."
    larry "Eu não queria que ninguém soubesse..."
    show larry 11
    show erikmom 52
    erimom "Por que voltou então? "
    show erikmom 51
    show erik 51
    show larry 10
    larry "Eu... queria ver meu único filho, {b}Erik{/b}..."
    larry "Vim aqui durante a noite nos últimos meses, na esperança de me encontrar com ele..."
    show larry 9
    show erik 52
    show erikmom 52
    erimom "Você deveria ter pensado nisso antes de nos deixar!!"
    erimom "Quer saber? Você não mudou nem um pouco."
    erimom "Você ainda pensa só em você mesmo!!"
    show erikmom 51
    show erik 53
    eri "{b}Mãe{/b}... O que vai acontecer?"
    show larry 11
    show erik 51
    show erikmom 52
    erimom "Chame a polícia."
    erimom "Deixaremos eles tomarem conta disso."
    hide erikmom
    hide erik
    hide larry
    with dissolve
    scene black with fade

    scene erik_house_night_cops
    pause
    show player 5f at Position (xpos=650)
    show erik 52 at Position (xpos=775)
    show erikmom 51 at right
    show harold 3f at left
    show larry 13 at Position (xpos=275)
    with dissolve
    harold "Foi bom você ter ligado!"
    harold "Estávamos tentando achá-lo fazem dois anos..."
    show harold 1f
    show erikmom 52
    show larry 12
    erimom "Eu... Eu nunca achei que veria ele novamente..."
    erimom "...Ele está sempre em confusão!"
    erimom "Só estou feliz que terminou e ele pode estar fora de nossas vidas para sempre!"
    show erikmom 51
    show larry 12b
    show erik 51
    show player 11f
    larry "{b}Erik{/b}!"
    show erik 52
    larry "Estou feliz que você esteja bem..."
    larry "...Senti sua falta!!"
    show larry 12
    show erik 50
    show player 5f
    eri "..."
    show larry 13
    show harold 3f
    harold "Vamos, {b}Larry{/b}. Vamos levar você para a delegacia."
    hide harold
    hide larry
    with dissolve
    show player 11f
    show erik 2
    show erikmom 61
    with dissolve
    pause
    hide player
    hide erik
    hide erikmom
    with dissolve
    $ erik.complete_events(erik_thief)
    show unlock44 at truecenter with dissolve
    pause
    hide unlock44 with dissolve
    jump sleeping
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
