from src.models.category_model import Category
from src.models.question_model import Question
from src.models.answer_model import Answer

def get_single_category(db_session, category_id):
    category = db_session.query(Category).filter_by(id=category_id).first()

    return {
        "id": category.id,
        "name": category.name,
        "description": category.description
    }

def get_all_categories(db_session):
    categories = db_session.query(Category).all()
    return [
        {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "passRate": 78
        }
        for category in categories
    ]

def get_questions_with_choices_by_category(db_session, category_id):
    questions = db_session.query(Question).filter_by(category_id=category_id).all()

    result = []
    for q in questions:
        answers = db_session.query(Answer).filter_by(question_id=q.id).all()
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
