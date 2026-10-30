# CodeAlpha Task Automation — JPG File Organizer

A small Python script that moves `.jpg` files from one folder into a destination folder.

## Safety notes
- Test using a temporary folder with sample images first.
- The script skips a file if the destination already contains the same filename.
- It moves only files directly inside the source folder (not nested subfolders).
- Moving files changes their location; make a backup if the files are important.

## Run
```bash
python organize_jpgs.py
```
Enter the source and destination folder paths when prompted.

## Concepts practiced
`pathlib`, `shutil`, functions, loops, conditions, and file-system operations.
