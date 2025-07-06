from sqlalchemy import select

from src.database import async_session
from src.database.modules import User


async def get_user(tg_id: int) -> User:
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))


async def create_user(tg_id: int, username: str | None = None) -> None:
    async with async_session() as session:
        session.add(User(tg_id=tg_id, username=username))
        await session.commit()