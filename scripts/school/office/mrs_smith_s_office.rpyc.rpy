label office_dialogue:
    $ location_count = "Mrs Smith's Office"
    if quest09_1 == True and quest09 not in completed_quests:
        scene office_clear
        show principal 22 at Position(xpos = 200, ypos = 764)
        player_name "!!!"
        window hide
        pause
        show principal 23
        window hide
        pause
        show principal 22
        window hide
        pause
        show principal 23
        window hide
        pause
        show principal 24 with hpunch
        smi "!!!"
        show principal 25
        smi "O que você está faznedo na {b}MINHA SALA{/b}??"
        show principal 24
        player_name "Eu.. eu queria entregar esse {b}recibo{/b} da entrega."
        show principal 25
        smi "Você idiota! Você não vê que estou ocupada??"
        show principal 24
        player_name "Desculpa, {b}Sra. Smith{/b}..."
        show principal 25
        smi "Ninguém te ensinou a {b}BATER{/b}?!"
        show principal 24
        player_name "..."
        show principal 25
        smi "Entregue o {b}recibo{/b} no meu {b}armário verde{/b}."
        show principal 24
        player_name "Sim, {b}Sra. Smith{/b}! Já vou..."

    elif office_count == 0:
        scene office
        show principal 5 at right with dissolve
        show player 1 at left with dissolve
        smi "O que você está fazendo aqui?!"
        show player 11 at left
        show principal 3 at right
        player_name "Oh... umm..."
        show player 21 at left
        player_name "Eu estava... procurando pelo banheiro!"
        show player 22 at left
        show principal 4 at right
        smi "Não se faça de burro, {b}[firstname]{/b}!"
        smi "Eu não te disse antes pra ir pra escola??!"
        show player 10 at left
        show principal 1 at right
        player_name "Bom..."
        show player 22 at left
        show principal 2 at right
        smi "Agora saia da minha {b}SALA{/b}!!!"
        hide player 22 at left with dissolve
        hide principal 2 at right with dissolve

    elif office_count == 1:
        scene office
        show principal 6 at right
        show player 1 at left
        with dissolve
        ann "{b}Sra. Smith{/b}?"
        show principal 7 at right
        smi "O que foi??"
        show principal 6 at right
        ann "Relatando infratores repetentes conforme você requisitou!"
        show principal 9 at right
        show player 13 at left
        smi "Esse... jovem aqui?"
        show principal 8 at right
        ann "Sim, senhora!"
        show principal 9 at right
        smi "Hmmm... Você deve ser o {b}[firstname]{/b}, certo?"
        show player 10 at left
        player_name "Uh.. Sim, senhora!"
        show player 5 at left
        smi "Você é quem estava causando problemas no vestiário..."
        smi "...e dando o que falar..."
        show principal 7 at right
        smi "O que aconteceu, na verdade, {b}Annie{/b}?"
        show principal 6 at right
        ann "Bom, Ele... ele... Ele está mostrando partes inadequadas do corpo para as garotas no vestiário, senhora."
        show principal 9 at right
        smi "É verdade?"
        show player 10 at left
        player_name "Bom... Eu posso explicar-"
        show player 22 at left
        show principal 10 at right with hpunch
        smi "{b}SILÊNCIO{/b}!!!"
        show principal 9 at right
        show player 5 at left
        smi "...Preciso ver exatamente o que aconteceu. Mostre-me o que você fez, agora."
        show principal 6 at right
        ann "Senhora, não vai funcionar..."
        ann "Parece que só funciona quando... ele vê uma mulher {b}nua{/b}, senhora."
        show principal 7 at right
        smi "Então o que você está esperando, {b}Annie{/b}?"
        smi "Você vai ajuda-lo com isso."
        show principal 11 at right
        show player 11 at left
        ann "{b}O quê??!{/b}"
        show principal 12 at right
        smi "Você foi quem testemunhou e relatou a infração..."
        smi "...É seu {b}dever{/b} cuidar disso!"
        player_name "Não precisamos fazer isso-"
        show principal 10 at right
        show player 22 at left
        smi "Ninguém vai sair até um relatório completo! Faça isso, ou os dois vão para a {b}DETENÇÃO{/b}!!!"
        show principal 13 at right
        ann "..."
        show player 8 at left
        show principal 14 at right
        window hide
        pause
        show player 63 at left
        show principal 15 at right
        window hide
        pause
        show principal 16 at right
        show player 64 at left
        smi "Olha para esses {b}peitos firmes{/b} dela..."
        show principal 17 at right
        smi "Você não quer... chupar eles? {b}[firstname]{/b}?"
        show player 65 at left
        player_name "..."
        show player 66 at left
        window hide
        pause
        show player 66 at left with hpunch
        window hide
        pause
        show player 67 at left
        smi "Aí está..."
        show principal 18 at right
        smi "Pronto, {b}Annie{/b}. Você pode ir..."
        show principal 5 at right with dissolve
        smi "Então!..."
        smi "Isto é o que eu tenho ouvido sobre esse tempo todo."
        hide player 67 at left
        show principal 19 at left
        with dissolve
        smi "Você fez uma boa reputação ao redor..."
        smi "E eu entendo por que..."
        smi "...isso foi uma..."
        show principal 20 at left
        window hide
        pause
        show principal 21 at left with hpunch
        window hide
        pause
        smi "...distração!"
        show player 69 at left
        show principal 1 at right
        with dissolve
        player_name "Desculpa, senhora!"
        player_name "Não vai acontecer de novo, juro!"
        show principal 5 at right
        show player 68 at left
        smi "Certo, jovem: Aqui está o acorod..."
        smi "Não o mando para a detenção, desde que você mantenha esse... \"problema\" para... você."
        smi "Minha prioridade é a ordem e a disciplina nesta escola, e eu quero manter assim!"
        show principal 1 at right
        show player 69 at left
        player_name "Sim, {b}Sra. Smith{/b}!"
        show principal 2 at right
        show player 68 at left
        smi "Agora, saia da minha {b}SALA{/b}!!"
        hide player 68 at left with dissolve
        hide principal 2 at right with dissolve
        $ office_count = 0
    $ callScreen(location_count)

