from pymongo import MongoClient

# Conectando com o Atlas e criando uma DB e coleção
cliente = MongoClient("mongodb+srv://paulo:admin@dbteste.3j0hm.mongodb.net/")
db = cliente.get_database("atividade3010")
colecao = db.get_collection("atividade3010")


# Criando a tarefa =======================
# tarefa = {
#     'titulo': 'Fazer a atividade',
#     'descricao': 'Terminar a atividade iniciada no dia 30/10',
#     'data_criacao': '30/10/2024',
#     'status': 'Em Andamento',
#     'tags': ['Tarefas', 'Faculdade']
# }

# colecao.insert_one(tarefa)


# Lendo a tarefa =======================
for tarefa in colecao.find():
    print("Tarefa ------------------------")
    print(f"Título: {tarefa.get('titulo')}\n"
          f"Descrição: {tarefa.get('descricao')}\n"
          f"Data de criação: {tarefa.get('data_criacao')}\n"
          f"Status: {tarefa.get('status')}")
    print("------------------------")
    
