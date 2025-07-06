from aiogram import Router

from . import common


def setup_callbacks_router() -> Router:
    router = Router()

    router.include_router(common.router)
    
    return router