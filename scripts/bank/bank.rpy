label bank_dialogue:
    $ location_count = "Bank"
    if bank_count == 0:
        scene bank
        show player 1 at left with dissolve
        show liu 2 at right with dissolve
        liu "Bem vindo ao {b}Saga Financial Bank{/b}!"
        show liu 1 at right
        show player 14 at left
        player_name "Oi!"
        show liu 3 at right
        show player 1 at left
        liu "Por favor, sinta-se livre para usar nossos {b}caixas eletrônicos{/b} para {b}depósitos{/b}!"
        liu "Ou nós podemos te ajudar com qualquer dúvida na {b}mesa de atendimentos{/b}!"
        show liu 1 at right
        show player 14 at left
        player_name "Claro, valeu!"
        hide player 14 at left with dissolve
        hide liu 1 at right with dissolve
        $ bank_count = 1
    $ callScreen(location_count)

label bank__tellerdialogue:
    if bank_teller_count == 0:
        scene bank
        show liu 10 at right
        show player 14 at left with dissolve
        window hide
        pause
        show player 11 at left
        player_name "..."
        show liu 9 at right
        show player 12 at left
        player_name "Pois não?"
        show liu 5 at right
        show player 1 at left
        liu "Ah! Me desculpe!"
        liu "Como posso te ajudar, senhor?"
        menu:
            "Checar conta.":
                show liu 4 at right
                show player 2 at left
                player_name "Pode me falar como anda minha conta?"
                show liu 5 at right
                show player 1 at left
                liu "Vejo que você tem uma conta conosco!"
                liu "Você recentemente criou uma conta poupança que tem..."
                liu "... {b}[inventory.savings]{/b} dólares depositados!"
                show liu 4 at right
                show player 17 at left
                player_name "Sim, são minhas economias para a faculdade."
                show liu 5 at right
                show player 1 at left
                liu "Algo a mais que eu poderia fazer por você?"
                menu:
                    "Mais informações." if more_account_info == 0:
                        show liu 4 at right
                        show player 4 at left
                        player_name "Hmmm..."
                        show player 30 at left
                        player_name "Pode me contar algo a mais sobre a economias de outras contas?"
                        show liu 5 at right
                        show player 1 at left
                        liu "Bom, você também tem a conta da família, que tem..."
                        show liu 9 at right
                        show player 11 at left
                        liu "Ah..."
                        show player 10 at left
                        player_name "O que foi?"
                        show liu 6 at right
                        show player 23 at left
                        liu "Bom... Parece que a conta principal da sua família está congelada..."
                        show liu 11 at right
                        show player 10 at left
                        player_name "Por quê?"
                        show liu 6 at right
                        show player 5 at left
                        liu "Um grande número de empréstimos não foram pagos."
                        show liu 11 at right
                        liu "..."
                        show liu 6 at right
                        show player 22 at left
                        liu "Eu tenho... outra má notícia..."
                        show player 11 at left
                        liu "Parece que sua família não pagou a {b}hipoteca{/b}..."
                        liu "...A última foi há mais de 6 meses..."
                        show liu 11 at right
                        show player 22 at left
                        player_name "..."
                        show player 23 at left with hpunch
                        player_name "O quê?!?"
                        show liu 6 at right
                        show player 5 at left
                        liu "Receio que a única opção será {b}tomarem a casa{/b}..."
                        show liu 11 at right
                        show player 10 at left
                        player_name "Não pode ser..."
                        show liu 6 at right
                        show player 5 at left
                        liu "Pela sua reação... Parece que você não sabia sobre isso."
                        show liu 11 at right
                        show player 24 at left
                        player_name "Bom... Eu sabia que meu {b}pai{/b} tinha alguns problemas... mas não tantos."
                        show liu 6 at right
                        liu "Lamento dizer, mas não tenho muita coisa para fazer."
                        show liu 11 at right
                        show player 25 at left
                        player_name "Está tudo bem, só queria saber..."
                        player_name "Tenho que ir agora..."
                        hide player 25 at left
                        hide liu 11 at right
                        with dissolve
                        $ more_account_info = 1
                    "Obrigado, tenho que ir.":

                        show liu 4 at right
                        show player 14 at left
                        player_name "Tenho que ir. Mas voltarei outra hora!"
                        show liu 5 at right
                        show player 1 at left
                        liu "Obrigada por fazer negócio conosco!"
                        liu "Volte logo!"
                        hide player 1 at left
                        hide liu 5 at right
                        with dissolve

            "Conversar." if bankteller_chat == 0:
                show liu 9 at right
                show player 10 at left
                player_name "Isso pode parece um pouco pessoal, mas..."
                player_name "Está tudo bem?"
                show liu 6 at right
                show player 13 at left
                liu "Ãhm... Claro!"
                liu "Por que pergunta?"
                show liu 9 at right
                show player 2 at left
                player_name "Sei lá, parece que você teve um terrível dia no trabalho..."
                show liu 6 at right
                show player 13 at left
                liu "Ahh... Não é isso...Trabalho foi bom, sério..."
                show liu 10 at right
                liu "{b}*suspiro*{/b}"
                show player 11 at left
                liu "É que... Sabe, Alguns problemas em casa..."
                show liu 6 at right
                liu "...Isso atinge você como-"
                show liu 8 at right
                liu "Espera... Por que estou te falando isso?"
                show liu 4 at right
                show player 29 at left
                player_name "Ah, Desculpa! Não quis incomodar."
                player_name "Às vezes, quando tenho problemas em casa..."
                show liu 9 at right
                show player 33 at left
                player_name "Eu falo para alguém sobre. Sabe, deixo isso sair!"
                show liu 5 at right
                show player 13 at left
                liu "Bom... Pois é, acho que você está certo."
                show liu 7 at right
                show player 13 at left
                liu "Tenho que voltar ao trabalho..."
                show liu 10 at right
                liu "..."
                show liu 5 at right
                show player 11 at left
                liu "Como é seu nome mesmo?"
                show liu 4 at right
                show player 17 at left
                player_name "Ah, meu nome é {b}[firstname]{/b}!"
                show liu 7 at right
                show player 2 at left
                liu "Prazer em te conhecer, {b}[firstname]{/b}, Me chamo {b}Liu Wang{/b}!"
                $ liu = Character('Liu Wang', color="#c8ffc8")
                show liu 4 at right
                show player 14 at left
                player_name "Vejo você na próxima, {b}Liu{/b}!"
                show liu 8 at right
                show player 1 at left
                liu "Tchau!"
                hide player 1 at left
                hide liu 8
                with dissolve
                $ bankteller_chat = 1
    $ callScreen(location_count)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
