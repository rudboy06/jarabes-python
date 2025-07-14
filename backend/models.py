from db import get_connection

def insertar_jarabe(nombre, ingredientes, descripcion):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO jarabes (nombre, ingredientes, descripcion)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nombre, ingredientes, descripcion))
            connection.commit()
            print("✅ Insert ejecutado")
            return {"mensaje": "Jarabe insertado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()
    else:
        return {"error": "No se pudo conectar a la base de datos"}

def obtener_jarabes():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM jarabes"
            cursor.execute(query)
            resultado = cursor.fetchall()
            return resultado
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()
    else:
        return {"error": "No se pudo conectar a la base de datos"}

def actualizar_jarabe(id, nombre, ingredientes, descripcion):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = """
                UPDATE jarabes
                SET nombre = %s,
                    ingredientes = %s,
                    descripcion = %s
                WHERE id = %s
            """
            cursor.execute(query, (nombre, ingredientes, descripcion, id))
            connection.commit()
            if cursor.rowcount == 0:
                return {"error": "No se encontró jarabe con ese ID"}
            return {"mensaje": "Jarabe actualizado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()
    else:
        return {"error": "No se pudo conectar a la base de datos"}

def eliminar_jarabe(id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM jarabes WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
            if cursor.rowcount == 0:
                return {"error": "No se encontró jarabe con ese ID"}
            return {"mensaje": "Jarabe eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()
    else:
        return {"error": "No se pudo conectar a la base de datos"}
