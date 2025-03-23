from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import get_session

router = APIRouter()


'''
Path ('/') -> Utilizando a raiz
status_code -> status esperado de retorno em caso de sucesso (201 - CREATED)
response_model -> modelo de resposta esperada no retorno (curso_schema)
'''
# POST curso
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    
    db.add(novo_curso)
    await db.commit()
    
    return novo_curso

# GET cursos
@router.get('/', response_model=List[CursoSchema]) #Define que o retorno será uma lista conforme schema JSON para cursos
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session: # O async with assegura que a sessão será fechada corretamente após a execução
        query = select(CursoModel) # Criando uma consulta que seleciona todos os cursos da tabela CursoModel, conforme modelo do SQLAlquemy
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all() # Extrai os valores dos resultados da consulta (os cursos) e all() converte o resultado em uma lista
        return cursos # A função retorna a lista de cursos, que será automaticamente convertida para o formato definido pelo CursoSchema devido ao parâmetro response_model=List[CursoSchema]