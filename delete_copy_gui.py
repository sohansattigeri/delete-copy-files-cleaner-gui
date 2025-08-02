import os
import shutil
import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog


def find_copy_items(base_dir, recursive):
    matches = []
    if recursive:
        for root, dirs, files in os.walk(base_dir):
            for name in dirs + files:
                if "Copy" in name:
                    matches.append(os.path.join(root, name))
    else:
        for item in os.listdir(base_dir):
            if "Copy" in item:
                matches.append(os.path.join(base_dir, item))
    return matches


def delete_item(path, trash_dir=None, dry_run=False, output=None):
    if dry_run:
        output.insert(tk.END, f"[Dry Run] Would delete: {path}\n")
        return

    try:
        if trash_dir:
            os.makedirs(trash_dir, exist_ok=True)
            shutil.move(path, os.path.join(trash_dir, os.path.basename(path)))
            output.insert(tk.END, f"Moved to trash: {path}\n")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            output.insert(tk.END, f"Deleted folder: {path}\n")
        else:
            os.remove(path)
            output.insert(tk.END, f"Deleted file: {path}\n")
    except Exception as e:
        output.insert(tk.END, f"Error deleting {path}: {e}\n")


def run_cleanup():
    output_text.delete(1.0, tk.END)
    base_dir = folder_path_var.get()

    if not base_dir or not os.path.isdir(base_dir):
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    recursive = recursive_var.get()
    dry_run = dry_run_var.get()
    use_trash = trash_var.get()
    log_enabled = log_var.get()

    trash_dir = os.path.join(base_dir, "trash") if use_trash else None
    log_file = os.path.join(base_dir, "deletion_log.txt") if log_enabled else None

    items = find_copy_items(base_dir, recursive)
    if not items:
        output_text.insert(tk.END, "No 'Copy' items found.\n")
        return

    for item in items:
        delete_item(item, trash_dir=trash_dir, dry_run=dry_run, output=output_text)
        if log_enabled and not dry_run:
            with open(log_file, "a") as log:
                log.write(f"{item}\n")

    output_text.insert(tk.END, f"\nProcessed {len(items)} item(s).\n")


def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_var.set(folder_selected)


# ---------------- GUI Setup ----------------
app = tk.Tk()
app.title("Delete 'Copy' Files and Folders")
app.geometry("750x550")

# Variables
dry_run_var = tk.BooleanVar()
recursive_var = tk.BooleanVar()
trash_var = tk.BooleanVar()
log_var = tk.BooleanVar()
folder_path_var = tk.StringVar()

# Path Selection
tk.Label(app, text="Target Folder:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
tk.Entry(app, textvariable=folder_path_var, width=60).grid(row=0, column=1, padx=5)
tk.Button(app, text="Browse", command=browse_folder).grid(row=0, column=2, padx=5)

# Options
tk.Checkbutton(app, text="Dry Run", variable=dry_run_var).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(app, text="Recursive", variable=recursive_var).grid(row=1, column=1, sticky="w", padx=10)
tk.Checkbutton(app, text="Move to Trash", variable=trash_var).grid(row=1, column=2, sticky="w", padx=10)
tk.Checkbutton(app, text="Log", variable=log_var).grid(row=1, column=3, sticky="w", padx=10)

# Run Button
tk.Button(app, text="Run Cleanup", command=run_cleanup, bg="tomato", fg="white", width=20).grid(row=2, column=0, columnspan=4, pady=10)

# Output log area
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=90, height=25)
output_text.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

app.mainloop()
