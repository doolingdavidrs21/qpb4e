"""
Lab 12: File Operations Exercise

Calculate total size of .test files (excluding symlinks) and move them to backup.
Implements solutions using both pathlib and os/os.path approaches.
"""

import os
from pathlib import Path


# ============================================================================
# PATHLIB IMPLEMENTATION
# ============================================================================

def get_test_files_size_pathlib(directory="."):
    """Calculate total size of .test files (excluding symlinks) using pathlib."""
    cur_path = Path(directory)
    total_size = 0

    for file_path in cur_path.rglob("*.test"):
        if not file_path.is_symlink():
            total_size += file_path.stat().st_size

    return total_size


def move_test_files_to_backup_pathlib(directory="."):
    """Move .test files to backup directory using pathlib.

    Returns the total size of files moved.
    """
    cur_path = Path(directory)
    backup_path = cur_path / "backup"
    backup_path.mkdir(exist_ok=True)

    total_size = 0
    for file_path in cur_path.rglob("*.test"):
        # Skip symlinks and files already in backup directory
        if not file_path.is_symlink() and "backup" not in file_path.parts:
            total_size += file_path.stat().st_size
            file_path.rename(backup_path / file_path.name)

    return total_size


# ============================================================================
# OS/OS.PATH IMPLEMENTATION
# ============================================================================

def get_test_files_size_os(directory="."):
    """Calculate total size of .test files (excluding symlinks) using os."""
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.test') and not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)

    return total_size


def move_test_files_to_backup_os(directory="."):
    """Move .test files to backup directory using os.

    Returns the total size of files moved.
    """
    backup_dir = os.path.join(directory, "backup")
    os.makedirs(backup_dir, exist_ok=True)

    total_size = 0
    for root, dirs, files in os.walk(directory):
        # Skip the backup directory itself
        if "backup" in root:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith('.test') and not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
                os.rename(file_path, os.path.join(backup_dir, file))

    return total_size


# ============================================================================
# DEMO / MAIN
# ============================================================================

def main():
    test_dir = "test_files"

    print("=" * 60)
    print("Lab 12: File Operations Exercise")
    print("=" * 60)

    # Part 1: Calculate size using pathlib
    print("\n--- Using pathlib ---")
    size_pathlib = get_test_files_size_pathlib(test_dir)
    print(f"Total size of .test files (pathlib): {size_pathlib} bytes")

    # Part 2: Calculate size using os
    print("\n--- Using os/os.path ---")
    size_os = get_test_files_size_os(test_dir)
    print(f"Total size of .test files (os): {size_os} bytes")

    # Part 3: Move files to backup (using pathlib version)
    print("\n--- Moving files to backup (using pathlib) ---")
    moved_size = move_test_files_to_backup_pathlib(test_dir)
    print(f"Moved {moved_size} bytes of .test files to backup/")

    # List backup contents
    backup_path = Path(test_dir) / "backup"
    if backup_path.exists():
        print("\nFiles in backup directory:")
        for f in backup_path.iterdir():
            print(f"  - {f.name} ({f.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
