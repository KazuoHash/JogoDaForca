" ---------------------------------------------------------------  Jogo Da Forca  ------------------------------------------------------------- "


# ----------------------------------------------------------------  Interface  ---------------------------------------------------------------- #

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

center = 0

stop = False

while not stop:

    def ClearScreen():
        print("\n" * 30)

    def ChangeLetter():
        global letra, palavra, letrasEncontradas
        return_tmp = ""
        for p, l in enumerate(palavra):
            if (l == letra):
                return_tmp += l
            else:
                return_tmp += letrasEncontradas[p]
        return return_tmp

    def ShowFoundLetters():
        global letrasEncontradas
        print((center - len(letrasEncontradas) + 5) * " ", end="")
        for l in letrasEncontradas:
            print("\033[4;32m", end="")
            if(l in " _"):
                print("\033[m", end="")
                print("\033[1;30m", end="")
            print(l + "\033[m\033[1;30m ", end="")
        print("\n" * 9)

    def ShowLettersUsed():
        global letrasUsadas
        print(("Você tem um total de 7 tentativas"))
        print((center - 2) * " " + "\033[1;30mLETRAS USADAS")
        print((center - int(len(letrasUsadas) / 2) + 5) * " ", end="")
        for l in letrasUsadas[0:-2]:
            print("\033[1;31m", end="")
            if(l==","):
                print("\033[1;30m", end="")
            print(l, end="")
        print("\n")

    def Body():
        global Corpo, center, error
        if (error == 1):
            Corpo[0] = "Õ"  
        elif (error == 2):
            Corpo[1] = "|"  
        elif (error == 3):
            Corpo[2] = "|"  
        elif (error == 4):
            Corpo[3] = "/"  
        elif (error == 5):
            Corpo[4] = " \\"  
        elif (error == 6):
            Corpo[5] = "/"  
        elif (error == 7):
            Corpo[6] = "\\"  

        print(center * " " + "\033[1;30m   ____ ")
        print(center * " " + "\033[1;30m  /    |")
        print(center * " " + "\033[1;30m /     \033[1;31m" + Corpo[0])
        print(center * " " + "\033[1;30m|     \033[1;31m" + Corpo[5] + Corpo[1] + Corpo[6])
        print(center * " " + "\033[1;30m|      \033[1;31m" + Corpo[2])
        print(center * " " + "\033[1;30m|     \033[1;31m" + Corpo[3] + Corpo[4])
        print(center * " " + "\033[1;30m|\n")

    def UpdateScreen():
        ClearScreen()
        print((center - 6) * " " + "\033[1;31m<ESPAÇO IGUAL A HÍFEN>" + "\n" * 3)
        ShowLettersUsed()
        Body()
        ShowFoundLetters()

    error = 0

    aux = "abcdefghijklmnopqrstuvwxyz-"
    Corpo = [" ", " ", " ", " ", " ", " ", " "]
    letrasUsadas = ""

    tipo = 0

    escolha = 0

    Tipo_Consulta = 0

    import pandas as pd

    tabela = pd.read_csv("TabelaForca.csv", sep=";")

    while tipo != 1:

        print((center - 4) * " " +"\033[1;30m" + "\n Escolha oque você quer fazer: \n\n [1] Jogar\n" + (center - 4) * " " + " [2] Consultar Palavras\n "  + (center - 4) * " " + "[3] Cadastrar Palavra\n " + (center - 4) * " " + "[4] Apagar Palavra\n"  + (center - 4) * " " + " [5] Listar Palavras\n\n ")


        tipo = int(input((center - 4) * " " + "Opção> "))


        if (tipo == 1):

            while escolha != 1 and escolha != 2 and escolha != 3:
                
                from random import choice

                print((center - 4) * " " + RESET + "\n Escolha a dificuldade: \n\n [1] Facil\n" + (center - 4) * " " + " [2] Medio\n" + (center - 4) * " " + " [3] Dificil\n")
                escolha = int(input((center - 4) * " " + "Opção> "))

                if (escolha == 1):
                    fac= tabela.loc[tabela['Dificuldade'] == 1, 'PALAVRA'].tolist()
                    palavra = choice(fac)    
                elif(escolha == 2):
                    med= tabela.loc[tabela['Dificuldade'] == 2, 'PALAVRA'].tolist()
                    palavra = choice(med)
                elif(escolha == 3):
                    dif= tabela.loc[tabela['Dificuldade'] == 3, 'PALAVRA'].tolist()
                    palavra = choice(dif)
                else:
                    print(RED +"\n-------------------------------------------------------\nDigite uma alternativa válida!!\n-------------------------------------------------------\n")

            QDJ_Antiga = tabela.loc[tabela['PALAVRA'] == palavra, 'QDJ']
            QDJ_Nova = QDJ_Antiga + 1
            tabela.loc[tabela['PALAVRA'] == palavra, 'QDJ'] = QDJ_Nova
            tabela.to_csv('TabelaForca.csv', index=False, sep= ';')

        elif (tipo == 2):
            lista_consulta = tabela ["PALAVRA"].tolist()
            print((center - 4) * " " + "\n Escolha o tipo de consulta: \n\n [1] Nome\n" + (center - 4) * " " + " [2] Dificuldade\n" + (center - 4) * " " + " [3] Pontuação\n")
            Tipo_Consulta = int(input((center - 4) * " " + "Opção> "))

            if (Tipo_Consulta == 1):
                Consulta = input("\nQual a palavra voce quer consultar? ")
                if Consulta in lista_consulta:
                    print(GREEN +"\n-------------------------------------------------------\nSim, esta palavra foi encontrada na lista!!\n------------------------------------------------------- \n")
                    print(tabela.loc[tabela['PALAVRA'] == Consulta])
                else:
                    print(RED +"\n-------------------------------------------------------\nNão, esta palavra não foi encontrada na lista!!\n------------------------------------------------------- ")

            elif(Tipo_Consulta == 2):  
                print((center - 4) * " " + "\n Escolha a dificuldade: \n\n [1] Facil\n" + (center - 4) * " " + " [2] Medio\n" + (center - 4) * " " + " [3] Dificil\n")
                Dificuldade_Consulta = int(input((center - 4) * " " + "Opção> "))         
                if (Dificuldade_Consulta == 1):
                    print("\nAs palavras de dificuldade 1 são: \n")
                    print(tabela.loc[tabela['Dificuldade'] == 1])
                elif(Dificuldade_Consulta == 2):
                    print("\nAs palavras de dificuldade 2 são: \n")
                    print(tabela.loc[tabela['Dificuldade'] == 2])
                elif(Dificuldade_Consulta == 3):
                    print("\nAs palavras de dificuldade 3 são: \n")
                    print(tabela.loc[tabela['Dificuldade'] == 3])
                else:
                    print(RED +"\n-------------------------------------------------------\nDigite uma alternativa válida!!\n-------------------------------------------------------")

            elif(Tipo_Consulta == 3):
                print(BLUE +"\nAs 5 mais jogadas são: \n")
                print(tabela.sort_values(by='QDJ', ascending=False).head(5))
                print(GREEN +"\n\nAs 5 mais acertadas são: \n")
                print(tabela.sort_values(by='QDA', ascending=False).head(5))
                print(RED +"\nAs 5 mais erradas são: \n")
                print(tabela.sort_values(by='QDA', ascending=True).head(5))

            else:
                print(RED +"\n-------------------------------------------------------\nDigite uma alternativa válida!!\n-------------------------------------------------------")

        elif (tipo == 3):
            Palavra_Cadastrar = input("\nQual palavra voce quer Cadastrar? ")
            lista_consulta = tabela ["PALAVRA"].tolist()
            if Palavra_Cadastrar in lista_consulta:
                print(RED +"\n-------------------------------------------------------\nDesculpe, mas esta palavra foi encontrada na lista!!\n------------------------------------------------------- ")
            else:
                print(GREEN +"\n-----------------------------------------------------------------------\nA palavra não foi encontrada na lista, podemos continuar!!\n------------------------------------------------------------------------ ")
                ID_Cadastrar = tabela.at[tabela.index[-2],'ID']
                Dificuldade_Cadastrar = input("\nQual a dificuldade da palavra? ")
                ID_Cadastrar += 1
                tabela = tabela.append({'PALAVRA': Palavra_Cadastrar, 'ID': ID_Cadastrar, 'Dificuldade': Dificuldade_Cadastrar, 'QDT': 7, 'QDJ': 0, 'QDA': 0}, ignore_index=True)
                print(GREEN +"\n-------------------------------------------------------\nA palavra foi adicionada na lista com sucesso!!\n------------------------------------------------------- ")
                tabela.to_csv('TabelaForca.csv', index=False, sep= ';')

        elif (tipo == 4):
            Palavra_Apagar = input("\nQual palavra voce quer remover? ")
            lista_consulta = tabela ["PALAVRA"].tolist()
            if Palavra_Apagar in lista_consulta:
                tabela.loc[tabela['PALAVRA'] == Palavra_Apagar, 'PALAVRA']
                tabela = tabela.drop(index=tabela[tabela['PALAVRA'] == Palavra_Apagar ].index)
                print(GREEN +"\n-------------------------------------------------------\nA palavra foi encontrada na lista, e foi apagada!!\n------------------------------------------------------- ")
                tabela.to_csv('TabelaForca.csv', index=False, sep= ';')
            else:
                print(RED +"\n-------------------------------------------------------\nA palavra não foi encontrada na lista, então não poderá ser apagada!!\n------------------------------------------------------- ")

        elif (tipo == 5):
            print(tabela)
        
        else:
            print(RED +"\n-------------------------------------------------------\nDigite uma alternativa válida!!\n-------------------------------------------------------")
            

    letrasEncontradas = "_" * len(palavra)
    UpdateScreen()



    # ----------------------------------------------------------------  Código Principal  ---------------------------------------------------------------- #


    while letrasEncontradas != palavra and error < 7:
        try:
            letra = input(center * " " + "\033[1;30mLetra> ")[0].lower()
        except:
            letra = ""

        if(letra == " "):
            letra = "-"

        if (letra not in letrasUsadas and letra in aux):
            letrasUsadas += letra + ", "
            if (letra in palavra):
                letrasEncontradas = ChangeLetter()
            else:
                error += 1

        UpdateScreen()

    ClearScreen()

    if (error == 7):
        print(center * " " + "\033[4;31mVocê perdeu!")
        print((center - int(len("a palavra era " + palavra) / 2) + 5) * " " + "\033[m\033[1;30ma palavra era\033[1;31m", palavra, "\n" * 15)
    else:
        print(center * " " + "\033[4;32mParabéns, você ganhou! =)")
        print((center - int(len("a palavra era " + palavra) / 2) + 5) * " " + "\033[m\033[1;30ma palavra era\033[1;32m", palavra, "\n" * 15)
        QDA_Antiga = tabela.loc[tabela['PALAVRA'] == palavra, 'QDA']
        QDA_Nova = QDA_Antiga + 1
        tabela.loc[tabela['PALAVRA'] == palavra, 'QDA'] = QDA_Nova
        tabela.to_csv('TabelaForca.csv', index=False, sep= ';')

    if input("Deseja sair (Y/N) ? ").lower() == "y":
        stop = True
