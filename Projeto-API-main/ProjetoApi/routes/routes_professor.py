# Professores routes
bp.route('/professores', methods=['GET'])(get_professores)
bp.route('/professores', methods=['POST'])(create_professor)
bp.route('/professores/<int:professor_id>', methods=['GET'])(get_professor)
