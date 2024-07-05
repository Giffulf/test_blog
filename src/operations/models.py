from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

publication = Table(
    "publication",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),  # Добавляем поле для заголовка публикации
    Column("content", String),  # Добавляем поле для содержания публикации
    Column("user_id", Integer),  # Добавляем поле для идентификатора пользователя, сделавшего публикацию
    Column("date", TIMESTAMP),
)

