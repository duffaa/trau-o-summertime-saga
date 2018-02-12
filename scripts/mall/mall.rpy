label mall_dialogue:
    $ location_count = "Mall"
    $ playSound("<loop 2 to 59>audio/ambience_mall.ogg", 1.0)
    if mall_count == 0:
        scene mall
        show player 14 with dissolve
        player_name "( Adoro o shopping! )"
        show player 17
        player_name "( Você pode comprar todo tipo de coisas, tem até um cinema! )"
        hide player 17 with dissolve
        $ mall_count = 1

    elif M_mom.get_state() == S_mom_mall_outing:
        scene location_mall_blur
        show player 13 at left with dissolve
        show mom 165 at Position(xpos=.75, ypos=1.0) with dissolve
        mom "Obrigada novamente por ter vindo comigo, querido!"
        show player 14
        show mom 164
        player_name "Sem problemas, [mom_name]. Estou me divertindo!"
        show player 13
        show mom 166
        mom "Eu também! Faz tanto tempo que nós dois não saímos e passamos algum tempo juntos..."
        show mom 164
        mom "..."
        show mom 165
        mom "Há alguma loja que você gostaria de visitar enquanto estamos aqui?"
        show player 14
        show mom 164
        player_name "Hmm, não, na verdade não."
        show player 13
        show mom 165
        mom "Tudo bem, a mãe de Erik estava me contando sobre esta nova loja que abriu recentemente."
        mom "Ela disse que se chamava, {b}Cupid{/b}."
        mom "Deveriamos ir ver! O que você acha?"
        show player 14
        show mom 164
        player_name "Claro, [mom_name]. Sem problemas."
        show player 13
        show mom 165
        mom "... Acho que ela disse que fica no {b}segundo andar{/b}."
        show mom 167 at right with dissolve
        mom "Me siga, querido."
        hide player
        hide mom
        with dissolve
        $ M_mom.trigger(T_mom_mall_arrival)
    $ callScreen(location_count)

label mom_mall_outing_block:
    if location_count == "Mall":
        scene location_mall_blur
    elif location_count == "Mall Second Floor":
        scene location_mall_upstairs_blur
    show player 1
    player_name "Hmm, eu deveria ir para uma loja chamada, {b}Cupid.{/b}"
    show player 4
    player_name "[mom_name] disse que ela está no {b}segundo andar{/b}."
    $ callScreen(location_count)

label rump_dialogue:
    scene mall_closeup
    show xtra 18 zorder 2 at left
    with dissolve
    player_name "( Parece que o novo prefeito está fazendo um discurso hoje. )"
    show rump 1 at Position(xpos = 330)
    show iwanka 1 at Position(xpos = 860)
    with dissolve
    pause
    show rump 2
    rump "Boa tarde, cidadães da Summerville."
    rump "É através do seu trabalho árduo e dedicação que eu posso estar aqui hoje e dizer..."
    rump "Estou muito honrado em ser eleito como o prefeito da nossa grande cidade."
    show rump 4 at Position(xpos = 374)
    show iwanka 2
    rump "Junto com minha filha, Iwanka."
    rump "Quem será responsável por todos os assuntos relacionados aos assuntos estrangeiros."
    show rump 3 at Position(xpos = 266)
    show iwanka 1
    rump "E como prometido durante a minha campanha..."
    rump "Vamos fazer esse shopping patética e transformá-lo em um ótimo {b}MALL{/b}!"
    show rump 2 at Position(xpos = 330)
    rump "Não será fácil!"
    rump "Não será rṕaido!"
    show rump 3 at Position(xpos = 266)
    rump "Mas como prefeito, eu garanto que a nossa maravilhosa cidade se torna {b}GRANDE NOVAMENTE!{/b}"
    hide rump
    hide iwanka
    with dissolve
    player_name "( Ele certamente sabe usar as palavras... )"
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
