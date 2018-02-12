label cafeteria_dialogue:
    $ location_count = "Cafeteria"
    if quest09 in quest_list and quest09 not in completed_quests and quest09_1 == False and quest09_2 == False and quest09_3 == False:
        scene cafeteria_b
        show player 163 at left with dissolve
        show annie 3 at right with dissolve
        ann "O que está acontecendo aqui??"
        show annie 1
        show player 164
        player_name "Oi, {b}Annie{/b}! Eu uh..."
        show annie 9
        player_name "Eu deveria entregar isso na cantina."
        player_name "É uma entrega de {b}leite{/b}!"
        show annie 4
        show player 163
        ann "Eu sei o que é isso. Eu tenho olhos."
        ann "O que eu não entendi, é por que vocẽ está entregando isso."
        show annie 1
        show player 164
        player_name "Ah, é da minha {b}tia{/b}..."
        player_name "Ela não ia conseguir fazer sozinha, então ela me perguntou se eu podia fazer."
        player_name "Aqui está o {b}recibo{/b}!"
        show annie 12
        show player 163
        ann "Hmm..."
        show annie 13
        ann "Não posso aceitar."
        ann "Você tem que entregar para a diretora {b}Smith{/b} na {b}diretoria{/b}."
        show annie 6
        show player 164
        player_name "Mas-"
        show player 163
        show annie 5
        ann "Não posso confiar em alguém que não tem permissão para entregas!"
        ann "Se a {b}Sra. Smith{/b} aprovar, eu aceito."
        show annie 6
        show player 164
        player_name "Tá bom então..."
        $ quest09_1 = True
        $ lock_ui()

    elif quest09 in quest_list and quest09 not in completed_quests and quest09_2 == True:
        scene cafeteria_b
        show player 164 at left with dissolve
        show annie 1 at right with dissolve
        player_name "Pronto!"
        show annie 9
        show player 163
        ann "..."
        show annie 3
        ann "{b}Sra. Smith{/b} pegou o {b}recibo{/b}?"
        show annie 1
        show player 164
        player_name "Sim, ela tava... meio... ocupada. Mas ela dise que eu devia entrega para você."
        show annie 5
        show player 163
        ann "Entendi..."
        show annie 15
        show player 1
        ann "Então eu vou aceitar."
        show annie 14
        show player 17
        player_name "Obrigado, {b}Annie{/b}!"
        hide player
        hide annie
        with dissolve
        $ inventory.items.remove(milk_carton)
        $ quest09_2 = False
        $ quest09_3 = True
        $ unlock_ui()

    elif not erik.known(erik_favor):
        scene cafeteria_b
        show player 2 at left with dissolve
        show kevin 1 at right with dissolve
        player_name "Eae, {b}Kevin{/b}!"
        show player 1 at left
        show kevin 2 at right
        kev "Eae, cara..."
        show kevin 1 at right
        show player 10 at left
        player_name "Você está trabalhando na cantina..."
        show kevin 2 at right
        show player 13 at left
        kev "Uhum! Tenho mais dois meses nessa porcaria."
        show kevin 1 at right
        show player 17 at left
        player_name "Que merda."
        show kevin 2 at right
        show player 1 at left
        kev "Pois é, mas o que eu posso fazer?"
        kev "Além do mais, {b}Dexter{/b} está enchendo o saco de vocês?"
        show kevin 1 at right
        show player 24 at left
        player_name "Sim, ele e a {b}Roxxy{/b} estão sempre na nossa cola..."
        show player 26 at left
        player_name "Mas não é nada. Eu não me importo no que eles dizem."
        show kevin 3 at right
        show player 11 at left
        kev "Cara, você deve se defender."
        show kevin 1 at right
        show player 10 at left
        player_name "Eu prefiro só evitar, sabe?"
        player_name "Não tem sentido de querer brigar com um cara que é o dobro do meu tamanho."
        show kevin 3 at right
        show player 11 at left
        kev "Vocẽ não pode deixar ele te dominar. Como você quer sobreviver na escola assim?"
        show kevin 1 at right
        show player 24 at left
        player_name "Eu sou muito fraco para fazer algo."
        show kevin 4 at right
        show player 11 at left
        kev "Hmm... Talvez você devesse tentar melhorar."
        show kevin 1 at right
        show player 10 at left
        player_name "Como assim?"
        show kevin 4 at right
        show player 1 at left
        kev "Eu poderia te ajuar na {b}academia{/b}..."
        kev "Tipo, te ajudar enquanto você está levantando peso, e te mostrar alguns truques."
        show kevin 2 at right
        show player 34 at left
        kev "Mas você tem que {b}achar um substituto{/b} para mim aqui na cantina."
        kev "Não aguento mais isso."
        show player 34 at left
        show kevin 1 at right
        player_name "Certo! Vou tentar achar alguém que possa te substituir."
        show kevin 2 at right
        show player 1 at left
        kev "Certo, cara. Tenho que voltar ao trabalho. Até mais tarde!"
        show kevin 1 at right
        show player 36 at left
        player_name "Até mais, {b}Kevin{/b}!"
        hide player
        hide kevin
        with dissolve
        $ erik.add_event(erik_favor)

    elif erik.known(erik_favor) and not erik.completed(erik_favor_2):
        scene cafeteria_b
        show player 2 at left with dissolve
        show kevin 1 at right with dissolve
        player_name "Hey, {b}Kevin{/b}!"
        show kevin 2 at right
        show player 1 at left
        kev "Eae, cara..."
        kev "Você achou alguém para me substituir?"
        menu:
            "Acho qu sim!" if erik.known(erik_favor_2):
                show player 14 at left
                show kevin 1 at right
                player_name "Acho que achei alguém para te substituir!"
                show kevin 2 at right
                show player 1 at left
                kev "Caraca! Isso é incrível!"
                kev "Quem vai me substituir?"
                show kevin 1 at right
                show player 17 at left
                player_name "O {b}Erik{/b}... E eu tive que subornar ele..."
                show kevin 2 at right
                show player 1 at left
                kev "Haha! Certo, valeu, cara!"
                kev "Agora posso ficar mais tempo na {b}academia{/b}!"
                show kevin 6 at right
                show player 11 at left
                kev "...E não vou precisar fazer mais isso!"
                show kevin 5 at right
                show player 12 at left
                player_name "Trabalhar aqui é desagradável..."
                show kevin 12 at right
                show player 1 at left
                kev "Hey! Se você procurar na acdemia, você vai saber onde me encontrar!"
                show kevin 5 at right
                show player 14 at left
                player_name "Beleza! Eu vou!"
                $ erik_favor_2.finish()
            "Ainda não.":

                show kevin 1 at right
                show player 26 at left
                player_name "Ainda não, mas eu vou continuar procurando!"
                show kevin 3 at right
                show player 1 at left
                kev "Certo..."
        hide player
        hide kevin
        with dissolve

    elif is_here("erik") and erik.completed(erik_favor_2):
        scene cafeteria_b
        show player 36 at left with dissolve
        show erik 11 at right with dissolve
        player_name "Eae, {b}Erik{/b}!"
        show erik 12 at right
        show player 1 at left
        eri "Eae, {b}[firstname]{/b}!"
        show erik 11 at right
        show player 21 at left
        player_name "Então... Como está trabalhar na cantina?"
        show erik 12 at right
        show player 13 at left
        eri "Poderia ser pior."
        eri "Eu geralmente não faço muita durante o almoço na escola..."
        show erik 11 at right
        show player 17 at left
        player_name "Feliz que você esteja bem com isso."
        show erik 12 at right
        show player 1 at left
        eri "Eu vou para casa jogar {b}Sea Dogs SAGA{/b}!"
        show erik 11 at right
        show player 14 at left
        player_name "Beleza! Vou deixar você voltar aos seus deveres..."
        show erik 11 at right
        show player 1 at left
        eri "Volto mais tarde!"
        hide erik
        hide player
        with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
