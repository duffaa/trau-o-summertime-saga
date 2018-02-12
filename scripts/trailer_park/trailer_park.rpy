default trailer_interior_first_visit = True

label trailer_park_dialogue:
    $ location_count = "Trailer Park"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label trailer_interior_dialogue:
    $ location_count = "Trailer Interior"
    if not gTimer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")
    if trailer_interior_first_visit:
        $ trailer_interior_first_visit = False
        scene expression gTimer.image("trailer_interior{}")
        show player 10 with dissolve
        player_name "( Aqui é onde a {b}Roxxy{/b} mora? )"
        player_name "( Tem lixo por todo lado... )"
        hide player with dissolve
    $ callScreen(location_count)

label trailer_bedroom_dialogue:
    $ location_count = "Trailer Bedroom"
    $ callScreen(location_count)

label roxmom_dialogue:
    scene expression gTimer.image("trailer_interior_c{}")
    if not crystal.known(crystal_intro):
        show player 11 at left
        show roxmom 2 at right
        with dissolve
        crys "Ora ora!!"
        crys "Quem nós temos aqui?"
        show roxmom 1
        show player 10
        player_name "Huh?"
        show player 5
        show roxmom 3 with dissolve
        crys "Qual namorado você é? {b}Dexter{/b}?"
        show roxmom 1 with dissolve
        show player 12
        player_name "Não sou o {b}Dexter{/b}..."
        show player 11
        show roxmom 4 with dissolve
        crys "*Gulp*"
        show roxmom 3 with dissolve
        crys "Você é amigo da minha filha?"
        show roxmom 1 with dissolve
        show player 10
        player_name "Suponho que você poderia dizer isso."
        show player 5
        show roxmom 2
        crys "Ela geralmente não tem amigos homens."
        show player 11
        crys "Ela gosta de homens por.... outros motivos. Assim como sua mãe!"
        show roxmom 1
        show player 22
        player_name "..."
        show roxmom 2
        crys "E então, garoto?"
        show player 5
        $ crystal.add_event(crystal_intro)
        $ crystal_intro.finish()
    else:

        show player 5 at left
        show roxmom 3 at right
        with dissolve
        crys "É o namorado da minha garotinha novamente."
        show roxmom 1 with dissolve
        show player 10
        player_name "Já te disse, não sou-"
        show player 5
        show roxmom 2
        crys "Não importa, garotinho."
        show roxmom 4 with dissolve
        crys "*Gulp*"
        show roxmom 2 with dissolve
        crys "So what do you want?"
    show roxmom 1
    menu roxmom_dialogue_repeat:
        "Onde está a Roxxy?":
            show player 10
            player_name "Você sabe onde eu poderia achar a {b}Roxxy{/b}?"
            show player 5
            show roxmom 3 with dissolve
            crys "Hah! Você acha que eu cuido da minha filha?"
            show roxmom 1 with dissolve
            show player 10
            player_name "Hmm..."
            show player 5
            show roxmom 2
            crys "Ela está fazendo coisas..."
            crys "...Mas, normalmente ela está na {b}escola{/b} ou no {b}shopping{/b}."
            show roxmom 1
            show player 14
            player_name "Ah. Entendi. Valeu!"
            show player 13
            show roxmom 2
            crys "Algo mais?"
            show roxmom 1
            jump roxmom_dialogue_repeat
        "Pai da Roxxy.":

            show player 10
            player_name "Qual é o pai da {b}Roxxy{/b}?"
            show player 11
            show roxmom 2
            crys "Hah! Ela não tem pai!"
            crys "Eu criei sozinha mesmo."
            show roxmom 1
            show player 10
            player_name "Entendi."
            show player 11
            show roxmom 2
            crys "Para dizer a verdade, não me lembro quem era..."
            show roxmom 4 with dissolve
            crys "*Gulp*"
            show roxmom 2 with dissolve
            crys "...Então, seu pai pode ser qualquer um, até onde eu sei."
            show roxmom 1
            show player 22
            player_name "!!!"
            show roxmom 2
            crys "Algo mais que você quer falar?"
            show player 5
            show roxmom 1
            jump roxmom_dialogue_repeat
        "Nada.":

            show player 10
            player_name "Ah, nada."
            player_name "Eu só estava de passagem..."
            show player 11
            show roxmom 2
            crys "Bem, eu recebi uma visita rápida, então por que não sai logo."
            show roxmom 1
            show player 10
            player_name "Perdão. Estou indo."
            player_name "Tchau!"
            hide player
            hide roxmom
            with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
