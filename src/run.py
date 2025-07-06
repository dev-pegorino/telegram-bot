import asyncio

from src.database import close_db, init_db
from src.init_bot import bot, dp, setup_bot
from src.utils.logger import logger_func

logger = logger_func(__name__)


async def main() -> None:
	await init_db()
	await setup_bot()
	
	try:
		await dp.start_polling(bot)
	except asyncio.CancelledError:
		logger.info("Бот остановлен")
	finally:
		await bot.session.close()
		await close_db()


def start() -> None:
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		logger.info("Бот остановлен")
	except Exception as e:
		logger.error(f"Ошибка при запуске бота: {e}")


if __name__ == "__main__":
	start()