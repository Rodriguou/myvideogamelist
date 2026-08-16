import customtkinter as ctk
from myvideogamelist.models.database import init_db
from myvideogamelist.views.main_view import MainView
from myvideogamelist.controllers.main_controller import MainController

def main():
    # Initialize the database (creates tables if they don't exist)
    init_db()

    # Configure CustomTkinter Appearance
    ctk.set_appearance_mode("dark")  # Force dark mode
    ctk.set_default_color_theme("dark-blue")  # Using built-in dark-blue as base, but we used custom hex colors for purple accents in views
    
    # Initialize the root window
    root = ctk.CTk()
    root.title("MyVideoGameList - Library Manager")
    root.geometry("900x600")
    root.minsize(800, 500)
    
    # Setup grid for root to allow MainView to expand
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    # Initialize View and Controller
    view = MainView(root, controller=None) # Controller passed later
    view.grid(row=0, column=0, sticky="nsew")
    
    controller = MainController(view)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
