'''
Arquivo destinado a armazenar as funções que devem ser feitas comunicando a interface com a API
'''

import requests

# URL da API onde os cursos estão sendo gerenciados
API_URL = "http://localhost:8000/api/v1/cursos"

# Função para adicionar um curso
def adicionar_curso(titulo: str, aulas: int, horas: int):
    # Capturando os dados informados pelo usuário na interface
    dados = {"titulo": titulo, "aulas": aulas, "horas": horas}
    resposta = requests.post(API_URL, json=dados)
    
    # Alterando retorno da função para um boolean (será usado para a interface gráfica)
    return resposta.status_code == 201

# Função para obter todos os cursos      
def obter_cursos():
    resposta = requests.get(API_URL)
    if resposta.status_code == 200:
        return resposta.json()  # Retorna a lista de cursos em um dicionário
    else:
        print('Erro ao obter cursos')
        return []

# Função para atualizar um curso
def atualizar_curso(id_curso: int, nome: str, aulas: int, horas: int):
    dados = {"titulo": nome, "aulas": aulas, "horas": horas}
    resposta = requests.put(f"{API_URL}/{id_curso}", json=dados)
    
    if resposta.status_code == 200:
        print('Curso atualizado com sucesso')
    else:
        print('Erro ao atualizar curso')
        
# Função para excluir um curso
def excluir_curso(id_curso: int):
    resposta = requests.delete(f"{API_URL}/{id_curso}")
    
    if resposta.status_code == 204:
        print('Curso excluído com sucesso')
    else:
        print('Erro ao excluir curso')