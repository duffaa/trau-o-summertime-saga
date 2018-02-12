label harolds_office:
    $ location_count = "Harold's House Office"
    if M_mia.get_state() == S_mia_midnight_help:
        scene mia_house_office_n_b
        player_name "{b}Mia{/b} não está aqui... E não vejo nenhuma chave."
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
