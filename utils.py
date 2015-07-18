def get_years_to_fetch(queries):
    return max(
        [q['average'] for q in queries if q.get('average')] or [1])
