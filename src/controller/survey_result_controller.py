from flask import Blueprint, request, jsonify
# from src.services.question_result_service import post_question_result_service, get_result_service
from src.services.survey_result_service import post_survey_result_service, get_result_service

survey_result_blueprint = Blueprint('survey_result', __name__, url_prefix='/survey_result')

@survey_result_blueprint.route('', methods=['POST'])
def post_result():
    try:
        data = request.get_json()
        result = post_survey_result_service(data)

        return jsonify({
            "status": "success",
            "message": "Survey result posted successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@survey_result_blueprint.route('<id>', methods=['GET'])
def get_result(id):
    try:
        result = get_result_service(id)

        return jsonify({
            "status": "success",
            "message": "Question result fetched successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500
