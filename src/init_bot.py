from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.callbacks import setup_callbacks_router
from src.config import settings
from src.handlers import setup_handlers_router
from src.utils.settings_bot import setup_description, setup_list_commands, setup_short_description

bot = Bot(
    token=settings.TOKEN_BOT.get_secret_value(),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()

handlers_router = setup_handlers_router()
callbacks_router = setup_callbacks_router()

dp.include_router(handlers_router)
dp.include_router(callbacks_router)


async def setup_bot():
    await setup_list_commands(bot)
    await setup_description(bot)
    await setup_short_description(bot)