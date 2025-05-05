from flask import Blueprint, request, jsonify
from src.services.check_learning_service import get_all_categories,\
    get_questions_with_choices_by_category, \
    get_single_category, \
    create_category_service, \
    delete_category_service, \
    save_question_with_choices, \
    delete_question_service

check_learning_blueprint = Blueprint('check_learning', __name__, url_prefix='/check_learning')

@check_learning_blueprint.route('/category', methods=['GET'])
def get_categories():
    try:
        data = get_all_categories()
        return jsonify({
            "status": "success",
            "message": "Categories fetched successfully",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@check_learning_blueprint.route('/category/<category_id>', methods=['GET'])
def get_category(category_id):
    try:
        data = get_single_category(category_id)
        return jsonify({
            "status": "success",
            "message": "Categories fetched successfully",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@check_learning_blueprint.route('/category', methods=['POST'])
def create_category():
    data = request.get_json()

    try:
        data = request.get_json()
        article = create_category_service(data)

        return jsonify({
            "status": "success",
            "message": "Category created successfully",
            "data": {
                "uuid": article.id
            }
        }), 201

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@check_learning_blueprint.route('/category/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        result = delete_category_service(category_id)

        if result:
            return jsonify({
                "status": "success",
                "message": "Category soft-deleted successfully",
                "data": {"id": category_id}
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Category not found or already deleted",
                "data": None
            }), 404
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@check_learning_blueprint.route('/question/<category_id>', methods=['GET'])
def list_questions_with_choices(category_id):
    try:
        questions = get_questions_with_choices_by_category(category_id)
        return jsonify({
            "status": "success",
            "message": "Questions with choices fetched successfully",
            "data": questions
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@check_learning_blueprint.route('/question', methods=['POST'])
def create_question():
    data = request.get_json()
    try:
        result = save_question_with_choices(data)

        return jsonify({
            "status": "success",
            "message": "Question saved successfully",
            "data": result
        }), 201
    except ValueError as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@check_learning_blueprint.route('/question/<question_id>', methods=['DELETE'])
def delete_question(question_id):
    try:
        result = delete_question_service(question_id)

        if result:
            return jsonify({
                "status": "success",
                "message": "Question soft-deleted successfully",
                "data": {"id": question_id}
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Question not found or already deleted",
                "data": None
            }), 404
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500
