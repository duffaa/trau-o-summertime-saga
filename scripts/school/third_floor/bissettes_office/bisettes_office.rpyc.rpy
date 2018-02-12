default bissette_office_first_visit = True

label bissette_office_dialogue:
    $ location_count = "Mrs Bissette's Office"
    if bissette_office_first_visit:
        $ bissette_office_first_visit = False
        scene school_office1_b with fade
        show player 10 with dissolve
        player_name "A sala da {b}Sra. Bisette{/b} parece tão...francesa!"
        show player 14
        player_name "Talvez um dia possamos fazer uma viagem escolar com ela..."
        hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
