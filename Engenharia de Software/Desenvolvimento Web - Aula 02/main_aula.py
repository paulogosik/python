import pyodbc

# String de conexão -----------------------------
conn_str = (
    r"Driver={SQL Server};"
    r"Server=PMW-L04N57767J\SQLEXPRESS;"
    r"Database=aula11_09;"
    r"UID=sa;"
    r"PWD=1234;"
)

# Conectando no banco --------------------------
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Questão 1 -----------------------------
print(f"Printando a View =======================")
query = "SELECT * from consulta_noticia_mundo"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
    
# Questão 2 -----------------------------
print(f"\nPrintando a procedure =======================")
query = "EXEC consulta_categoria ?"
categoria = 1
cursor.execute(query, categoria)
results = cursor.fetchall()
for row in results:
    print(row)
    
# Questão 3 -----------------------------
print(f"\nINSERT na tabela =======================")
query = '''INSERT INTO Categoria(titulo) 
        VALUES (?)'''
titulo = "Esportes"
cursor.execute(query, titulo)
conn.commit()
# results = cursor.fetchall()
# for row in results:
#     print(row)
print("INSERT com sucesso!")
query = "SELECT * FROM Categoria"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)

# Questão 4 -----------------------------
print(f"\nUPDATE na tabela =======================")
query = '''UPDATE Categoria
        SET titulo = 'E-sports'
        WHERE titulo = ?
        '''
titulo = "Esportes"
cursor.execute(query, titulo)
conn.commit()
# results = cursor.fetchall()
# for row in results:
#     print(row)
print("UPDATE com sucesso!")
query = "SELECT * FROM Categoria"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)


# Questão 5 -----------------------------
print(f"\nDELETE na tabela =======================")
query = "DELETE FROM Categoria WHERE titulo = ?"
titulo = "E-sports"
cursor.execute(query, titulo)
conn.commit()
# results = cursor.fetchall()
# for row in results:
#     print(row)
print("DELETE com sucesso!")
query = "SELECT * FROM Categoria"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)



# Fechando o banco -----------------------
cursor.close()
conn.close()# Questão 1 -----------------------------
print(f"Printando a View =======================")
query = "SELECT * from consulta_noticia_mundo"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
    
# Questão 2 -----------------------------
print(f"\nPrintando a procedure =======================")
query = "EXEC consulta_categoria ?"
categoria = 1
cursor.execute(query, categoria)
results = cursor.fetchall()
for row in results:
    print(row)
    
# Questão 3 -----------------------------
print(f"\nINSERT na tabela =======================")
query = '''INSERT INTO Categoria(titulo) 
        VALUES (?)'''
titulo = "Esportes"
cursor.execute(query, titulo)
conn.commit()
# results = cursor.fetchall()
# for row in results:
#     print(row)
print("INSERT com sucesso!")
query = "SELECT * FROM Categoria"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)

# Questão 4 -----------------------------
print(f"\nUPDATE na tabela =======================")
query = '''UPDATE Categoria
        SET titulo = 'E-sports'
        WHERE titulo = ?
        '''
titulo = "Esportes"
cursor.execute(query, titulo)
conn.commit()
# results = cursor.fetchall()
# for row in results:
#     print(row)
print("UPDATE com sucesso!")
query = "SELECT * FROM Categoria"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)


# Questão 5 -----------------------------
print(f"\nDELETE na tabela =======================")
query = "DELETE FROM Categoria WHERE titulo = ?"
titulo = "E-sports"
cursor.execute(query, titulo)
conn.commit()
# results = cursor.fetchall()
# for row in results:
#     print(row)
print("DELETE com sucesso!")
query = "SELECT * FROM Categoria"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)



# Fechando o banco -----------------------
cursor.close()
conn.close()
