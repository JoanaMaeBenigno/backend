import uuid
from datetime import datetime
from sqlalchemy import func
from src.models.question_result_model import QuestionResult, QuestionResultAudit
from src.models.question_model import Question
from src.models.category_model import Category
from src.config.extensions import db

def get_category_average(user_average: float, category_id: str):
  count_all = db.session.query(func.count(QuestionResult.id)).filter_by(category_id=category_id).scalar()
  filter_count = db.session.query(func.count(QuestionResult.id)).filter(
    user_average > (QuestionResult.correct_answer / QuestionResult.question_count),
    QuestionResult.category_id == category_id
  ).scalar()

  percentage_higher = (filter_count / count_all) * 100

  return percentage_higher

def post_question_result_service(data):
  category_id = data.get('category_id')
  answers = data.get('answers')

  category = db.session.query(Category).filter_by(id=category_id, is_deleted=False).first()
  if category is None:
    return None

  correct_answer = 0
  result_id = str(uuid.uuid4())

  for user_question_id, user_answer_id in answers.items():
    question = db.session.query(Question).filter_by(category_id=category_id, id=user_question_id).first()
    is_correct = False
    if (question.correct_option == user_answer_id):
      correct_answer = correct_answer + 1
      is_correct = True

    question_result_audit = QuestionResultAudit(
      id = str(uuid.uuid4()),
      result_id = result_id,
      question_id = user_question_id,
      answer_id = user_answer_id,
      is_correct = is_correct,
      created_date = datetime.now()
    )

    db.session.add(question_result_audit)
    db.session.commit()

  question_count = len(answers)
  question_result = QuestionResult(
    id = result_id,
    category_id = category_id,
    question_count = question_count,
    correct_answer = correct_answer,
    higher_percentage = get_category_average(correct_answer / question_count, category_id),
    created_date = datetime.now()
  )

  db.session.add(question_result)
  db.session.commit()

  return {
    "id": question_result.id
  }

def get_result_service(question_result_id):
  question = db.session.query(QuestionResult).filter_by(id=question_result_id).first()
  category = db.session.query(Category).filter_by(id=question.category_id).first()

  if question is None:
    return None

  return {
    'question_count': question.question_count,
    'correct_count': question.correct_answer,
    'category_name': category.name,
    'percentage': "{:.0f}".format((question.correct_answer / question.question_count) * 100),
    'higher_percentage': "{:.0f}".format(question.higher_percentage),
    'created_date': question.created_date
  }
