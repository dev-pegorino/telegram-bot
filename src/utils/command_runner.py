import subprocess
from typing import Tuple

from src.utils.logger import logger_func

logger = logger_func(__name__)


def run_command(command: str) -> Tuple[bool, str]:
    logger.info(f"Executing command: {command}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.strip()
        if output:
            logger.debug(f"Command output:\n{output}")
        return True, output
    except subprocess.CalledProcessError as e:
        error_msg = (
            f"Command failed with code {e.returncode}\n"
            f"Output: {e.stdout}\nError: {e.stderr}"
        )
        logger.error(error_msg)
        return False, error_msg
    except Exception as e:
        error_msg = f"Error executing command: {str(e)}"
        logger.error(error_msg)
        return False, error_msg