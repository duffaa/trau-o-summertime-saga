default kassy_first_visit = True

label cupid_dialogue:
    $ location_count = "Cupid"
    if M_mom.get_state() == S_mom_cupid_store:
        scene location_mall_cupid_blur
        show player 5 at left
        show mom 165f at Position(xpos=0.5, ypos=1.0)
        with dissolve
        mom "Ah, uau!"
        show mom 166f
        mom "Olha para essas coisas lindas!"
        show mom 165 at Position(xpos=0.75, ypos=1.0) with dissolve
        mom "Não é maravilhoso!?"
        show mom 164
        player_name "..."
        show player 10
        player_name "Não sei, {b}[mom_name]{/b}, parece cosias de mulheres..."
        show player 5
        show mom 165
        mom "Bom, é..."
        show mom 166
        mom "Mas eu SOU uma garota, querido."
        show mom 164
        mom "..."
        show mom 165
        mom "Além do mais, você está começando a se interessar em garotas."
        show mom 167 at right with dissolve
        mom "E se você quiser uma namorada, você terá que começar a se familiarizar com lugares como este!"
        show mom 164 at Position(xpos=0.9, ypos=1.0) with dissolve
        show player 10
        player_name "Sério?"
        show player 5
        show mom 166
        mom "Hehe, é claro!"
        show mom 165
        mom "Por que você não me ajuda a achar um. Acho que vai ser bom para você praticar!"
        show player 10
        show mom 164
        player_name "Praticar?"
        show player 5
        show mom 166
        mom "É!"
        show mom 165
        mom "{b}[firstname]{/b}, {b}dar presentes{/b} é muito importante em um {b}encontro{/b}."
        show player 43
        show mom 164
        player_name "Sim, eu sei, {b}[mom_name]{/b}!"
        show player 5
        show mom 165
        mom "Ok, bom... Imagine que você esteja saindo comigo."
        show mom 164
        player_name "..."
        show player 12
        player_name "Sério?"
        show player 11
        show mom 166
        mom "Hehe, Siiiim!"
        show mom 165
        mom "Que tipo de presente você acha que eu gostaria?"
        show player 10
        show mom 164
        player_name "Hmm, não sei."
        show player 11
        show mom 165
        mom "De uma olhada ao redor e veja se você encontra algo!"
        mom "Vou estar esperano bem aí."
        show player 10
        show mom 164
        player_name "Beleza."
        hide mom with dissolve
        show player 4 at Position(xpos=0.375, ypos=1.0) with dissolve
        player_name "( O que a {b}[mom_name]{/b} gostaria? )"
        player_name "( ... )"
        player_name "( Um colar? )"
        hide player with dissolve
        $ M_mom.trigger(T_mom_cupid_arrival)
    $ callScreen(location_count)

label kass_dialogue:
    scene location_mall_cupid_blur
    if kassy_first_visit:
        $ kassy_first_visit = False
        show player 1f at right
        show kass 2 at left
        with dissolve
        Kass "Bem-vindo ao {b}Cupid{/b}. Meu nome é {b}Kassy{/b}, eu poderia te ajudar em algo?"
        show player 2f
        show kass 1
        player_name "Não, valeu, só to dando uma olhada."
        show player 1f
        show kass 2
        Kass "Beleza. Me diga se você encontrar algo."
        show player 2f
        show kass 1
        player_name "Irei! Obrigado, {b}Kassy{/b}."
        show player 1f
        show kass 2
        Kass "Eu que agradeço!"
    else:

        show player 2f at right
        show kass 1 at left
        with dissolve
        player_name "Oi, {b}Kassy{/b}!"
        show player 1f
        show kass 2
        Kass "Oi, como posso te ajudar?"
        show player 2f
        show kass 1
        player_name "Nada por enquanto, só tô dando uma olhada."
        show player 1f
        show kass 2
        Kass "Certo. Me avise se você quiser algo."
        show player 2f
        show kass 1
        player_name "Farei! Obrigado, {b}Kassy{/b}."
    hide kass
    hide player
    with dissolve
    $ callScreen(location_count)

label necklace_display:

    if M_mom.get_state() == S_mom_choose_gift:
        scene location_mall_cupid_blur
        show player 4 zorder 0 at left
        player_name "Sim, um colar deve funcionar."
        player_name "Mas qual?"
        show player 492
        show xtra 33 zorder 1 at Position(xpos=0.295, ypos=0.749)
        with dissolve
        player_name "Hmm, não... muito jovem para a {b}[mom_name]{/b}, eu acho."
        show xtra 32 with dissolve
        player_name "... Não. Muito chamativo."
        show xtra 31 with dissolve
        player_name "Ooh, esse é ótimo e vai ficar lindo nela."
        show popup_item_necklace1 at truecenter with dissolve
        $ inventory.items.append(pearl_necklace)
        pause
        hide popup_item_necklace1 with dissolve
        player_name "Perfeito!"
        player_name "Vamos ver se ela vai gostar!"
        hide xtra
        hide player
        with dissolve
        $ M_mom.trigger(T_mom_pick_necklace)
    else:

        show screen popup_unfinished
    $ callScreen(location_count)

