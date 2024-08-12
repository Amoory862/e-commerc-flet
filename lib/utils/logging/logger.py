import logging

class LoggerHelper:
    def __init__(self):
        # Create a custom logger
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)  # Set the desired log level

        # Create handlers
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)  # Set the level for console handler

        # Create and set formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self._logger.addHandler(console_handler)

    def debug(self, message):
        self._logger.debug(message)

    def info(self, message):
        self._logger.info(message)

    def warning(self, message):
        self._logger.warning(message)

    def error(self, message, exc_info=False):
        self._logger.error(message, exc_info=exc_info)


# Example usage
if __name__ == '__main__':
    logger = LoggerHelper()

    # Log messages
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    try:
        1 / 0  # Example of an exception
    except ZeroDivisionError as e:
        logger.error('An error occurred', exc_info=True)


