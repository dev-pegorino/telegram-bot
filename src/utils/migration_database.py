import argparse

from src.utils.command_runner import run_command
from src.utils.logger import logger_func

logger = logger_func(__name__)


def main():
    parser = argparse.ArgumentParser(description='Database migration tool')
    subparsers = parser.add_subparsers(dest='command', required=True)
    migrate_parser = subparsers.add_parser('name', help='Run database migrations')
    migrate_parser.add_argument('name', help='Name of the migration')
    
    args = parser.parse_args()
    
    if args.command == 'name':
        logger.info(f"Starting database migration process: {args.name}")
        logger.info("Creating database migration...")
        success, output = run_command(f'alembic revision --autogenerate -m "{args.name}"')
        if not success:
            return logger.error("Migration creation failed")
        
        logger.info("Migration created successfully")
        logger.info("Applying database migration...")
        success, output = run_command('alembic upgrade head')
        if not success:
            return logger.error("Migration application failed")
        
        logger.info("Migration applied successfully")


if __name__ == "__main__":
    main()