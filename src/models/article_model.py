from src.config.extensions import db

class Article(db.Model):
    __tablename__ = 'articles'
    __table_args__ = {'schema': 'thesis'}

    uuid = db.Column(db.Text, primary_key=True)
    posted_date = db.Column(db.Date)
    title = db.Column(db.Text)
    thumbnail_image = db.Column(db.Text)
    subtitle = db.Column(db.Text)
    author = db.Column(db.Text)
    content = db.Column(db.Text)