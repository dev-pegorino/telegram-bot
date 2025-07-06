# Base Telegram Bot in aiogram 3.x

A base Telegram bot built with aiogram 3.x, featuring SQLAlchemy, Alembic, and support for SQLite/MySQL databases. This project provides a ready-to-use template for quickly starting Telegram bot development with modern tools.

[🇷🇺 Русская версия](README.ru.md)

## Project Description

This project is a ready-made template for creating Telegram bots using:
- **aiogram 3.x** - modern library for working with Telegram Bot API
- **SQLAlchemy 2.x** - ORM for database operations
- **Alembic** - migration system for database schema management
- **Pydantic Settings** - configuration management
- **Ruff** - fast Python linter and formatter
- **UV** - modern Python package manager

## Project Structure

```
telegram-bot/
├── src/                          # Main application code
│   ├── database/                 # Database operations
│   │   ├── __init__.py           # Database module initialization
│   │   ├── base.py               # Database base settings
│   │   ├── models.py             # Data models
│   │   ├── bot.db                # SQLite database (if used)
│   │   ├── modules/              # Database models
│   │   │   ├── __init__.py       # Models module initialization
│   │   │   └── user.py           # User model
│   │   └── requests/             # Database queries
│   │       ├── __init__.py       # Requests module initialization
│   │       └── user.py           # User queries
│   ├── handlers/                 # Message handlers
│   │   ├── __init__.py           # Handlers module initialization
│   │   └── commands.py           # Command handlers
│   ├── callbacks/                # Callback query handlers
│   │   ├── __init__.py           # Callbacks module initialization
│   │   └── common.py             # Common callback handlers
│   ├── utils/                    # Utilities
│   │   ├── keyboards/            # Keyboards
│   │   │   ├── __init__.py       # Keyboards module initialization
│   │   │   └── builders.py       # Keyboard builders
│   │   ├── logger.py             # Logging configuration
│   │   ├── migration_database.py # Migration utility
│   │   ├── command_runner.py     # Command execution utility
│   │   └── settings_bot.py       # Bot settings
│   ├── config.py                 # Application configuration
│   ├── init_bot.py               # Bot initialization
│   ├── run.py                    # Application entry point
│   └── .example.env              # Environment variables example
├── alembic/                      # Migration configuration
│   ├── versions/                 # Migration files
│   ├── env.py                    # Alembic environment settings
│   └── script.py.mako            # Migration template
├── logs/                         # Application logs
├── pyproject.toml                # Project configuration and dependencies
├── uv.lock                       # Dependency lock file
├── alembic.ini                   # Alembic configuration
├── ruff.toml                     # Ruff linter configuration
├── .python-version               # Python version
└── .gitignore                    # Git exclusions
```

### Key Files Description

- **`src/run.py`** - Main file for running the bot
- **`src/config.py`** - Application settings and environment variables loading
- **`src/init_bot.py`** - Bot and dispatcher initialization
- **`src/database/`** - All database-related files
- **`src/utils/migration_database.py`** - Utility for creating and applying migrations
- **`pyproject.toml`** - Project configuration, dependencies, and scripts
- **`alembic.ini`** - Migration system settings

## Installation and Setup

### 1. Install UV

#### Windows
```powershell
# Via PowerShell
irm https://astral.sh/uv/install.ps1 | iex

# Or via pip
pip install uv
```

#### Unix systems (Linux/macOS)
```bash
# Via curl
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

### 2. Clone and setup project

```bash
git clone <repository-url>
cd telegram-bot
```

### 3. Configure environment variables

Copy the environment variables example file:
```bash
cp src/.example.env src/.env
```

Edit `src/.env` and add:
```env
TOKEN_BOT=your_telegram_bot_token_here
DB_URL=sqlite+aiosqlite:///src/database/bot.db
```

**DB_URL options:**
- SQLite: `sqlite+aiosqlite:///src/database/bot.db`
- MySQL: `mysql+aiomysql://username:password@localhost:3306/database_name`

### 4. Run the bot

```bash
uv run start
```

This command will automatically:
- Create a virtual environment
- Install all dependencies
- Start the bot

## Database Migrations

### 1. Configure Alembic

First, copy the example Alembic configuration:
```bash
cp example.alembic.ini alembic.ini
```

Edit `alembic.ini` and update the database URL to match your `.env` file:
```ini
sqlalchemy.url = your_database_url_here
```

### 2. Create and apply migration

```bash
uv run migrate name "migration_description"
```

This command will:
1. Create a new migration with the specified description
2. Automatically apply it to the database

### Usage examples

```bash
# Create migration for adding new table
uv run migrate name "add_users_table"

# Create migration for structure changes
uv run migrate name "update_user_fields"
```

## Development

### Code formatting

The project uses Ruff for linting and formatting:

```bash
# Check code
uv run ruff check

# Fix code issues
uv run ruff --fix
```

### Structure for adding new functionality

1. **Message handlers** - add to `src/handlers/`
2. **Callback handlers** - add to `src/callbacks/`
3. **Data models** - add to `src/database/models.py`
4. **Keyboards** - add to `src/utils/keyboards/`

## Requirements

- Python 3.13+
- UV (package manager)
- Telegram Bot Token
- Database (SQLite or MySQL)

## License

MIT License
