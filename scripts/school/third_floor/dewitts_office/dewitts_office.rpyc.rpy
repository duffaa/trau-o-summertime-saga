default dewitt_office_first_visit = True

label dewitt_office_dialogue:
    $ location_count = "Mrs Dewitt's Office"
    if dewitt_office_first_visit:
        $ dewitt_office_first_visit = False
        scene school_office2_b with fade
        show player 14 with dissolve
        player_name "Uau... A sala da {b}Sra. Dewitt{/b} é bem arrumada!"
        player_name "Parece que ela traz estudantes para aulas particulares..."
        player_name "...E ela tem um sofá aqui!!"
        hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
