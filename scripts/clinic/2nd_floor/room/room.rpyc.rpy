label hospital_second_floor_room_dialogue:
    $ location_count = "Hospital 2nd Floor Room"
    $ callScreen(location_count)

label erik_bullying_2:
    $ location_count = "Hospital 2nd Floor Room"
    scene hospital_bed
    show player 392 at Position (xpos=805, ypos=665)
    show micoe 5 at left
    with fade
    "Oi, como-"
    "..."
    show micoe 4
    "Hum hum!!"
    player_name "Uh...."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 3
    "Ah, bom! Você está acordando."
    show micoe 2
    "Como você está se sentindo?"
    show micoe 1
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Eu..."
    show player 397 at Position (xpos=772, ypos=660)
    player_name "Eu me sinto bem."
    show player 394 at Position (xpos=768, ypos=660)
    player_name "Um pouco tonto na verdade."
    pause
    show player 396 at Position (xpos=772, ypos=660)
    player_name "Onde estou?"
    show player 397
    show micoe 5
    "No hospital."
    show micoe 4
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Estou?"
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 3
    "Está!"
    show micoe 2
    micoe "Sou a {b}enfermeira Micoe{/b}."
    show micoe 5
    micoe "Você teve uma pequena concussão, mas você vai ficar bem."
    micoe "Você poderá ir para casa quando se sentir bem."
    micoe "Você tem que tomar bastante água e descansar."
    show micoe 4
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Oh, Entendido... Obrigado."
    show player 397 at Position (xpos=772, ypos=660)
    show micoe 2
    micoe "Esqueci de dizer, mas você tem visitas!"
    hide micoe with dissolve
    pause
    show player 393
    pause
    show erik 4f at left with dissolve
    eri "Eai, {b}[firstname]{/b}!"
    eri "Como você está?"
    show erik 1f
    show player 395
    player_name "Eae {b}Erik{/b}. Estou bem, eu acho!"
    show player 393
    show erik 5f
    eri "Dexter deu uma surra, hein."
    show erik 1f
    show player 395
    player_name "Nah, {b}Dexter{/b} briga como uma garoa!"
    show player 393
    show erik 4f
    eri "Heh heh."
    eri "Obrigado por me defender hoje."
    show erik 1f
    show player 395
    player_name "Não foi nada."
    show player 393
    show erik 5f
    eri "Ninguém nunca enfrentou {b}Dexter{/b} antes."
    show erik 4f
    eri "Todo mundo na escola está falando de você."
    show erik 1f
    show player 398 at Position (xpos=772, ypos=664)
    player_name "Eh... Não queria que fosse assim..."
    player_name "...E eu ainda levei uma surra!"
    show player 393 at Position (xpos=772, ypos=660)
    show erik 4f
    eri "Bom, {b}Dexter{/b} vai pensar duas vezes antes de fazer isso antes."
    show erik 1f
    show player 395
    player_name "Heh! Veremos."
    show player 393
    pause
    show erik 4f
    eri "Ei, eu ouvi a enfermeira dizer que você pode ir para casa."
    eri "Pronto?"
    show erik 1f
    show player 395
    player_name "Sim."
    hide player
    hide erik
    with dissolve
    $ erik_bullying_2.finish()
    show unlock40 at truecenter with dissolve
    $ loc_clinic_unlocked = True
    $ gTimer.tick(3)
    pause
    hide unlock40 with dissolve
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
