from loguru import logger
import sys
from pathlib import Path

# Log File Path
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Loguru Configuration
logger.remove()  # Remove default logger

logger.add(
    sys.stdout,  # 콘솔 출력
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    level="INFO",
)

logger.add(
    LOG_DIR / "app.log",
    rotation="100 MB",  # 10MB 초과 시 새 파일 생성
    retention="7 days",  # 7일간 보관
    compression="zip",  # 압축 보관
    enqueue=True,
    level="INFO",
    encoding="utf-8",
)


def get_logger(name: str = None):
    """Get a logger instance with an optional name."""
    return logger.bind(name=name or "RoomeApp")
