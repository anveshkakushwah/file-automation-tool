


from pathlib import Path
import shutil

# STEP 1: Set the folder to organize
SOURCE_FOLDER = Path("test_files")

# STEP 2: Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "PDFs": [".pdf"],
    "Documents": [".doc", ".docx", ".txt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Python_Files": [".py"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(file_path):
    """Return a category based on the file extension."""
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_files():
    """Organize files into category folders safely."""

    if not SOURCE_FOLDER.exists():
        print(f"Error: Folder not found: {SOURCE_FOLDER}")
        return

    if not SOURCE_FOLDER.is_dir():
        print(f"Error: This path is not a folder: {SOURCE_FOLDER}")
        return

    moved_count = 0
    skipped_count = 0
    error_count = 0

    # Only process files directly inside test_files
    files = [
        item for item in SOURCE_FOLDER.iterdir()
        if item.is_file()
    ]

    if not files:
        print("No files found to organize.")
        return

    print("Starting file organization...\n")

    for file_path in files:
        category = get_category(file_path)
        target_folder = SOURCE_FOLDER / category
        destination = target_folder / file_path.name

        # Avoid overwriting a file with the same name
        if destination.exists():
            print(f"Skipped (name already exists): {file_path.name}")
            skipped_count += 1
            continue

        try:
            # Create the category folder if needed
            target_folder.mkdir(exist_ok=True)

            # Move the file into its category folder
            shutil.move(str(file_path), str(destination))

            print(f"Moved: {file_path.name} -> {category}/")
            moved_count += 1

        except OSError as error:
            print(f"Could not move {file_path.name}: {error}")
            error_count += 1

    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files found: {len(files)}")
    print(f"Files moved: {moved_count}")
    print(f"Files skipped: {skipped_count}")
    print(f"Errors: {error_count}")
    print(f"Organized folder: {SOURCE_FOLDER.resolve()}")


# STEP 3: Run the program
if __name__ == "__main__":
    organize_files()
