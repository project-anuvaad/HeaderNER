import logging
import os

DEBUG = True
API_URL_PREFIX = "/api/v0"
HOST = 'localhost'
PORT = 5001

# FILE_STORAGE_PATH =  '/home/naresh/Food_Recognition_API/src/sample_images/chicke_curry.jpeg'#'/home/naresh/Tarento/Food_Recognition/Food_Recognition_API/src/sample_images/pancake.jpg' #'/home/dddhiraj/Documents/Tarento/Anuwad/Tabular_data_extraction/sample_images'# '/Users/kd/Workspace/python/github/data/input/' #
# MODEL_STFILE_STORAGE_PATHORAGE_PATH =  '/home/naresh/model4b.10-0.68.hdf5'
# IMAGE_BASE_PATH = '/opt/nginx/'
ENABLE_CORS = False


logging.basicConfig(
    filename=os.getenv("SERVICE_LOG", "server.log"),
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
