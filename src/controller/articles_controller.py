from flask import Blueprint, request, jsonify
from src.services.articles_service import get_paginated_posts, get_article_by_uuid
from src.config.extensions import db

article_blueprint = Blueprint('articles', __name__, url_prefix='/article')

@article_blueprint.route('', methods=['GET'])
def list_posts():
    try:
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 10))
        result = get_paginated_posts(db.session, page, page_size)

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

@article_blueprint.route('/<uuid>', methods=['GET'])
def get_article(uuid):
    try:
        article = get_article_by_uuid(db.session, uuid)
        if article:
            return jsonify({
                "status": "success",
                "message": "Article fetched successfully",
                "data": article
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Article not found",
                "data": None
            }), 404
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "data": None
        }), 500
