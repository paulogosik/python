import pyodbc

# String de conexão -----------------------------
conn_str = (
    r"Driver={SQL Server};"
    r"Server=PMW-L04N577820\SQLEXPRESS;"
    r"Database=empresa;"
    r"UID=sa;"
    r"PWD=1234;"
)


# Criando funções das questões ---------------------------
def novo_departamento(nome):
    query = '''INSERT INTO departamentos(nome) 
            VALUES (?)'''
    cursor.execute(query, nome)
    conn.commit()
    print("\nNovo departamento criado!")
    
    
def novo_funcionario(nome, cargo, salario, departamento_id):
    query = '''INSERT INTO funcionarios(nome, cargo, salario, departamento_id) 
            VALUES (?, ?, ?, ?)'''
    info = (nome, cargo, salario, departamento_id)
    cursor.execute(query, info)
    conn.commit()
    print("\nNovo funcionário criado e adicionado ao departamento!")
    

def novo_projeto(nome):
    query = '''INSERT INTO projetos(nome) 
            VALUES (?)'''
    cursor.execute(query, nome)
    conn.commit()
    print("\nNovo projeto criado!")
    

def get_id_funcionario(nome):
    query = "SELECT id FROM funcionarios WHERE nome = ?"
    cursor.execute(query, nome)
    results = cursor.fetchall()
    for row in results:
        return row[0]
    

def get_id_projeto(nome):
    query = "SELECT id FROM projetos WHERE nome = ?"
    cursor.execute(query, nome)
    results = cursor.fetchall()
    for row in results:
        return row[0]
    

def associar_funcionario_projeto(nome_funcionario, nome_projeto):
    funcionario_id = get_id_funcionario(nome_funcionario)
    projeto_id = get_id_projeto(nome_projeto)
    query = '''INSERT INTO funcionarios_projetos(funcionario_id, projeto_id) 
            VALUES (?, ?)'''
    info = (funcionario_id, projeto_id)
    cursor.execute(query, info)
    conn.commit()
    print("\nFuncionário associado ao projeto com sucesso!")
    
    
def atualizar_salario(novo_salario, nome_funcionario):
    funcionario_id = get_id_funcionario(nome_funcionario)
    query = '''UPDATE funcionarios SET salario = ? WHERE id = ?'''
    info = (novo_salario, funcionario_id)
    cursor.execute(query, info)
    conn.commit()
    print("\nSalário do funcionário atualizado!")
    

def excluir_funcionario(id_funcionario):
    query = '''DELETE FROM funcionarios WHERE id = ?'''
    cursor.execute(query, id_funcionario)
    conn.commit()
    print("\nFuncionário excluído com sucesso!")
    
    
def consultar_funcionarios_departamentos():
    print("\nTodos os funcionários e seus departamentos: ")
    query = '''SELECT
	            F.nome 'Nome Funcionário',
	            F.cargo 'Cargo',
	            F.salario 'Salário',
	            D.nome 'Nome Departamento'
            FROM funcionarios F
            JOIN departamentos D ON F.departamento_id = D.id'''
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
        

def consultar_funcionarios_projetos():
    print("\nTodos os funcionários e seus projetos: ")
    query = '''SELECT
                P.nome 'Nome Projeto',
                F.nome 'Nome Funcionário',
                F.cargo 'Cargo'
            FROM funcionarios_projetos FP
            JOIN funcionarios F ON FP.funcionario_id = F.id
            JOIN projetos P ON FP.funcionario_id = P.id'''
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
        
        
def view_funcionarios_departamentos():
    query = "SELECT * FROM view_funcionarios_departamentos"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

# Conectando no banco --------------------------
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


# Programa principal ------------------------
    # novo_departamento("T.I.")
    # novo_funcionario("Teste", "Desenvolvedor Backend", 15000.0, 1)
    # novo_projeto("Desenvolvimento Login")
    # associar_funcionario_projeto("Paulo Moita", "Desenvolvimento Login")
    # atualizar_salario(16000.0, "Paulo Moita")
    # excluir_funcionario(4)
    # consultar_funcionarios_departamentos()
    # consultar_funcionarios_projetos()
view_funcionarios_departamentos()


# Fechando o banco -----------------------
cursor.close()
conn.close()
