default ross_office_first_visit = True

label ross_office_dialogue:
    $ location_count = "Mrs Ross' Office"
    if ross_office_first_visit:
        $ ross_office_first_visit = False
        scene school_office3_b with fade
        show player 11 with dissolve
        player_name "*Sniff*"
        show player 12
        player_name "Que cheiro é esse?"
        player_name "Parece...incenso...e algumas ervas..."
        player_name "{b}Sra. Ross{/b} deve ficar um bom tempo aqui."
        hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
