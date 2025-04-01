'''
Arquivo para organização de todas as telas da aplicação 
'''

import customtkinter as ctk
# Importando as funções de request da API
from services.crud import adicionar_curso, obter_cursos, excluir_curso, atualizar_curso, excluir_curso_nome
# Importando os elementos comuns de interface gráfica
from gui.componentes import create_button, create_entry, create_label, create_message


class Pages:
    def __init__(self, root):
        '''Inicializa a classe Pages com a referência da janela principal'''
        self.root = root
        self.frame_atual = None #Variável para armazenar o frame ativo
        
    def limpar_tela(self):
        '''Remove o frame atual antes de carregar uma nova tela'''
        if self.frame_atual:
            self.frame_atual.destroy()
            
    def mostrar_menu_principal(self):
        '''Ativa o menu principal'''
        self.limpar_tela()
        tela_menu = ctk.CTkFrame(self.root)
        tela_menu.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_menu
        botao_adicionar = create_button(parent=tela_menu, text='Adicionar curso', command=self.abrir_tela_adicionar_curso)
        
        botao_ver = create_button(parent=tela_menu, text='Ver cursos', command=self.abrir_tela_ver_cursos)
        
        botao_alterar = create_button(parent=tela_menu, text='Alterar curso', command=self.abrir_tela_adicionar_curso)
        
        botao_excluir = create_button(parent=tela_menu, text='Excluir curso', command=self.abrir_tela_deletar_curso)
        
    def abrir_tela_ver_cursos(self):
        '''Tela para visualizar todos os cursos cadastrados'''
        # Limpando a tela principal
        self.limpar_tela()
        #Abrindo aidiconar cursos na janela principal
        tela_ver_cursos = ctk.CTkFrame(self.root)
        tela_ver_cursos.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_ver_cursos
        create_label(parent=tela_ver_cursos, text='Todos os cursos cadastrados')
        
        retorno_cursos = obter_cursos() #Retorno em forma de dicionário
        
        # Tratativa para verificar se houve retorno de cursos cadastrados e, se não houver, mostrar mensagem na tela 
        if len(retorno_cursos) > 0:
            # Imprimindo todos os cursos, com título, horas e aulas
            for curso in retorno_cursos:
                create_label(parent=tela_ver_cursos, text=f"Título: {curso['titulo']} \n Aulas: {curso['aulas']} \n Horas {curso['horas']}") 
        else:
            create_label(parent=tela_ver_cursos, text='Não há cursos cadastrados')
    
                    
        botao_voltar = create_button(tela_ver_cursos, text='Voltar', command=self.mostrar_menu_principal)
    
    
    def abrir_tela_adicionar_curso(self):
        ''' Tela que permite ao usuário cadastrar um novo curso'''
        # Limpando a tela principal
        self.limpar_tela()
        tela_adicionar_curso = ctk.CTkFrame(self.root)
        tela_adicionar_curso.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_adicionar_curso
        create_label(parent=tela_adicionar_curso, text='Informe os dados do curso a ser cadastrado')
        
        # Criando entrada para o nome do curso
        create_label(parent=tela_adicionar_curso, text='Nome do curso')
        entry_nome_curso = create_entry(parent=tela_adicionar_curso)
        
        
        # Criando entrada para o número de aulas
        create_label(parent=tela_adicionar_curso, text='Número de aulas')
        entry_aulas_curso = create_entry(parent=tela_adicionar_curso)
        
        
        # Criando entrada para o número de horas
        create_label(parent=tela_adicionar_curso, text='Horas de curso')
        entry_horas_curso = create_entry(parent=tela_adicionar_curso)
        
        
        # Definindo que os dados só serão enviados quando o botão for pressionado
        botao_enviar_curso = create_button(
            parent=tela_adicionar_curso,
            text='Enviar',
            command=lambda: (
        create_message(tela_adicionar_curso, "✅ Sucesso!", True) 
        if adicionar_curso(entry_nome_curso.get(), entry_horas_curso.get(), entry_aulas_curso.get()) 
        else create_message(tela_adicionar_curso, "❌ Erro!", False)
    ) if all([entry_nome_curso.get(), entry_horas_curso.get(), entry_aulas_curso.get()]) 
    else create_message(tela_adicionar_curso, "⚠ Campos vazios!", False)
)        
        
        # Adicionando botão para retorno ao menu principal
        botao_voltar = create_button(tela_adicionar_curso, text='Voltar', command=self.mostrar_menu_principal)
        
    def abrir_tela_deletar_curso(self):
        ''' Tela que permite ao usuário excluir um curso'''
        # Limpando a tela principal
        self.limpar_tela()
        tela_excluir_curso = ctk.CTkFrame(self.root)
        tela_excluir_curso.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_excluir_curso
        create_label(parent=tela_excluir_curso, text='Informe o nome do curso para excluir')
        
        # Criando entrada para o nome do curso
        create_label(parent=tela_excluir_curso, text='Nome do curso')
        entry_nome_curso = create_entry(parent=tela_excluir_curso)

        botao_deletar_curso = create_button(
            parent=tela_excluir_curso,
            text='Enviar',
            command=lambda: (
                create_message(tela_excluir_curso, "✅ Sucesso!", True)
                if excluir_curso_nome(entry_nome_curso.get())
                else create_message(tela_excluir_curso, "❌ Erro!", False)
            ) if entry_nome_curso.get()
            else create_message(tela_excluir_curso, "⚠ Campo vazio!", False)
            )
        
        # Adicionando botão para retorno ao menu principal
        botao_voltar = create_button(tela_excluir_curso, text='Voltar', command=self.mostrar_menu_principal)
        
        
        
        
        
        
    
    
    
    
    
    
    
    