import uuid
from datetime import datetime
from sqlalchemy import func
from src.models.category_model import Category
from src.models.question_model import Question
from src.models.answer_model import Choices
from src.models.survey_model import Survey
from src.models.question_result_model import QuestionResult
from src.config.extensions import db

def get_check_learning_service():
    passing_percentage = 50
    total_exam = db.session.query(func.count(QuestionResult.id)).scalar()
    pass_count = db.session.query(func.count(QuestionResult.id)).filter(
        ((QuestionResult.correct_answer / QuestionResult.question_count) * 100) >= passing_percentage
    ).scalar()
    sum_answer = db.session.query(func.sum(QuestionResult.correct_answer)).scalar()

    return {
        "total_exam_taken": total_exam,
        "total_passed_exam": pass_count,
        "passing_rate": int(round((pass_count / total_exam) * 100, 0)),
        "average_score": round(sum_answer / total_exam, 2)
    }
