from marshmallow import Schema, fields


class QueryableFieldSchema(Schema):

    """Single query to get in queryset."""

    field = fields.Select(
        choices=['roe', 'pe', 'market_cap', 'debt_percent'], required=True)
    averaged_years = fields.Integer(default=1)

    class Meta:
        fields = ('field', 'averaged_years', 'min', 'max', 'rank')


class QuerySetSchema(Schema):

    """Set of queries for ranking on."""

    query = fields.Nested(QueryableFieldSchema, many=True)
