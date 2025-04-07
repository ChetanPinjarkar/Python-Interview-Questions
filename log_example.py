from loguru import logger
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

logger.remove()
logger.add(f"{log_dir}/my_log_file.log", rotation="5 MB")

logger.success("Success")
logger.info("writing info log")
logger.error("writing error")
