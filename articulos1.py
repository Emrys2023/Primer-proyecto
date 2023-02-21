import sqlite3

conexion=sqlite3.connect("basedato1.db")

try:
    conexion.execute("""create table Articulos(
                        codigo integer primary key autoincrement,
                        descripcion text,
                        precio real    
                    );""")

    print("Se creo la tabla")

except sqlite3.OperationalError:
    print("No se creo la tabla, puede ser que ya exista.")

conexion.close()