from flask import Blueprint, request

from app.controllers.locations_controller import get_federal_subjects, get_locations, get_location, \
    get_federal_subject_locations, get_hexagons_locations, get_funding_sport_types, \
    get_construction_sport_types

locations = Blueprint('locations', __name__)


@locations.route('/api/federalSubjects', methods=['GET'])
def api_get_federal_subjects():
    """
    Endpoint поулчения списка субъектов РФ
    """
    return get_federal_subjects()


@locations.route('/api/federalSubjectsLocations', methods=['GET'])
def api_get_federal_subjects_locations():
    """
    Endpoint получения координат полигонов субъектов РФ
    """
    return get_federal_subject_locations()


@locations.route('/api/hexagonLocations', methods=['GET'])
def api_get_hexagon_locations():
    """
    Endpoint получения координат гексагонов спортивных объектов, которые строили
    """
    return get_hexagons_locations()


@locations.route('/api/locations', methods=['GET'])
def api_get_locations():
    """
    Endpoint получаения координат точек всех спортивных комплексов
    """
    return get_locations()


@locations.route('/api/location/<int:obj_id>', methods=['GET'])
def api_get_locations_info(obj_id: int):
    """
    Endpoint получения информации о конкретной точке на карте
    """
    return get_location(obj_id)


@locations.route('/api/fundingSportTypes', methods=['GET'])
def api_get_funding_sport_types():
    """
    Endpoint получения информации для графика распределения средств по типам спортивных комплексов
    """
    return get_funding_sport_types()


@locations.route('/api/constructionSportTypes', methods=['GET'])
def api_get_construction_sport_types():
    """
    Endpoint получения информации для графика распределения выделенного бюджета по годам
    """
    return get_construction_sport_types()
