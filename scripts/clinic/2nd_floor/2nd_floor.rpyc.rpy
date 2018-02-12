label hospital_second_floor_dialogue:
    $ location_count = "Hospital 2nd Floor"
    if mrsj.started(mrsj_sex_ed) and not Roz.completed(roz_storage):
        scene expression gTimer.image("hospital_second{}_b")
        if Roz.started(roz_storage) and hospital_access_card in inventory.items:
            show player 410
            with dissolve
            player_name "( Deve ser isso! )"
            player_name "( Deixa eu ver se funciona... )"

        elif Roz.started(roz_storage):
            show player 12
            with dissolve
            player_name "( A recepcionista deve ter uma cópia de todas as chaves... )"
            player_name "( Talvez eu pudesse achar na mesa dela. )"
        else:

            show player 35
            with dissolve
            player_name "Hmm..."
            player_name "( Onde será que guardam todos os remédios... )"
            show player 30
            player_name "( Eu deveria ir até a {b}sala de armazenamento{/b}. )"
        hide player
        with dissolve
    $ callScreen(location_count)

label hospital_second_floor_phone_dialogue:
    scene hospital_phone
    pause
    if mrsj.started(mrsj_sex_ed) and Roz.completed(roz_intro) and Roz.known(roz_storage) and not Roz.known(roz_trick):
        show player 404 with dissolve
        pause
        show player 406 with dissolve
        player_name "Oi!"
        pause
        player_name "Eu... Umm... Tem uma emergência no segundo andar!!"
        show player 407
        pause
        show player 408
        pause
        show player 407
        pause
        pause
        show player 406
        player_name "Ah, sim, o paciente não tem registro..."
        show player 407
        pause
        pause
        show player 406
        player_name "Sim, é urgente!"
        show player 408
        pause
        pause
        show player 407
        pause
        show player 406
        player_name "Obrigado..."
        show player 407
        pause
        show player 405 with dissolve
        player_name "( Isso deve funcionar... )"
        player_name "( Vou ver se ela está na mesa... )"
        hide player
        with dissolve
        $ Roz.add_event(roz_trick)
    else:
        player_name "( Não preciso ligar para ninguém. )"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
