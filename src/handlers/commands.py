from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from src.database.requests import create_user, get_user
from src.utils.keyboards import kb_builders
from src.utils.logger import logger_func

router = Router()
logger = logger_func(__name__)


@router.message(CommandStart())
@router.callback_query(F.data == "main_menu")
async def start_command(message: Message | CallbackQuery):
    from_user = message.from_user

    user_id = from_user.id
    username = from_user.username
    first_name = from_user.first_name
    last_name = from_user.last_name
    full_name = f"{first_name} {last_name}" if last_name else first_name

    mention = from_user.mention_html(full_name)
    user = await get_user(user_id)

    template = dict(
        text = (
            f"Привет, {mention} 👋!"
        ),
        reply_markup=kb_builders.inline(
            ["🚀 GitHub", "👤 Профиль", "mini apps"],
            callback_data=[None, "profile", None],
            url=["https://github.com/dev-pegorino", None, None],
            web_app=[None, None, "https://dev-pegorino.github.io/index.html"],
            sizes=1
        )
    )
    
    if not user:
        await create_user(user_id, username)
    if isinstance(message, CallbackQuery):
        await message.message.edit_text(**template)
        return await message.answer()
    await message.answer(**template)