label cupid_dressroom:
    $ location_count = "Cupid Dressroom"
    if M_mom.get_state() == S_mom_dressing_room:
        scene location_mall_cupid_blur
        show player 10
        player_name "{b}[mom_name]{/b}, você está bem?"
        player_name "Por que tanta demora?"
        show player 11
        mom "Na verdade, querido, você poderia entrar aqui?"
        player_name "..."
        show player 10
        player_name "Você quer que eu entre aí?!"
        show player 11
        mom "Sim, por favor."
        show player 10
        player_name "... Ok."
        show player 11

        scene location_mall_cupid_closeup_stall

        show mom 169 zorder 1 at Position(xpos=0.65, ypos=1.0)
        show player 10 at Position(xpos=0.35, ypos=1.0)
        show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
        with dissolve
        player_name "Qual o problema?"
        show player 11
        show mom 168
        mom "Ah, o colar se enroscou em algo e não consigo tirar."
        mom "Você poderia me ajudar?"
        show player 10
        show mom 169
        player_name "C-claro."
        show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
        show mom 178 zorder 1 at Position(xpos=0.60, ypos=1.0)
        hide mneck 1
        with dissolve

        mom "Oh!"
        show mom 177b
        mom "..."
        show mom 178b
        mom "Oh meu..."
        show player 228c
        show mom 177b
        player_name "O que é isso?"

        show mom 178b
        show player 228d
        mom "*Ahem* N-nada, querido."
        mom "Você pode ver onde está preso??"
        show player 228c
        show mom 177b
        player_name "Sim, já vi. Só espere um segundo."
        show player 228d
        player_name "..."
        show player 228c
        player_name "Cara, está bem preso."
        show player 228d
        mom "..."
        show player 228c
        player_name "Quaaaase..."
        player_name "Pronto..."
        show player 228d
        player_name "..."
        show mom 179
        mom "Hehehe."
        show player 228c
        player_name "O que?"
        show player 228d
        show mom 178
        mom "N-nada. É estúpido."
        show player 228c
        show mom 177
        player_name "Vai mãe, me diga."
        show player 228d
        show mom 178
        mom "Eu só estou pensando sobre aquele filme que assistimos na outra noite."
        show player 228c
        show mom 177
        player_name "Aquele filme de romance ruim?"
        show player 228d
        show mom 178
        mom "S-sim."
        show player 228c
        show mom 177
        player_name "O que tem?"
        show player 228d
        show mom 178
        mom "Tinha uma cena parecida... Lembra?"
        show mom 177
        player_name "..."
        show player 228c
        player_name "Ah, sim!"
        player_name "Ele ajudou a moça com o colar e então se-"
        show player 227d at Position(xpos=0.35, ypos=1.0) with dissolve
        player_name "*gulp*"
        show player 227c
        player_name "Beijaram."
        show player 227d
        show mom 178
        mom "Uh huh."
        show player 228d at Position(xpos=0.475, ypos=1.0) with dissolve
        mom "Você já beijou alguma mulher, [firstname]?"
        show player 228c
        show mom 177
        player_name "... Não."
        show player 228d
        mom "..."
        show mom 179
        mom "Tudo bem, querido! Não tem nada de errado com isso."
        show mom 177
        player_name "..."
        show mom 178
        mom "Não quer tentar?"
        show player 227c at Position(xpos=0.35, ypos=1.0) with dissolve
        show mom 177
        player_name "Sério?!"
        show player 227d
        show mom 178
        mom "Bom, sim... Eu ac-"
        hide player
        hide mom
        show mom 180b
        with dissolve

        mom "( !!! )"

        show mom 180
        pause
        show mom 181
        mom "Mmm..."
        show mom 182
        pause

        mom "... Wow."
        mom "Querido, não podemos... Q-quer dizer, eu não devia..."
        hide mom
        show player 5 at Position(xpos=0.35, ypos=1.0)
        show mom 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
        show mneck 1 zorder 2 at Position(xpos=0.65, ypos=0.535)
        with dissolve
        player_name "..."
        mom "..."
        show player 10
        player_name "Desculpa, {b}[mom_name]{/b}."
        show player 5
        show mom 168
        mom "NÃO! Não... Sou eu, eu não deveria ter deixado..."
        show mom 169b
        mom "..."
        show mom 168
        mom "*Ahem* P-por que você não tira esse colar logo."
        show mom 169b
        player_name "..."
        show player 10
        player_name "S-sim, claro, {b}[mom_name]{/b}."
        show player 228b zorder 2 at Position(xpos=0.475, ypos=1.0)
        show mom 177 zorder 1 at Position(xpos=0.60, ypos=1.0)
        hide mneck 1
        with dissolve
        pause
        player_name "..."
        pause

        show player 492 zorder 3 at Position(xpos=0.35, ypos=1.0)
        show xtra 31 zorder 4 at Position(xpos=0.4575, ypos=0.749)
        show mom 169b zorder 1 at Position(xpos=0.65, ypos=1.0)
        with dissolve
        player_name "Pronto, tudo pronto."
        show player 493
        mom "..."
        show mom 168
        mom "Obrigada, querido."
        mom "Por que você não vai lá e devolve o colar?"
        mom "Já vou lá também."
        show player 492
        show mom 169b
        player_name "Sim, ok."
        hide player
        hide xtra
        with dissolve
        mom "..."
        show mom 164b with dissolve
        mom "( Oh céus... Não acreito que eu fiz isso! )"
        mom "( O coitado já está passando por tempos difíceis. )"
        mom "( Onde estava a minha cabeça... )"
        hide mom with dissolve
        $ M_player.set("jerk mom", True)
        $ M_mom.trigger(T_mom_dressing_room_check)
        $ location_count = "Cupid"
        $ unlock_ui()
        $ gTimer.tick()
    $ callScreen(location_count)

