label mias_upstairs:
    $ location_count = "Mia's House Upstairs"
    if M_mia.get_state() in [S_mia_consult, S_mia_impress_harold, S_mia_parent_unblock, S_mia_strip_aftermath, S_mia_midnight_call] and gTimer.is_dark():
        scene mia_house_upstairs_n_b
        show player 1 at left
        show helen 2 at right
        with dissolve
        helen "O que você está fazneod?"
        show helen 1
        show player 22
        player_name "!!!" with vpunch
        show helen 1
        show player 10
        player_name "Eu, err-"
        show player 5
        show helen 2
        helen "Você está tentando ir ver a {b}Mia{/b}?"
        show player 10
        show helen 1
        player_name "Mas, eu não queria-"
        show player 5
        show helen 2
        helen "Você não tem nada pra fazer aqui, garoto."
        show helen 3
        helen "Fique longe da minha filha. Entendido?"
        show player 10
        show helen 1
        player_name "Sim, senhora..."
        $ location_count = "Mia's House"

    elif M_mia.get_state() in [S_mia_midnight_help, S_mia_locked_room]:
        scene mia_house_upstairs_n_b
        show player 11 with dissolve
        "*Voz abafada*"
        show player 30
        player_name "Huh?"
        player_name "( Ouvi a voz vindo do {b}quarto da esquerda{/b}... )"
        hide player with dissolve

    elif M_mia.get_state() == S_mia_unexpected_visit:
        scene mia_house_upstairs_b
        show player 30 with dissolve
        player_name "Huh?"
        show player 10
        player_name "( Ouvi essas vozes do quarto da {b}Helen{/b}... )"
        player_name "( ...{b}Mia{/b} deve estar lá com a mãe dela. )"
        hide player with dissolve
        hide player with dissolve

    elif M_helen.get_state() == S_helen_aftersex_mia_suspicious:
        scene mia_house_upstairs_n_b
        show mia 44f at right
        show player 22 at left
        with dissolve
        player_name "!!!" with hpunch
        show mia 43f
        mia "{b}[firstname]{/b}?"
        show mia 44f
        show player 29 with dissolve
        player_name "Oh... Uh... Oi!"
        show player 3
        show mia 43f
        mia "Não sabia que você estava aqui."
        show mia 44f
        show player 12 with dissolve
        player_name "Oh..."
        show player 11
        show mia 43f
        mia "E o que você está fazendo na cama da minha mãe?"
        show mia 44f
        show player 10
        player_name "Ummm... Bom... Ela..."
        player_name "...Só queria conversar comigo sobre...uhhh...coisas da bíblia."
        show player 5
        show mia 43f
        mia "Sério? Desde quando você se importa com a igreja?"
        show mia 44f
        show player 29 with dissolve
        player_name "Oh... Uh... Bom. Eu comecei a me envolver."
        player_name "Eae! Quer sair? Eu terminei de...conversar...com sua mãe."
        show player 3
        show mia 46f
        mia "Não acho que eu gostaria."
        mia "Acho que vou ficar no meu quarto um pouco."
        show mia 45f
        show player 29
        player_name "Ok..."
        player_name "Acho que vou voltar para casa então."
        show player 3
        show mia 46f
        mia "Parece bom."
        hide mia
        show player 24
        with dissolve
        player_name "...Tchau..."
        hide player with dissolve
        $ gTimer.tick()
        $ unlock_ui()
        $ M_helen.trigger(T_mia_stay_alone)
    $ callScreen(location_count)

label helens_locked_room_block:
    scene expression gTimer.image("mia_house_upstairs{}_b")
    player_name "( A porta está trancada. )"
    if M_mia.get_state() == S_mia_midnight_help:
        player_name "( Tenho que encontrar a {b}chave{/b}... )"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
