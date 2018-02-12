label donut_shop_dialogue:
    $ location_count = "Donut Shop"
    if not gTimer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ callScreen(location_count)

label donut_interior_dialogue:
    $ location_count = "Donut Shop Interior"
    $ callScreen(location_count)

label beth_dialogue:
    scene donut_c
    show beth 2 zorder 1 at right
    show xtra 27 zorder 2 at center
    show player 1 zorder 3 at left
    with dissolve
    beth "Olá, senhor!"
    show player 14
    show beth 1
    player_name "Oi."
    show player 1
    show beth 2
    beth "Está pensando em comprar algum donut?"
    show beth 1
    menu:
        "Não sei." if not M_mia.is_set("buy donuts"):
            show player 14
            player_name "Hmm... Não sei qual eu devo comprar."
            show player 1
            show beth 2
            beth "Você não sabe?"
            show player 14
            show beth 1
            player_name "Estou comprando isso para alguém como presente, mas não tenho certeza de qual ele gosta."
            show player 1
            show beth 2
            beth "Não consigo te ajudar se você não sabe o que a pessoa gostaria!"
            show player 14
            show beth 1
            player_name "Voltarei quando souber os sabores."

        "<>Quero comprar donuts! (50$)" if inventory.money < 50 and M_mia.is_set("buy donuts"):
            $ pass

        "Quero comprar donuts! (50$)" if inventory.money >= 50 and M_mia.is_set("buy donuts"):
            show player 14 at left
            show beth 1 at right
            player_name "Que comprar uma caixa pequena de donuts, por favor."
            show player 1
            show beth 2
            beth "Ótimo!"
            beth "Que tipo de cobertura e sabor você quer?"
            call screen donut_minigame
        "Não, valeu.":

            show beth 1 at right
            show player 14 at left
            player_name "Não, valeu!"
            player_name "Quem sabe outra hora..."
            show player 1
            show beth 2
            beth "Claro, até mais!"
    hide player
    hide xtra
    hide beth
    with dissolve
    $ callScreen(location_count)

label donut_buy_dialogue:
    show beth 2
    beth "Aqui vai."
    show unlock51 at truecenter with dissolve
    pause
    hide unlock51 with dissolve
    show player 17
    show beth 1
    player_name "Valeu."
    show player 1
    show beth 2
    beth "Espero que você goste!"
    hide player
    hide xtra
    hide beth
    with dissolve
    $ callScreen(location_count)

label donut_locked:
    scene expression gTimer.image("backgrounds/location_donut{}_blur.jpg")
    show player 10 with dissolve
    player_name "( Eu deveria voltar durante o dia enquanto estão abertos. )"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
