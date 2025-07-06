from typing import List, Union

from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder


def inline(
    text: Union[str, List[str]],
    callback_data: Union[str, List[str], None] = None,
    sizes: Union[int, List[int]] = 2,
    url: Union[str, List[str], None] = None,
    web_app: Union[str, List[str], None] = None,
    **kwargs
) -> InlineKeyboardMarkup:
    """Creates an Inline keyboard for Telegram bot.

    Args:
        text (Union[str, List[str]]): Button text. Can be a string for a single button
            or a list of strings for multiple buttons.
        callback_data (Union[str, List[str]], optional): Callback data for buttons.
            Must match the number of text elements. Defaults to None.
        sizes (Union[int, List[int]], optional): Number of buttons per row. Can be a number
            for uniform row sizes or a list of numbers for different sizes.
            Defaults to 2.
        url (Union[str, List[str]], optional): URL links for buttons. Defaults to None.
        web_app (Union[str, List[str]], optional): Mini App links for buttons.
            Defaults to None.
        **kwargs: Additional parameters for InlineKeyboardMarkup constructor.

    Returns:
        InlineKeyboardMarkup: Ready-to-use inline keyboard.

    Examples:
        # Simple keyboard with callback_data
        kb = inline(["Yes", "No"], callback_data=["yes", "no"])

        # Keyboard with URL buttons
        kb = inline(
            ["Наш сайт", "Telegram"],
            url=["https://example.com", "https://t.me/channel"],
            sizes=1
        )

        # Keyboard with different number of buttons per row
        kb = inline(
            ["1", "2", "3", "4", "5"],
            callback_data=["1", "2", "3", "4", "5"],
            sizes=[2, 1, 2]
        )

    ----

    Создает встроенную Inline клавиатуру для Telegram бота.

    Args:
        text (Union[str, List[str]]): Текст кнопок. Может быть строкой для одной кнопки
            или списком строк для нескольких кнопок.
        callback_data (Union[str, List[str]], optional): Данные обратного вызова для кнопок.
            Должны соответствовать количеству текстовых элементов. По умолчанию None.
        sizes (Union[int, List[int]], optional): Количество кнопок в ряду. Может быть числом
            для одинакового размера всех рядов или списком чисел для разных размеров.
            По умолчанию 2.
        url (Union[str, List[str]], optional): URL-ссылки для кнопок. По умолчанию None.
        web_app (Union[str, List[str]], optional): Ссылки на mini-приложения для кнопок.
            По умолчанию None.
        **kwargs: Дополнительные параметры для конструктора InlineKeyboardMarkup.

    Returns:
        InlineKeyboardMarkup: Готовая встроенная клавиатура.

    Examples:
        # Простая клавиатура с callback_data
        kb = inline(["Да", "Нет"], callback_data=["yes", "no"])

        # Клавиатура с URL-кнопками
        kb = inline(
            ["Наш сайт", "Telegram"],
            url=["https://example.com", "https://t.me/channel"],
            sizes=1
        )

        # Клавиатура с разным количеством кнопок в рядах
        kb = inline(
            ["1", "2", "3", "4", "5"],
            callback_data=["1", "2", "3", "4", "5"],
            sizes=[2, 1, 2]
        )
    """
    builder = InlineKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(callback_data, str):
        callback_data = [callback_data]
    if isinstance(sizes, int):
        sizes = [sizes]
    if isinstance(url, str):
        url = [url]
    if isinstance(web_app, str):
        web_app = [web_app]

    for i, txt in enumerate(text):
        if callback_data and i < len(callback_data) and callback_data[i]:
            builder.button(text=txt, callback_data=callback_data[i])
        elif url and i < len(url) and url[i]:
            builder.button(text=txt, url=url[i])
        elif web_app and i < len(web_app) and web_app[i]:
            builder.button(text=txt, web_app=WebAppInfo(url=web_app[i]))
        else:
            raise ValueError(f"No action specified for button '{txt}' at index {i}")
    return builder.adjust(*sizes).as_markup(**kwargs)