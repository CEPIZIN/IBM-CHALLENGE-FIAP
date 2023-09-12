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

#adicionar relatorios
def adicionar_relatorio():
    validar_senha()
    while True:
        print("Adicionar um relatório (comece com a data de ocorrência - DD/MM/YYYY):")
        data_ocorreu = input("Data: ")
        hora_ocorreu = input("Hora: ")
        conteudo_relatorio = input("Relatório: ")
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

  #visualizar relatorio           
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

def encerrar_programa():
    print("Encerrando...")
    exit()
    return

# Configuração do menu
opcoes_menu = {
    "1": adicionar_relatorio,
    "2": visualizar_relatorios,
    "3": encerrar_programa,
}

while True:
    print("\nSelecione uma opção:")
    print("1 - Adicionar relatórios de eventos")
    print("2 - Visualizar lista de eventos")
    print("3 - Sair")

    escolha = input("->")
    if escolha in opcoes_menu:
        opcoes_menu[escolha]()
    else:
        print("Opção inválida. Por favor, digite novamente.")