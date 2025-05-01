from flask import Blueprint, jsonify
from src.services.check_learning_service import get_all_categories, get_questions_with_choices_by_category, get_single_category
from src.models.category_model import Category
from src.config.extensions import db

check_learning_blueprint = Blueprint('cheack_learning', __name__, url_prefix='/check_learning')

@check_learning_blueprint.route('/category', methods=['GET'])
def get_categories():
    try:
        data = get_all_categories(db.session)
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
        data = get_single_category(db.session, category_id)
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

@check_learning_blueprint.route('/question/<category_id>', methods=['GET'])
def list_questions_with_choices(category_id):
    try:
        questions = get_questions_with_choices_by_category(db.session, category_id)
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
