from flask import Blueprint 
from controllers.turma_controller import get_turma, create_turma, update_turma, delete_turma

bp = Blueprint('turma', __name__)

@bp.route('/turmas', methods=['GET'])
def get_turmas_route():
    return get_turmas()

@bp.route('/turmas', methods=['POST'])
def create_turma_route():
    return create_turma()

@bp.route('/turmas/<int:turma_id>', methods=['PUT'])
def get_turma_route(turma_id):
    return update_turma(turma_id)

@bp.route('/turmas/<int:turma_id>', methods=['DELETE'])
def delete_turma_route(turma_id):
    return delete_turma(turma_id)
