import customtkinter as ctk

class SagaDialog(ctk.CTkToplevel):
    def __init__(self, master, controller, sagas):
        super().__init__(master)
        self.controller = controller
        self.sagas = sagas
        
        self.title("Manage Sagas")
        self.geometry("400x500")
        self.resizable(False, False)
        
        self.transient(master)
        self.grab_set()
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Add Saga Frame
        self.add_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.add_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.add_frame.grid_columnconfigure(0, weight=1)
        
        self.entry_new_saga = ctk.CTkEntry(self.add_frame, placeholder_text="New Saga Name")
        self.entry_new_saga.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        
        self.btn_add_saga = ctk.CTkButton(self.add_frame, text="Add", command=self.add_saga, width=60, fg_color="#6200EE", hover_color="#3700B3")
        self.btn_add_saga.grid(row=0, column=1)
        
        # List of Sagas
        self.list_frame = ctk.CTkScrollableFrame(self)
        self.list_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.list_frame.grid_columnconfigure(0, weight=1)
        
        self.radio_var = ctk.IntVar(value=-1)
        self.radio_buttons = []
        
        self.populate_sagas()
        
        # Actions Frame
        self.action_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.action_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        
        self.btn_edit = ctk.CTkButton(self.action_frame, text="Edit Selected", command=self.edit_saga)
        self.btn_edit.grid(row=0, column=0, padx=(0, 10))
        
        self.btn_delete = ctk.CTkButton(self.action_frame, text="Delete Selected", command=self.delete_saga, fg_color="#CF6679", hover_color="#A94442", text_color="black")
        self.btn_delete.grid(row=0, column=1)

    def populate_sagas(self):
        for rb in self.radio_buttons:
            rb.destroy()
        self.radio_buttons.clear()
        
        for i, saga in enumerate(self.sagas):
            rb = ctk.CTkRadioButton(self.list_frame, text=saga['name'], variable=self.radio_var, value=saga['id'])
            rb.grid(row=i, column=0, pady=5, sticky="w")
            self.radio_buttons.append(rb)
            
    def add_saga(self):
        name = self.entry_new_saga.get().strip()
        if name:
            if self.controller.save_new_saga(name):
                self.entry_new_saga.delete(0, "end")
                self.sagas = self.controller.get_all_sagas()
                self.populate_sagas()
                
    def edit_saga(self):
        selected_id = self.radio_var.get()
        if selected_id == -1: return
        
        # Simple prompt for new name
        dialog = ctk.CTkInputDialog(text="Enter new name for the saga:", title="Edit Saga")
        new_name = dialog.get_input()
        
        if new_name and new_name.strip():
            if self.controller.save_edit_saga(selected_id, new_name.strip()):
                self.sagas = self.controller.get_all_sagas()
                self.populate_sagas()
                
    def delete_saga(self):
        selected_id = self.radio_var.get()
        if selected_id != -1:
            if self.controller.delete_saga(selected_id):
                self.radio_var.set(-1)
                self.sagas = self.controller.get_all_sagas()
                self.populate_sagas()
