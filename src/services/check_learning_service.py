import uuid
from datetime import datetime
from src.models.category_model import Category
from src.models.question_model import Question
from src.models.answer_model import Answer
from src.config.extensions import db

def get_single_category(category_id):
    category = db.query(Category).filter_by(id=category_id).first()

    return {
        "id": category.id,
        "name": category.name,
        "description": category.description
    }

def get_all_categories():
    categories = db.query(Category).all()
    return [
        {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "passRate": 78
        }
        for category in categories
    ]

def create_category_service(data):
    article = Category(
        id=str(uuid.uuid4()),
        created_date=datetime.now(),
        name=data.get('title'),
        description=data.get('description'),
        is_deleted=False
    )

    db.session.add(article)
    db.session.commit()

    return article

def delete_category_service(id):
    category = Category.query.filter_by(id=id, is_deleted=False).first()

    if category:
        category.is_deleted = True
        db.session.commit()
        return True

    return False

def get_questions_with_choices_by_category(category_id):
    questions = db.query(Question).filter_by(category_id=category_id).all()

    result = []
    for q in questions:
        answers = db.query(Answer).filter_by(question_id=q.id).all()
        choices = [
            {"id": a.id, "answer_text": a.answer_text}
            for a in answers
        ]

        result.append({
            "id": q.id,
            "question_text": q.question_text,
            "choices": choices
        })

    return result
