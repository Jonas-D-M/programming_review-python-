import logging
from logging import FileHandler
from logging import Formatter


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

#Hotelgast_properties_logger
Hotelgast_properties_log_file = 'hotel\\logs\\Hotelgast_properties_logfile.txt'

Hotelgast_properties_logger = logging.getLogger('Hotelgast.properties')
Hotelgast_properties_logger.setLevel(LOG_LEVEL)
Hotelgast_properties_logger_file_handler = FileHandler(Hotelgast_properties_log_file)
Hotelgast_properties_logger_file_handler.setLevel(LOG_LEVEL)
Hotelgast_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
Hotelgast_properties_logger.addHandler(Hotelgast_properties_logger_file_handler)