import customtkinter as ctk
from tkinter import ttk

class MainView(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        
        # Configure grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Top Bar (Title & Actions)
        self.top_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.top_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")
        self.top_frame.grid_columnconfigure(0, weight=1)
        
        self.title_label = ctk.CTkLabel(self.top_frame, text="My Video Game List", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.grid(row=0, column=0, sticky="w")
        
        self.btn_add_game = ctk.CTkButton(self.top_frame, text="Add Game", command=lambda: self.controller.open_add_game_dialog(), fg_color="#6200EE", hover_color="#3700B3")
        self.btn_add_game.grid(row=0, column=1, padx=(10, 0))
        
        self.btn_manage_sagas = ctk.CTkButton(self.top_frame, text="Manage Sagas", command=lambda: self.controller.open_manage_sagas_dialog(), fg_color="#333333", hover_color="#555555")
        self.btn_manage_sagas.grid(row=0, column=2, padx=(10, 0))
        
        # Search Bar
        self.search_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Search games...", width=200)
        self.search_entry.grid(row=0, column=3, padx=(20, 0))
        self.search_entry.bind("<KeyRelease>", lambda event: self.controller.search_games(self.search_entry.get()))
        
        # Game List (Treeview styling for dark mode)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="#1E1E1E",
                        foreground="white",
                        rowheight=30,
                        fieldbackground="#1E1E1E",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#6200EE')])
        style.configure("Treeview.Heading",
                        background="#333333",
                        foreground="white",
                        relief="flat",
                        font=("Arial", 10, "bold"))
        style.map("Treeview.Heading", background=[('active', '#555555')])

        # Treeview frame
        self.tree_frame = ctk.CTkFrame(self)
        self.tree_frame.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="nsew")
        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        columns = ("id", "name", "release_date", "status", "store", "saga")
        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings", selectmode="browse")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Name", command=lambda: self.controller.sort_games("name"))
        self.tree.heading("release_date", text="Release Date", command=lambda: self.controller.sort_games("release_date"))
        self.tree.heading("status", text="Status")
        self.tree.heading("store", text="Store")
        self.tree.heading("saga", text="Saga")
        
        self.tree.column("id", width=50, stretch=False)
        self.tree.column("name", width=200)
        self.tree.column("release_date", width=100, stretch=False)
        self.tree.column("status", width=120, stretch=False)
        self.tree.column("store", width=120, stretch=False)
        self.tree.column("saga", width=150)
        
        self.tree.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Bottom Actions
        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        
        self.btn_edit_game = ctk.CTkButton(self.bottom_frame, text="Edit Selected", command=lambda: self.controller.open_edit_game_dialog())
        self.btn_edit_game.grid(row=0, column=0, padx=(0, 10))
        
        self.btn_delete_game = ctk.CTkButton(self.bottom_frame, text="Delete Selected", command=lambda: self.controller.delete_selected_game(), fg_color="#CF6679", hover_color="#A94442", text_color="black")
        self.btn_delete_game.grid(row=0, column=1)

    def populate_games(self, games):
        """Clears the tree and populates it with games."""
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        for game in games:
            self.tree.insert("", "end", values=(
                game['id'],
                game['name'],
                game['release_date'],
                game['status'],
                game['store'],
                game['saga_name'] if game['saga_name'] else "None"
            ))

    def get_selected_game_id(self):
        """Returns the ID of the selected game, or None if no selection."""
        selected_item = self.tree.selection()
        if selected_item:
            return self.tree.item(selected_item[0])['values'][0]
        return None
