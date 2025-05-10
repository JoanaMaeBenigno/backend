from flask import Blueprint, request, jsonify
from src.services.file_service import create_file_service, \
  get_files_by_type_service, \
  get_single_file_service, \
  delete_file_service

file_blueprint = Blueprint('file', __name__, url_prefix='/file')

WORKSHEET = 'WORKSHEET'
LESSON = 'LESSON'

# Common related
@file_blueprint.route('/common/<id>', methods=['GET'])
def get_file(id):
  try:
    data = get_single_file_service(id)

    if data is None:
      return jsonify({
        "status": "error",
        "message": "File not found",
        "data": data
      }), 404

    return jsonify({
        "status": "success",
        "message": "File fetched successfully",
        "data": data
    })
  except Exception as e:
    return jsonify({
      "status": "error",
      "message": str(e),
      "data": None
    }), 500

@file_blueprint.route('/common/<id>', methods=['DELETE'])
def delete_file(id):
  try:
    result = delete_file_service(id)

    if result:
      return jsonify({
        "status": "success",
        "message": "File soft-deleted successfully",
        "data": {"id": id}
      })
    else:
      return jsonify({
        "status": "error",
        "message": "File not found or already deleted",
        "data": None
      }), 404
  except Exception as e:
      return jsonify({
        "status": "error",
        "message": str(e),
        "data": None
      }), 500

# Worksheet related
@file_blueprint.route('/worksheet', methods=['GET'])
def get_worksheets():
  try:
    data = get_files_by_type_service(WORKSHEET)

    return jsonify({
      "status": "success",
      "message": "Worksheet fetched successfully",
      "data": data
    })

  except Exception as e:
    return jsonify({
      "status": "error",
      "message": str(e),
      "data": None
    }), 500

@file_blueprint.route('/worksheet', methods=['POST'])
def create_worksheet():
  data = request.get_json()

  try:
    data = request.get_json()
    worksheet = create_file_service(data, WORKSHEET)

    return jsonify({
      "status": "success",
      "message": "Worksheet created successfully",
      "data": {
        "id": worksheet.id
      }
    }), 201

  except Exception as e:
    return jsonify({
      "status": "error",
      "message": str(e),
      "data": None
    }), 500

# Lesson related
@file_blueprint.route('/lesson', methods=['GET'])
def get_lessons():
  try:
    data = get_files_by_type_service(LESSON)

    return jsonify({
      "status": "success",
      "message": "Worksheet fetched successfully",
      "data": data
    })

  except Exception as e:
    return jsonify({
      "status": "error",
      "message": str(e),
      "data": None
    }), 500

@file_blueprint.route('/lesson', methods=['POST'])
def create_lesson():
  data = request.get_json()

  try:
    data = request.get_json()
    lesson = create_file_service(data, LESSON)

    return jsonify({
      "status": "success",
      "message": "Lesson created successfully",
      "data": {
        "id": lesson.id
      }
    }), 201

  except Exception as e:
    return jsonify({
      "status": "error",
      "message": str(e),
      "data": None
    }), 500
