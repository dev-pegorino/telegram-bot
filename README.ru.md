# Base Telegram Bot in aiogram 3.x

Базовый Telegram бот, построенный на aiogram 3.x с поддержкой SQLAlchemy, Alembic и возможностью работы с SQLite/MySQL базами данных. Проект включает в себя готовую структуру для быстрого старта разработки Telegram ботов с современными инструментами.

[🇺🇸 English version](README.md)

## Описание проекта

Этот проект представляет собой готовый шаблон для создания Telegram ботов с использованием:
- **aiogram 3.x** - современная библиотека для работы с Telegram Bot API
- **SQLAlchemy 2.x** - ORM для работы с базами данных
- **Alembic** - система миграций для управления схемой базы данных
- **Pydantic Settings** - управление конфигурацией
- **Ruff** - быстрый линтер и форматтер кода
- **UV** - современный менеджер пакетов Python

## Структура проекта

```
telegram-bot/
├── src/                          # Основной код приложения
│   ├── database/                 # Работа с базой данных
│   │   ├── __init__.py           # Инициализация модуля БД
│   │   ├── base.py               # Базовые настройки БД
│   │   ├── models.py             # Модели данных
│   │   ├── bot.db                # SQLite база данных (если используется)
│   │   ├── modules/              # Модели базы данных
│   │   │   ├── __init__.py       # Инициализация модуля моделей
│   │   │   └── user.py           # Модель пользователя
│   │   └── requests/             # Запросы к базе данных
│   │       ├── __init__.py       # Инициализация модуля запросов
│   │       └── user.py           # Запросы пользователей
│   ├── handlers/                 # Обработчики сообщений
│   │   ├── __init__.py           # Инициализация модуля обработчиков
│   │   └── commands.py           # Обработчики команд
│   ├── callbacks/                # Обработчики callback-запросов
│   │   ├── __init__.py           # Инициализация модуля callback
│   │   └── common.py             # Общие обработчики callback
│   ├── utils/                    # Утилиты
│   │   ├── keyboards/            # Клавиатуры
│   │   │   ├── __init__.py       # Инициализация модуля клавиатур
│   │   │   └── builders.py       # Построители клавиатур
│   │   ├── logger.py             # Настройка логирования
│   │   ├── migration_database.py # Утилита для миграций
│   │   ├── command_runner.py     # Утилита выполнения команд
│   │   └── settings_bot.py       # Настройки бота
│   ├── config.py                 # Конфигурация приложения
│   ├── init_bot.py               # Инициализация бота
│   ├── run.py                    # Точка входа приложения
│   └── .example.env              # Пример файла с переменными окружения
├── alembic/                      # Конфигурация миграций
│   ├── versions/                 # Файлы миграций
│   ├── env.py                    # Настройки окружения Alembic
│   └── script.py.mako            # Шаблон для миграций
├── logs/                         # Логи приложения
├── pyproject.toml                # Конфигурация проекта и зависимости
├── uv.lock                       # Файл блокировки зависимостей
├── alembic.ini                   # Конфигурация Alembic
├── ruff.toml                     # Конфигурация линтера Ruff
├── .python-version               # Версия Python
└── .gitignore                    # Исключения для Git
```

### Описание ключевых файлов

- **`src/run.py`** - Главный файл для запуска бота
- **`src/config.py`** - Настройки приложения и загрузка переменных окружения
- **`src/init_bot.py`** - Инициализация бота и диспетчера
- **`src/database/`** - Все файлы, связанные с базой данных
- **`src/utils/migration_database.py`** - Утилита для создания и применения миграций
- **`pyproject.toml`** - Конфигурация проекта, зависимости и скрипты
- **`alembic.ini`** - Настройки системы миграций

## Установка и запуск

### 1. Установка UV

#### Windows
```powershell
# Через PowerShell
irm https://astral.sh/uv/install.ps1 | iex

# Или через pip
pip install uv
```

#### Unix системы (Linux/macOS)
```bash
# Через curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Или через pip
pip install uv
```

### 2. Клонирование и настройка проекта

```bash
cd telegram-bot
```

### 3. Настройка переменных окружения

Скопируйте файл с примером переменных окружения:
```bash
cp src/.example.env src/.env
```

Отредактируйте `src/.env` и добавьте:
```env
TOKEN_BOT=your_telegram_bot_token_here
DB_URL=sqlite+aiosqlite:///src/database/bot.db
```

**Варианты DB_URL:**
- SQLite: `sqlite+aiosqlite:///src/database/bot.db`
- MySQL: `mysql+aiomysql://username:password@localhost:3306/database_name`

### 4. Запуск бота

```bash
uv run start
```

Эта команда автоматически:
- Создаст виртуальное окружение
- Установит все зависимости
- Запустит бота

## Миграции базы данных

### 1. Настройка Alembic

Сначала скопируйте пример конфигурации Alembic:
```bash
cp example.alembic.ini alembic.ini
```

Отредактируйте `alembic.ini` и обновите URL базы данных в соответствии с вашим файлом `.env`:
```ini
sqlalchemy.url = your_database_url_here
```

### 2. Создание и применение миграции

```bash
uv run migrate name "описание_миграции"
```

Эта команда:
1. Создаст новую миграцию с указанным описанием
2. Автоматически применит её к базе данных

### Примеры использования

```bash
# Создание миграции для добавления новой таблицы
uv run migrate name "add_users_table"

# Создание миграции для изменения структуры
uv run migrate name "update_user_fields"
```

## Разработка

### Форматирование кода

Проект использует Ruff для линтинга и форматирования:

```bash
# Проверка кода
uv run ruff check

# Исправление проблем в коде
uv run ruff --fix
```

### Структура для добавления нового функционала

1. **Обработчики сообщений** - добавляйте в `src/handlers/`
2. **Callback обработчики** - добавляйте в `src/callbacks/`
3. **Модели данных** - добавляйте в `src/database/models.py`
4. **Клавиатуры** - добавляйте в `src/utils/keyboards/`

## Требования

- Python 3.13+
- UV (менеджер пакетов)
- Telegram Bot Token
- База данных (SQLite или MySQL)

## Лицензия

MIT License
