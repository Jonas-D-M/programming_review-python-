import logging
from logging import FileHandler
from logging import Formatter


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

#adres_properties_logger
adres_properties_log_file = 'oefen_examen\\logs\\adres_properties_logfile.txt'

adres_properties_logger = logging.getLogger('adres.properties')
adres_properties_logger.setLevel(LOG_LEVEL)
adres_properties_logger_file_handler = FileHandler(adres_properties_log_file)
adres_properties_logger_file_handler.setLevel(LOG_LEVEL)
adres_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
adres_properties_logger.addHandler(adres_properties_logger_file_handler)

#handelszaak properties
handelszaak_properties_log_file = 'oefen_examen\\logs\\handelszaak_properties_logfile.txt'

handelszaak_properties_logger = logging.getLogger('handelszaak.properties')
handelszaak_properties_logger.setLevel(LOG_LEVEL)
handelszaak_properties_logger_file_handler = FileHandler(handelszaak_properties_log_file)
handelszaak_properties_logger_file_handler.setLevel(LOG_LEVEL)
handelszaak_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
handelszaak_properties_logger.addHandler(handelszaak_properties_logger_file_handler)

#huisartspraktijk properties
huisartspraktijk_properties_log_file = 'oefen_examen\\logs\\huisartspraktijk_properties_logfile.txt'

huisartspraktijk_properties_logger = logging.getLogger('huisartspraktijk.properties')
huisartspraktijk_properties_logger.setLevel(LOG_LEVEL)
huisartspraktijk_properties_logger_file_handler = FileHandler(huisartspraktijk_properties_log_file)
huisartspraktijk_properties_logger_file_handler.setLevel(LOG_LEVEL)
huisartspraktijk_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
huisartspraktijk_properties_logger.addHandler(huisartspraktijk_properties_logger_file_handler)