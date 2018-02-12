label church_bell_dialogue:
    $ location_count = "Church Cloister Bell"
    $ callScreen(location_count)

label church_bell:
    scene location_church_bell_closeup
    if M_aqua.get_state() == S_aqua_bell_search:
        player_name "Esse sino é enorme!"
        player_name "( Como que Ben Dover está ligado a isso? )"
        player_name "( Talvez ele tenha ajudado a construir? )"
        player_name "( ...Com certeza, parece muito antigo. )"
        player_name "( e há uma gravura sobre isso também, assim como na lápide! )"
        player_name "Hmm..."
        player_name "( Parece algum {b}feito de pedra{/b}, com {b}arcore{/b} ao redor e com a {b}lua{/b} brilhando. )"
        player_name "( Uma das árvore tem um {b}buraco{/b}. )"
        player_name "( O que será que é isso? )"
        player_name "( Onde eu posso achar algo parecido com isso no Summerville? )"
        $ M_aqua.trigger(T_aqua_bell_engraving)
    else:

        pause
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
