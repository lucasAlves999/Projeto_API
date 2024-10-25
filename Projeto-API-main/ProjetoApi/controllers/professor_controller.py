from flask import jsonify, request
from models.professor import professores

def get_professores():
    return jsonify({'professores': professores})

def create_professor():
    data = request.json
    professor = {
        'id': len(professores) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'materia': data['materia'],
        'observacao': data['observacao']
    }
    professores.append(professor)
    return jsonify(professor), 201

def get_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            return jsonify(professor)
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404


def update_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            data = request.json
            professor['nome'] = data.get('nome', professor['nome'])
            professor['idade']= data.get('idade', professor['idade'])
            professor['materia']= data.get('materia', professor['materia'])
            professor['observacao']= data.get('observacao', professor['observacao'])
            return jsonify(professor)
    return jsonify({'mensagem': 'professor não encontrado'}), 404    

def delete_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            professor.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404