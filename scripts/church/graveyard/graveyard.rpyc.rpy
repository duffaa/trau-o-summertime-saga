label church_graveyard_dialogue:
    $ location_count = "Church Graveyard"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 2>audio/ambience_graveyard.ogg"):
            $ playSound("<loop 2>audio/ambience_graveyard.ogg")
    $ callScreen(location_count)

label right_tombstone:
    scene location_church_graveyard_tombstone01
    if M_aqua.get_state() == S_aqua_graveyard_search:
        player_name "( O nome dessa lápide é Ben Dover! )"
        player_name "( Esse deve ser o único. )"
        player_name "( Mas agora que encontrei, não tenho certeza do que eu deveria estar procurando... )"
        player_name "Hmm..."
        player_name "( Talvez tenha alguma {b}pista{/b} em algum lugar? )"
        player_name "( Esta gravura se destaca... )"
        player_name "( Talvez eu deva procurar por um grande {b}sino{/b} em algum lugar na cidade? )"
        $ M_aqua.trigger(T_aqua_tomb_engraving)
    else:

        pause
    $ callScreen(location_count)

label stray_cat:
    scene location_church_graveyard_closeup
    if not M_player.is_set("found cat"):
        $ M_player.set("found cat", True)
        show player 11 at left with dissolve
        cat "Meow"
        show player 10
        player_name "Uhh, oi?"
        show player 11
        cat "Meow"
        show player 10
        player_name "De onde vem esse som?"
        cat "Groooour!"
        show player 11
        show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
        pause
        show player 1
        pause
        show player 2
        player_name "Aww."
        player_name "Bom, aqui está."
        show player 1
        show cat 4
        cat "Brrrep"
        show player 2
        show cat 3
        player_name "O que você está fazendo aqui sozinho?"
        player_name "Você está perdido?"
        show player 1
        show cat 4
        cat "Brrrep"
        show player 2
        show cat 3
        player_name "Coitado."
        player_name "Ele não usa uma coleira."
        show cat 3
        player_name "Deve ser abandonado..."
        player_name "Onde era a sua casa?"
        show player 1
        show cat 4
        cat "Groooour!"
        show player 11
        show cat 3
        pause
        show player 10
        player_name "Qual é o problema??"
        show player 11
        show cat 4
        cat "Groooour!"
        show player 30
        show cat 3
        player_name "Hmm..."
        show player 2
        player_name "AAAH, entendi!"
        player_name "Você é uma garota, não?!"
        show player 1
        show cat 4
        cat "Brrrep"
        show cat 5 with dissolve
        cat "Prrrr"
        show player 2
        player_name "Você parece estar faminta."
        player_name "Você está com fome, garota?"
        show player 1
        show cat 4
        cat "Meow"
        show player 2
        show cat 3
        if cat_food in inventory.items:
            jump feed_cat
        player_name "Hehe, certo. Talvez eu possa achar algo para você."
        show player 4
        show cat 3
        player_name "(Hmm.)"
        player_name "(Deveria procurar algo para ela comer.)"
        player_name "(Acho que na {b}Consum-r{/b} tem algo.)"

    elif cat_food not in inventory.items:
        show player 1 at left
        show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
        pause
        show cat 4
        cat "Meow"
        show player 2
        show cat 3
        player_name "Aww... Ainda com fome, é?"
        show player 1
        show cat 4
        cat "Brrrep"
        show player 2
        show cat 5
        player_name "Você é tão fofa!"
        player_name "Vou procurar algo para você comer, ok?"
        show player 1
        show cat 4
        cat "Prrrr"
        show player 2
        show cat 5
        player_name "Fique aqui!"

    elif cat_food in inventory.items:
        show player 1 at left with dissolve
        show cat 3 at Position(xpos=0.57, ypos=0.77) with dissolve
        pause
        show cat 4
        cat "Meow"
        show player 2
        show cat 3
        player_name "Olá de novo, pequenina."
        show player 1
        show cat 4
        cat "Meow"
        show player 2
        show cat 3
        label feed_cat:
            player_name "Sabe o que eu trouxe para você?"
            show player 239_240
            pause
            hide player with dissolve
            show cplayer 1 at left with dissolve
            show cat 4
            cat "Brrrep"
            show cplayer 2
            show cat 3
            player_name "Isso mesmo, trouxe uma ração!"
            show cat 4
            cat "Meow"
            hide cat with dissolve
            show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
            pause



            hide cat with dissolve
            show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
            player_name "!!!" with hpunch
            hide cplayer with dissolve
            hide cat with dissolve
            show cat 8 at left with dissolve
            pause
            show cat 9
            cat "Prrrr"
            show cat 10
            player_name "Hehe, isso."
            player_name "Ração para o gatinho!"
            show cat 9
            cat "Brrrep"
            show cat 8

            scene black with fade
            $ inventory.items.remove(cat_food)
            scene location_church_graveyard_closeup with fade

            show cat 17 at left
            player_name "Wow, você está com muita fome, não está?"
            show cat 18
            cat "Buuuuuurp!"
            show cat 17
            player_name "..."
            player_name "Hah, fico feliz que você gostou..."
            hide cplayer with dissolve
            show player 2 at left
            show cat 3 at Position(xpos=0.57, ypos=0.77)
            with dissolve
            player_name "Agora está melhor, não está?"
            show player 1
            show cat 4
            cat "Brrrep"
            show player 2
            show cat 5
            player_name "Você é tão fofa."
            show player 4
            player_name "( Hmm... )"
            player_name "( Talvez eu devesse levar você para casa. )"
            player_name "( Acho que [mom_name] não iria se importar... )"
            menu:
                "Levar para casa.":
                    show player 2
                    player_name "O que você quer dizer, garota?"
                    player_name "Quer vir comigo?"
                    show player 1
                    show cat 4
                    cat "Brrrep!"
                    hide cat with dissolve
                    show cat 6 at Position(xpos=0.578, ypos=0.77) with dissolve
                    pause
                    hide cat with dissolve
                    show cat 7 at Position(xpos=0.45, ypos=0.70) with dissolve
                    player_name "!!!" with hpunch
                    hide player
                    hide cat
                    with dissolve
                    show cat 13 at left with dissolve
                    pause
                    show cat 16
                    pause
                    show cat 14
                    player_name "Hehe, aww..."
                    show cat 15
                    pause
                    show cat 14
                    player_name "Vou considerar como um sim!"
                    show cat 12
                    cat "Prrrr"
                    show cat 14
                    player_name "Você vai precisar de um nome se quiser vir comigo..."
                    call screen cat_name_input
                    if cat_name.strip() == "":
                        $ cat_name = "Pussywillow"
                    $ cat = Character("[cat_name]")
                    player_name "O que você acha de... [cat]?"
                    player_name "Você gostou?"
                    show cat 12
                    cat "Meow"
                    show cat 14
                    player_name "heh, certo. [cat]!"
                    show cat 15
                    cat "Prrrr"
                    show cat 16
                    pause
                    show cat 14
                    player_name "Vamos [cat], vamos para casa!"
                    show popup_cat at truecenter with dissolve
                    $ M_player.set("pet cat", True)
                    pause
                    hide popup_cat with dissolve
                "Deixar ela aqui.":

                    show player 10 at left
                    show cat 5
                    player_name "Hmm, desculpa, gatinha."
                    player_name "Acho que [mom_name] não ficaria feliz se levasse você para casa."
                    show player 11
                    show cat 4
                    cat "Meow"
                    show player 10
                    show cat 5
                    player_name "Pelo menos te trouxe um pouco de comida..."
                    show player 11
                    show cat 4
                    cat "Brrrep"
                    show player 10
                    show cat 5
                    player_name "Você é uma boa garota."
                    player_name "Cuide-se, ok?"
                    show player 11
                    show cat 4
                    cat "Meow"
    hide cat
    hide player
    with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
