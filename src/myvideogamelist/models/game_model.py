from myvideogamelist.models.database import get_db_connection

def get_all_games():
    """Retrieves all games from the database along with their saga names."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = '''
            SELECT games.*, sagas.name as saga_name
            FROM games
            LEFT JOIN sagas ON games.saga_id = sagas.id
            ORDER BY games.name ASC
        '''
        cursor.execute(query)
        games = [dict(row) for row in cursor.fetchall()]
        return games

def add_game(name, release_date, status, store, saga_id):
    """Adds a new game to the database."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO games (name, release_date, status, store, saga_id)
                VALUES (?, ?, ?, ?, ?)
            ''', (name, release_date, status, store, saga_id))
            conn.commit()
            return True
    except Exception as e:
        print(f"Error adding game: {e}")
        return False

def update_game(game_id, name, release_date, status, store, saga_id):
    """Updates an existing game in the database."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
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

def delete_game(game_id):
    """Deletes a game from the database."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM games WHERE id = ?", (game_id,))
            conn.commit()
            return True
    except Exception as e:
        print(f"Error deleting game: {e}")
        return False
