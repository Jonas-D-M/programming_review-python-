import logging
from logging import FileHandler
from logging import Formatter


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

#hotelgast_properties_logger
hotelgast_properties_log_file = 'hotel\\logs\\hotelgast_properties_logfile.txt'

hotelgast_properties_logger = logging.getLogger('hotelgast.properties')
hotelgast_properties_logger.setLevel(LOG_LEVEL)
hotelgast_properties_logger_file_handler = FileHandler(hotelgast_properties_log_file)
hotelgast_properties_logger_file_handler.setLevel(LOG_LEVEL)
hotelgast_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
hotelgast_properties_logger.addHandler(hotelgast_properties_logger_file_handler)