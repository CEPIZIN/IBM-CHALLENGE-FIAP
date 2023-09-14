from datetime import datetime

senha = "548400"
dados = []

def validar_senha():
    senha_usuario = input("SENHA -> ")
    if senha_usuario == senha:
        print("Acesso concedido.")
    else:
        print("Senha inválida.")
        validar_senha()
    return

# cria relatorios
def adicionar_relatorio():
    validar_senha()
    while True:
        print("Adicionar um relatório ")
        data_ocorreu = input("Data (DD/MM/YYYY): ")
        hora_ocorreu = input("Hora (HH:MM): ")
        conteudo_relatorio = input("Relatório: ")
        try:
           datetime.strptime(data_ocorreu, "%d/%m/%Y")
           datetime.strptime(hora_ocorreu, "%H:%M")
        except ValueError:
            print("Formato da data ou hora inválido. Use DD/MM/YYYY e HH:MM. ")
            continue
        relatorio = {
            "data": data_ocorreu,
            "hora": hora_ocorreu,
            "conteudo": conteudo_relatorio,
        }
        dados.append(relatorio)
        print("Relatório adicionado com sucesso.")
        adicionar_mais = input("Deseja adicionar outro relatório? (s/n): ")
        if adicionar_mais.lower() == 'n':
            break
        elif adicionar_mais.lower() != 's':
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")
    return

# visualizar relatorio           
def visualizar_relatorios():
    validar_senha()
    print("\nALERTA!")
    print("Esta seção é apenas para visualização")
    if not dados:
        print("Nenhum dado registrado")
    else:
        for i, relatorio in enumerate(dados, 1):
            print(f"{i}. Data: {relatorio['data']} Hora: {relatorio['hora']} - {relatorio['conteudo']}")
    return

#buscar eventos
def buscar_eventos():
    validar_senha()
    termo_busca = input("Digite um termo para buscar: ")
    resultados = []
    for relatorio in dados:
        if termo_busca.lower() in relatorio['conteudo'].lower():
            resultados.append(relatorio)

    if not resultados:
        print(f"Nenhum resultado encontrado para '{termo_busca}'.")
    else:
        print(f"Resultados encontrados para '{termo_busca}':")
        for i, relatorio in enumerate(resultados, 1):
            print(f"{i}. Data: {relatorio['data']} Hora: {relatorio['hora']} - {relatorio['conteudo']}")

def encerrar_programa():
    print("Encerrando...")
    exit()
    return

# Configuração do menu
opcoes_menu = {
    "1": adicionar_relatorio,
    "2": visualizar_relatorios,
    "3": buscar_eventos,  
    "4": encerrar_programa,
}
while True:
    print("\nSelecione uma opção:")
    print("1 - Adicionar relatórios de eventos")
    print("2 - Visualizar lista de eventos")
    print("3 -  Buscar relatorio")
    print("4- Sair")

    escolha = input("->")
    if escolha in opcoes_menu:
        opcoes_menu[escolha]()
    else:
        print("Opção inválida. Por favor, digite novamente.")