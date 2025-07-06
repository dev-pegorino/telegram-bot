from aiogram import Router

from . import commands


def setup_handlers_router() -> Router:
    router = Router()

    router.include_router(commands.router)

    return router