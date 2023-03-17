from flask import Blueprint, request

from app.controllers.locations_controller import get_federal_subjects, get_locations, get_location, \
    get_federal_subject_locations, get_hexagons_locations, get_funding_sports_type

locations = Blueprint('locations', __name__)


@locations.route('/api/federalSubjects', methods=['GET'])
def api_get_federal_subjects():
    return get_federal_subjects()


@locations.route('/api/federalSubjectsLocations', methods=['GET'])
def api_get_federal_subjects_locations():
    return get_federal_subject_locations()


@locations.route('/api/hexagonLocations', methods=['GET'])
def api_get_hexagon_locations():
    return get_hexagons_locations()


@locations.route('/api/locations', methods=['GET'])
def api_get_locations():
    return get_locations()


@locations.route('/api/location/<int:obj_id>', methods=['GET'])
def api_get_locations_info(obj_id: int):
    return get_location(obj_id)


@locations.route('/api/fundingSportTypes', methods=['GET'])
def api_get_funding_sport_types():
    return get_funding_sports_type()
