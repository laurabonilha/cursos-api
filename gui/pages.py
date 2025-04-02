'''
Arquivo para organização de todas as telas da aplicação 
'''

import customtkinter as ctk
# Importando as funções de request da API
from services.crud import adicionar_curso, obter_cursos, excluir_curso, atualizar_curso, excluir_curso_nome, valida_curso, altera_curso_completo
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
        
        botao_alterar = create_button(parent=tela_menu, text='Alterar curso', command=self.abrir_tela_alterar_curso_consulta)
        
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
        
    def abrir_tela_alterar_curso_consulta(self):
        ''' Tela inicial de alteração de dados de um curso - verifica se o curso a ser alterado existe no banco'''
        
        # Inicializando variável de indicação de consulta de curso
        # Limpando a tela principal
        self.limpar_tela()
        tela_alterar_curso_consulta = ctk.CTkFrame(self.root)
        tela_alterar_curso_consulta.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_alterar_curso_consulta
        create_label(parent=tela_alterar_curso_consulta, text='Informe o nome do curso para alterar')
        
        # Criando entrada para o nome do curso
        create_label(parent=tela_alterar_curso_consulta, text='Nome do curso')
        entry_nome_curso = create_entry(parent=tela_alterar_curso_consulta)
        
        def verificar_curso():
            nome_curso = entry_nome_curso.get()
            if not nome_curso:
                create_message(tela_alterar_curso_consulta, "⚠ Campo vazio!", False)
            elif valida_curso(nome_curso):
                create_message(tela_alterar_curso_consulta, "✅ Curso encontrado!", True)
                self.abrir_tela_alterar_curso_main(curso_consultado=nome_curso)
            else:
                create_message(tela_alterar_curso_consulta, "❌ Curso não encontrado!", False)
        
        botao_verifica_curso = create_button(
            parent=tela_alterar_curso_consulta,
            text='Enviar',
            command= verificar_curso
        )
        
        # Adicionando botão para retorno ao menu principal
        botao_voltar = create_button(tela_alterar_curso_consulta, text='Voltar', command=self.mostrar_menu_principal)
           
    def abrir_tela_alterar_curso_main(self, curso_consultado):
        '''Função para abrir a tela que de fato irá alterar os dados de um curso'''
        self.limpar_tela()
        tela_alterar_curso_main = ctk.CTkFrame(self.root)
        tela_alterar_curso_main.pack(fill='both', expand=True, padx=20, pady=20)
        self.frame_atual = tela_alterar_curso_main
        
        create_label(parent=tela_alterar_curso_main, text='Informe os dados que deseja alterar')
        
        # Criando entrada para o nome do curso
        create_label(parent=tela_alterar_curso_main, text='Novo nome do curso')
        entry_nome_curso = create_entry(parent=tela_alterar_curso_main)
        
        # Criando entrada para as aulas do curso
        create_label(parent=tela_alterar_curso_main, text='Novo número de aulas')
        entry_aulas_curso = create_entry(parent=tela_alterar_curso_main)
        
        # Criando entrada para as horas do curso
        create_label(parent=tela_alterar_curso_main, text='Novo número de horas')
        entry_horas_curso = create_entry(parent=tela_alterar_curso_main)

        def enviar_alteracao():
            # Obter valores SOMENTE quando o botão for pressionado
            novo_nome = entry_nome_curso.get()
            novo_horas = entry_horas_curso.get()
            novo_aulas = entry_aulas_curso.get()
            
            # Validar campos
            if not all([novo_nome, novo_horas, novo_aulas]):
                create_message(tela_alterar_curso_main, "⚠ Campos vazios!", False)
                return
            
            # Validar valores numéricos
            try:
                novo_horas = int(novo_horas)
                novo_aulas = int(novo_aulas)
            except ValueError:
                create_message(tela_alterar_curso_main, "⚠ Horas/Aulas devem ser números!", False)
                return
            
            # Chamar função de alteração
            if altera_curso_completo(curso_consultado, novo_nome, novo_horas, novo_aulas):
                create_message(tela_alterar_curso_main, "✅ Curso alterado com sucesso!", True)
            else:
                create_message(tela_alterar_curso_main, "❌ Falha ao alterar curso!", False)

        botao_enviar_curso = create_button(
            parent=tela_alterar_curso_main,
            text='Enviar',
            command=enviar_alteracao
        )
        
        # Botão de voltar
        botao_voltar = create_button(tela_alterar_curso_main, text='Voltar', command=self.mostrar_menu_principal)
            
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    