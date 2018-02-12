init python:
    class ComicItem:
        def __init__(self, item, name = "", image = "", popup = "", idle = "", hover = "", price = 0, category = "", purchased = False):
            self.name = name
            self.image = image
            self.popup = popup
            self.idle = idle
            self.hover = hover
            self.price = price
            self.category = category
            self.item = item
            self.purchased = purchased


    class ComicStore (object) :
        def __init__(self):
            self.items = []

default comic_first_visit = True

label comic_store_dialogue:
    $ location_count = "Comic Store"
    if June.started(june_cosplay) and orcette_cosplay not in inventory.items:
        scene comic_b
        show player 14
        with dissolve
        player_name "Parece que tem algumas trajes pendurados na parede."
        player_name "Eu deveria dar uma olhada neles..."
        player_name "... talvez eles tenham aquelas roupas de orcs."
        hide player with dissolve
    elif erik.started(erik_vr):
        scene comic_b
        if game02 in inventory.items and virtualsaga in inventory.items:
            show player 14 with dissolve
            player_name "( Acho que isso é o que o {b}Erik{/b} queria. )"
            player_name "( Vou levar para ele... )"
        else:
            show player 35 with dissolve
            player_name "( Aqui deve ter as coisas que o {b}Erik{/b} queria. )"
            show player 12 with dissolve
            player_name "( Talvez nessas prateleiras do balcão? )"
        hide player with dissolve
    elif comic_first_visit == True:
        scene comic_b
        show player 1 at left
        show tatia 3 at right
        with dissolve
        tati "Oi!"
        show tatia 2
        tati "Primeira vez na {b}Cosmic Cumics{/b}?"
        show tatia 1
        show player 29
        player_name "Umm... Sim! Não sabia que essa loja existia..."
        show tatia 2
        show player 1
        tati "Sim, abrimos recentemente!"
        show tatia 1
        show player 2
        player_name "Ah, legal!"
        player_name "Vocês vendem jogos também?"
        show tatia 3
        show player 1
        tati "Claro."
        show tatia 2
        tati "Vendemos vários produtos desde {b}jogos{/b},{b}revistas em quadrinhos{/b}, {b}roupas{/b}, {b}posters{/b} e {b}colecionáveis{/b}!"
        show tatia 1
        show player 2
        player_name "Oh. Então... coisas nerds..."
        show tatia 3
        show player 1
        tati "Isso!"
        tati "De uma olhada ao redor, e me diga se você quiser algo!"
        $ comic_first_visit = False
        hide tatia
        hide player
        hide comic_b with None
    $ callScreen(location_count)

label tatiana_dialogue:
    scene comic_c
    show xtra 17 zorder 2
    show tatia 2 zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    tati "Eai?"
    label comic_tatiana_menu:
        show tatia 1
        menu:
            "Você me parece familiar.":
                show tatia 1
                show player 4
                player_name "Sinto que já te vi em algum lugar."
                show tatia 3
                show player 1
                tati "Sim. Provavelmente me viu na internet..."
                show tatia 2
                tati "Eu faço {b}transmissões de jogos{/b} e posto no meu {b}canal no YouTube{/b}."
                show tatia 4
                tati "Eu suo o nick de {b}PureRuby87{/b}."
                show tatia 5
                show player 17
                player_name "Ah, sim! Meu amigo {b}Erik{/b} adora suas coisas!"
                show player 21
                player_name "Ele fica falando dos seus vídeos e da sua {b}gigante{/b}... err... quantidade de fãs!"
                show tatia 3
                show player 1
                tati "Aww... Vocês são tão legais."
                show tatia 2
                tati "Tem algo a mais que você queira conversar?"
                jump comic_tatiana_menu
            "Algum sugestão?":

                show tatia 1
                show player 2
                player_name "Você tem alguma sugestão? Produtos que você recomenda?"
                show player 1
                tati "Hmmm..."
                show tatia 2
                tati "Well, eu adoro os {b}cosplays{/b}!"
                show tatia 4
                tati "Eu gosto de vestir {b}roupas sexys{/b}. Temos algumas novas roupas que acabaram de chegar!"
                show tatia 5
                show player 21
                player_name "Oh, é? Parece interessante..."
                show tatia 4
                show player 1
                tati "É um pouco dificil de... umm... eu entrar nele."
                tati "Fazem eles tão apertados, sabe?"
                show tatia 3
                tati "Mas homens não se importam muito!"
                show tatia 5
                show player 29
                player_name "Haha. Pois é."
                show player 2
                player_name "Obrigado, vou dar uma olhada."
                jump comic_tatiana_menu
            "Achei o que eu queria.":

                show tatia 1
                show player 2
                player_name "Sim, acho que tenho tudo o que eu quero. Obrigado!"
                show tatia 2
                show player 1
                tati "Ótimo! Agradeço por comprar na {b}Cosmic Cumics{/b}..."
                show tatia 3
                show player 13
                tati "E fale ao seu amigo sobre nós!"
    hide tatia
    hide player
    hide xtra
    hide comic_c
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
