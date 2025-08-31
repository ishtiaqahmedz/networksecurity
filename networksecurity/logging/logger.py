import logging
import os
from datetime import datetime
import sys


#LOG_FILE=f"{datetime.now().strftime('%y%m%d-%H%M%S')}.log"  



LOG_FOLDER= os.path.join(os.getcwd(),"logs")
                         
os.makedirs(LOG_FOLDER,exist_ok=True)


LOG_FILE_PATH=os.path.join(LOG_FOLDER,"logging.log") #"logs" will create folder called log


logging_str="[%(asctime)s: %(levelname)s :%(module)s:%(message)s]"


logging.basicConfig(
#filename=LOG_FILE_PATH,
format= logging_str,
level=logging.INFO,
handlers=[
    logging.FileHandler(LOG_FILE_PATH),
    logging.StreamHandler(sys.stdout)]


)

logger=logging.getLogger("networksecurity")

"""
Use filename if you only want to log to a file.
Use handlers if you want multiple outputs (e.g., file + console).
"""