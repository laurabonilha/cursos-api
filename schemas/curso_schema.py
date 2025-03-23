'''
Classe criada para definir o esquema dos dados que serão passados no arquivo JSON.
- id (int)
- titulo (str)
- aulas (int)
- horas (int)
'''

from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    id: Optional[int] # ID será criado pelo próprio Banco de Dados
    titulo: str
    aulas: int
    horas: int
    
    class Config:
        orm_mode = True
        