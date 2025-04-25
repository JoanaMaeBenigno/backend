from src.models.article_model import Article
from sqlalchemy import func

def get_paginated_posts(db_session, page=1, page_size=10):
    offset = (page - 1) * page_size

    posts_query = db_session.query(Article.uuid, Article.title, Article.thumbnail_image, Article.subtitle)\
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
    article = db_session.query(Article).filter_by(uuid=uuid).first()

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
