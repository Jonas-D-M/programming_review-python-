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

#hotelkamer properties logger
hotelkamer_properties_log_file = 'hotel\\logs\\hotelkamer_properties_logfile.txt'

hotelkamer_properties_logger = logging.getLogger('hotelkamer.properties')
hotelkamer_properties_logger.setLevel(LOG_LEVEL)
hotelkamer_properties_logger_file_handler = FileHandler(hotelkamer_properties_log_file)
hotelkamer_properties_logger_file_handler.setLevel(LOG_LEVEL)
hotelkamer_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
hotelkamer_properties_logger.addHandler(hotelkamer_properties_logger_file_handler)

#hotel properties logger
hotel_properties_log_file = 'hotel\\logs\\hotel_properties_logfile.txt'

hotel_properties_logger = logging.getLogger('hotel.properties')
hotel_properties_logger.setLevel(LOG_LEVEL)
hotel_properties_logger_file_handler = FileHandler(hotel_properties_log_file)
hotel_properties_logger_file_handler.setLevel(LOG_LEVEL)
hotel_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
hotel_properties_logger.addHandler(hotel_properties_logger_file_handler)