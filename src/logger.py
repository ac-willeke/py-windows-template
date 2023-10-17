import datetime
import logging
import logging.config
import os
import sys

import yaml

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
config_file = os.path.join(project_dir, "config/config_logger.yaml")


def reset_logger():
    """Reset the logger configuration to default."""
    logging.shutdown()
    logging.root.handlers = []  # Remove all handlers
    logging.root.setLevel(logging.WARNING)  # Set the root logger to a default level
    return


def setup_logging(
    default_path="../config/logging.yaml",
    default_level=logging.INFO,
):
    """
    Setup logging configuration

    Parameters
    ----------
    default_path : str
        Default value = 'config/logging.yaml')
    default_level : logging level
        Default value = logging.INFO)

    Returns
    -------
    Void
        Creates logging instance
    """
    path = default_path

    if os.path.exists(path):
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())

        # update logfile path and add to handler

        # logfile_name
        logfile_name = (
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            + "_"
            + os.path.splitext(os.path.basename(sys.argv[0]))[0]
            + ".log"
        )

        # update info file handler
        config["handlers"]["info_file_handler"]["filename"] = os.path.join(
            project_dir, "log", logfile_name
        )

        # load configuration
        logging.config.dictConfig(config)
        logging.info("Logging configuration file found and loaded.")

    else:
        logging.basicConfig(level=default_level)
        logging.info(
            "Logging configuration file not found. Using default configuration."
        )


## Example usage of logger within modules
## TODO move to tests/test_logger.py
def test_function():
    """Test function for logging"""

    logger = logging.getLogger(__name__)
    logger.info("This is a information message.")
    logger.debug("This is a debug message.")
    logger.warning("This is a warning message.")
    logger.error("This is a error message.")
    logger.critical("This is a critical message.")
    return


class Test(object):
    """
    Test class for logging.

    Parameters
    ----------
    logger : logging instance
        Default value = None

    Attributes
    ----------
    logger : logging instance
        Default value = None

    Methods
    -------
        - log_config: Log project configuration
        - log_best_practices: Log best practices
    """

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def log_config(self):
        """Log project configuration"""
        try:
            # loaded as module
            from src.config import load_catalog, load_parameters  # noqa
        except ModuleNotFoundError:
            # standalone use of logger.py
            from config import load_catalog, load_parameters  # noqa

        self.logger.info("Log project configuration:")

        catalog = load_catalog()
        parameters = load_parameters()
        # Access configuration variables
        self.logger.info("DATA_PATH: %s", catalog["name"]["filepath"])
        self.logger.info(
            "SPATIAL_REFERENCE: %s", parameters["spatial_reference"]["utm33"]
        )
        self.logger.info("Project configuration logged.")

    def log_best_practices(self):
        """Log best practices"""
        self.logger.info("Logging best practices:")
        self.logger.info("Use __name__ as the logger name.")
        self.logger.info(
            "Do not use logger at module level,\n\
            get logger within functions or classes instead.\n\
            Otherwise, the logger will be initialized when the module is imported,\n\
            this is often before the logging configuration is set up."
        )
        self.logger.info("Best practices logged.")


if __name__ == "__main__":
    # setup loggging for standalone use of logger.py
    setup_logging()
    logger = logging.getLogger(__name__)

    # test project logger
    Test(logger).log_config()
    Test(logger).log_best_practices()

    # test custom logger
    test_function()

    pass
