atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app de todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]

class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    return atividades

def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound(f'Atividade com ID {id_atividade} não encontrada.')

def criar_atividade(dados):
    nova_atividade = {
        'id_atividade': len(atividades) + 1,
        'id_disciplina': dados['id_disciplina'],
        'enunciado': dados['enunciado'],
        'respostas': dados.get('respostar', [])
    }
    atividades.append(nova_atividade)
    return nova_atividade

def atualizar_atividade(id_atividade, dados):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            atividade['id_disciplina'] = dados.get("id_disciplina", atividade['id_disciplina'])
            atividade['enunciado'] = dados.get("enunciado", atividade['enunciado'])
            atividade['respostas'] = dados.get("respostas", atividade['respostas'])
            return atividade
        raise AtividadeNotFound(f"Atividade com ID {id_atividade} não encontrada.")

def excluir_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            atividades.remove(atividade)
            return
    raise AtividadeNotFound(f"Atividade com ID {id_atividade} não encontrada.")