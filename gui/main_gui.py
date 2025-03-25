import customtkinter as ctk
import json
from gui.pages import Pages


'''
COMPONENTES DE INTERFACE GRÁFICA
'''

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.geometry("400x500")
janela.title("Menu de Opções")

pages = Pages(janela)
pages.mostrar_menu_principal()

janela.mainloop()