from src.config.extensions import db

class SurveyResult(db.Model):
  __tablename__ = 'survey_result'
  __table_args__ = {'schema': 'thesis'}

  id = db.Column(db.Text, primary_key=True)
  category_id = db.Column(db.Text)
  average = db.Column(db.Integer)
  created_date = db.Column(db.DateTime)

class SurveyResultAudit(db.Model):
  __tablename__ = 'survey_result_audit'
  __table_args__ = {'schema': 'thesis'}

  id = db.Column(db.Text, primary_key=True)
  result_id = db.Column(db.Text)
  survey_id = db.Column(db.Text)
  answer = db.Column(db.Text)
  created_date = db.Column(db.DateTime)
