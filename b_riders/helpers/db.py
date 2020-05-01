import logging

from tenacity import retry, stop_after_attempt, wait_fixed, before_log, after_log

from b_riders.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def check_db_availability() -> bool:
    logger.info("Initializing service")
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute("SELECT 1")
        return True
    except Exception as e:
        logger.error(e)
        return False


