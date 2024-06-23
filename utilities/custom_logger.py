import logging

class LogGen:
    def loggen(self):
        logger = logging.getLogger(__name__)
        # Check if the logger already has handlers
        if not logger.hasHandlers():
            filehandler = logging.FileHandler(filename=r"C:\Users\Admin\Desktop\Automation\pytest_framework\logs\automation.log")
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
            logger.setLevel(logging.DEBUG)

        return logger


