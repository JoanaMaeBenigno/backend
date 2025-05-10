from src.config.extensions import db

class Files(db.Model):
    __tablename__ = 'files'
    __table_args__ = {'schema': 'thesis'}

    id = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    type = db.Column(db.Text)
    file_url = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean, default = False)
