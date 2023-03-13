from app.controllers.responses_controller import resp_ok
from app.controllers.db_controller import db_get_federals, db_get_locations, db_get_locations_info, \
    db_get_locations_spending, db_get_locations_supervisory, db_get_federals_locations

from json import loads, dumps

def get_federal_subjects() -> dict:
    resp = []
    res = db_get_federals()
    if res:
        for row in res:
            resp.append({
                'fedId': row.fed_id,
                'fedName': row.federal_subject
            })
    return resp_ok(resp)


def get_federal_subject_locations() -> dict:
    resp = []
    res = db_get_federals_locations()
    if res:
        resp = [row[0] for row in res]
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


def get_locations_info(obj_id: int) -> dict:
    resp = {}
    res = db_get_locations_info(obj_id)
    if res:
        resp.update({
            'objId': obj_id,
            'active': res.active,
            'description': res.description,
            'descriptionLong': res.description_long,
            'municipalityEntity': res.municipal_entity,
            'locality': res.locality,
            'address': res.address,
            'sportsComplexType': res.sports_complex_type,
            'sportsTypes': res.sports_types,
            'websiteUrl': res.website_url,
            'workHoursWeekdays': res.work_hours_weekdays,
            'saturdayWorkingHours': res.saturday_working_hours,
            'sundayWorkingHours': res.sunday_working_hours
        })
    return resp_ok(resp)


def get_locations_spending(obj_id: int) -> dict:
    resp = {}
    res = db_get_locations_spending(obj_id)
    if res:
        resp.update({
            'objId': obj_id,
            'objectActions': res.object_actions,
            'constructionStartDate': res.construction_start_date,
            'constructionEndDate': res.construction_end_date,
            'totalFunding': res.total_funding,
            'federalBudgetFunding': res.federal_budget_funding,
            'federalBudgetFundingSpent': res.federal_budget_funding_spent,
            'regionalBudgetFunding': res.regional_budget_funding,
            'regionalBudgetFundingSpent': res.regional_budget_funding_spent,
            'localBudgetFunding': res.local_budget_funding,
            'localBudgetFundingSpent': res.local_budget_funding_spent,
            'offBudgetFunding': res.off_budget_funding,
            'offBudgetFundingSpent': res.off_budget_funding_spent
        })
    return resp_ok(resp)


def get_locations_supervisory(obj_id: int) -> dict:
    resp = {}
    res = db_get_locations_supervisory(obj_id)
    if res:
        resp.update({
            'objId': obj_id,
            'supervisoryAuthority': res.supervisory_authority,
            'supervisoryAuthorityPhone': res.supervisory_authority_phone,
            'contactPhone': res.contact_phone,
            'email': res.email,
            'registeredInRegistry': res.registered_in_registry
        })
    return resp_ok(resp)
