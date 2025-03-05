import time
from bs4 import BeautifulSoup
import requests
import os
from tqdm import tqdm 
import pyfiglet
from colorama import init
from colorama import Fore
from unidecode import unidecode
init(autoreset=True)

arquivo = "arquivo.txt"
titulo = []
_QUESTIONS_ = []
_KEYSWORDS_ = []
_INDICES_K_ = []
_RESPOSTAS_ = []
Titutlo = pyfiglet.figlet_format("WIKIBOT - 1.0")
print(f"{Fore.CYAN}{Titutlo}")
escolha = input(f" 👋  {Fore.GREEN}Olá \n\n ❓  {Fore.BLUE}Como quer Prosseguir  ❓ \n\n 🧠 {Fore.LIGHTBLACK_EX}Armazenar Informações na Memória  🧠 \n\n 📄  {Fore.MAGENTA}Armazenar Informações no Arquivo.txt  📄 \n\n {Fore.WHITE}Pressione [M] para Memória \n\n Pressione [A] para Documento txt \n\n o que você prefere ?")

while not escolha or escolha.lower() != "m" and escolha.lower() != "a":
    if not escolha:
        print(f"❌ {Fore.RED}ERROR  ❌")
        print(F"⚠️  {Fore.YELLOW}ALERTA: {Fore.WHITE}VALOR INVÁLIDO  ⚠️")
        escolha = input(F" ❓  {Fore.BLUE}Como quer Prosseguir  ❓ \n\n 🧠 {Fore.LIGHTBLACK_EX}Armazenar Informações na Memória  🧠 \n\n 📄  {Fore.MAGENTA}Armazenar Informações no Arquivo.txt  📄 \n\n {Fore.WHITE}Pressione [M] para Memória \n\n Pressione [A] para Documento txt \n\n o que você prefere ?")
    if escolha.lower() != "m":
        print(f"❌ {Fore.RED}ERROR  ❌")
        print(F"⚠️  {Fore.YELLOW}ALERTA: {Fore.WHITE}VALOR INVÁLIDO  ⚠️")
        escolha = input(F" ❓  {Fore.BLUE}Como quer Prosseguir  ❓ \n\n 🧠 {Fore.LIGHTBLACK_EX}Armazenar Informações na Memória  🧠 \n\n 📄  {Fore.MAGENTA}Armazenar Informações no Arquivo.txt  📄 \n\n {Fore.WHITE}Pressione [M] para Memória \n\n Pressione [A] para Documento txt \n\n o que você prefere ?")
    if escolha.lower() != "a":
        print(f"❌ {Fore.RED}ERROR  ❌")
        print(F"⚠️  {Fore.YELLOW}ALERTA: {Fore.WHITE}VALOR INVÁLIDO  ⚠️")
        escolha = input(F" ❓  {Fore.BLUE}Como quer Prosseguir  ❓ \n\n 🧠 {Fore.LIGHTBLACK_EX}Armazenar Informações na Memória  🧠 \n\n 📄  {Fore.MAGENTA}Armazenar Informações no Arquivo.txt  📄 \n\n {Fore.WHITE}Pressione [M] para Memória \n\n Pressione [A] para Documento txt \n\n o que você prefere ?")
