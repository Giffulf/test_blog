from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import get_async_session
from models import publication  # Изменили импорт модели на publication
from schemas import PublicationCreate  # Изменили импорт схемы на PublicationCreate

router = APIRouter(
    prefix="/publications",  # Изменили префикс на /publications
    tags=["Publication"]  # Изменили тег на Publication
)


@router.get("/")
async def get_specific_publications(publication_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(publication).where(publication.c.type == publication_type)  # Изменили на publication и type
    result = await session.execute(query)
    return result.all()


@router.post("/")
async def add_specific_publications(new_publication: PublicationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(publication).values(**new_publication.dict())  # Изменили на publication
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}  # Возвращаем статус "success"
