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

# Exemplo 1 ---------------------------
print("\nExemplo 1 ===========================")
query = "SELECT * FROM Noticia"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
    
# Exemplo 2 ----------------------
print("\nExemplo 2 ===========================")
query = "SELECT codigo, titulo FROM Noticia WHERE codigo = ? OR codigo = ?"
codigos_noticia = (1, 3)
cursor.execute(query, codigos_noticia)

results = cursor.fetchall()
for row in results:
    print(row.codigo, row.titulo)
 
# Fechando o banco -----------------------
cursor.close()
conn.close()
