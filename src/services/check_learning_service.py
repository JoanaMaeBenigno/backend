import uuid
from datetime import datetime
from sqlalchemy import func
from src.models.category_model import Category
from src.models.question_model import Question
from src.models.answer_model import Choices
from src.models.survey_model import Survey
from src.models.question_result_model import QuestionResult
from src.config.extensions import db

def get_single_category(category_id):
    category = db.session.query(Category).filter_by(id=category_id).first()

    return {
        "id": category.id,
        "name": category.name,
        "description": category.description
    }

def __get_passrate(category_id):
    passing_percentage = 50

    takers_count = db.session.query(func.count(QuestionResult.id)).filter(QuestionResult.category_id == category_id).scalar()
    pass_count = db.session.query(func.count(QuestionResult.id)).filter(
        ((QuestionResult.correct_answer / QuestionResult.question_count) * 100) >= passing_percentage,
        QuestionResult.category_id == category_id
    ).scalar()
    if pass_count == 0:
        return 0

    return int(round((pass_count / takers_count) * 100, 0))

def get_all_categories():
    categories = db.session.query(Category).filter_by(is_deleted=False).all()
    return [
        {
            "id": category.id,
            "name": category.name,
            "description": category.description,
            "passRate": __get_passrate(category.id)
        }
        for category in categories
    ]

def create_category_service(data):
    article = Category(
        id=str(uuid.uuid4()),
        created_date=datetime.now(),
        name=data.get('name'),
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

def get_questions_with_choices_by_category(category_id, with_answer):
    questions = db.session.query(Question).filter_by(category_id=category_id, is_deleted=False).all()

    result = []
    for q in questions:
        answers = db.session.query(Choices).filter_by(question_id=q.id).all()
        choices = [
            {
                "id": a.id,
                "answer_text": a.answer_text
            }
            for a in answers
        ]

        to_append = {
            "id": q.id,
            "question_text": q.question_text,
            "choices": choices,
            **({"correct_option": q.correct_option} if with_answer else {})
        }

        result.append(to_append)

    return result

def save_question_with_choices(data):
    category = db.session.query(Category).filter_by(id=data["category_id"], is_deleted=False).first()
    if not category:
        raise ValueError(f"Category ID '{data['category_id']}' does not exist.")

    question_id = str(uuid.uuid4())

    # Set the correct_option UUID now to match one of the generated choices
    choices_data = []
    for choice in data["choices"]:
        choice_id = str(uuid.uuid4())
        choices_data.append({
            "id": choice_id,
            "answer_text": choice["answer_text"]
        })
        # Replace text match with real UUID in correct_option
        if choice["id"] == data["correct_option"]:
            data["correct_option"] = choice_id

    question = Question(
        id=question_id,
        category_id=data["category_id"],
        question_text=data["question_text"],
        correct_option=data["correct_option"],
        is_deleted=False,
        created_date=datetime.now()
    )
    db.session.add(question)

    for choice in choices_data:
        answer = Choices(
            id=choice["id"],
            question_id=question_id,
            answer_text=choice["answer_text"]
        )
        db.session.add(answer)

    db.session.commit()

    return {"id": question_id}

def delete_question_service(id):
    question = Question.query.filter_by(id=id, is_deleted=False).first()

    if question:
        question.is_deleted = True
        db.session.commit()
        return True

    return False

# Survey Related
def save_survey(data):
    category = db.session \
        .query(Category) \
        .filter_by(id=data["category_id"], is_deleted=False) \
        .first()

    if not category:
        raise ValueError(f"Category ID '{data['category_id']}' does not exist.")

    survey_id = str(uuid.uuid4())

    survey = Survey(
        id=survey_id,
        category_id=data["category_id"],
        question_text=data["question_text"],
        is_deleted=False,
        created_date=datetime.now()
    )
    db.session.add(survey)

    db.session.commit()

    return {"id": survey_id}

def get_survey_questions_by_category(category_id):
    survey_questions = db.session \
        .query(Survey.id, Survey.question_text) \
        .filter_by(category_id=category_id, is_deleted=False) \
        .all()

    results = [
        {
            "id": survey.id,
            "question_text": survey.question_text
        }
        for survey in survey_questions
    ]

    return results

def delete_survey_question_service(id):
    survey_question = Survey.query.filter_by(id=id, is_deleted=False).first()

    if survey_question:
        survey_question.is_deleted = True
        db.session.commit()
        return True

    return False
