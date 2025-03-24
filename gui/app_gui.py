'''
ARQUIVO DE INTERFACE GRÁFICA - OPCIONAL - PARA UTILIZAR A API USANDO CUSTOMTKINTER

'''

import customtkinter as ctk
import requests

# Configuração inicial do tema e aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Criando a Janela Principal
app = ctk.CTk()
app.geometry("500x400")
app.title("Gerenciamento de Cursos")

# Adicionando um curso
def adicionar_curso():
    nome = nome_entry.get()
    aulas = aulas_entry.get()
    
    if nome and aulas.isdigit():
        dados = {"nome": nome, "numero_aulas": int(aulas)}
        resposta = requests.post("http://127.0.0.1:8000/cursos", json=dados)
    

# Componentes da interface
nome_label = ctk.CTkLabel(app, text="Nome do Curso:")
nome_label.pack(pady=5)

# Cria os campos de entrada de texto onde o usuário pode digitar informações
nome_entry = ctk.CTkEntry(app, width=300)
nome_entry.pack(pady=5)



# Adicionando o loop principal da interface gráfica
app.mainloop()