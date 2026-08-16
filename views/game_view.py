import customtkinter as ctk

class GameDialog(ctk.CTkToplevel):
    def __init__(self, master, controller, game=None, sagas=None):
        super().__init__(master)
        self.controller = controller
        self.game = game
        self.sagas = sagas if sagas else []
        
        title = "Edit Game" if game else "Add New Game"
        self.title(title)
        self.geometry("400x500")
        self.resizable(False, False)
        
        # Make it modal
        self.transient(master)
        self.grab_set()
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        
        # Name
        ctk.CTkLabel(self, text="Name:").grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.entry_name = ctk.CTkEntry(self, width=200)
        self.entry_name.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")
        
        # Release Date
        ctk.CTkLabel(self, text="Release Date:").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.entry_date = ctk.CTkEntry(self, width=200, placeholder_text="YYYY-MM-DD")
        self.entry_date.grid(row=1, column=1, padx=20, pady=10, sticky="w")
        
        # Status
        ctk.CTkLabel(self, text="Status:").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.status_options = ["Not Started", "Playing", "Finished", "Dropped"]
        self.combo_status = ctk.CTkComboBox(self, values=self.status_options, width=200)
        self.combo_status.grid(row=2, column=1, padx=20, pady=10, sticky="w")
        
        # Store
        ctk.CTkLabel(self, text="Store:").grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.entry_store = ctk.CTkEntry(self, width=200)
        self.entry_store.grid(row=3, column=1, padx=20, pady=10, sticky="w")
        
        # Saga
        ctk.CTkLabel(self, text="Saga:").grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.saga_options = ["None"] + [s['name'] for s in self.sagas]
        self.combo_saga = ctk.CTkComboBox(self, values=self.saga_options, width=200)
        self.combo_saga.grid(row=4, column=1, padx=20, pady=10, sticky="w")
        
        # Populate if editing
        if self.game:
            self.entry_name.insert(0, self.game['name'])
            if self.game['release_date']:
                self.entry_date.insert(0, self.game['release_date'])
            if self.game['status']:
                self.combo_status.set(self.game['status'])
            if self.game['store']:
                self.entry_store.insert(0, self.game['store'])
            if self.game['saga_name']:
                self.combo_saga.set(self.game['saga_name'])
        
        # Buttons
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.grid(row=5, column=0, columnspan=2, pady=30)
        
        self.btn_save = ctk.CTkButton(self.btn_frame, text="Save", command=self.save, fg_color="#6200EE", hover_color="#3700B3")
        self.btn_save.grid(row=0, column=0, padx=10)
        
        self.btn_cancel = ctk.CTkButton(self.btn_frame, text="Cancel", command=self.destroy, fg_color="#333333", hover_color="#555555")
        self.btn_cancel.grid(row=0, column=1, padx=10)

    def save(self):
        name = self.entry_name.get().strip()
        release_date = self.entry_date.get().strip()
        status = self.combo_status.get().strip()
        store = self.entry_store.get().strip()
        saga_name = self.combo_saga.get()
        
        if not name:
            return # Simple validation, could add a messagebox
            
        saga_id = None
        if saga_name != "None":
            # Find saga id by name
            for s in self.sagas:
                if s['name'] == saga_name:
                    saga_id = s['id']
                    break
                    
        data = {
            'name': name,
            'release_date': release_date,
            'status': status,
            'store': store,
            'saga_id': saga_id
        }
        
        if self.game:
            self.controller.save_edit_game(self.game['id'], data)
        else:
            self.controller.save_new_game(data)
            
        self.destroy()
