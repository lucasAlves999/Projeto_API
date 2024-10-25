from flask import Blueprint 
from controllers.professor_controller import get_professor, create_professor, update_professor , delete_professor

bp = Blueprint('professor', __name__)

@bp.route('/professor', methods=['GET'])
def get_professor_route():
    return get_professor()

@bp.route('/professor', methods=['POST'])
def create_professor_route():
    return create_professor()

@bp.route('/professor/<int:professor_id>', methods=['PUT'])
def update_professor_route(professor_id):
    return update_professor(professor_id)

@bp.route('/professor/<int:professor_id>', methods=['DELETE'])
def delete_professor_route(professor_id):
    return delete_professor(professor_id)
