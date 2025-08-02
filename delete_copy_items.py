import os
import shutil
import argparse
import datetime


def find_copy_items(base_dir, recursive):
    """Find files and folders with 'Copy' in the name."""
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


def delete_item(path, trash_dir=None, dry_run=False):
    if dry_run:
        print(f"[Dry Run] Would delete: {path}")
        return

    try:
        if trash_dir:
            os.makedirs(trash_dir, exist_ok=True)
            shutil.move(path, os.path.join(trash_dir, os.path.basename(path)))
            print(f"Moved to trash: {path}")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Deleted folder: {path}")
        else:
            os.remove(path)
            print(f"Deleted file: {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")


def log_deletion(path, log_file):
    with open(log_file, "a") as log:
        log.write(f"{datetime.datetime.now()} - Deleted: {path}\n")


def main():
    parser = argparse.ArgumentParser(description="Delete or move files/folders with 'Copy' in the name.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be deleted without actually deleting.")
    parser.add_argument("--recursive", action="store_true", help="Search subdirectories recursively.")
    parser.add_argument("--log", action="store_true", help="Log deletions to a file.")
    parser.add_argument("--trash", action="store_true", help="Move items to a trash folder instead of deleting.")

    args = parser.parse_args()

    current_dir = os.getcwd()
    trash_dir = os.path.join(current_dir, "trash") if args.trash else None
    log_file = os.path.join(current_dir, "deletion_log.txt") if args.log else None

    targets = find_copy_items(current_dir, args.recursive)

    if not targets:
        print("No files or folders with 'Copy' in the name found.")
        return

    for item in targets:
        delete_item(item, trash_dir=trash_dir, dry_run=args.dry_run)
        if args.log and not args.dry_run:
            log_deletion(item, log_file)

    print(f"\nProcessed {len(targets)} item(s).")


if __name__ == "__main__":
    main()
