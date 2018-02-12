label stairs_dialogue:
    $ location_count = "School Right Hallway"
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not gTimer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if stairs_dialogue_count == 0:
        scene stairs
        show player 4 at left with dissolve
        player_name "Hmmm..."
        player_name "( Não tem muitas pessoas na cantina ainda. )"
        show player 12 at left
        player_name "( Não é o horário de almoço. )"
        hide player 12 at left with dissolve
        $ stairs_dialogue_count = 1
    $ callScreen(location_count)

label annie_button_dialogue:
    scene location_school_second_closeup
    show player 14 at left with dissolve
    show annie 1 at right
    player_name "Oi, Annie!"
    show annie 5
    show player 1
    ann "Não desperdice meu tempo!"
    show annie 6
    show player 17
    player_name "Oh, não é nada... Só queria falar oi!"
    show annie 4
    show player 18
    ann "Estou cuidando dos corredores... e você está desperdiçando meu tempo."
    show annie 6
    show player 11
    player_name "..."
    show player 12
    player_name "Certo. Desculpa por te incomodar, tchau!"

label unfinished_dialogue2:
    scene stairs
    show player 18 at left
    player_name "Este conteúdo ainda não está pronto! Volte quando a próxima atualização do jogo for lançada!"
    $ callScreen(location_count)

label quest09_1:
    scene stairs
    show player 166 with dissolve
    player_name "( Não posso ir. )"
    if not quest09_2:
        player_name "( Tenho que entregar o {b}recibo{/b} para a {b}Sra. Smith{/b}, e então entregar a encomenda para a {b}Annie{/b}. )"
    else:
        player_name "( Ainda tenho que entregar a encomenda para a {b}Annie{/b}. )"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
