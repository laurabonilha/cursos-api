'''
Arquivo principal que gerencia a interface gráfica
Esse arquivo inicializa a interface e carrega a página inicial.
'''

import customtkinter as ctk
from pages import HomePage

# Configuração inicial do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Gerenciamento de Cursos")

        # Página inicial
        self.home_page = HomePage(self)
        self.home_page.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = App()
    app.mainloop()
