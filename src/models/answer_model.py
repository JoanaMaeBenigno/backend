from src.config.extensions import db

class Answer(db.Model):
    __tablename__ = 'answers'
    __table_args__ = {'schema': 'thesis'}

    id = db.Column(db.Text, primary_key=True)
    answer_text = db.Column(db.Text)
    question_id = db.Column(db.Text)
