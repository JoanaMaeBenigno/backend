from flask import Blueprint, request, jsonify
from src.services.check_learning_service import get_all_categories,\
    get_questions_with_choices_by_category, \
    get_single_category, \
    create_category_service, \
    delete_category_service, \
    save_question_with_choices, \
    delete_question_service, \
    save_survey, \
    get_survey_questions_by_category, \
    delete_survey_question_service

check_learning_blueprint = Blueprint('check_learning', __name__, url_prefix='/check_learning')

# Category Related
@check_learning_blueprint.route('/category', methods=['GET'])
def get_categories():
    try:
        data = get_all_categories()
        print(data)
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
        category = create_category_service(data)

        return jsonify({
            "status": "success",
            "message": "Category created successfully",
            "data": {
                "uuid": category.id
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

# Question Related
@check_learning_blueprint.route('/question/<category_id>', methods=['GET'])
def list_questions_with_choices(category_id):
    try:
        questions = get_questions_with_choices_by_category(category_id, False)
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

@check_learning_blueprint.route('/question/with_answer/<category_id>', methods=['GET'])
def list_questions_with_choices_and_answer(category_id):
    try:
        questions = get_questions_with_choices_by_category(category_id, True)
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

# Survey Related
@check_learning_blueprint.route('/survey', methods=['POST'])
def create_survey():
    data = request.get_json()
    try:
        result = save_survey(data)

        return jsonify({
            "status": "success",
            "message": "Survey question saved successfully",
            "data": result
        }), 201
    except ValueError as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

@check_learning_blueprint.route('/survey/<category_id>', methods=['GET'])
def list_survey_questions(category_id):
    try:
        survey_questions = get_survey_questions_by_category(category_id)
        return jsonify({
            "status": "success",
            "message": "Survey questions fetched successfully",
            "data": survey_questions
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500

@check_learning_blueprint.route('/survey/<survey_id>', methods=['DELETE'])
def delete_survey(survey_id):
    try:
        result = delete_survey_question_service(survey_id)

        if result:
            return jsonify({
                "status": "success",
                "message": "Survey question soft-deleted successfully",
                "data": {"id": survey_id}
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Survey question not found or already deleted",
                "data": None
            }), 404
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500
