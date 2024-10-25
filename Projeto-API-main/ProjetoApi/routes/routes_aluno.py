from flask import Blueprint
from controllers.aluno_controller import get_alunos, create_aluno, update_aluno, delete_aluno

# Criação do Blueprint
bp = Blueprint('alunos', __name__)

# Alunos routes
@bp.route('/alunos', methods=['GET'])
def get_alunos_route():
    return get_alunos()

@bp.route('/alunos', methods=['POST'])
def create_aluno_route():
    return create_aluno()

@bp.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno_route(aluno_id):
    return update_aluno(aluno_id)

@bp.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno_route(aluno_id):
    return delete_aluno(aluno_id)
