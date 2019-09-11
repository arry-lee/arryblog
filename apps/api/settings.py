REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS':"rest_framework.versioning.URLPathVersioning",
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
    'VERSION_PARAM': 'version',

    'DEFAULT_THROTTLE_CLASSES': [
        'tpl.throttling.AnonRateThrottle',
        'tpl.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        '_anon': '10/m',
        '_user': '20/m',
    },
}