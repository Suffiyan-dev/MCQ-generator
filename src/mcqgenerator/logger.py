import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")#getcwd() returns the current working directory
os.makedirs(log_path, exist_ok=True)  # Create logs directory if it doesn't exist

LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,
        filename=LOG_FILEPATH,
        format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'

)
#logging.INFO means that it will log all messages with level INFO and above

