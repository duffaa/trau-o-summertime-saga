default teach_lounge_first_visit = True

label teach_lounge_dialogue:
    $ location_count = "Teacher's Lounge"
    if teach_lounge_first_visit:
        $ teach_lounge_first_visit = False
        scene school_lounge_b with fade
        show player 14 with dissolve
        player_name "Esta deve ser a sala dos professores."
        player_name "Seu pequeno refúgio privado de meus colegas de classe."
        hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
