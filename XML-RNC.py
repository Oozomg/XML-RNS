import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class XMLProcessorGUI:
    def __init__(self, master):
        self.master = master
        master.title("XML-Datenverarbeitung")

        # Pfadauswahl XML-Ordner
        self.xml_path_label = ttk.Label(master, text="Ausgewählter XML-Ordner:")
        self.xml_path_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.xml_path_display = ttk.Label(master, text="")
        self.xml_path_display.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        self.browse_xml_button = ttk.Button(master, text="XML-Ordner auswählen", command=self.browse_xml_folder)
        self.browse_xml_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # Pfadauswahl Word-Vorlage
        self.word_template_label = ttk.Label(master, text="Ausgewählte Word-Vorlage:")
        self.word_template_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.word_template_display = ttk.Label(master, text="")
        self.word_template_display.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        self.browse_word_button = ttk.Button(master, text="Word-Vorlage auswählen", command=self.browse_word_template)
        self.browse_word_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        # Zahlenbereich
        self.range_label = ttk.Label(master, text="Vierstelliger Zahlenbereich der Dateien:")
        self.range_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.from_label = ttk.Label(master, text="Von:")
        self.from_label.grid(row=5, column=0, padx=5, pady=2, sticky="w")
        self.from_entry = ttk.Entry(master, width=10, validate="focusout", validatecommand=(master.register(self.validate_four_digit), "%P")) # Optionale Live-Validierung
        self.from_entry.grid(row=5, column=1, padx=5, pady=2, sticky="ew")

        self.to_label = ttk.Label(master, text="Bis:")
        self.to_label.grid(row=6, column=0, padx=5, pady=2, sticky="w")
        self.to_entry = ttk.Entry(master, width=10, validate="focusout", validatecommand=(master.register(self.validate_four_digit), "%P")) # Optionale Live-Validierung
        self.to_entry.grid(row=6, column=1, padx=5, pady=2, sticky="ew")

        # Sprachauswahl
        self.language_label = ttk.Label(master, text="Gewünschte Sprache:")
        self.language_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        self.language = tk.StringVar(value=None)
        self.de_radio = ttk.Radiobutton(master, text="DE", variable=self.language, value="DE")
        self.de_radio.grid(row=8, column=0, padx=5, pady=2, sticky="w")
        self.en_radio = ttk.Radiobutton(master, text="EN", variable=self.language, value="EN")
        self.en_radio.grid(row=8, column=1, padx=5, pady=2, sticky="w")
        self.fr_radio = ttk.Radiobutton(master, text="FR", variable=self.language, value="FR")
        self.fr_radio.grid(row=8, column=2, padx=5, pady=2, sticky="w")

        # Komponentenliste
        self.components_label = ttk.Label(master, text="Verfügbare Komponenten:")
        self.components_label.grid(row=9, column=0, padx=5, pady=5, sticky="w")

        self.components_list = tk.Listbox(master, selectmode=tk.MULTIPLE, height=10, width=40)
        self.components_list.grid(row=10, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.components_list.yview)
        self.scrollbar.grid(row=10, column=3, sticky="ns")
        self.components_list.config(yscrollcommand=self.scrollbar.set)

        # Buttons
        self.load_components_button = ttk.Button(master, text="Komponenten auslesen", command=self.load_components)
        self.load_components_button.grid(row=11, column=0, padx=5, pady=10, sticky="ew")

        self.export_button = ttk.Button(master, text="Daten exportieren", command=self.export_data)
        self.export_button.grid(row=11, column=1, columnspan=2, padx=5, pady=10, sticky="ew")

        # Konfiguration des Grids für responsives Verhalten
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_rowconfigure(10, weight=1)

        # Initialisierung der Pfade
        self.xml_folder_path = ""
        self.word_template_path = ""

    def validate_four_digit(self, new_value):
        return len(new_value) == 0 or (new_value.isdigit() and len(new_value) == 4)


    def browse_xml_folder(self):
        self.xml_folder_path = filedialog.askdirectory()
        self.xml_path_display.config(text=self.xml_folder_path)
        print(f"Ausgewählter XML-Ordner: {self.xml_folder_path}")

    def browse_word_template(self):
        self.word_template_path = filedialog.askopenfilename(
            defaultextension=".docx",
            filetypes=[("Word-Dokumente", "*.docx"), ("Alle Dateien", "*.*")]
        )
        self.word_template_display.config(text=self.word_template_path)
        print(f"Ausgewählte Word-Vorlage: {self.word_template_path}")

    def load_components(self):
        if not self.xml_folder_path:
            messagebox.showerror("Fehler", "Bitte wählen Sie zuerst einen XML-Ordner aus.")
            return

        start_str = self.from_entry.get()
        end_str = self.to_entry.get()

        if not (start_str.isdigit() and len(start_str) == 4 and
                end_str.isdigit() and len(end_str) == 4):
            messagebox.showerror("Fehler", "Der Zahlenbereich muss aus vierstelligen Zahlen bestehen.")
            return

        try:
            start_range = int(start_str)
            end_range = int(end_str)
            if start_range > end_range:
                messagebox.showerror("Fehler", "Der 'Von'-Wert muss kleiner oder gleich dem 'Bis'-Wert sein.")
                return
        except ValueError:
            messagebox.showerror("Fehler", "Ungültiger Zahlenbereich.") # Sollte durch die vorherige Prüfung abgedeckt sein

        selected_language = self.language.get()
        if not selected_language:
            messagebox.showerror("Fehler", "Bitte wählen Sie eine Sprache aus.")
            return

        self.components_list.delete(0, tk.END)

        print(f"Suche im Ordner: {self.xml_folder_path}")
        print(f"Zahlenbereich: {start_range} bis {end_range}")
        print(f"Gewählte Sprache: {selected_language}")

        # *** Hier folgt später die Logik zum Durchsuchen der Dateien, Parsen des XML und Anzeigen der Komponenten ***
        dummy_components = [f"Komponente A ({selected_language})", f"Komponente B ({selected_language})", f"Komponente C ({selected_language})"]
        for component in dummy_components:
            self.components_list.insert(tk.END, component)

    def export_data(self):
        if not self.word_template_path:
            print("Bitte wählen Sie zuerst eine Word-Vorlage aus.")
            return

        selected_indices = self.components_list.curselection()
        selected_components = [self.components_list.get(i) for i in selected_indices]
        print("Ausgewählte Komponenten:", selected_components)
        if not selected_components:
            print("Bitte wählen Sie mindestens eine Komponente aus.")
            return

        # *** Hier folgt später die Logik zum Auslesen der Detailinformationen aus den XML-Dateien
        # *** und zum Schreiben in die Word-Vorlage ***
        print(f"Verwende Word-Vorlage: {self.word_template_path}")
        print("Exportiere Daten in die Vorlage...")

if __name__ == "__main__":
    root = tk.Tk()
    gui = XMLProcessorGUI(root)
    root.mainloop()
