import tkinter as tk
from tkinter import filedialog, messagebox


class DuplicateFileManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Duplicate File Manager")
        self.geometry("500x200")
        self.resizable(False, False)

        self.folder_path = tk.StringVar()

        tk.Label(self, text="Selecione a pasta raiz:").pack(pady=10)
        frame = tk.Frame(self)
        frame.pack(pady=5)
        tk.Entry(frame, textvariable=self.folder_path, width=40, state="readonly").pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(frame, text="Procurar", command=self.select_folder).pack(side=tk.LEFT)
        tk.Button(self, text="Buscar Duplicados", command=self.find_duplicates).pack(
            pady=20
        )

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)

    def find_duplicates(self):
        import os
        import hashlib

        folder = self.folder_path.get()
        if not folder:
            messagebox.showwarning("Aviso", "Selecione uma pasta raiz.")
            return

        file_hashes = {}
        duplicates = []

        for root, _, files in os.walk(folder):
            for name in files:
                file_path = os.path.join(root, name)
                try:
                    file_hash = self.hash_file(file_path)
                except Exception:
                    continue
                if file_hash in file_hashes:
                    duplicates.append((file_hashes[file_hash], file_path))
                else:
                    file_hashes[file_hash] = file_path

        self.show_duplicates(duplicates)

    def hash_file(self, file_path, chunk_size=8192):
        hasher = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    def show_duplicates(self, duplicates):
        win = tk.Toplevel(self)
        win.title("Arquivos Duplicados")
        win.geometry("700x400")
        if not duplicates:
            tk.Label(win, text="Nenhum arquivo duplicado encontrado.").pack(pady=20)
            return
        tk.Label(win, text="Arquivos Duplicados Encontrados:").pack(pady=10)
        frame = tk.Frame(win)
        frame.pack(fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox = tk.Listbox(frame, width=100, height=20, yscrollcommand=scrollbar.set)
        for original, duplicate in duplicates:
            listbox.insert(tk.END, f"{original}\n{duplicate}\n---")
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)


if __name__ == "__main__":
    app = DuplicateFileManagerApp()
    app.mainloop()
