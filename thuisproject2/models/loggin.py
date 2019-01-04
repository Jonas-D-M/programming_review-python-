import logging
from logging import FileHandler
from logging import Formatter


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

#melding_properties_logger 
melding_properties_log_file = 'thuisproject2\\logs\\melding_properties_logfile.txt'

melding_properties_logger = logging.getLogger('melding_properties.logs')
melding_properties_logger.setLevel(LOG_LEVEL)
melding_properties_logger_file_handler = FileHandler(melding_properties_log_file)
melding_properties_logger_file_handler.setLevel(LOG_LEVEL)
melding_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
melding_properties_logger.addHandler(melding_properties_logger_file_handler)

#melding inlezen file logger
melding_static_methods_log_file = 'thuisproject2\\logs\\melding_static_methods_logfile.txt'

melding_static_methods_logger = logging.getLogger('melding_static_methods.logs')
melding_static_methods_logger.setLevel(LOG_LEVEL)
melding_static_methods_logger_file_handler = FileHandler(melding_static_methods_log_file)
melding_static_methods_logger_file_handler.setLevel(LOG_LEVEL)
melding_static_methods_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
melding_static_methods_logger.addHandler(melding_static_methods_logger_file_handler)