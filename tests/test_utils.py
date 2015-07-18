from .. import utils


def test_get_years_to_fetch():
    input_data = [dict(code='ANZ', average=5), dict(code='CBA', average=1)]
    assert utils.get_years_to_fetch(input_data) == 5

    input_data = [dict(code='ANZ'), dict(code='CBA')]
    assert utils.get_years_to_fetch(input_data) == 1
