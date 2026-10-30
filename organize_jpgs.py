from pathlib import Path
import shutil


def move_jpg_files(source_folder, destination_folder):
    source = Path(source_folder).expanduser()
    destination = Path(destination_folder).expanduser()

    if not source.is_dir():
        print(f"Source folder does not exist: {source}")
        return

    # Avoid moving files into the same folder being scanned.
    if source.resolve() == destination.resolve():
        print("Choose a different destination folder.")
        return

    destination.mkdir(parents=True, exist_ok=True)
    moved = 0

    for file_path in source.iterdir():
        if file_path.is_file() and file_path.suffix.lower() == ".jpg":
            target = destination / file_path.name
            if target.exists():
                print(f"Skipped (destination already has this name): {file_path.name}")
                continue
            shutil.move(str(file_path), str(target))
            print(f"Moved: {file_path.name}")
            moved += 1

    print(f"Done. Moved {moved} JPG file(s).")


if __name__ == "__main__":
    print("JPG File Organizer")
    source_path = input("Enter the source folder path: ").strip().strip('"')
    destination_path = input("Enter the destination folder path: ").strip().strip('"')
    move_jpg_files(source_path, destination_path)
