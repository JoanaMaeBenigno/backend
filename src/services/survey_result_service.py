import uuid
from datetime import datetime
from src.models.survey_result_model import SurveyResult, SurveyResultAudit
from src.models.category_model import Category
from src.config.extensions import db

def post_survey_result_service(data):
  category_id = data.get('category_id')
  answers = data.get('answers')

  category = db.session.query(Category).filter_by(id=category_id, is_deleted=False).first()
  if category is None:
    return None

  result_id = str(uuid.uuid4())

  for user_survey_id, user_answer in answers.items():
    survey_result_audit = SurveyResultAudit(
      id = str(uuid.uuid4()),
      result_id = result_id,
      survey_id = user_survey_id,
      answer = user_answer,
      created_date = datetime.now()
    )

    db.session.add(survey_result_audit)
    db.session.commit()

  survey_count = len(answers)
  survey_result = SurveyResult(
    id = result_id,
    category_id = category_id,
    average = sum(answers.values()) / survey_count,
    created_date = datetime.now()
  )

  db.session.add(survey_result)
  db.session.commit()

  return {
    "id": survey_result.id
  }

def get_result_service(survey_result_id):
  survey = db.session.query(SurveyResult).filter_by(id=survey_result_id).first()
  category = db.session.query(Category).filter_by(id=survey.category_id).first()

  if survey is None:
    return None

  return {
    'category_name': category.name,
    'average': "{:.2f}".format(survey.average),
    'created_date': survey.created_date
  }
