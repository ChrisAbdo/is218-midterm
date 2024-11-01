import logging
import os
import logging.config

logging_conf_path = 'logging.conf'
if os.path.exists(logging_conf_path):
    logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
else:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Logging configured.")

logging.warning("this is a test")