from flask import Blueprint, request, jsonify
from src.services.question_result_service import post_question_result_service, get_result_service

question_result_blueprint = Blueprint('question_result', __name__, url_prefix='/question_result')

@question_result_blueprint.route('', methods=['POST'])
def post_result():
    try:
        data = request.get_json()
        result = post_question_result_service(data)

        return jsonify({
            "status": "success",
            "message": "Posts fetched successfully",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@question_result_blueprint.route('<id>', methods=['GET'])
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
