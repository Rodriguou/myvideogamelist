from myvideogamelist.models.database import get_connection

def get_all_sagas():
    """Retrieves all sagas from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sagas ORDER BY name ASC")
    sagas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return sagas

def add_saga(name):
    """Adds a new saga to the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO sagas (name) VALUES (?)", (name,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding saga: {e}")
        return False
    finally:
        conn.close()

def update_saga(saga_id, new_name):
    """Updates the name of an existing saga."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE sagas SET name = ? WHERE id = ?", (new_name, saga_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating saga: {e}")
        return False
    finally:
        conn.close()

def delete_saga(saga_id):
    """Deletes a saga from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM sagas WHERE id = ?", (saga_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting saga: {e}")
        return False
    finally:
        conn.close()
