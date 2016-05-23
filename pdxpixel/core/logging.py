import os

LOGGING_MODULE = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d  \
                %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{0}/logs/debug.log'.format(os.path.dirname(__file__)),
            'maxBytes': 1024*1024*10,
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'request_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '{0}/logs/request.log'.format(os.path.dirname(__file__)),
            'maxBytes': 1024*1024*10,
            'backupCount': 5,
            'formatter': 'verbose'
        },
    },
    # TODO -- fine tune the logging configuration
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'request_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'apps.blog': {
            'handlers': ['console', 'mail_admins', 'debug_file'],
            'level': 'INFO',
        },
        'apps.accounts': {
            'handlers': ['console', 'mail_admins', 'debug_file'],
            'level': 'INFO',
        },
        'apps.search': {
            'handlers': ['console', 'mail_admins', 'request_file'],
            'level': 'DEBUG',
        }
    }
}