label mom_cupid_outing:
    scene location_mall_cupid_blur
    if M_mom.get_state() == S_mom_choose_gift:
        show player 5 at left with dissolve
        show mom 165 at Position(xpos=.75, ypos=1.0) with dissolve
        mom "Achou algo, querido?"
        show player 10
        show mom 164
        player_name "Ainda estou procurando."
        show player 5
        show mom 166
        mom "Hehe, ok!"
        show mom 165
        mom "Não fique tão nervoso. É fácil! Só pegue algo que você acha que eu gostaria..."
        show mom 164
        pause
        hide mom with dissolve
        show player 4 at Position(xpos=0.5, ypos=1.0) with dissolve
        player_name "( ... )"
        player_name "( Algo que a {b}[mom_name]{/b} gostasse? )"
        player_name "( Um colar, talvez? )"

    elif M_mom.get_state() == S_mom_show_necklace:
        $ inventory.items.remove(pearl_necklace)
        show player 492 zorder 0 at left
        show xtra 31 zorder 1 at Position(xpos=0.295, ypos=0.749)
        with dissolve
        show mom 164 at Position(xpos=0.75, ypos=1.0) with dissolve
        player_name "Ok, {b}[mom_name]{/b}. Que tal isso?"
        hide xtra
        show player 1 with dissolve
        show mom 170 at Position(xpos=0.7, ypos=1.0) with dissolve
        show mom 172
        mom "Oh, [firstname]... É lindo!"
        show mom 170
        show player 14
        player_name "Você gostou?"
        show player 13
        show mom 171
        mom "Sim! Você tem um ótimo gosto, querido."
        show mom 170
        show player 14
        player_name "Heh, obrigado, {b}[mom_name]{/b}!"
        show player 13
        show mom 173 at Position(xpos=0.775, ypos=1.0)
        pause 1
        show mom 174 at Position(xpos=0.7, ypos=1.0)
        pause 1
        show mom 175
        pause 2
        show mom 164 zorder 1 at Position(xpos=0.75, ypos=1.0)
        show mneck 1 zorder 2 at Position(xpos=0.7475, ypos=0.535)
        pause
        show mom 165
        mom "Então?"
        show player 14
        show mom 164
        player_name "... Hmm?"
        show player 13
        show mom 166
        mom "Como estou?"
        show player 14
        show mom 164
        player_name "Linda, {b}[mom_name]{/b}!"
        show player 13
        show mom 166
        mom "Aww... Obrigada, querido."
        show mom 164
        mom "Hmm..."
        show mom 165
        mom "Onde está um espelho quando se precisa de um?"
        show mom 164
        player_name "..."
        show player 14
        player_name "Deve ter um no provador de roupas..."
        show player 13
        show mom 165
        mom "Bem pensado, querido!"
        mom "Já volto."
        hide mom
        hide mneck
        with dissolve
        show player 14
        player_name "Ok."
        $ M_mom.trigger(T_mom_give_necklace)
    hide player with dissolve
    $ callScreen(location_count)

label mom_cupid_outing_block:
    scene location_mall_cupid_blur
    if M_mom.get_state() == S_mom_choose_gift:
        show player 4 with dissolve
        player_name "Hmm, eu deveria a prateleira de colar para ver se tem algo que a {b}[mom_name]{/b} gostaria..."
    elif M_mom.get_state() == S_mom_show_necklace:
        show player 4 with dissolve
        player_name "Eu deveria levar esse colar para a {b}[mom_name]{/b} vai gostar."
    elif M_mom.get_state() == S_mom_dressing_room:
        show player 14 with dissolve
        player_name "Tenho que esperar a {b}[mom_name]{/b}."
        show player 13
        player_name "..."
        show player 10
        player_name "Por que será que ela está demorando tanto?"
    hide player with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
