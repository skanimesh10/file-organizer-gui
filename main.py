import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Define your categories
categories = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'webp'],
    'documents': ['pdf', 'docx', 'txt', 'pptx', 'csv'],
    'videos': ['mp4', 'mov', 'avi'],
    'music': ['mp3', 'wav', 'aac'],
    'application': ['dmg']
}

# Log file for uncategorized extensions
log_file = 'uncategorized_extensions.txt'


def categorize_file(file_path, destination_folder, output_text):
    file_extension = file_path.suffix[1:].lower()
    categorized = False

    for category, extensions in categories.items():
        if file_extension in extensions:
            category_folder = destination_folder / category
            category_folder.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(category_folder / file_path.name))
            output_text.insert(tk.END, f"Moved {file_path.name} to {category_folder}\n")
            categorized = True
            break

    if not categorized:
        others_folder = destination_folder / 'others'
        others_folder.mkdir(exist_ok=True)
        shutil.move(str(file_path), str(others_folder / file_path.name))
        output_text.insert(tk.END, f"Moved {file_path.name} to {others_folder}\n")

        # Append the uncategorized extension to the log file
        with open(log_file, 'a') as log:
            log.write(f"{file_extension}: {file_path.name}\n")


def organize_files(source_folder, output_text):
    destination_folder = source_folder / 'organized_files'
    destination_folder.mkdir(exist_ok=True)

    for file_path in source_folder.glob('*'):
        if file_path.is_file():
            categorize_file(file_path, destination_folder, output_text)

    output_text.insert(tk.END, "Files have been organized.\n")
    output_text.insert(tk.END, f"Check '{log_file}' for any uncategorized file extensions.\n")


def browse_and_organize():
    folder_path = filedialog.askdirectory()
    if folder_path:
        source_folder = Path(folder_path)

        output_text.delete(1.0, tk.END)  # Clear previous output
        organize_files(source_folder, output_text)
    else:
        messagebox.showwarning("No Folder Selected", "Please select a folder to organize.")


# Set up the main application window
root = tk.Tk()
root.title("File Organizer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Button to browse and select the folder
browse_button = tk.Button(frame, text="Select Folder to Organize", command=browse_and_organize)
browse_button.pack()

# Output area to show the results
output_text = scrolledtext.ScrolledText(frame, width=60, height=20)
output_text.pack()

# Start the Tkinter event loop
root.mainloop()
