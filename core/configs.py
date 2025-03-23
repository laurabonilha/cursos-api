from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    '''
    Configurações gerais usadas na aplicação
    '''
    API_V1_STR: str = '/api/v1' #URL base da API
    DB_URL: str = 'postgresql+asyncpg://postgres:admin@localhost:5432/faculdade' #Alterar usuário e senha conforme o estabelecido no Postgre
    DBBaseModel = declarative_base() #Variável para que os módulos herdem todos os recursos do SQL Alchemy
    
    class Config:
        case_sensitive = True 
        
settings = Settings() #Instanciando objeto da classe Settings para acesso posterior