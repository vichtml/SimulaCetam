import os, datetime, random, getch, socket

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('clear')

def linha():
    print('-----------------------------------------------------------------------------------------')

def print_limitado(texto, limite):
    partes = [texto[i:i+limite] for i in range(0, len(texto), limite)]
    for parte in partes:
        print(parte)

def print_centralizado(palavra):
    largura_terminal = os.get_terminal_size().columns
    print(palavra.center(largura_terminal))

def data_hora():
    # Obtém a data e hora atual
    agora = datetime.datetime.now()
    # Formata a data e hora para imprimir
    data_completa = agora.strftime("%A, %d de %B de %Y - %H:%M:%S")
    # Imprime a data e hora completa
    print("  DATA E HORA: ", data_completa)

def mostra_host_ip():
    # Obtém o hostname do sistema
    hostname = socket.gethostname()
    # Obtém o endereço IP do sistema
    endereco_ip = socket.gethostbyname(hostname)
    print("  HOSTNAME:", hostname + '.' + "IP: ", endereco_ip)

def aguarde():
    print('  Pressione qualquer tecla para prosseguir...')
    getch.getch()

def hello():
    print('')
    os.system('figlet ....SIMULA CETAM')   
    print('              😊' + ' ALEGRIA 1.0 - SIMULADOR DE QUESTÕES DE TECNOLOGIA')  
    print('')
    print('')
    print('                    CENTRO DE EDUCAÇÃO TECNOLÓGICA DO AMAZONAS')
    print('                               by: professor.bugador@gmail.com')
    linha()
    data_hora()
    mostra_host_ip()
    
# Função para carregar as questões do arquivo
def carregar_questoes(nome_arquivo):
    questoes = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                questao, resposta = linha.strip().split('; ')
                questoes.append((questao, resposta))
    except FileNotFoundError:
        print("Arquivo de questões não encontrado.")
    return questoes

def selecionar_questoes(arquivo, quantidade):
    # Lista para armazenar as questões selecionadas
    questoes_selecionadas = []

    # Abre o arquivo e lê todas as linhas
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    # Embaralha as linhas para seleção aleatória
    random.shuffle(linhas)

    # Itera sobre as linhas para selecionar as questões
    for linha in linhas:
        # Divide a linha em pergunta e resposta
        pergunta, resposta = linha.strip().split('; ')
        print(pergunta, resposta)
        # Verifica se a resposta é 'V' (verdadeira) ou 'F' (falsa)
        if resposta == 'V':
            questoes_selecionadas.append((pergunta, "V"))
        elif resposta == 'F':
            questoes_selecionadas.append((pergunta, "F"))

        # Se já foram selecionadas a quantidade desejada de questões, sai do loop
        if len(questoes_selecionadas) == quantidade:
            break

    return questoes_selecionadas

# Exemplo de uso da função
#questoes = selecionar_questoes('quiz.dat', 30)
#for i, (pergunta, resposta) in enumerate(questoes, start=1):
#    print(f"{i}. {pergunta} (Resposta: {'Verdadeira' if resposta else 'Falsa'})")


# Função para iniciar o quiz
def iniciar_quiz(questoes):
    limpar_tela()
    pontuacao = 0
    for questao, resposta in questoes:
        hello()
        linha()
        print('')
        texto = "  PERGUNTA ==> " + questao + " : " +  resposta
        print_limitado(texto, 88)
        print('')
        print('  RESPOSTA: (V/F)')

        resposta_usuario = input("  =======>: ").upper()        
        print('')            
        if resposta_usuario == resposta:
                print("  Resposta correta!")
                pontuacao += 1
        else:
                print("  Resposta incorreta.")

        print('  RESUMO: ')
        print("  Pontuação: {}/{}".format(pontuacao, len(questoes)))
        linha()
        aguarde()
        limpar_tela()

# Função para carregar um novo arquivo de questões
def carregar_novo_arquivo():
    nome_arquivo = input("Digite o nome do novo arquivo de questões: ")
    return carregar_questoes(nome_arquivo)

# Função para mostrar o total de questões na base de dados
def mostrar_total_questoes(questoes):
    print("Número de questões na base de dados:", len(questoes))

# Função principal
def main():
    nome_arquivo = "quiz.dat"  # Nome padrão do arquivo de questões
    #questoes = carregar_questoes(nome_arquivo)
    #questoes = selecionar_questoes("quiz.dat", 5)
    #iniciar_quiz(questoes)

    while True:
        limpar_tela()
        linha()
        hello()
        linha()
        print("  MENU DE OPÇÕES:")
        linha()
        print("  1. INICIAR QUIZ")
        print("  2. REGISTRAR NICKNAME")
        print("  3. MOSTRAR OS TOP20")
        print("  4. SELECIONAR QUESTÕES")
        print("  0. SAIR")
        linha();       
        opcao = input("  SELECIONE A OPÇÃO DESEJADA ==> : ")

        if opcao == "1":
            limpar_tela()
            questoes = selecionar_questoes("quiz.dat", 5)
            iniciar_quiz(questoes)
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            limpar_tela()
            questoes = carregar_novo_arquivo()
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            limpar_tela()
            mostrar_total_questoes(questoes)
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            limpar_tela()
            questoes = selecionar_questoes("quiz.dat", 2)
            input("Pressione Enter para continuar...")

        elif opcao == "0":
            limpar_tela()
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

