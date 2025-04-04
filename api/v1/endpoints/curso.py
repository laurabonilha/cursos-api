from typing import List
from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema, CursoPatchSchema
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
    
# GET curso - ID
@router.get('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id) #Filtrando pelo ID recebido
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        
        if curso: return curso
        else: raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)

# GET curso - nome
@router.get('/nome/{nome_curso}', response_model=CursoSchema, status_code=status.HTTP_200_OK)
async def get_curso_nome(nome_curso: str, db: AsyncSession = Depends(get_session)):    
    async with db as session:
        nome_curso = nome_curso.strip()
        query = select(CursoModel).filter(func.lower(CursoModel.titulo) == func.lower(nome_curso))
        result = await session.execute(query)
        curso = result.scalar_one_or_none()

        if not curso:
            raise HTTPException(status_code=404, detail="Curso não encontrado")
        
        return curso
  
# PUT curso - informando ID
@router.put('/{curso_id}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    ''' Função para alteração completa de um curso - todos os campos (titulo, horas e aulas)'''
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id) #Filtrando pelo ID recebido
        result = await session.execute(query)
        curso_up = result.scalar_one_or_none()
        
        # Se encontrado o curso, atualiza os dados conforme os novos dados informados
        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas
            
            await session.commit()
             
            return curso_up
        
        else: 
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        
# PUT curso - informando nome
@router.put('/nome/{nome_curso}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_curso_nome(nome_curso: str, curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    ''' Função para alteração completa de um curso - todos os campos (titulo, horas e aulas)'''
    async with db as session:
        query = select(CursoModel).filter(func.lower(CursoModel.titulo) == func.lower(nome_curso)) #Filtrando pelo nome recebido
        result = await session.execute(query)
        curso_up = result.scalar_one_or_none()
        
        # Se encontrado o curso, atualiza os dados conforme os novos dados informados
        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas
            
            await session.commit()
             
            return curso_up
        
        else: 
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)

# PATCH curso - por nome
@router.patch('/nome/{nome_curso}', response_model=CursoSchema, responses={
    200: {"description": "Curso atualizado parcialmente"},
    404: {"description": "Curso não encontrado"},
    422: {"description": "Dados inválidos"}
})
async def patch_curso_parcial(nome_curso: str, curso_update: CursoPatchSchema, db: AsyncSession = Depends(get_session)):
    ''' Patch para alteração parcial de um curso - 1 ou mais dados a serem alterados'''
    async with db as session:
        # Busca case-insensitive
        query = select(CursoModel).filter(func.lower(CursoModel.titulo) == func.lower(nome_curso))
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        
        if not curso:
            raise HTTPException(detail=f'Curso {nome_curso} não encontrado!', status_code=status.HTTP_404_NOT_FOUND)
        
        # Atualiza apenas os campos fornecidos
        update_data = curso_update.model_dump(excluse_unset=True)
        for field, value in update_data.items():
            setattr(curso, field, value)

# DELETE curso - informando ID
@router.delete('/{curso_id}',  status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id) #Filtrando pelo ID recebido
        result = await session.execute(query)
        curso_del = result.scalar_one_or_none()
        
        # Se encontrado o curso, deleta
        if curso_del:
            
            await session.delete(curso_del)
            await session.commit()
             
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else: 
            raise HTTPException(detail='Curso não encontrado', status_code=status.HTTP_404_NOT_FOUND)
        
# DELETE curso - informando nome
@router.delete('/nome/{nome_curso}', status_code=status.HTTP_404_NOT_FOUND)
async def delete_curso_por_nome(nome_curso: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.titulo == nome_curso) # Realizando select no db pelo nome do curso
        result = await session.execute(query)
        curso_del_nome = result.scalar_one_or_none()
        
        # Se encontrar o curso, deleta
        if curso_del_nome:
            await session.delete(curso_del_nome)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Curso com este nome não foi encontrado', status_code=status.HTTP_404_NOT_FOUND)

    
        