# app/logging_config.py

import logging
import logging.config

# Define the logging configuration
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'level': logging.INFO,
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'formatter': 'verbose',
            'level': logging.DEBUG,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': logging.DEBUG,
            'propagate': True,
        },
    },
}

def setup_logging():
    """Set up logging configuration."""
    logging.config.dictConfig(LOGGING_CONFIG)
    logging.info("Logging configured successfully.")
