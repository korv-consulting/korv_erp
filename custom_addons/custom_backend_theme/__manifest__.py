{
    'name': 'Custom Backend Theme',
    'version': '1.0',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'custom_backend_theme/static/src/scss/backend.scss',
        ],
    },
    'installable': True,
}