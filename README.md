# File Organizer with GUI

This Python project provides a simple graphical user interface (GUI) to organize files in a specified folder based on their file types. The files are categorized into different folders like `images`, `documents`, `videos`, `music`,`application` and `others`. If a file type is not recognized, it is moved to an `others` folder, and its extension is logged.

## Features

- **Easy File Organization**: Automatically categorize files into folders based on their extensions.
- **Uncategorized Files Logging**: Log unrecognized file extensions in a text file (`uncategorized_extensions.txt`).
- **GUI Interface**: Simple GUI built with `tkinter` for selecting the folder and displaying results.

## Categories

The script organizes files into the following categories:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.pptx`, `.csv`
- **Videos**: `.mp4`, `.mov`, `.avi`
- **Music**: `.mp3`, `.wav`, `.aac`
- **Application**: `.dmg`
- **Others**: Any file that doesn't match the above categories

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/skanimesh10/file-organizer-gui.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd file-organizer-gui
    ```

3. **Install required dependencies:**

    This project requires Python 3.x and the `tkinter` library, which is included with Python on most systems. No additional installations are required.

## Usage

1. **Run the script:**

    ```bash
    python file_organizer_gui.py
    ```

2. **Select the folder to organize:**

    - Click the "Select Folder to Organize" button.
    - Choose the folder containing the files you want to organize.

3. **View the results:**

    - The files will be organized into the `organized_files` folder inside the selected directory.
    - The GUI will display which files were moved to which folders.
    - If there are any uncategorized files, their extensions will be logged in the `uncategorized_extensions.txt` file.

## Customization

You can customize the categories by editing the `categories` dictionary in the script. For example, to add a new category for `archives` with file types `.zip`, `.tar`, and `.gz`:

```python
categories = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'webp'],
    'documents': ['pdf', 'docx', 'txt', 'pptx', 'csv'],
    'videos': ['mp4', 'mov', 'avi'],
    'music': ['mp3', 'wav', 'aac'],
    'application': ['dmg']
    'archives': ['zip', 'tar', 'gz']  # New category
}
