from flask import request
from flask.ext.api import FlaskAPI
from flask.ext.api.exceptions import ParseError

from marshmallow import ValidationError

import schema


app = FlaskAPI(__name__)


app.config['DEFAULT_RENDERERS'] = [
    'flask.ext.api.renderers.JSONRenderer',
    'flask.ext.api.renderers.BrowsableAPIRenderer',
]


@app.route('/query', methods=['GET', 'POST'])
def stocks():
    """Simplest possible implementation of this algorithm."""
    s = schema.QuerySetSchema(strict=True)

    try:
        q = s.load(request.data)
    except ValidationError as err:
        raise ParseError(detail='Bad fields: {}'.format(err.field_names))

    return dict(data=q)


if __name__ == '__main__':
    app.run(debug=True)
