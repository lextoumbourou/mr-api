import json
from ..app import app


class TestApp(object):

    def setup(self):
        self.app = app.test_client()

    def test_invalid_query_fails(self):
        resp = self.app.post(
            '/query',
            content_type='application/json',
            data=json.dumps({
                'query': [
                    {'field': 'Haxx'},
                    {'field': 'roe', 'average_years': 5}
                ]
            })
        )
        assert resp.status_code == 400
