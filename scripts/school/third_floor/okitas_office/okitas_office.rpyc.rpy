default okita_office_first_visit = True

label okita_office_dialogue:
    $ location_count = "Mrs Okita's Office"
    if okita_office_first_visit:
        $ okita_office_first_visit = False
        scene school_office4_b with fade
        show player 14 with dissolve
        player_name "!!!"
        player_name "Não sabia que a {b}Sra. Okita{/b} teria tantas ferramentas aqui."
        show player 12
        player_name "Hmm..."
        player_name "Esses planos."
        player_name "Parece que ela está trabalhando em algo..."
        hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
