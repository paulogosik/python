from pymongo import MongoClient


# Conectando com o Atlas e criando uma DB e coleção
cliente = MongoClient("mongodb+srv://paulo:admin@dbteste.3j0hm.mongodb.net/")
db = cliente.get_database("atividade3010")
colecao = db.get_collection("atividade3010")


# Funções: -------------------------

def criar_tarefa(id: str, titulo: str, descricao: str, data_criacao: str, status: str, tags: list):
    tarefa = {
        'id': id,
        'titulo': titulo,
        'descricao': descricao,
        'data_criacao': data_criacao,
        'status': status,
        'tags': tags
    }

    colecao.insert_one(tarefa)
    print("Tarefa criada com sucesso!")


def ler_tarefas() -> None:
    for i, tarefa in enumerate(colecao.find()):
        print(f"\nTarefa #{i+1} ------------------------")
        print(f"ID: {tarefa.get('id')}\n"
              f"Título: {tarefa.get('titulo')}\n"
              f"Descrição: {tarefa.get('descricao')}\n"
              f"Data de criação: {tarefa.get('data_criacao')}\n"
              f"Status: {tarefa.get('status')}")
    print("------------------------")
    

def atualizar_tarefa(id: str, campo: str, valores):
    colecao.update_one({'id': id}, {"$set": {campo: valores}})
    print(f"Campo [{campo}] atualizado com sucesso!")


def excluir_tarefa(id: str):
    colecao.delete_one({'id': id})
    print(f"Tarefa de ID {id} excluída com sucesso!")


# Funções: -------------------------
    # Criando tarefas:
criar_tarefa('01', 'Terminar atividade', 'Terminar a atividade passada pelo professor no dia 30/10', '30/10/2024',
             'Em andamento', ['Tarefas', 'Banco de Dados'])
criar_tarefa('02', 'Cortar o cabelo', 'Marcar com o barbeiro e cortar o cabelo', '11/11/2024',
             'Pendente', ['Tarefas', 'Cabelo'])
    
    # Lendo as tarefas:
ler_tarefas()

    # Atualizando as tarefas:
atualizar_tarefa("02", "titulo", "Cabelo")

    # Excluindo as tarefas:
excluir_tarefa("02")
