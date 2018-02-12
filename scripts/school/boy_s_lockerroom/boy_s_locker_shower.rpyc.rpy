label lockershowers_dialogue:
    $ location_count = "Boy's Locker Shower"
    $ callScreen(location_count)

label latinas_button_dialogue:
    if lockershowers_count == 0 and gTimer.gameDay() >= 1:
        scene location_lockershowers_closeup
        show player 57 at left with dissolve
        show latinas 1 at right with dissolve
        lopez "Ei! O que você está fazendo aqui?"
        show player 58 at left
        show latinas 1 at right
        player_name "Umm... Tentando tomar banho?"
        show latinas 2 at right
        show player 59 at left
        lopez "Escuta, garoto. Este é o nosso território, então cai fora!"
        show latinas 3 at right
        martinez "Espera, {b}Lopez{/b}!"
        martinez "Aqui, acho que é esse garoto que as pessoas estão falando!"
        show latinas 2 at right
        lopez "O quê?! Sério...?"
        lopez "Você está me dizendo que esse garoto tem um {b}pau enorme{/b}?"
        show latinas 3 at right
        martinez "Tudo bem garoto! Mostre-nos o que seu pau, e você pode entrar!"
        show latinas 1 at right
        show player 60 at left
        player_name "Uhh... Acho que não. Vou tomar banho em casa então-"
        show latinas 4 at right
        window hide
        pause
        show player 61 at left
        show latinas 5 at right with hpunch
        window hide
        pause
        player_name "..."
        show player 62 at left
        martinez "Aí está!"
        show latinas 6 at right
        lopez "...É isso que você chama de {b}grande{/b}?"
        show latinas 7 at right
        show player 63 at left
        martinez "Você está mole?!..."
        martinez "...Ele precisa de algum incentivo..."
        martinez "...Hmm..."
        show latinas 8 at right
        martinez "...Isso deverá funcionar!"
        show latinas 9 at right
        window hide
        pause
        show player 64 at left
        show latinas 10 at right with hpunch
        window hide
        pause
        show latinas 11 at right
        lopez "Oh meu deus, puta!"
        martinez "Calma, todo mundo da escola já viu mesmo! Haha!"
        show latinas 12 at right
        lopez "Não adiantou..."
        show latinas 13 at right
        martinez "Talvez isso funcione?"
        show latinas 14 at right
        lopez "Aí, isso funcionou!"
        show latinas 15 at right
        window hide
        pause
        show latinas 15 at right with hpunch
        window hide
        pause
        show player 65 at left
        player_name "...Oh... Não..."
        show player 65 at left
        window hide
        pause
        show player 66 at left with hpunch
        window hide
        pause
        show latinas 16 at right
        show player 67 at left
        lopez "Oh, merda!"
        lopez "{b}Annie{/b} está vindo!!"
        show latinas 17 at right
        show player 68 at left
        show annie 1
        ann "..."
        show annie 3
        ann "O que você está fazendo aqui??"
        show player 69 at left
        show annie 1
        player_name "Eu estava tentando-"
        show player 68 at left
        show annie 3
        ann "Se expor indevidamente?"
        show annie 4
        ann "{b}DENOVO{/b}!?"
        show player 69 at left
        show annie 6
        player_name "Não, não é-"
        show player 68 at left
        show annie 5
        ann "Não quero ouvir suas desculpas esfarrapadas!"
        ann "Minhas ordens são trazer infratores insistentes para a {b}diretoria{/b}!"
        show annie 7
        ann "Me siga, {b}AGORA{/b}!!!"
        show annie 8f
        ann "...e vocês duas, saiam antes que eu mande vocês para a detenção!!!"
        hide latinas 17 at right
        hide player 68 at left
        hide annie 8f
        with dissolve

        $ lockershowers_count = 1
        $ office_count = 1

        jump office_dialogue
    else:

        scene location_lockershowers_closeup
        show player 57 at left with dissolve
        show latinas 1 at right with dissolve
        lopez "Ei! Você está aqui para nos dar problemas novamente?"
        show player 58 at left
        show latinas 1 at right
        player_name "Umm... Só queria tomar banho..."
        show player 59 at left
        show latinas 3 at right
        martinez "Saia daqui, idiota!"
        show latinas 1 at right
        player_name "..."
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
