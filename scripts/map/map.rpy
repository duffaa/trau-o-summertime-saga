label map_dialogue:
    $ location_count = "Town Map"
    if gTimer.gameDay() > 1:
        $ tick_skip_active = True
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)

        if June.started(june_mc_help):
            scene outside_school_b
            show player 10
            with dissolve
            player_name "Eu deveria falar para o {b}Erik{/b} que não vai dar certo com a {b}June{/b}..."
            player_name "... e que eu vou passar um tempo com ela."
            player_name "Ele vai ficar triste."
            hide player
            $ june_mc_help.finish()

        elif June.started(june_erik_help):
            scene outside_school_b
            show player 17
            with dissolve
            player_name "Eu deveria falar ao {b}Erik{/b} as boas notícia!"
            player_name "Ele ficará tão animado com isso!"
            show player 14
            player_name "{b}June{/b} parece ser perfeita para ele!"
            hide player
            $ june_erik_help.finish()

        elif erik.in_progress(erik_intro):
            scene event01
            show erik 4 at right with dissolve
            eri "Eae, {b}[firstname]{/b}!"
            show player 10 at left with dissolve
            show erik 1 at right
            player_name "Ah... Oi..."
            show erik 4 at right
            eri "Como foi seu primeiro dia de volta?"
            show player 37 at left
            show erik 1 at right
            player_name "Ugh... Nem quero falar sobre isso."
            show erik 5 at right
            eri "Entendo..."
            show player 5 at left
            eri "O que você está fazendo agora?"
            show erik 1 at right
            show player 26 at left
            player_name "Eu disse para minha mãe que eu ia visitar a {b}tia Diane{/b}."
            player_name "Ela tem um pequeno {b}trabalho{/b} pra mim, para ganhar dinheiro, e..."
            show erik 3 at right
            show player 13 at left
            eri "Cara... Queria ter um emprego..."
            show erik 4 at right
            eri "Um trabalho que eu pudesse sentar na frente do computador e jogar o dia todo, heh..."
            show erik 1 at right
            show player 14 at left
            player_name "Oh! Falando em computador... Acho que o meu está {b}quebrado{/b}"
            show player 35 at left
            player_name "Acho que tenho que mudar umas peças, ou algo do tipo..."
            show player 12 at left
            player_name "Você conhece uma loja que eu possa comprar?"
            show erik 4 at right
            show player 1 at left
            eri "Hmmm... Geralmente eu compro as peças no {b}CONSUM-R{/b} lá no {b}shopping{/b}."
            eri "Eles vendem várias coisas por um bom preço."
            show erik 1 at right
            show player 14 at left
            player_name "Beleza, vou dar uma olhada!"
            show erik 7 at right
            show player 36 at left
            eri "Até mais!"
            hide erik 7 at right with dissolve
            hide player 36 at left with dissolve

            show unlock15 at truecenter with dissolve
            $ loc_aunt_unlocked = True
            $ renpy.pause()
            hide unlock15 with dissolve

            show unlock16 at truecenter with dissolve
            $ loc_mall_unlocked = True
            $ renpy.pause()
            hide unlock16 with dissolve

            show unlock48 at truecenter with dissolve
            $ loc_beach_unlocked = True
            $ renpy.pause()
            hide unlock48 with dissolve

            show unlock46 at truecenter with dissolve
            $ loc_treehouse_unlocked = True
            $ renpy.pause()
            hide unlock46 with dissolve

            show unlock49 at truecenter with dissolve
            $ loc_hill_unlocked = True
            $ renpy.pause()
            hide unlock49 with dissolve

            show popup_warehouse at truecenter with dissolve
            $ loc_warehouse_unlocked = True
            $ renpy.pause()
            hide popup_warehouse with dissolve

            if quest05 not in completed_quests:
                $ quest_list.append(quest05)
            $ erik.complete_events(erik_intro)
            $ event_outside_school_count = 0
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label night_sleep_map:
    scene townmap_night
    player_name "Não posso ir lá de noite!"
    $ callScreen("Town Map")

label sleep_locked:
    scene expression gTimer.image("townmap{}")
    player_name "Não posso dormir agora."
    $ callScreen("Town Map")

label weekend_locked:
    scene townmap
    player_name "Não preciso vir aqui, está fechado nos finais de semana."
    $ callScreen("Town Map")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
