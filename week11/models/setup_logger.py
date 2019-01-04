import logging

def create_log(file_name):
    logging.basicConfig(filename=file_name, format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', level=logging.DEBUG)
    logger = logging.getLogger('spam')