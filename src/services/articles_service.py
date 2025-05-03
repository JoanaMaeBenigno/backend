import uuid
import json
from datetime import datetime
from src.config.extensions import db
from src.models.article_model import Article
from sqlalchemy import func

def get_paginated_posts(db_session, page=1, page_size=10):
    offset = (page - 1) * page_size

    posts_query = db_session.query(Article.uuid, Article.title, Article.thumbnail_image, Article.subtitle)\
        .filter_by(is_deleted=False)\
        .order_by(Article.posted_date.desc())\
        .limit(page_size)\
        .offset(offset)

    posts = [
        {
            "uuid": post.uuid,
            "title": post.title,
            "thumbnail_image": post.thumbnail_image,
            "subtitle": post.subtitle
        }
        for post in posts_query
    ]

    total_items = db_session.query(func.count(Article.uuid)).scalar()
    total_pages = (total_items + page_size - 1) // page_size

    return {
        "posts": posts,
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
            "total_items": total_items
        }
    }

def get_article_by_uuid(db_session, uuid):
    article = db_session.query(Article).filter_by(uuid=uuid, is_deleted=False).first()

    if article:
        return {
            "uuid": article.uuid,
            "title": article.title,
            "thumbnail_image": article.thumbnail_image,
            "subtitle": article.subtitle,
            "author": article.author,
            "content": article.content,
            "posted_date": article.posted_date
        }
    return None

def create_article_service(data):
    article = Article(
        uuid=str(uuid.uuid4()),
        posted_date=datetime.now(),
        title=data.get('title'),
        subtitle=data.get('subtitle'),
        author=data.get('author'),
        thumbnail_image=data.get('thumbnail'),
        content=json.dumps(data.get('content')),
        is_deleted=False
    )

    db.session.add(article)
    db.session.commit()

    return article

def delete_article_service(id):
    article = Article.query.filter_by(uuid=id, is_deleted=False).first()

    if article:
        article.is_deleted = True
        db.session.commit()
        return True

    return False
