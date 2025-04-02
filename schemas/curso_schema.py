'''
Classe criada para definir o esquema dos dados que serão passados no arquivo JSON.
- id (int)
- titulo (str)
- aulas (int)
- horas (int)
'''

from typing import Optional
from pydantic import BaseModel as SCBaseModel, Field, root_validator

class CursoSchema(SCBaseModel):
    id: Optional[int] # ID será criado pelo próprio Banco de Dados
    titulo: str
    aulas: int
    horas: int
    
    class Config:
        orm_mode = True
        
class CursoPutSchema(CursoSchema):
    ''' Criando schema para PUT (atualização completa - todos os campos obrigatórios)'''
    pass # Herda todos os campos como obrigatórios

class CursoPatchSchema(SCBaseModel):
    ''' Criando schema para PATCH (atualização parcial - campos opcionais)'''
    titulo: Optional[str] = Field (
        default=None,  # Definindo valor padrão se o campo não for enviado
        min_length = 3, # Validação: mínimo 3 caracteres
        max_length=100, # Validação: máximo de 100 caracteres
        examples=["Novo Título"], # Adicionando exemplo para a documentação
        description='Novo título para o curso (3-100 caracteres)' # Descrição para documentação
    )
    
    aulas: Optional[int] = Field(
        None,
        ge=1, #Definindo que deve ser um número maior ou igual a 1
        le=200,
        examples=[20, 60], # Adicionando exemplo para a documentação
        description='Número de aulas (1-200)'
        
    )
    
    horas: Optional[int] = Field(
        None,
        ge=1,
        le=400,
        examples=[5,12],
        description='Número de horas (1-400)'
    )
    
    @root_validator
    def validar_campos(cls, values):
        if not any(values.values()):
            raise ValueError("Pelo menos um campo deve ser fornecido")
        return values