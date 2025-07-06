from aiogram import Bot
from aiogram.types import BotCommand

from src.config import settings
from src.utils.logger import logger_func

logger = logger_func(__name__)


async def setup_list_commands(bot: Bot) -> None:
    logger.info('Setup list commands...')
    commands = []
    for command in settings.COMMANDS:
        commands.append(BotCommand(command=command[0], description=command[1]))
    try:
        await bot.set_my_commands(commands=commands)
        logger.info('Installation of the list of teams successfully')
    except Exception as e:
        logger.error(f'Error when installing commands: {e}')


async def setup_description(bot: Bot) -> None:
    logger.info('Installation of a description in the section "What can this bot can do?"...')
    try:
        await bot.set_my_description(description=settings.DESCRIPTION)
        logger.info(
            'Installation of a description in the section "What can this bot can do?" successfully'
        )
    except Exception as e:
        logger.error(f'Error when installing the description: {e}')


async def setup_short_description(bot: Bot) -> None:
    logger.info('Installation Description in the section "About the bot" ...')
    try:
        await bot.set_my_short_description(short_description=settings.SHORT_DESCRIPTION)
        logger.info('Installation Description in the "About the Bot" section successfully')
    except Exception as e:
        logger.error(f'An error when installing a short description: {e}')