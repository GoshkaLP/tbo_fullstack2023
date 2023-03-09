from flask import Blueprint, request

from app.controllers.locations_controller import get_federal_subjects, get_locations

locations = Blueprint('locations', __name__)


@locations.route('/api/federalSubjects', methods=['GET'])
def api_get_federal_subjects():
    return get_federal_subjects()


@locations.route('/api/locations', methods=['POST'])
def api_get_locations():
    return get_locations(request.json)
