from src.config.extensions import db

class Question(db.Model):
    __tablename__ = 'questions'
    __table_args__ = {'schema': 'thesis'}

    id = db.Column(db.Text, primary_key=True)
    category_id = db.Column(db.Text)
    question_text = db.Column(db.Text)
    correct_option = db.Column(db.Text)
    is_deleted = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime)
