from myvideogamelist.models.database import get_connection

def get_all_games():
    """Retrieves all games from the database along with their saga names."""
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT games.*, sagas.name as saga_name
        FROM games
        LEFT JOIN sagas ON games.saga_id = sagas.id
        ORDER BY games.name ASC
    '''
    cursor.execute(query)
    games = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return games

def add_game(name, release_date, status, store, saga_id):
    """Adds a new game to the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO games (name, release_date, status, store, saga_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, release_date, status, store, saga_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error adding game: {e}")
        return False
    finally:
        conn.close()

def update_game(game_id, name, release_date, status, store, saga_id):
    """Updates an existing game in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE games
            SET name = ?, release_date = ?, status = ?, store = ?, saga_id = ?
            WHERE id = ?
        ''', (name, release_date, status, store, saga_id, game_id))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating game: {e}")
        return False
    finally:
        conn.close()

def delete_game(game_id):
    """Deletes a game from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM games WHERE id = ?", (game_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting game: {e}")
        return False
    finally:
        conn.close()
