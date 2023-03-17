from app.controllers.responses_controller import resp_ok
from app.controllers.db_controller import db_get_federals, db_get_locations, db_get_location, \
    db_get_federals_locations, db_get_hexagon_locations, db_get_funding_sport_types, db_get_construction_sport_types
from collections import defaultdict


funding = {
    'federal_budget_funding': 'Федеральное финансирование',
    'regional_budget_funding': 'Финансирование субъекта федерации',
    'local_budget_funding': 'Финансирование МО'
}


def get_federal_subjects() -> dict:
    """
    Фукнкция для преобразования в Json информации о субъектах РФ
    """
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
    """
    Фукнкция для преобразования в Json информации о координатах субъектов РФ
    """
    resp = []
    res = db_get_federals_locations()
    if res:
        resp = [row[0] for row in res]
    return resp_ok(resp)


def get_hexagons_locations() -> dict:
    """
    Фукнкция для преобразования в Json информации о координатах гексагонов спортивных космлексов, которые строились
    """
    resp = []
    res = db_get_hexagon_locations()
    if res:
        resp = [row[0] for row in res]
    return resp_ok(resp)


def get_locations() -> dict:
    """
    Фукнкция для преобразования в Json информации о координатах спортивных комплексов
    """
    resp = []
    res = db_get_locations()
    if res:
        for row in res:
            resp.append({
                'objId': row[0],
                'address': row[1],
                'federalSubject': row[2],
                'fedId': row[3],
                'longitude': row[4],
                'latitude': row[5]
            })
    return resp_ok(resp)


def get_location(obj_id: int) -> dict:
    """
    Фукнкция для преобразования в Json информации о конкретном спортивном комплексе
    """
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
                'registeredInRegistry': location_supervisory.registered_in_registry,
                'websiteUrl': location_supervisory.website_url,
                'workHoursWeekdays': location_supervisory.work_hours_weekdays,
                'saturdayWorkingHours': location_supervisory.saturday_working_hours,
                'sundayWorkingHours': location_supervisory.sunday_working_hours
            }
        })
    return resp_ok(resp)


def get_funding_sport_types() -> dict:
    """
    Фукнкция для преобразования в Json информации необходимой для построения графика распределения средств по
    типам спортивных комплексов
    """
    resp = {}
    res = db_get_funding_sport_types()
    if res:
        data_dict = defaultdict(lambda: defaultdict(float))
        for row in res:
            sports_complex_type, funding_type, count = row
            data_dict[funding_type][sports_complex_type] += count

        categories = sorted(list(set([row[0] for row in res])))

        series = []
        for funding_type in data_dict:
            data = [data_dict[funding_type][category] for category in categories]
            series.append({'name': funding.get(funding_type), 'data': data})

        resp = {'series': series, 'categories': categories}

    return resp_ok(resp)


def get_construction_sport_types() -> dict:
    """
    Фукнкция для преобразования в Json информации необходимой для построения графика распределения выделенного бюджета по годам
    """
    resp = {}
    res = db_get_construction_sport_types()
    if res:
        res = sorted(res, key=lambda x: (x.funding_type, x.construction_start_date))

        series = []
        categories = sorted(list(set([row.construction_start_date for row in res])))

        for budget_funding in set([row.funding_type for row in res]):
            item_series = {
                'name': funding.get(budget_funding),
                'data': [row.count for row in res if row.funding_type == budget_funding]
            }

            series.append(item_series)

        resp = {'series': series, 'categories': categories}

    return resp_ok(resp)
