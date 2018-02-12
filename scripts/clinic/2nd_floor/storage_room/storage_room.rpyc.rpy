label hospital_storage_room_dialogue:
    if M_roz.is_set("fun time"):
        jump roz_storage_sex

    elif hospital_access_card not in inventory.items:
        scene hospital_lock
        player_name "Merda, está trancado!"
        player_name "Parece que eu preciso de um {b}cartão de acesso{/b} para destrancar a porta..."
        if not Roz.known(roz_storage):
            $ Roz.add_event(roz_storage)
        $ callScreen(location_count)
    $ location_count = "Hospital Storage Room"
    $ roz_trick.finish()
    $ roz_storage.finish()
    $ callScreen(location_count)

label hospital_storage_cabinet_dialogue:
    $ location_count = "Hospital Storage Cabinet"
    if mrsj.started(mrsj_sex_ed) and birth_control_pills not in inventory.items:
        scene hospital_cabinet_filled
        player_name "Hmm..."
        player_name "Tem algumas pílulas aqui."
        player_name "Talvez na caixa verde?"
    $ callScreen(location_count, False)

label roz_storage_sex:
    $ M_roz.set("fun time", False)
    $ gTimer.tick()
    scene location_hospital_sex with fade
    if M_roz.get_state() == S_roz_end:
        show player 11f at Position(xpos=.7,ypos=1.0)
        pause
        show roz 4 at left with dissolve
        show player 13f
        pause
        show roz 5
        roz "Surpreso ver você de volta tão cedo. Eu ainda tenho uma impressão."
        show player 14f
        show roz 4
        player_name "Você está bonita!"
        show player 13f
        show roz 5
        roz "Hah, você não chegará na idade sem aprender alguns truques, criança."
        show roz 8
        pause
        show roz 9
        roz "Bom então..."
        hide roz
        hide player
        show roz 16 at right with dissolve
        show player 24 at Position(xpos=.25,ypos=1.0) with dissolve
        pause
        show roz 17
        pause
        show roz 18
        pause
        show player 80
        pause
        show roz 19
        roz "Por que você não tira esse monstro para fora para que começamos logo."
        show player 83
        player_name "Sim, senhora!"
        hide player with dissolve
        show roz 18
        show player 480 at Position(xpos=.35,ypos=1.0)
        pause
        show roz 19
        roz "É bem grande para sua idade."
        show roz 18
        show player 482
        pause
        show roz 19
        roz "Não se esqueça de gozar dentro..."
        show roz 18
        show player 481
        player_name "S-sim, senhora!"
        show player 483 at Position (xpos=.36,ypos=1.0)
        show roz 19
        roz "Bom garoto..."
    else:

        show player 12 at center with dissolve
        player_name "Tenho certeza que a Roz disse que as caixas estariam aqui."
        show player 11 zorder 2
        player_name "Mas eu não vejo isso. Talvez ela tenha mudado do lugar e esquecido?"
        show roz 5 zorder 1 at left with dissolve

        roz "Precisa de ajuda?"
        show player 23f at Position(xpos=.7,ypos=1.0)
        show roz 4
        player_name "Whoa!"
        show player 22f
        player_name "..."
        show player 10f
        player_name "Oh, o-oi Roz. Você me assustou!"
        show player 11f
        show roz 5
        roz "Ahh, não se faça de bobo! Só vim aqui para te dar uma ajuda."
        show player 10f
        show roz 4
        player_name "Uhh tá, ok. Umm, você tem certeza que a caixa está aqui? Eu não achei."
        show player 11f
        show roz 5
        roz "Não? Estranho."
        roz "Talvez eu tenha mudado de lugar e esqueci."
        roz "Essa memória não é como costumava ser."
        show roz 4
        player_name "..."
        show player 10f
        player_name "O-ok. Sem problemas, eu vou descer as escadas e-"
        show player 22f
        show roz 6

        player_name "!!!" with hpunch
        show roz 7
        roz "Qual a pressa?"
        roz "Parece que temos algum tempo sozinho aqui..."
        roz "E eu acho que há algo que você pode fazer por mim."
        show player 38f
        show roz 6
        player_name "Oh uh, c-claro. O que voce tem em mente?"
        show player 3f
        show roz 7
        roz "Escuta, {b}[firstname]{/b}."
        roz "Faz anos desde a última vez que a minha piriquita voou. Você entendeu o que eu quis dizer?"
        show player 10f
        show roz 6
        player_name "Umm, voou?"
        show player 11f
        show roz 7
        roz "Isso. Voou."
        show roz 10
        pause


        show roz 8
        pause
        show player 23f
        player_name "!!!" with hpunch
        show player 42f
        player_name "Whoa! Roz, O que você está fazendo?"
        show roz 9
        roz "Eh? O que parece que estou fazendo?"
        roz "Tire as roupas e vamos."
        show player 10f
        show roz 8
        player_name "Espera, vocẽ quer que eu--M-mas eu não posso fazer isso!"
        show player 11f
        show roz 9
        roz "Huh? Você quer os {b}registros{/b} não quer?"
        show player 10f
        show roz 8
        player_name "Bom, sim, eu quero mas-"
        show player 11f
        show roz 9
        roz "Então, está eseprando o que? Você me ajuda que eu te ajudo, entendeu?"
        show player 24f
        show roz 8
        player_name "Ehhh... entendi."
        show roz 9
        roz "Ótimo!"
        hide roz
        hide player
        show roz 16 at right with dissolve
        show player 24 at Position(xpos=.25,ypos=1.0) with dissolve
        pause
        show roz 17
        pause
        show roz 18
        pause
        show player 78
        pause
        show roz 19
        roz "Heh, vamos lá."
        show player 80
        show roz 18
        pause
        show roz 19
        roz "O que está esperando?"
        show player 83
        player_name "Ah, cara..."
        hide player with dissolve
        show roz 18
        show player 480 at Position(xpos=.35,ypos=1.0)
        pause
        show roz 19
        roz "Uau! Que monstro!"
        show roz 18
        show player 482
        pause
        show roz 19
        roz "Eu sabia que seria uma boa ideia!"
        show roz 18
        pause
        show roz 19
        roz "Agora mostre o que a velha Roz estava perdendo."
        show roz 18
        show player 481
        player_name "O-Ok!"
        show player 483 at Position (xpos=.36,ypos=1.0)
        show roz 19
        roz "Bom garoto..."

    scene location_hospital_sex
    $ M_roz.set('sex speed', .175)
    show rozs 1_2_3_4_5_6_7 at right
    with fade
    roz "Isso, garoto, gostoso e profundo."
    pause
    roz "Oh Yeeaah..."
    pause
    roz "Não se preocupe em enfiar tudo."
    roz "Eu gosto de sentir isso dentro de mim."
    $ M_roz.set('sex speed', .125)
    show rozs 1_2_3_4_5_6_7
    roz "Isso, assim."
    pause
    roz "Vai, rapaz, mais forte!"
    $ M_roz.set('sex speed', .075)
    $ anim_toggle = True
    show rozs 1_2_3_4_5_6_7
    pause

    label roz_sex_loop:
        hide screen roz_sex_options
        show screen xray_scr
        pause
        hide screen xray_scr
        if anim_toggle:
            $ animcounter = 0
            while animcounter < 4:
                show rozs 1_2_3_4_5_6_7 at right
                pause 5
                if animcounter == 1:
                    roz "Ahhhh!!!{p=1}{nw}"
                if animcounter == 3:
                    roz "Oh!!!{p=1}{nw}"
                    player_name "Uhhh...{p=1}{nw}"
                pause 3
                $ animcounter += 1
        else:

            $ animcounter = 0
            while animcounter < 4:
                show rozs 1 at right
                pause
                show rozs 2
                pause
                show rozs 3
                pause
                show rozs 4
                pause
                show rozs 5
                pause
                show rozs 6
                pause
                show rozs 7
                pause
                if animcounter == 1:
                    roz "Ahhhh!!!"
                if animcounter == 3:
                    roz "Oh!!!"
                    player_name "Uhhh..."
                $ animcounter += 1

        show screen roz_sex_options
        pause
        jump roz_sex_loop

    label roz_faster_sex:
        $ M_roz.set('sex speed', M_roz.get('sex speed') - 0.05)
        jump roz_sex_loop

    label roz_slower_sex:
        $ M_roz.set('sex speed', M_roz.get('sex speed') + 0.05)
        jump roz_sex_loop

    label roz_sex_cum:
        hide screen roz_sex_options
        player_name "Roz, eu não posso aguentar... p-por muito tempo."
        roz "Goze dentro de mim!"
        pause
        roz "Oh céééééuuuusss!!!"
        show rozs 8_9 with flash
        player_name "UHHH!!"
        roz "AAAAHHH!!!!"
        pause
        hide rozs
        show player 482 zorder 2 at Position(xpos=.36,ypos=1.0)
        show roz 18 zorder 1 at right
        show rozs 144 zorder 3 at Position(xpos=.5158,ypos=.895)
        show players 143 zorder 4 at Position(xpos=.435,ypos=.8625)
        pause
        show roz 19
        roz "*wheeze* ... Whew."
        roz "Querido... *toce* isso foi muito bom, [firstname]!"
        show roz 18
        show player 481
        player_name "S-sim..."
        show player 482
        show roz 19
        roz "Apenas me dê um tempo... parece recuperar a respiração."
        scene black with fade

    scene location_hospital_sex with fade
    if M_roz.get_state() == S_roz_end:
        show player 1f at Position(xpos=.7,ypos=1.0) with dissolve
        show roz 13 at left with dissolve
        pause
        show roz 15
        roz "Está tudo pronto hoje, criança."
        roz "Melhorou muito."
        show player 29f
        show roz 14
        player_name "Sério? Heh, valeu. Eu acho..."
        show player 3f
        show roz 15
        roz "Pazer é todo meu, {b}[firstname]{/b}."
        roz "Você volta e vê o ole Roz novamente em breve. Entendeu?"
        show player 29f
        show roz 14
        player_name "S-sim."
        hide roz
        hide player
        with dissolve
    else:

        show player 5f at Position(xpos=.7,ypos=1.0)
        show roz 4 at left
        pause
        show roz 12
        roz "Aqui, os registros."
        show player 12f
        show roz 11
        player_name "Você tinha eles o tempo todo?!"
        show player 462
        show roz 5
        roz "Claro, eu disse que sabia onde estava."
        show roz 4
        player_name "..."
        show roz 5
        roz "Não conheço o nome que você está procurando..."
        roz "Mas se ele está no {b}cemitéiro{/b}, então ele estará nesses {b}registros{/b}."
        show roz 13
        pause
        show player 463
        show roz 14
        player_name "...Valeu, eu acho."
        show player 462
        show roz 15
        roz "Sem problemas, criança."
        roz "Volte sempre. Sabe, se você precisar de algo."
        show roz 14
        pause
        show roz 15
        roz "Tipo um segundo roud, hehehe!"
        show roz 14
        hide roz with dissolve
        pause
        show player 37f
        player_name "(Eu... não acredito que acabei de transar com a Roz.)"
        player_name "(Ela é velha o suficiente para ser minha avó...)"
        show player 24f
        player_name "(Pelo menos eu consegui os {b}rigstros de óbito{/b}.)"
        player_name "(Creio que o cara do barco vai estar aqui em algum lugar.)"
        hide player with dissolve
        $ inventory.items.append(obituary_records)
        $ M_roz.trigger(T_roz_fuckery)
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
