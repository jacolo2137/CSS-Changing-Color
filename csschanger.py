import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import re

class CSSCodeColorizer:
    def __init__(self, root):
        self.root = root
        self.root.title("CSS Code Colorizer")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.text = tk.Text(self.root, wrap=tk.WORD)
        self.text.pack(fill=tk.BOTH, expand=True)
        
        self.old_color_label = tk.Label(self.root, text="Aktualny kolor:")
        self.old_color_label.pack(side=tk.TOP, padx=5, pady=2)
        
        self.old_color_entry = tk.Entry(self.root)
        self.old_color_entry.pack(side=tk.TOP, padx=5, pady=2)
        
        self.new_color_label = tk.Label(self.root, text="Nowy kolor:")
        self.new_color_label.pack(side=tk.TOP, padx=5, pady=2)
        
        self.new_color_entry = tk.Entry(self.root)
        self.new_color_entry.pack(side=tk.TOP, padx=5, pady=2)
        
        self.button_apply_color = tk.Button(self.root, text="Zmień kolor", command=self.apply_color)
        self.button_apply_color.pack(side=tk.TOP, padx=5, pady=5)
        
        self.button_load = tk.Button(self.root, text="Wczytaj CSS", command=self.load_css)
        self.button_load.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.button_save = tk.Button(self.root, text="Zapisz zmiany", command=self.save_changes)
        self.button_save.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def load_css(self):
        file_path = filedialog.askopenfilename(filetypes=[("Pliki CSS", "*.css")])
        if file_path:
            with open(file_path, "r") as file:
                css_code = file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, css_code)
                
    def apply_color(self):
        old_color = self.old_color_entry.get().strip()
        new_color = self.new_color_entry.get().strip()
        
        if old_color and new_color:
            updated_css = re.sub(r"\b" + re.escape(old_color) + r"\b", new_color, self.text.get("1.0", tk.END))
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, updated_css)
        else:
            messagebox.showerror("Błąd", "Proszę wypełnić oba pola.")
            
    def save_changes(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".css", filetypes=[("Pliki CSS", "*.css")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text.get("1.0", tk.END))
            messagebox.showinfo("Zapisano", "Zmiany zostały zapisane pomyślnie.")
        
    def on_close(self):
        if messagebox.askokcancel("Zamknij", "Czy na pewno chcesz zamknąć program?"):
            self.root.destroy()

root = tk.Tk()
app = CSSCodeColorizer(root)
root.mainloop()