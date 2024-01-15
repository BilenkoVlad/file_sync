import logging


class OwnLogger:
    _formatter = logging.Formatter('\n %(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def __init__(self):
        self._logger = logging.getLogger("file_sync_task")
        self._logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("logfile.log")
        console_handler.setFormatter(self._formatter)
        file_handler.setFormatter(self._formatter)

        self._logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    @property
    def logger(self):
        return self._logger
