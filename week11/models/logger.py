import logging
from logging import FileHandler
from logging import Formatter


LOG_FORMAT = (
    "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.INFO

#bier_properties_logger
bier_properties_log_file = 'week11\\logs\\bier_properties_logfile.txt'

bier_properties_logger = logging.getLogger('bier.properties')
bier_properties_logger.setLevel(LOG_LEVEL)
bier_properties_logger_file_handler = FileHandler(bier_properties_log_file)
bier_properties_logger_file_handler.setLevel(LOG_LEVEL)
bier_properties_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
bier_properties_logger.addHandler(bier_properties_logger_file_handler)


#Bier file reader logger
bier_file_reader_log_file = 'week11\\logs\\bier_file_reader_logfile.txt'

bier_file_reader_logger = logging.getLogger('bier.file_reader')
bier_file_reader_logger.setLevel(LOG_LEVEL)
bier_file_reader_logger_file_handler = FileHandler(bier_file_reader_log_file)
bier_file_reader_logger_file_handler.setLevel(LOG_LEVEL)
bier_file_reader_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
bier_file_reader_logger.addHandler(bier_file_reader_logger_file_handler)


#zoek bieren op naam logger
bier_opnaam_log_file = 'week11\\logs\\bier_opnaam_logfile.txt'

bier_opnaam_logger = logging.getLogger('bier.opnaam')
bier_opnaam_logger.setLevel(LOG_LEVEL)
bier_opnaam_logger_file_handler = FileHandler(bier_opnaam_log_file)
bier_opnaam_logger_file_handler.setLevel(LOG_LEVEL)
bier_opnaam_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
bier_opnaam_logger.addHandler(bier_opnaam_logger_file_handler)


#zoek bieren op alcohol percentage logger
bier_opalcohol_log_file = 'week11\\logs\\bier_opalcohol_logfile.txt'

bier_opalcohol_logger = logging.getLogger('bier.opalcohol')
bier_opalcohol_logger.setLevel(LOG_LEVEL)
bier_opalcohol_logger_file_handler = FileHandler(bier_opalcohol_log_file)
bier_opalcohol_logger_file_handler.setLevel(LOG_LEVEL)
bier_opalcohol_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
bier_opalcohol_logger.addHandler(bier_opalcohol_logger_file_handler)


#zoek bieren op brouwerij
bier_opbrouwerij_log_file = 'week11\\logs\\bier_opbrouwerij_logfile.txt'

bier_opbrouwerij_logger = logging.getLogger('bier.opbrouwerij')
bier_opbrouwerij_logger.setLevel(LOG_LEVEL)
bier_opbrouwerij_logger_file_handler = FileHandler(bier_opbrouwerij_log_file)
bier_opbrouwerij_logger_file_handler.setLevel(LOG_LEVEL)
bier_opbrouwerij_logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
bier_opbrouwerij_logger.addHandler(bier_opbrouwerij_logger_file_handler)