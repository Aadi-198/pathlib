import shutil
import time
from pathlib import Path
from tkinter import filedialog, ttk
import tkinter as tk

from config import extension_map

class FileSorterApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configure Main Application Window
        self.title("Minimal File Sorter")
        self.geometry("500x380")
        self.resizable(False, False)

        # Force Mac to bring the window to the front on launch
        self.lift()
        self.attributes('-topmost', True)
        self.after(10, lambda: self.attributes('-topmost', False))

        # Use native macOS styling theme
        self.style = ttk.Style()
        self.style.theme_use('aqua')

        # 1. Title Label
        self.title_label = tk.Label(
            self, 
            text="🗂️ System File Sorter", 
            font=("Helvetica", 20, "bold")
        )
        self.title_label.pack(pady=(25, 15))

        # 2. Main Action Button
        self.select_btn = ttk.Button(
            self, 
            text="Choose Folder to Sort", 
            command=self.browse_folder
        )
        self.select_btn.pack(pady=10, ipady=5)

        # 3. Text Streams Terminal Logging Window (Forced dark terminal style)
        self.status_box = tk.Text(
            self, 
            width=55, 
            height=10, 
            font=("Courier", 12),
            bg="#1c1c1e",       # Dark charcoal background
            fg="#00ff00",       # Classic matrix green text for readability
            insertbackground="white",
            relief="sunken",
            bd=1
        )
        self.status_box.pack(pady=20, padx=20)
        self.status_box.insert("0.0", "System Ready...\nSelect a target directory to automatically sort extensions.")
        self.status_box.configure(state="disabled")

    def log_message(self, message):
        """Streams updates smoothly onto the app text window."""
        self.status_box.configure(state="normal")
        self.status_box.insert("end", f"\n{message}")
        self.status_box.see("end")  # Forces automatic scrolling
        self.status_box.configure(state="disabled")
        self.update_idletasks()  # Refreshes the display grid in real-time

    def browse_folder(self):
        """Triggers the official macOS native Finder folder picker."""
        chosen_dir = filedialog.askdirectory(title="Select Folder to Sort")
        
        if not chosen_dir:
            return  # Safety exit if user cancels out of Finder
            
        target_path = Path(chosen_dir).resolve()
        
        # Flushes the visual terminal box clean for a fresh operational run
        self.status_box.configure(state="normal")
        self.status_box.delete("1.0", "end")
        self.status_box.configure(state="disabled")
        
        self.log_message(f"Scanning target: {target_path.name}...")
        self.sort_engine(target_path)

    def sort_engine(self, target_path):
        """Core backend file manipulation framework."""
        total_files = 0
        moved_files = 0
        unique_extensions = set()

        for item in target_path.iterdir():
            if item.is_dir():
                continue

            total_files += 1
            file_ext = item.suffix.lower()

            if file_ext:
                unique_extensions.add(file_ext)
                folder_name = extension_map.get(file_ext, "Others")
                destination_dir = target_path / folder_name
                destination_dir.mkdir(exist_ok=True)
                final_destination = destination_dir / item.name
                
                try:
                    item.rename(final_destination)
                    self.log_message(f"Moved: {item.name} -> {folder_name}/")
                    moved_files += 1
                except Exception as e:
                    self.log_message(f"❌ Could not move {item.name}: {e}")
                    
        self.log_message("\n✨ Scan Completed Successfully!")
        self.log_message(f"Total loose files found: {total_files} | Sorted: {moved_files}")
        self.log_message(f"Unique extensions: {', '.join(unique_extensions) if unique_extensions else 'None'}")

if __name__ == "__main__":
    app = FileSorterApp()
    app.mainloop()