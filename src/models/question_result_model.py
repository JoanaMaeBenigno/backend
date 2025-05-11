from src.config.extensions import db

class QuestionResult(db.Model):
  __tablename__ = 'question_result'
  __table_args__ = {'schema': 'thesis'}

  id = db.Column(db.Text, primary_key=True)
  category_id = db.Column(db.Text)
  question_count = db.Column(db.Integer)
  correct_answer = db.Column(db.Integer)
  higher_percentage = db.Column(db.Double)
  created_date = db.Column(db.DateTime)

class QuestionResultAudit(db.Model):
  __tablename__ = 'question_result_audit'
  __table_args__ = {'schema': 'thesis'}

  id = db.Column(db.Text, primary_key=True)
  result_id = db.Column(db.Text)
  question_id = db.Column(db.Text)
  answer_id = db.Column(db.Text)
  is_correct = db.Column(db.Boolean)
  created_date = db.Column(db.DateTime)
