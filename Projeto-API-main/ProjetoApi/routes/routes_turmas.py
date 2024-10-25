# Turmas routes
bp.route('/turmas', methods=['GET'])(get_turmas)
bp.route('/turmas', methods=['POST'])(create_turma)
bp.route('/turmas/<int:turma_id>', methods=['GET'])(get_turma)