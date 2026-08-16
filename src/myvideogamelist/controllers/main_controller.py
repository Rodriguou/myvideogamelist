from myvideogamelist.models import game_model, saga_model
from myvideogamelist.views.game_view import GameDialog
from myvideogamelist.views.saga_view import SagaDialog

class MainController:
    def __init__(self, view):
        self.view = view
        self.view.controller = self
        self.sort_column = "name"
        self.sort_reverse = False
        self.refresh_main_view()
        
    def refresh_main_view(self):
        """Fetches games from DB, applies search and sorting, then updates the view."""
        games = game_model.get_all_games()
        
        # Apply Search Filter
        if hasattr(self.view, 'search_entry'):
            query = self.view.search_entry.get().strip().lower()
            if query:
                games = [g for g in games if query in g['name'].lower()]
                
        # Apply Sorting
        def sort_key(game):
            val = game.get(self.sort_column)
            return (val is None, val if val is not None else "")
            
        games.sort(key=sort_key, reverse=self.sort_reverse)
        self.view.populate_games(games)

    def search_games(self, query):
        self.refresh_main_view()
        
    def sort_games(self, column):
        if self.sort_column == column:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_column = column
            self.sort_reverse = False
        self.refresh_main_view()

    def get_all_sagas(self):
        return saga_model.get_all_sagas()

    # --- Game Actions ---
    def open_add_game_dialog(self):
        sagas = self.get_all_sagas()
        dialog = GameDialog(self.view, self, sagas=sagas)
        
    def open_edit_game_dialog(self):
        game_id = self.view.get_selected_game_id()
        if not game_id: return
        
        # Find game details
        games = game_model.get_all_games()
        game_to_edit = next((g for g in games if g['id'] == game_id), None)
        
        if game_to_edit:
            sagas = self.get_all_sagas()
            dialog = GameDialog(self.view, self, game=game_to_edit, sagas=sagas)

    def save_new_game(self, data):
        game_model.add_game(
            data['name'], 
            data['release_date'], 
            data['status'], 
            data['store'], 
            data['saga_id']
        )
        self.refresh_main_view()
        
    def save_edit_game(self, game_id, data):
        game_model.update_game(
            game_id,
            data['name'], 
            data['release_date'], 
            data['status'], 
            data['store'], 
            data['saga_id']
        )
        self.refresh_main_view()
        
    def delete_selected_game(self):
        game_id = self.view.get_selected_game_id()
        if game_id:
            game_model.delete_game(game_id)
            self.refresh_main_view()

    # --- Saga Actions ---
    def open_manage_sagas_dialog(self):
        sagas = self.get_all_sagas()
        dialog = SagaDialog(self.view, self, sagas=sagas)
        
    def save_new_saga(self, name):
        result = saga_model.add_saga(name)
        # Sagas might affect game view if we wanted, but not needed on add.
        return result
        
    def save_edit_saga(self, saga_id, new_name):
        result = saga_model.update_saga(saga_id, new_name)
        self.refresh_main_view() # Update treeview as saga names might have changed
        return result
        
    def delete_saga(self, saga_id):
        result = saga_model.delete_saga(saga_id)
        self.refresh_main_view() # Update treeview as games might now have NULL sagas
        return result