if escolha.lower() == 'm':
    _TEXTO = ""
    with open(arquivo , "r" , encoding="utf-8") as file:
        if len(file.read()) > 0:
            with open('Parametros/Parametros.txt' , "r" , encoding="utf-8") as file:
                array_file = file.read().split()
                for i in array_file:
                    # faz a requisição (requests.get(url))
                    response = requests.get(str(i))
                    # variavel (dados) = BeautifulSoup (Sopa Bonita) , BeautifulSoup(requesicao.texto , 'html-parser')
                    # html-parser = padrão do Python que lê documentos HTML
                    dados = BeautifulSoup(response.text , 'html.parser') # traz uma array de elementos HTML requeridos da pagina
                    # variavel (elementFather) = variavel (dados) '.' find (encontre) find(tag_html , class_tag) 
                    elementFather = dados.find("div",class_="mw-content-ltr mw-parser-output")
                    if elementFather is not None:
                        # acessa todos os filhos do elemento tag HTML
                        element = elementFather.find_all("p") # find_all(tag_html_filhos) , retorna array
                        for i in tqdm(element,desc="Extraindo Informações"):
                            _TEXTO = _TEXTO + str(i) 
    pergunta = input("🤔  Qual é a Sua Pergunta ? ")
    for i in pergunta.split():
        _QUESTIONS_.append(i)
    for i in _QUESTIONS_:
        if len(i) > 3 and i not in _KEYSWORDS_ or i.upper() == i and i.upper() not in ['Quem', 'O que', 'Que', 'Qual', 'Quais', 'Quanto', 'Quanta', 'Quantos', 'Quantas', 'Onde', 'Como', 'Por que', 'Para que', 'De onde', 'A que','A','E','I','O','U','ÃO']:
            _KEYSWORDS_.append(i)
    for i in _KEYSWORDS_:
        for j in _TEXTO.split():
            if unidecode(i).lower() == unidecode(j).lower():
                if unidecode(i).lower() == unidecode(j).lower():
                    # inicia o contador em 0
                    start = 0
                    # enquanto verdade for verdade (loop constante)
                    while True:
                        # indice vai ser igual:
                        # texto.find(i,start)
                        # ele encontra o índice da palavra no texto a partir do inicio 0 (start)
                        # tipo: 
                        # na frase: 
                        # 'O Gato Corre Muito Rápido , e o Gato Gosta de Correr com o Gato'
                        # o trecho: 
                        #  pos = texto.find(i, start) , sendo i = 'Gato' , busca por:
                        # 'Gato' , sendo assim:
                        #  pos = texto.find(i, start) fica no fluxo:
                        #  pos = texto.find('Gato', 0)
                        # isso retornaria 2 , porque ? , a Primeira Letra da Palavra Gato , ou seja 'G' esta situada no índice [2] da frase
                        # [0] =>  O
                        # [1] =>  
                        # [2] => G
                        # [3] => a
                        # [4] => t
                        # [5] => o
                        # [6] =>  
                        # [7] => C
                        # [8] => o
                        # [9] => r
                        # [10] => r
                        # [11] => e
                        # [12] => 
                        # [13] => M
                        # [14] => u
                        # [15] => i
                        # [16] => t
                        # [17] => o
                        # [18] =>  
                        # [19] => R
                        # [20] => á
                        # [21] => p
                        # [22] => i
                        # [23] => d
                        # [24] => o
                        # [25] =>  
                        # [26] => ,
                        # [27] =>  
                        # [28] => e
                        # [29] =>  
                        # [30] => o
                        # [31] =>  
                        # [32] => G
                        # [33] => a
                        # [34] => t
                        # [35] => o
                        # [36] =>  
                        # [37] => G
                        # [38] => o
                        # [39] => s
                        # [40] => t
                        # [41] => a
                        # [42] =>  
                        # [43] => d
                        # [44] => e
                        # [45] =>  
                        # [46] => C
                        # [47] => o
                        # [48] => r
                        # [49] => r
                        # [50] => e
                        # [51] => r
                        # [52] =>  
                        # [53] => c
                        # [54] => o
                        # [55] => m
                        # [56] =>  
                        # [57] => o
                        # [58] =>  
                        # [59] => G
                        # [60] => a
                        # [61] => t
                        # [62] => o
                        # isso significa que:
                        # pos = texto.find(i, start) => 2
                        indice = _TEXTO.find(i,start)
                        # se o indice por acaso for -1 , ou seja não encontrado , ja buscou todos os índices e eles não se encontram mais , ou o índice não existe , ele resultará em -1
                        if indice == -1:
                            # quebre o loop
                            break
                        # se não
                        # insira o indice aqui na array
                        if indice not in _INDICES_K_:
                            _INDICES_K_.append(indice)
                        # incrementa o start , para que ? 
                        # start = 0 , mas agora passa a ser:
                        # start = 2 + 1
                        # start = 3
                        start = indice + 1
                        # ele retornará la encima não como indice = texto.find("Gato",0) , uma nova busca será iniciada pois o start não é mais [0] , mas sim [3] , sendo:
                        # indice = texto.find("Gato",3) , buscando a partir do índice [3] , analisando a lista cima , onde se encontra o proximo "G" de "Gato" além do índice [2] ? 
                        # índice [32] é onde se encontra o primeiro "G" da segunda palavra "Gato" no texto , sendo assim: 
                        # start = índice + 1
                        # start = 32 + 1
                        # start = 33 
                        # uma nova procura 
                        # indice = texto.find("Gato",33)
                        # resumindo , o que estou fazendo ? , estou buscando incrementando o start , assim:
                        # - O QUE ACONTECEU - 
                        # indice = texto.find("Gato",0) - 0 porque inicia no índice [0] do texto , primeiro letra do texto até a letra "G" de "Gato" , ou seja se "G" de "Gato" é [2] então incremente mais +1 e se torna [a] , [a] de G[a]to , [a] é igual a [G] de [G]ato ? não então uma nova busca se inicia do primeiro [a] de G[a]to até o proximo [G] de [G]ato , sendo: 
                        # [G]ato = [2] -> indice = texto.find("Gato",0) - indice = [2] | [G] é encontrado no índice , então indice é [2] | start = indice + 1 =>> start = 2 + 1 =>> start = 3
                        # G[a]to = [3] -> indice = texto.find("Gato",3) - | nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' | 
                        # [G]ato = [32] -> indice = texto.find("Gato",32) indice = [32]| [G] é encontrado no índice , então índice é [32] | start = indice + 1 =>> start = 32 + 1 =>> start = 33
                        # G[a]to = [33] -> indice = texto.find("Gato",33) | nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' |
                        # [G]ato = [59] -> indice = texto.find("Gato",59) indice = [59]| [G] é encontrado no índice , então índice é [59] | start = indice + 1 =>> start = 59 + 1 =>> start = 60
                        # G[a]to = [60] -> indice = texto.find("Gato",60) indice = [60]| nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' | 
                        # se não existir mais NENHUM ÍNDICE REFERENTE AO [G] , ELE RETORNARÁ -1 , ou seja , nenhum índice foi encontrado , então -break- o loop while True 
                        # indice = texto.find("Gato",3) - 3 porque ele achou no índice [2] ai incrementou + 1 , pois a nova procura será do índice [3] em diante , sendo do índice [3] até a letra "G" da proxima Palavra "Gato" , 
                        # indice = texto.find("Gato",33) - 32 porque ele achou o índice [32] ai incremento + 1 , pois a nova procura será do índice [33] em diante , sendo do índice [33] até a letra "G" da proxima Palavra "Gato"
                        # 
                        # RECAPTULANDO
                        # 
                        # 1ª Busca : texto.find("Gato", 0) → Retorna índice: [2] - "G" da Primeira Palavra "Gato" na Frase/Texto
                        # Atualiza: start = [2] + 1 → start = 3
                        #
                        # 2ª Busca : texto.find("Gato", 3) → Retorna índice: [32] - "G" da Segunda Palavra "Gato" na Frase/Texto
                        # Atualiza: start = [32] + 1 → start = 33
                        #
                        # 3ª Busca : texto.find("Gato", 33) → Retorna índice: [59] - "G" da Terceira Palavra "Gato" na Frase/Texto
                        # Atualiza: start = [59] + 1 → start = 60
                        # 
                        # 4ª Busca : texto.find("Gato", 60) → Retorna índice: [-1] - Não Encontra Mais [-1] significa que não foi achado , então -break- finaliza o loop
        
    _INDICES_K_.sort()
    for i in _INDICES_K_:
        _RESPOSTAS_.append(_TEXTO[i:int(i + 1000)].replace('H2O', 'H₂O').replace('CO2', 'CO₂').replace('NaCl', 'NaCl').replace('Fe2O3', 'Fe₂O₃').replace('Al2O3', 'Al₂O₃').replace('CuSO4', 'CuSO₄').replace('H2SO4', 'H₂SO₄').replace('NH3', 'NH₃')  )
    resposta = 1
    for i in _RESPOSTAS_:
        print(f"\n {resposta}° - Resposta: \n")
        for j in i:
            time.sleep(.01)
            print(f"{j}",end="",flush=True)
            time.sleep(.01)
        resposta = resposta + 1
