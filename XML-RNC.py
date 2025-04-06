import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Für modernere Widgets (optional, aber empfohlen)

class XMLProcessorGUI:
    def __init__(self, master):
        self.master = master
        master.title("XML-Datenverarbeitung")

        # Pfadauswahl
        self.path_label = ttk.Label(master, text="Ausgewählter XML-Ordner:")
        self.path_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.path_display = ttk.Label(master, text="")
        self.path_display.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

        self.browse_button = ttk.Button(master, text="XML-Ordner auswählen", command=self.browse_folder)
        self.browse_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        # Zahlenbereich
        self.range_label = ttk.Label(master, text="Zahlenbereich der Dateien:")
        self.range_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.from_label = ttk.Label(master, text="Von:")
        self.from_label.grid(row=3, column=0, padx=5, pady=2, sticky="w")
        self.from_entry = ttk.Entry(master, width=10)
        self.from_entry.grid(row=3, column=1, padx=5, pady=2, sticky="ew")

        self.to_label = ttk.Label(master, text="Bis:")
        self.to_label.grid(row=4, column=0, padx=5, pady=2, sticky="w")
        self.to_entry = ttk.Entry(master, width=10)
        self.to_entry.grid(row=4, column=1, padx=5, pady=2, sticky="ew")

        # Sprachauswahl
        self.language_label = ttk.Label(master, text="Gewünschte Sprache:")
        self.language_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        self.language = tk.StringVar(value=None)
        self.de_radio = ttk.Radiobutton(master, text="DE", variable=self.language, value="DE")
        self.de_radio.grid(row=6, column=0, padx=5, pady=2, sticky="w")
        self.en_radio = ttk.Radiobutton(master, text="EN", variable=self.language, value="EN")
        self.en_radio.grid(row=6, column=1, padx=5, pady=2, sticky="w")
        self.fr_radio = ttk.Radiobutton(master, text="FR", variable=self.language, value="FR")
        self.fr_radio.grid(row=6, column=2, padx=5, pady=2, sticky="w")

        # Komponentenliste
        self.components_label = ttk.Label(master, text="Verfügbare Komponenten:")
        self.components_label.grid(row=7, column=0, padx=5, pady=5, sticky="w")

        self.components_list = tk.Listbox(master, selectmode=tk.MULTIPLE, height=10, width=40)
        self.components_list.grid(row=8, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL, command=self.components_list.yview)
        self.scrollbar.grid(row=8, column=3, sticky="ns")
        self.components_list.config(yscrollcommand=self.scrollbar.set)

        # Buttons
        self.load_components_button = ttk.Button(master, text="Komponenten auslesen", command=self.load_components)
        self.load_components_button.grid(row=9, column=0, padx=5, pady=10, sticky="ew")

        self.export_button = ttk.Button(master, text="Daten exportieren", command=self.export_data)
        self.export_button.grid(row=9, column=1, columnspan=2, padx=5, pady=10, sticky="ew")

        # Konfiguration des Grids für responsives Verhalten
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_rowconfigure(8, weight=1)

        # Initialisierung des ausgewählten Pfads
        self.xml_folder_path = ""

    def browse_folder(self):
        self.xml_folder_path = filedialog.askdirectory()
        self.path_display.config(text=self.xml_folder_path)
        print(f"Ausgewählter Ordner: {self.xml_folder_path}") # Nur zur Überprüfung

    def load_components(self):
        # Hier kommt die Logik zum Einlesen der XML-Dateien und der Komponenten
        if not self.xml_folder_path:
            print("Bitte wählen Sie zuerst einen Ordner aus.") # Später durch eine GUI-Meldung ersetzen
            return

        try:
            start_range = int(self.from_entry.get())
            end_range = int(self.to_entry.get())
        except ValueError:
            print("Ungültiger Zahlenbereich.") # Später durch eine GUI-Meldung ersetzen
            return

        selected_language = self.language.get()
        if not selected_language:
            print("Bitte wählen Sie eine Sprache aus.") # Später durch eine GUI-Meldung ersetzen
            return

        self.components_list.delete(0, tk.END) # Liste leeren

        # *** Hier folgt die Logik zum Durchsuchen der Dateien, Parsen des XML und Anzeigen der Komponenten ***
        print(f"Suche im Ordner: {self.xml_folder_path}")
        print(f"Zahlenbereich: {start_range} bis {end_range}")
        print(f"Gewählte Sprache: {selected_language}")

        # Zum Testen (später durch echte Logik ersetzen)
        dummy_components = [f"Komponente A ({selected_language})", f"Komponente B ({selected_language})", f"Komponente C ({selected_language})"]
        for component in dummy_components:
            self.components_list.insert(tk.END, component)

    def export_data(self):
        # Hier kommt die Logik zum Exportieren der ausgewählten Daten in ein Word-Dokument
        selected_indices = self.components_list.curselection()
        selected_components = [self.components_list.get(i) for i in selected_indices]
        print("Ausgewählte Komponenten:", selected_components) # Nur zur Überprüfung
        if not selected_components:
            print("Bitte wählen Sie mindestens eine Komponente aus.") # Später durch eine GUI-Meldung ersetzen
            return

        # *** Hier folgt die Logik zum Auslesen der Detailinformationen und Erstellen des Word-Dokuments ***
        print("Exportiere Daten...")

if __name__ == "__main__":
    root = tk.Tk()
    gui = XMLProcessorGUI(root)
    root.mainloop()
