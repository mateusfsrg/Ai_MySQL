import customtkinter
import tkinter as tk
from tkinter import Scrollbar
import mysql.connector
import google.generativeai as genai
from prettytable import PrettyTable

# estetica inicial
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
janela = customtkinter.CTk()
janela.geometry("800x800")

# criando def para conectar a base de dados,
# com mensagem de erro caso não consiga conectar
def conector(host, user, password, database):
    try:
        meuBd = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return meuBd
    except mysql.connector.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

# cria variavel para inserir a chave de api
def key(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')
# cria a variavel vazia do modelo
model = None

# Função para executar a consulta ou adição/alteração no banco de dados
def executar_prompt(meuBd, tipo, entrada_prompt, resultado_textbox):
    pre_texto = 'Apenas envie os comandos, pois irá direto para um script no MySQL.'
    prompt = pre_texto + entrada_prompt.get()  # Obtém o texto do campo de entrada

    try:
        response = model.generate_content(prompt)
        resposta_texto = response._result.candidates[0].content.parts[0].text
        resposta_texto = resposta_texto.strip().replace("```sql", "").replace("```", "").strip('"').strip()

        cursor = meuBd.cursor()
        resultado_textbox.delete("1.0", customtkinter.END)  # Limpa a caixa de texto antes de exibir novos resultados
        if tipo == "Consulta":
            cursor.execute(resposta_texto)
            resultado = cursor.fetchall()

            if resultado:
                table = PrettyTable()
                colunas = [desc[0] for desc in cursor.description]
                table.field_names = colunas
                for row in resultado:
                    table.add_row(row)
                resultado_textbox.insert(customtkinter.END, str(table) + "\n")
                resultado_textbox.configure(state='normal')  # Permitir edição para scroll horizontal
                print('Comando executado')
            else:
                resultado_textbox.insert(customtkinter.END, "Nenhum resultado encontrado.\n")
        elif tipo == "Adicionar/Alterar":
            cursor.execute(resposta_texto)
            meuBd.commit()
            resultado_textbox.insert(customtkinter.END, "Operação realizada com sucesso.\n")
        cursor.close()
    except Exception as e:
        resultado_textbox.insert(customtkinter.END, f"Erro: {e}\n")

# Função para iniciar a tela principal após login bem-sucedido
def tela_app(meuBd):
    # Limpa os widgets da tela de login
    for widget in janela.winfo_children():
        widget.destroy()

    # Adiciona novos widgets para a nova tela
    novo_texto = customtkinter.CTkLabel(janela, text="Tela de Busca")
    novo_texto.pack(padx=20, pady=20)

    entrada_prompt = customtkinter.CTkEntry(janela, placeholder_text="Digite seu prompt aqui", width=650)
    entrada_prompt.pack(padx=20, pady=20)

    # Criando um frame para o resultado e a barra de rolagem
    resultado_frame = tk.Frame(janela)
    resultado_frame.pack(padx=20, pady=20)

    # Caixa de texto para resultados com rolagem horizontal
    resultado_textbox = tk.Text(resultado_frame, wrap='none', height=10, width=80)
    resultado_textbox.pack(side=tk.LEFT)

    # Adicionando barra de rolagem horizontal
    scroll_x = Scrollbar(resultado_frame, orient=tk.HORIZONTAL, command=resultado_textbox.xview)
    resultado_textbox.configure(xscrollcommand=scroll_x.set)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

    consulta_button = customtkinter.CTkButton(
        janela, text="Consulta",
        command=lambda: executar_prompt(meuBd, "Consulta", entrada_prompt, resultado_textbox)
    )
    consulta_button.pack(padx=20, pady=20)

    alterar_button = customtkinter.CTkButton(
        janela, text="Adicionar/Alterar",
        command=lambda: executar_prompt(meuBd, "Adicionar/Alterar", entrada_prompt, resultado_textbox)
    )
    alterar_button.pack(padx=20, pady=20)

    sair = customtkinter.CTkButton(janela, text="Sair", command=janela.quit)
    sair.pack(padx=20, pady=20)

# Função chamada ao clicar no botão "Entrar" para conectar ao banco e abrir a nova tela
def clique():
    global model  # Permite acesso global ao model
    host_input = host.get()
    user_input = user.get()
    senha_input = senha.get()
    database_input = database.get()
    api_key_input = api_key.get()  # Obtém a chave da API

    meuBd = conector(host_input, user_input, senha_input, database_input)
    if meuBd:
        print("Login efetuado com sucesso!")
        model = key(api_key_input)  # Configura a chave da API
        tela_app(meuBd)
    else:
        print("Falha no login. Verifique as credenciais e tente novamente.")

# Widgets da tela inicial de login
texto = customtkinter.CTkLabel(janela, text="Controle de Acesso")
user = customtkinter.CTkEntry(janela, placeholder_text="Digite o User: ")
senha = customtkinter.CTkEntry(janela, placeholder_text="Digite a senha: ", show="*")
host = customtkinter.CTkEntry(janela, placeholder_text="Digite o host: ")
database = customtkinter.CTkEntry(janela, placeholder_text="Digite a database: ")
api_key = customtkinter.CTkEntry(janela, placeholder_text="Digite sua chave da API Gemini: ")  # Novo campo para a chave da API
botao = customtkinter.CTkButton(janela, text="Entrar", command=clique)

# Posicionando widgets na tela inicial
texto.pack(padx=10, pady=10)
user.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
host.pack(padx=10, pady=10)
database.pack(padx=10, pady=10)
api_key.pack(padx=10, pady=10)  # Posicionando o campo da chave da API
botao.pack(padx=10, pady=10)


def abrir_linkedin(event):
    import webbrowser
    webbrowser.open("https://www.linkedin.com/in/mateusfsrgsouza/")

rodape = customtkinter.CTkLabel(janela, text="Criado por Mateus Souza", cursor="hand2")
rodape.pack(side=tk.BOTTOM, pady=10)
rodape.bind("<Button-1>", abrir_linkedin)

# Exibindo a janela
janela.mainloop()
