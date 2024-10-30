from pymongo import MongoClient

# Conectando com o Atlas e criando uma DB e coleção
cliente = MongoClient("mongodb+srv://paulo:admin@dbteste.3j0hm.mongodb.net/")
db = cliente.get_database("atividade3010")
colecao = db.get_collection("atividade")

tarefa = {
    'titulo': 'Fazer a atividade',
    'descricao': 'Terminar a atividade iniciada no dia 30/10',
    'data_criacao': '30/10/2024',
    'status': 'Em Andamento',
    'tags': ['Tarefas', 'Faculdade']
}
