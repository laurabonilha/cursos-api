'''
Classe criada para compilar elementos em comum da interface gráfica
'''
import tkinter as tk
import customtkinter as ctk


def create_label(parent, text):
    '''Cria um label'''
    label = ctk.CTkLabel(
        parent,
        text=text,
        font=('Poppins', 16),  # Definindo tamanho e fonte
        text_color='white',    # Ajuste de cor 
        anchor='center'             # Alinha o texto no centro
    )
    label.pack(pady=5, anchor='center')  # Ajusta o alinhamento e o espaçamento vertical
    return label


def create_entry(parent):
    '''Cria um campo de entrada'''
    entry = tk.Entry(
        parent,
        font=('Poppins', 12),
        width=20,
        bg='black',        # Cor de fundo preta
        fg='white',        # Cor do texto branca
        insertbackground='white'  # Cor do cursor também branco
    )
    entry.pack(pady=5)
    return entry


def create_button(parent,text,command):
    '''Cria um botão'''
    button = tk.Button(parent,text=text, command=command, font=('Poppins', 12), bg='blue', fg='white')
    button.pack(pady=10)
    return button

