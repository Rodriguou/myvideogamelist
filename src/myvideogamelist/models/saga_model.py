from myvideogamelist.models.database import get_db_connection

def get_all_sagas():
    """Retrieves all sagas from the database."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM sagas ORDER BY name ASC")
        sagas = [dict(row) for row in cursor.fetchall()]
        return sagas

def add_saga(name):
    """Adds a new saga to the database."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sagas (name) VALUES (?)", (name,))
            conn.commit()
            return True
    except Exception as e:
        print(f"Error adding saga: {e}")
        return False

def update_saga(saga_id, new_name):
    """Updates the name of an existing saga."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE sagas SET name = ? WHERE id = ?", (new_name, saga_id))
            conn.commit()
            return True
    except Exception as e:
        print(f"Error updating saga: {e}")
        return False

def delete_saga(saga_id):
    """Deletes a saga from the database."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM sagas WHERE id = ?", (saga_id,))
            conn.commit()
            return True
    except Exception as e:
        print(f"Error deleting saga: {e}")
        return False
