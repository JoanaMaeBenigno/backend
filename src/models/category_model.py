from src.config.extensions import db

class Category(db.Model):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'thesis'}

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
