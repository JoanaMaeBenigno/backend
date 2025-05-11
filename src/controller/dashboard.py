from flask import Blueprint, jsonify
from src.services.dashboard import get_check_learning_service

dashboard_blueprint = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Category Related
@dashboard_blueprint.route('/check_learning', methods=['GET'])
def get_check_learning_dashboard():
    try:
        data = get_check_learning_service()
        return jsonify({
            "status": "success",
            "message": "Check learning dashboard fetched successfully",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500
