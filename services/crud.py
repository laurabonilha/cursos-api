'''
Arquivo destinado a armazenar as funções que devem ser feitas comunicando a interface com a API
'''

import requests
import customtkinter as ctk

# URL da API onde os cursos estão sendo gerenciados
API_URL = "http://localhost:8000/cursos"

# Adicionando um curso
def adicionar_curso():
    # Capturando os dados informados pelo usuário na interface
    nome = nome_entry.get()
    aulas = aulas_entry.get()
    horas = horas_entry.get()
    
    # Verifica se foi informado nome e se aulas e horas são números
    if nome and aulas.isdigit() and horas.isdigit():
        dados = {"titulo": str(nome), "aulas": int(aulas), "horas": int (horas)}
        # Envia uma requisição POST para a API FastAPI para adicionar o curso no banco de dados.
        resposta = requests.post("http://localhost:8000/api/v1/cursos", json=dados)
        
        # Em caso de resposta de sucesso informa que o curso foi adicionado com sucesso
        if resposta.status_code == 201:
            print('Curso adicionado com sucesso')
            # status_label.configure(text="Curso adicionado com sucesso!", text_color="green")
        else:
            print('Erro ao adicionar curso')
            # status_label.configure(text="Erro ao adicionar curso", text_color="red")
    else:
        print('Preencha os campos corretamente')
        # status_label.configure(text="Preencha os campos corretamente", text_color="red")


janela = ctk.CTkToplevel()
janela.geometry("400x300")
janela.title("Adicionar Curso")

# Componentes da interface
# RÓTULO - "Digite o nome do curso"
nome_label = ctk.CTkLabel(
    janela, 
    text="Nome do Curso:",       # Texto exibido
    text_color="white",          # Cor do texto (pode ser "red", "blue", "#HEX")
    font=("Poppins", 16, "bold"),# Fonte do texto (família, tamanho, estilo)
    bg_color="transparent",      # Cor de fundo do label
    width=200,                   # Largura do label
    height=30,                   # Altura do label
    anchor="w"                   # Alinhamento do texto ("w" = esquerda, "center" = centro, "e" = direita)
)
nome_label.pack(pady=5)

# INPUT - curso
nome_entry = ctk.CTkEntry(
    janela, 
    width=300,                  # Largura do campo
    height=40,                  # Altura do campo
    placeholder_text="Digite o nome do curso",  # Texto dentro do campo antes de digitar
    text_color="white",          # Cor do texto digitado
    fg_color="#1E1E1E",         # Cor do fundo do campo
    corner_radius=10,           # Arredondamento das bordas
    border_width=2,             # Largura da borda
    border_color="blue",        # Cor da borda
    font=("Poppins", 14)        # Fonte do texto dentro do campo
)
nome_entry.pack(pady=5)

# RÓTULO - "Digite o número de aulas"
aulas_label = ctk.CTkLabel(
    janela, 
    text="Número de aulas:",       # Texto exibido
    text_color="white",          # Cor do texto (pode ser "red", "blue", "#HEX")
    font=("Poppins", 16, "bold"),# Fonte do texto (família, tamanho, estilo)
    bg_color="transparent",      # Cor de fundo do label
    width=200,                   # Largura do label
    height=30,                   # Altura do label
    anchor="w"                   # Alinhamento do texto ("w" = esquerda, "center" = centro, "e" = direita)
)
aulas_label.pack(pady=5)

# INPUT - aulas
aulas_entry = ctk.CTkEntry(
    janela, 
    width=300,                  # Largura do campo
    height=40,                  # Altura do campo
    placeholder_text="Digite a quantidade de aulas",  # Texto dentro do campo antes de digitar
    text_color="white",          # Cor do texto digitado
    fg_color="#1E1E1E",         # Cor do fundo do campo
    corner_radius=10,           # Arredondamento das bordas
    border_width=2,             # Largura da borda
    border_color="blue",        # Cor da borda
    font=("Poppins", 14)        # Fonte do texto dentro do campo
)
aulas_entry.pack(pady=5)

# RÓTULO - "Digite o número de horas"
horas_label = ctk.CTkLabel(
    janela, 
    text="Número de horas:",       # Texto exibido
    text_color="white",          # Cor do texto (pode ser "red", "blue", "#HEX")
    font=("Poppins", 16, "bold"),# Fonte do texto (família, tamanho, estilo)
    bg_color="transparent",      # Cor de fundo do label
    width=200,                   # Largura do label
    height=30,                   # Altura do label
    anchor="w"                   # Alinhamento do texto ("w" = esquerda, "center" = centro, "e" = direita)
)
horas_label.pack(pady=5)

# INPUT - horas
horas_entry = ctk.CTkEntry(
    janela, 
    width=300,                  # Largura do campo
    height=40,                  # Altura do campo
    placeholder_text="Digite a quantidade de horas",  # Texto dentro do campo antes de digitar
    text_color="white",          # Cor do texto digitado
    fg_color="#1E1E1E",         # Cor do fundo do campo
    corner_radius=10,           # Arredondamento das bordas
    border_width=2,             # Largura da borda
    border_color="blue",        # Cor da borda
    font=("Poppins", 14)        # Fonte do texto dentro do campo
)
horas_entry.pack(pady=5)


# Botão de adicionar curso
botao_adicionar = ctk.CTkButton(janela, text="Adicionar Curso", command=adicionar_curso)
botao_adicionar.pack(pady=20)