elif escolha.lower() == "a":
    if not os.path.exists(arquivo):
        with open('Parametros/Parametros.txt' , "r" , encoding="utf-8") as file:
            array_file = file.read().split()
            for i in array_file:
                response = requests.get(str(i))
                dados = BeautifulSoup(response.text , 'html.parser')
                elementFather = dados.find("div",class_="mw-content-ltr mw-parser-output")
                if elementFather is not None:
                    element = elementFather.find_all("p")
                    with open(arquivo , "a" , encoding="utf-8") as text:
                        for m in tqdm(element,desc="Extraindo Informações"):
                            text.write(f"{str(m.get_text())}")
        with open(arquivo, "r" , encoding="utf-8") as read:
            text = read.read()
            pergunta = input("🤔  Qual é a Sua Pergunta ? ")
            for i in pergunta.split():
                _QUESTIONS_.append(i)
            for i in _QUESTIONS_:
                if len(i) > 3 and i not in _KEYSWORDS_ or i.upper() == i and i.upper() not in ['Quem', 'O que', 'Que', 'Qual', 'Quais', 'Quanto', 'Quanta', 'Quantos', 'Quantas', 'Onde', 'Como', 'Por que', 'Para que', 'De onde', 'A que','A','E','I','O','U','ÃO']:
                    _KEYSWORDS_.append(i)
            for i in _KEYSWORDS_:
                for j in text.split():
                    if unidecode(i).lower() == unidecode(j).lower():
                        if unidecode(i).lower() == unidecode(j).lower():
                            # inicia o contador em 0
                            start = 0
                            # enquanto verdade for verdade (loop constante)
                            while True:
                                # indice vai ser igual:
                                # texto.find(i,start)
                                # ele encontra o índice da palavra no texto a partir do inicio 0 (start)
                                # tipo: 
                                # na frase: 
                                # 'O Gato Corre Muito Rápido , e o Gato Gosta de Correr com o Gato'
                                # o trecho: 
                                #  pos = texto.find(i, start) , sendo i = 'Gato' , busca por:
                                # 'Gato' , sendo assim:
                                #  pos = texto.find(i, start) fica no fluxo:
                                #  pos = texto.find('Gato', 0)
                                # isso retornaria 2 , porque ? , a Primeira Letra da Palavra Gato , ou seja 'G' esta situada no índice [2] da frase
                                # [0] =>  O
                                # [1] =>  
                                # [2] => G
                                # [3] => a
                                # [4] => t
                                # [5] => o
                                # [6] =>  
                                # [7] => C
                                # [8] => o
                                # [9] => r
                                # [10] => r
                                # [11] => e
                                # [12] => 
                                # [13] => M
                                # [14] => u
                                # [15] => i
                                # [16] => t
                                # [17] => o
                                # [18] =>  
                                # [19] => R
                                # [20] => á
                                # [21] => p
                                # [22] => i
                                # [23] => d
                                # [24] => o
                                # [25] =>  
                                # [26] => ,
                                # [27] =>  
                                # [28] => e
                                # [29] =>  
                                # [30] => o
                                # [31] =>  
                                # [32] => G
                                # [33] => a
                                # [34] => t
                                # [35] => o
                                # [36] =>  
                                # [37] => G
                                # [38] => o
                                # [39] => s
                                # [40] => t
                                # [41] => a
                                # [42] =>  
                                # [43] => d
                                # [44] => e
                                # [45] =>  
                                # [46] => C
                                # [47] => o
                                # [48] => r
                                # [49] => r
                                # [50] => e
                                # [51] => r
                                # [52] =>  
                                # [53] => c
                                # [54] => o
                                # [55] => m
                                # [56] =>  
                                # [57] => o
                                # [58] =>  
                                # [59] => G
                                # [60] => a
                                # [61] => t
                                # [62] => o
                                # isso significa que:
                                # pos = texto.find(i, start) => 2
                                indice = text.find(i,start)
                                # se o indice por acaso for -1 , ou seja não encontrado , ja buscou todos os índices e eles não se encontram mais , ou o índice não existe , ele resultará em -1
                                if indice == -1:
                                    # quebre o loop
                                    break
                                # se não
                                # insira o indice aqui na array
                                if indice not in _INDICES_K_:
                                    _INDICES_K_.append(indice)
                                # incrementa o start , para que ? 
                                # start = 0 , mas agora passa a ser:
                                # start = 2 + 1
                                # start = 3
                                start = indice + 1
                                # ele retornará la encima não como indice = texto.find("Gato",0) , uma nova busca será iniciada pois o start não é mais [0] , mas sim [3] , sendo:
                                # indice = texto.find("Gato",3) , buscando a partir do índice [3] , analisando a lista cima , onde se encontra o proximo "G" de "Gato" além do índice [2] ? 
                                # índice [32] é onde se encontra o primeiro "G" da segunda palavra "Gato" no texto , sendo assim: 
                                # start = índice + 1
                                # start = 32 + 1
                                # start = 33 
                                # uma nova procura 
                                # indice = texto.find("Gato",33)
                                # resumindo , o que estou fazendo ? , estou buscando incrementando o start , assim:
                                # - O QUE ACONTECEU - 
                                # indice = texto.find("Gato",0) - 0 porque inicia no índice [0] do texto , primeiro letra do texto até a letra "G" de "Gato" , ou seja se "G" de "Gato" é [2] então incremente mais +1 e se torna [a] , [a] de G[a]to , [a] é igual a [G] de [G]ato ? não então uma nova busca se inicia do primeiro [a] de G[a]to até o proximo [G] de [G]ato , sendo: 
                                # [G]ato = [2] -> indice = texto.find("Gato",0) - indice = [2] | [G] é encontrado no índice , então indice é [2] | start = indice + 1 =>> start = 2 + 1 =>> start = 3
                                # G[a]to = [3] -> indice = texto.find("Gato",3) - | nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' | 
                                # [G]ato = [32] -> indice = texto.find("Gato",32) indice = [32]| [G] é encontrado no índice , então índice é [32] | start = indice + 1 =>> start = 32 + 1 =>> start = 33
                                # G[a]to = [33] -> indice = texto.find("Gato",33) | nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' |
                                # [G]ato = [59] -> indice = texto.find("Gato",59) indice = [59]| [G] é encontrado no índice , então índice é [59] | start = indice + 1 =>> start = 59 + 1 =>> start = 60
                                # G[a]to = [60] -> indice = texto.find("Gato",60) indice = [60]| nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' | 
                                # se não existir mais NENHUM ÍNDICE REFERENTE AO [G] , ELE RETORNARÁ -1 , ou seja , nenhum índice foi encontrado , então -break- o loop while True 
                                # indice = texto.find("Gato",3) - 3 porque ele achou no índice [2] ai incrementou + 1 , pois a nova procura será do índice [3] em diante , sendo do índice [3] até a letra "G" da proxima Palavra "Gato" , 
                                # indice = texto.find("Gato",33) - 32 porque ele achou o índice [32] ai incremento + 1 , pois a nova procura será do índice [33] em diante , sendo do índice [33] até a letra "G" da proxima Palavra "Gato"
                                # 
                                # RECAPTULANDO
                                # 
                                # 1ª Busca : texto.find("Gato", 0) → Retorna índice: [2] - "G" da Primeira Palavra "Gato" na Frase/Texto
                                # Atualiza: start = [2] + 1 → start = 3
                                #
                                # 2ª Busca : texto.find("Gato", 3) → Retorna índice: [32] - "G" da Segunda Palavra "Gato" na Frase/Texto
                                # Atualiza: start = [32] + 1 → start = 33
                                #
                                # 3ª Busca : texto.find("Gato", 33) → Retorna índice: [59] - "G" da Terceira Palavra "Gato" na Frase/Texto
                                # Atualiza: start = [59] + 1 → start = 60
                                # 
                                # 4ª Busca : texto.find("Gato", 60) → Retorna índice: [-1] - Não Encontra Mais [-1] significa que não foi achado , então -break- finaliza o loop
            _INDICES_K_.sort()
            for i in _INDICES_K_:
                _RESPOSTAS_.append(text[i:int(i + 1000)].replace('H2O', 'H₂O').replace('CO2', 'CO₂').replace('NaCl', 'NaCl').replace('Fe2O3', 'Fe₂O₃').replace('Al2O3', 'Al₂O₃').replace('CuSO4', 'CuSO₄').replace('H2SO4', 'H₂SO₄').replace('NH3', 'NH₃')  )
            resposta = 1
            for i in _RESPOSTAS_:
                print(f"\n {resposta}° - Resposta: \n")
                for j in i:
                    time.sleep(.01)
                    print(f"{j}",end="",flush=True)
                    time.sleep(.01)
                resposta = resposta + 1
    elif os.path.exists(arquivo):
        with open(arquivo , "r" , encoding="utf-8") as file:
            texto = file.read()
            pergunta = input("🤔  Qual é a Sua Pergunta ? ")
            for i in pergunta.split():
                _QUESTIONS_.append(i)
            for i in _QUESTIONS_:
                if len(i) > 3 and i not in _KEYSWORDS_ or i.upper() == i and i.upper() not in ['Quem', 'O que', 'Que', 'Qual', 'Quais', 'Quanto', 'Quanta', 'Quantos', 'Quantas', 'Onde', 'Como', 'Por que', 'Para que', 'De onde', 'A que','A','E','I','O','U','ÃO']:
                    _KEYSWORDS_.append(i)
            for i in _KEYSWORDS_:
                for j in texto.split():
                    if unidecode(i).lower() == unidecode(j).lower():
                        # inicia o contador em 0
                        start = 0
                        # enquanto verdade for verdade (loop constante)
                        while True:
                            # indice vai ser igual:
                            # texto.find(i,start)
                            # ele encontra o índice da palavra no texto a partir do inicio 0 (start)
                            # tipo: 
                            # na frase: 
                            # 'O Gato Corre Muito Rápido , e o Gato Gosta de Correr com o Gato'
                            # o trecho: 
                            #  pos = texto.find(i, start) , sendo i = 'Gato' , busca por:
                            # 'Gato' , sendo assim:
                            #  pos = texto.find(i, start) fica no fluxo:
                            #  pos = texto.find('Gato', 0)
                            # isso retornaria 2 , porque ? , a Primeira Letra da Palavra Gato , ou seja 'G' esta situada no índice [2] da frase
                            # [0] =>  O
                            # [1] =>  
                            # [2] => G
                            # [3] => a
                            # [4] => t
                            # [5] => o
                            # [6] =>  
                            # [7] => C
                            # [8] => o
                            # [9] => r
                            # [10] => r
                            # [11] => e
                            # [12] => 
                            # [13] => M
                            # [14] => u
                            # [15] => i
                            # [16] => t
                            # [17] => o
                            # [18] =>  
                            # [19] => R
                            # [20] => á
                            # [21] => p
                            # [22] => i
                            # [23] => d
                            # [24] => o
                            # [25] =>  
                            # [26] => ,
                            # [27] =>  
                            # [28] => e
                            # [29] =>  
                            # [30] => o
                            # [31] =>  
                            # [32] => G
                            # [33] => a
                            # [34] => t
                            # [35] => o
                            # [36] =>  
                            # [37] => G
                            # [38] => o
                            # [39] => s
                            # [40] => t
                            # [41] => a
                            # [42] =>  
                            # [43] => d
                            # [44] => e
                            # [45] =>  
                            # [46] => C
                            # [47] => o
                            # [48] => r
                            # [49] => r
                            # [50] => e
                            # [51] => r
                            # [52] =>  
                            # [53] => c
                            # [54] => o
                            # [55] => m
                            # [56] =>  
                            # [57] => o
                            # [58] =>  
                            # [59] => G
                            # [60] => a
                            # [61] => t
                            # [62] => o
                            # isso significa que:
                            # pos = texto.find(i, start) => 2
                            indice = texto.find(i,start)
                            # se o indice por acaso for -1 , ou seja não encontrado , ja buscou todos os índices e eles não se encontram mais , ou o índice não existe , ele resultará em -1
                            if indice == -1:
                                # quebre o loop
                                break
                            # se não
                            # insira o indice aqui na array
                            if indice not in _INDICES_K_:
                                _INDICES_K_.append(indice)
                            # incrementa o start , para que ? 
                            # start = 0 , mas agora passa a ser:
                            # start = 2 + 1
                            # start = 3
                            start = indice + 1
                            # ele retornará la encima não como indice = texto.find("Gato",0) , uma nova busca será iniciada pois o start não é mais [0] , mas sim [3] , sendo:
                            # indice = texto.find("Gato",3) , buscando a partir do índice [3] , analisando a lista cima , onde se encontra o proximo "G" de "Gato" além do índice [2] ? 
                            # índice [32] é onde se encontra o primeiro "G" da segunda palavra "Gato" no texto , sendo assim: 
                            # start = índice + 1
                            # start = 32 + 1
                            # start = 33 
                            # uma nova procura 
                            # indice = texto.find("Gato",33)
                            # resumindo , o que estou fazendo ? , estou buscando incrementando o start , assim:
                            # - O QUE ACONTECEU - 
                            # indice = texto.find("Gato",0) - 0 porque inicia no índice [0] do texto , primeiro letra do texto até a letra "G" de "Gato" , ou seja se "G" de "Gato" é [2] então incremente mais +1 e se torna [a] , [a] de G[a]to , [a] é igual a [G] de [G]ato ? não então uma nova busca se inicia do primeiro [a] de G[a]to até o proximo [G] de [G]ato , sendo: 
                            # [G]ato = [2] -> indice = texto.find("Gato",0) - indice = [2] | [G] é encontrado no índice , então indice é [2] | start = indice + 1 =>> start = 2 + 1 =>> start = 3
                            # G[a]to = [3] -> indice = texto.find("Gato",3) - | nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' | 
                            # [G]ato = [32] -> indice = texto.find("Gato",32) indice = [32]| [G] é encontrado no índice , então índice é [32] | start = indice + 1 =>> start = 32 + 1 =>> start = 33
                            # G[a]to = [33] -> indice = texto.find("Gato",33) | nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' |
                            # [G]ato = [59] -> indice = texto.find("Gato",59) indice = [59]| [G] é encontrado no índice , então índice é [59] | start = indice + 1 =>> start = 59 + 1 =>> start = 60
                            # G[a]to = [60] -> indice = texto.find("Gato",60) indice = [60]| nova procura do [a] até proxímo [G] da proxíma palavra 'Gato' | 
                            # se não existir mais NENHUM ÍNDICE REFERENTE AO [G] , ELE RETORNARÁ -1 , ou seja , nenhum índice foi encontrado , então -break- o loop while True 
                            # indice = texto.find("Gato",3) - 3 porque ele achou no índice [2] ai incrementou + 1 , pois a nova procura será do índice [3] em diante , sendo do índice [3] até a letra "G" da proxima Palavra "Gato" , 
                            # indice = texto.find("Gato",33) - 32 porque ele achou o índice [32] ai incremento + 1 , pois a nova procura será do índice [33] em diante , sendo do índice [33] até a letra "G" da proxima Palavra "Gato"
                            # 
                            # RECAPTULANDO
                            # 
                            # 1ª Busca : texto.find("Gato", 0) → Retorna índice: [2] - "G" da Primeira Palavra "Gato" na Frase/Texto
                            # Atualiza: start = [2] + 1 → start = 3
                            #
                            # 2ª Busca : texto.find("Gato", 3) → Retorna índice: [32] - "G" da Segunda Palavra "Gato" na Frase/Texto
                            # Atualiza: start = [32] + 1 → start = 33
                            #
                            # 3ª Busca : texto.find("Gato", 33) → Retorna índice: [59] - "G" da Terceira Palavra "Gato" na Frase/Texto
                            # Atualiza: start = [59] + 1 → start = 60
                            # 
                            # 4ª Busca : texto.find("Gato", 60) → Retorna índice: [-1] - Não Encontra Mais [-1] significa que não foi achado , então -break- finaliza o loop
            _INDICES_K_.sort()
            for i in _INDICES_K_:
                _RESPOSTAS_.append(texto[i:int(i + 1000)].replace('H2O', 'H₂O').replace('CO2', 'CO₂').replace('NaCl', 'NaCl').replace('Fe2O3', 'Fe₂O₃').replace('Al2O3', 'Al₂O₃').replace('CuSO4', 'CuSO₄').replace('H2SO4', 'H₂SO₄').replace('NH3', 'NH₃')  )
            resposta = 1
            for i in _RESPOSTAS_:
                print(f"\n {resposta}° - Resposta: \n")
                for j in i:
                    time.sleep(.01)
                    print(f"{j}",end="",flush=True)
                    time.sleep(.01)
                resposta = resposta + 1