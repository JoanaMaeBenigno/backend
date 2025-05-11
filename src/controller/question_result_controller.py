from flask import Blueprint, request, jsonify
# from src.services.articles_service import get_paginated_posts, get_article_by_uuid, create_article_service, delete_article_service
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

# @question_result_blueprint.route('/<uuid>', methods=['GET'])
# def get_article(uuid):
#     try:
#         article = get_article_by_uuid(db.session, uuid)
#         if article:
#             return jsonify({
#                 "status": "success",
#                 "message": "Article fetched successfully",
#                 "data": article
#             })
#         else:
#             return jsonify({
#                 "status": "error",
#                 "message": "Article not found",
#                 "data": None
#             }), 404
#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": str(e),
#             "data": None
#         }), 500

# @question_result_blueprint.route('', methods=['POST'])
# def create_article():
#     try:
#         data = request.get_json()
#         article = create_article_service(data)

#         return jsonify({
#             "status": "success",
#             "message": "Article created successfully",
#             "data": {
#                 "uuid": article.uuid
#             }
#         }), 201

#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": str(e),
#             "data": None
#         }), 500

# @question_result_blueprint.route('/<uuid>', methods=['POST'])
# def delete_article(uuid):
#     try:
#         result = delete_article_service(uuid)

#         if result:
#             return jsonify({
#                 "status": "success",
#                 "message": "Article soft-deleted successfully",
#                 "data": {"uuid": uuid}
#             })
#         else:
#             return jsonify({
#                 "status": "error",
#                 "message": "Article not found or already deleted",
#                 "data": None
#             }), 404

#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": str(e),
#             "data": None
#         }), 500

