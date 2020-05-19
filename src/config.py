import logging
import os

DEBUG = True
API_URL_PREFIX = "/api/v0"
HOST = 'localhost'
PORT = 5001

mix_model_dir = '/opt/share/python/upload/models/exp_3_mix/'
model_dir_order = '/opt/share/python/upload/models/exp_3_order/'
model_dir_judgment = '/opt/share/python/upload/models/exp_3_judgment/'

ENABLE_CORS = False


logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
