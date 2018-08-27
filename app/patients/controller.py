from http import HTTPStatus

from flask import Blueprint, request, json

from app import util
from app.patients import service, error, constant


bp = Blueprint('patients', __name__, url_prefix='/patients')


@bp.route("/autocomplete", methods=['GET'])
def get_patients_autocomplete():
    q = request.args.get('q')
    if not q:
        return util.response_error(
            error.ERR_PATIENTS_AUTOCOMPLETE_QUERYPARAM_Q_REQUIRED,
            HTTPStatus.BAD_REQUEST
        )
    elif len(q) < constant.VALIDATE_PATIENTS_AUTOCOMPLETE_QUERYPARAM_Q_MIN_LENGTH:
        return util.response_error(
            error.ERR_PATIENTS_AUTOCOMPLETE_QUERYPARAM_Q_MIN_LENGTH,
            HTTPStatus.BAD_REQUEST
        )

    try:
        # Search patients on service
        result = service.get_patients_by_name(q)
    except Exception as e:
        # Service error
        return util.response_error(
            error.ERR_PATIENTS_AUTOCOMPLETE_INTERNAL_SERVER_ERROR,
            HTTPStatus.INTERNAL_SERVER_ERROR
        )

    # Patients not found
    if len(result) == 0:
        return util.response_error(
            error.ERR_PATIENTS_AUTOCOMPLETE_NOT_FOUND,
            HTTPStatus.NOT_FOUND
        )

    # Response success
    return util.response_success(
        result,
        HTTPStatus.OK
    )
