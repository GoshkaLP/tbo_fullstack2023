from flask import Blueprint, request

from app.controllers.locations_controller import get_federal_subjects, get_locations, get_locations_info, \
    get_locations_spending, get_locations_supervisory

locations = Blueprint('locations', __name__)


@locations.route('/api/federalSubjects', methods=['GET'])
def api_get_federal_subjects():
    return get_federal_subjects()


@locations.route('/api/locations', methods=['POST'])
def api_get_locations():
    return get_locations(request.json)


@locations.route('/api/locationsInfo/<int:obj_id>', methods=['GET'])
def api_get_locations_info(obj_id: int):
    return get_locations_info(obj_id)


@locations.route('/api/locationsSpending/<int:obj_id>', methods=['GET'])
def api_get_locations_spending(obj_id: int):
    return get_locations_spending(obj_id)


@locations.route('/api/locationsSupervisory/<int:obj_id>', methods=['GET'])
def api_get_locations_supervisory(obj_id: int):
    return get_locations_supervisory(obj_id)
