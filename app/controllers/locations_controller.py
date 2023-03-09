from app.controllers.responses_controller import resp_ok
from app.controllers.db_controller import db_get_federals, db_get_locations


def get_federal_subjects() -> dict:
    resp = []
    res = db_get_federals()
    if res:
        for row in res:
            resp.append({
                'fedId': row[0],
                'fedName': row[1]
            })
    return resp_ok(resp)


def get_locations(form: dict | None = None) -> dict:
    resp = []
    res = db_get_locations(form.get('fedIds') if form else None)
    if res:
        for row in res:
            resp.append({
                'objId': row[0],
                'name': row[1],
                'address': row[2],
                'federalSubject': row[3],
                'longitude': row[4],
                'latitude': row[5]
            })
    return resp_ok(resp)
