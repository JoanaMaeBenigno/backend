from src.config.extensions import db

class Question(db.Model):
    __tablename__ = 'multiple_choice_questions'
    __table_args__ = {'schema': 'thesis'}

    id = db.Column(db.Text, primary_key=True)
    category_id = db.Column(db.Text)
    question_text = db.Column(db.Text)
    correct_option = db.Column(db.Text)
