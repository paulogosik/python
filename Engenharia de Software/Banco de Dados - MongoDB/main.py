from pymongo import MongoClient


# Conectando com o Atlas e criando uma DB e coleção
cliente = MongoClient("mongodb+srv://paulo:admin@dbteste.3j0hm.mongodb.net/")
db = cliente.get_database("atividade3010")
colecao = db.get_collection("atividade3010")


# Funções: -------------------------
    # Criando a tarefa
def criar_tarefa(titulo: str, descricao: str, data_criacao: str, status: str, tags: list):
    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'data_criacao': data_criacao,
        'status': status,
        'tags': tags
    }

    colecao.insert_one(tarefa)
    print("Tarefa criada com sucesso!")

    # Lendo a tarefa
def ler_tarefas() -> None:
    for tarefa in colecao.find():
        print("Tarefa ------------------------")
        print(f"Título: {tarefa.get('titulo')}\n"
              f"Descrição: {tarefa.get('descricao')}\n"
              f"Data de criação: {tarefa.get('data_criacao')}\n"
              f"Status: {tarefa.get('status')}")
        print("------------------------")


# Funções: -------------------------
criar_tarefa('Terminar atividade', 'Terminar a atividade passada pelo professor no dia 30/10', '30/10/2024',
             'Em andamento', ['Tarefas', 'Banco de Dados'])
# ler_tarefas()
