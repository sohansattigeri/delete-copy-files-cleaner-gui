# 🧹 Delete Copy Items Script

This Python script deletes or moves to trash any **file or folder** with **"Copy"** (case-sensitive) in its name from a specified directory. It's ideal for cleaning up duplicate or backup files and folders.

---

## ✅ Features

* 🔄 Recursive scanning of subdirectories
* 🧪 Dry-run mode (preview before deleting)
* 🗑️ Trash folder support (move instead of delete)
* 🪵 Logging of deletions to a file
* 🪟 Simple GUI application with folder selection

---

## 🚀 Usage

### 🧾 Command-Line Version

```bash
python delete_copy_items.py [options]
```

#### 🔧 Options

| Option        | Description                                  |
| ------------- | -------------------------------------------- |
| `--dry-run`   | Preview what will be deleted                 |
| `--recursive` | Search in subdirectories                     |
| `--trash`     | Move files to `./trash/` instead of deleting |
| `--log`       | Log deleted paths to `deletion_log.txt`      |

### 🔁 Command-Line Examples

**Dry run preview:**

```bash
python delete_copy_items.py --dry-run
```

**Delete recursively and log:**

```bash
python delete_copy_items.py --recursive --log
```

**Move to trash instead of deleting:**

```bash
python delete_copy_items.py --trash
```

**Fully featured run:**

```bash
python delete_copy_items.py --recursive --log --trash
```

---

### 🖥️ GUI Version

A GUI app is available via `delete_copy_gui.py`.

#### 📦 Features

* Select the folder you want to scan
* Toggle dry-run, recursive, trash, and logging options
* Click a button to clean up files/folders
* View deleted/moved items and logs inside the app

#### ▶️ How to Run

```bash
python delete_copy_gui.py
```

This will open a simple desktop app where you can choose the target folder and options, and run the cleanup interactively.

---

## ⚠️ Caution

* The match is **case-sensitive**: only items with "Copy" (not "copy") are affected.
* Always run with `--dry-run` or select it in the GUI before permanent deletion.
* Use `--trash` or GUI's trash option if you want the option to recover items later.

---

## 📂 Output

* If `--trash` or trash checkbox is used, deleted items go into a folder named `trash/` inside the selected folder.
* If `--log` or log checkbox is used, a `deletion_log.txt` file is created inside the selected folder with deletion timestamps.

---

## 📜 License

This script is free to use and modify. Attribution appreciated but not required.
