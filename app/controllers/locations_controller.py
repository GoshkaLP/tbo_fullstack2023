from app.controllers.responses_controller import resp_ok
from app.controllers.db_controller import db_get_federals, db_get_locations, db_get_location, \
    db_get_federals_locations, db_get_hexagon_locations, db_get_funding_sport_types


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


def get_hexagons_locations() -> dict:
    resp = []
    res = db_get_hexagon_locations()
    if res:
        resp = [row[0] for row in res]
    return resp_ok(resp)


def get_locations() -> dict:
    resp = []
    res = db_get_locations()
    if res:
        for row in res:
            resp.append({
                'objId': row[0],
                'name': row[1],
                'address': row[2],
                'federalSubject': row[3],
                'fedId': row[4],
                'longitude': row[5],
                'latitude': row[6]
            })
    return resp_ok(resp)


def get_location(obj_id: int) -> dict:
    resp = {}
    res = db_get_location(obj_id)
    if res:
        location_info = res[0]
        location_spending = res[1]
        location_supervisory = res[2]
        resp.update({
            'objId': obj_id,
            'info': {
                'name': location_info.name,
                'active': location_info.active,
                'description': location_info.description,
                'descriptionLong': location_info.description_long,
                'municipalityEntity': location_info.municipal_entity,
                'locality': location_info.locality,
                'address': location_info.address,
                'sportsComplexType': location_info.sports_complex_type,
                'sportsTypes': location_info.sports_types,
                'websiteUrl': location_info.website_url,
                'workHoursWeekdays': location_info.work_hours_weekdays,
                'saturdayWorkingHours': location_info.saturday_working_hours,
                'sundayWorkingHours': location_info.sunday_working_hours
            },
            'spending': {
                'objectActions': location_spending.object_actions,
                'constructionStartDate': location_spending.construction_start_date,
                'constructionEndDate': location_spending.construction_end_date,
                'totalFunding': location_spending.total_funding,
                'federalBudgetFunding': location_spending.federal_budget_funding,
                'federalBudgetFundingSpent': location_spending.federal_budget_funding_spent,
                'regionalBudgetFunding': location_spending.regional_budget_funding,
                'regionalBudgetFundingSpent': location_spending.regional_budget_funding_spent,
                'localBudgetFunding': location_spending.local_budget_funding,
                'localBudgetFundingSpent': location_spending.local_budget_funding_spent,
                'offBudgetFunding': location_spending.off_budget_funding,
                'offBudgetFundingSpent': location_spending.off_budget_funding_spent
            },
            'supervisory': {
                'supervisoryAuthority': location_supervisory.supervisory_authority,
                'supervisoryAuthorityPhone': location_supervisory.supervisory_authority_phone,
                'contactPhone': location_supervisory.contact_phone,
                'email': location_supervisory.email,
                'registeredInRegistry': location_supervisory.registered_in_registry
            }
        })
    return resp_ok(resp)


def get_funding_sports_type() -> dict:
    resp = {}
    res = db_get_funding_sport_types()
    if res:
        series_dict = {}
        categories = set()
        for row in res:
            funding_type = row[1]
            category = row[0]
            categories.add(category)
            if funding_type not in series_dict:
                series_dict[funding_type] = [0] * len(categories)
            index = list(categories).index(category)
            series_dict[funding_type].extend([0] * (index - len(series_dict[funding_type]) + 1))
            series_dict[funding_type][index] += row[2]

        resp = {
            'series': [{'name': funding_type, 'data': count_list} for funding_type, count_list in series_dict.items()],
            'categories': list(categories)
        }

    return resp_ok(resp)
