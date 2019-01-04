import logging
from logging import FileHandler
from logging import Formatter


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

#bier_properties_logger
bier_properties_log_file = 'week11\\bier_properties_logfile.txt'

bier_properties_logger = logging.getLogger('bier.properties')
bier_properties_logger.setLevel(LOG_LEVEL)
bier_properties_logger_file_handler = FileHandler(bier_properties_log_file)
bier_properties_logger_file_handler.setLevel(LOG_LEVEL)
bier_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
bier_properties_logger.addHandler(bier_properties_logger_file_handler)


#Bier file reader logger
bier_file_reader_log_file = 'week11\\bier_file_reader_logfile.txt'

bier_file_reader_logger = logging.getLogger('bier.file_reader')
bier_file_reader_logger.setLevel(LOG_LEVEL)
bier_file_reader_logger_file_handler = FileHandler(bier_properties_log_file)
bier_file_reader_logger_file_handler.setLevel(LOG_LEVEL)
bier_file_reader_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
bier_file_reader_logger.addHandler(bier_file_reader_logger_file_handler)