label desk03_locked_dialogue:
    scene office
    show player 30 at left
    player_name "Hmmm... O que será que tem ali?"
    show player 22 at left with hpunch
    show principal 4 at right with dissolve
    smi "O que você está fazendo?"
    show principal 1 at right
    show player 29 at left
    player_name "Oh, Desculpa... Só estava olhando!"
    show player 3 at left
    show principal 5 at right
    smi "Se eu ver você fazer isso {b}DE NOVO{/b}..."
    show principal 2 at right
    smi "...pode ter certeza, você vai ficar o resto do ano na {b}DETENÇÃO{/b}!!!"
    $ callScreen(location_count)

label principle_drawer:
    scene principle_drawer
    show expression "objects/object_papers_01.png" at Position(xpos = 378, ypos = 526)
    player_name "..."
    player_name "O que são essas... coisas de couro... aqui?"
    player_name "estranho..."
    call screen principle_drawer

label milk_delivery:
    scene office with None
    show player 167f at right
    show titty 1 at left
    show principal 28f at Position (xpos = 470)
    with dissolve
    smi "Ah, ótimo."
    smi "São as novas {b}encomendas de leite{/b}?"
    show player 168f
    show principal 26f at Position (xpos = 415)
    player_name "Umm... sim."
    show principal 27f
    show player 163f
    smi "Eu provei o último lote..."
    smi "Sâo bem... gostosos. Você tem sorte de eu estar de bom humor."
    smi "Por favor, diga para a fornecedora que eu quero o dobro da próxima vez."
    smi "Estamos ficando sem. Os alunos amaram!"
    show principal 26f
    show player 164f
    player_name "Farei! Onde posso colocar esse lote?"
    show principal 27f
    show player 163f
    smi "Entregue para a {b}Annie{/b}, ela cuida do resto."
    show principal 4f at Position (xpos = 470)
    show player 167f
    smi "Agora, saia da minha sala, tenho uns trabalhoas que ainda não acabaram aqui."
    show principal 26f at Position (xpos = 415)
    show player 168f
    player_name "Sim, {b}Sra. Smith{/b}!"
    hide principal
    hide titty
    hide player
    with dissolve
    $ quest09_1 = False
    $ quest09_2 = True
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
