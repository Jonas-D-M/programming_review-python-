import logging
from logging import FileHandler
from logging import Formatter


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

#melding_properties_logger 
melding_properties_log_file = 'thuisproject2\\logs\\melding_properties_logfile.txt'

melding_properties_logger = logging.getLogger('logs.melding_properties')
melding_properties_logger.setLevel(LOG_LEVEL)
melding_properties_logger_file_handler = FileHandler(melding_properties_log_file)
melding_properties_logger_file_handler.setLevel(LOG_LEVEL)
melding_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
melding_properties_logger.addHandler(melding_properties_logger_file_handler)

#melding inlezen file logger
melding_static_methods_log_file = 'thuisproject2\\logs\\melding_static_methods_logfile.txt'

melding_static_methods_logger = logging.getLogger('logs.melding_static_methods')
melding_static_methods_logger.setLevel(LOG_LEVEL)
melding_static_methods_logger_file_handler = FileHandler(melding_static_methods_log_file)
melding_static_methods_logger_file_handler.setLevel(LOG_LEVEL)
melding_static_methods_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
melding_static_methods_logger.addHandler(melding_static_methods_logger_file_handler)

#locatie logger
locatie_log_file = 'thuisproject2\\logs\\locatie_logfile.txt'

locatie_logger = logging.getLogger('logs.locatie')
locatie_logger.setLevel(LOG_LEVEL)
locatie_logger_file_handler = FileHandler(locatie_log_file)
locatie_logger_file_handler.setLevel(LOG_LEVEL)
locatie_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
locatie_logger.addHandler(locatie_logger_file_handler)

#stadsmedewerker properties logger
stadsmedewerker_properties_log_file = 'thuisproject2\\logs\\stadsmedewerker_properties_logfile.txt'

stadsmedewerker_properties_logger = logging.getLogger('logs.stadsmedewerker_properties')
stadsmedewerker_properties_logger.setLevel(LOG_LEVEL)
stadsmedewerker_properties_logger_file_handler = FileHandler(stadsmedewerker_properties_log_file)
stadsmedewerker_properties_logger_file_handler.setLevel(LOG_LEVEL)
stadsmedewerker_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
stadsmedewerker_properties_logger.addHandler(stadsmedewerker_properties_logger_file_handler)

#stadsmedewerker methods logger
stadsmedewerker_methods_log_file = 'thuisproject2\\logs\\stadsmedewerker_methods_logfile.txt'

stadsmedewerker_methods_logger = logging.getLogger('logs.stadsmedewerker_methods')
stadsmedewerker_methods_logger.setLevel(LOG_LEVEL)
stadsmedewerker_methods_logger_file_handler = FileHandler(stadsmedewerker_methods_log_file)
stadsmedewerker_methods_logger_file_handler.setLevel(LOG_LEVEL)
stadsmedewerker_methods_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
stadsmedewerker_methods_logger.addHandler(stadsmedewerker_methods_logger_file_handler)
