from datetime import datetime

from pydantic import BaseModel

class PublicationCreate(BaseModel):
    id: int
    title: str
    content: str
    publication_date: datetime
    author: str
