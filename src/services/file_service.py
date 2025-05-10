import uuid
from datetime import datetime
from src.models.file_model import Files
from src.config.extensions import db

def get_single_file_service(file_id):
  file = db.session.query(Files).filter_by(id=file_id, is_deleted=False).first()
  if file is None:
    return None

  return {
    "id": file.id,
    "title": file.title,
    "description": file.description,
    "file_url": file.file_url,
    "created_date": file.created_date
  }

def get_files_by_type_service(type):
    files = db.session.query(Files).filter_by(is_deleted=False, type=type).all()

    return [
        {
          "id": file.id,
          "title": file.title,
          "file_url": file.file_url,
          "description": file.description,
          "created_date": file.created_date
        }
        for file in files
    ]

def create_file_service(data, type):
    article = Files(
        id=str(uuid.uuid4()),
        title=data.get('title'),
        description=data.get('description'),
        file_url=data.get('file_url'),
        type=type,
        created_date=datetime.now(),
        is_deleted=False
    )
    db.session.add(article)
    db.session.commit()

    return article

def delete_file_service(id):
    files = Files.query.filter_by(id=id, is_deleted=False).first()

    if files:
      files.is_deleted = True
      db.session.commit()
      return True

    return False
