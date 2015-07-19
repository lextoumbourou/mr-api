import private


class Config(object):
    SQLALCHEMY_DATABASE_URI = private.SQLALCHEMY_DATABASE_URI
    DEFAULT_RENDERERS = [
        'flask.ext.api.renderers.JSONRenderer',
        'flask.ext.api.renderers.BrowsableAPIRenderer',
    ]

