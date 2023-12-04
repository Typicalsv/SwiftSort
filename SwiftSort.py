import os
import shutil
import tkinter as tk

base_directory = 'General'

if not os.path.exists(base_directory):
    os.makedirs(base_directory)

if not os.path.exists(f'{base_directory}/Mixed'):
    os.makedirs(f'{base_directory}/Mixed')

if not os.path.exists(f'{base_directory}/Images'):
    os.makedirs(f'{base_directory}/Images')

if not os.path.exists(f'{base_directory}/Videos'):
    os.makedirs(f'{base_directory}/Videos')

if not os.path.exists(f'{base_directory}/Audio'):
    os.makedirs(f'{base_directory}/Audio')

if not os.path.exists(f'{base_directory}/Text-Docs'):
    os.makedirs(f'{base_directory}/Text-Docs')

if not os.path.exists(f'{base_directory}/Word'):
    os.makedirs(f'{base_directory}/Word')

if not os.path.exists(f'{base_directory}/Excel'):
    os.makedirs(f'{base_directory}/Excel')

if not os.path.exists(f'{base_directory}/PowerPoint'):
    os.makedirs(f'{base_directory}/PowerPoint')

if not os.path.exists(f'{base_directory}/Compressed'):
    os.makedirs(f'{base_directory}/Compressed')

if not os.path.exists(f'{base_directory}/Others'):
    os.makedirs(f'{base_directory}/Others')

def move_files():
    mixed_directory = 'General/Mixed'

    # Ensure the 'Mixed' directory exists
    if not os.path.exists(mixed_directory):
        log_text.insert(tk.END, "The 'Mixed' directory does not exist.\n")
        return

    files = os.listdir(mixed_directory)
    if not files:
        log_text.insert(tk.END, "The directory Mixed is empty.\n")
    else:
        for file in files:
            file_name, extension = os.path.splitext(file)
            source_path = os.path.join(mixed_directory, file)

            if extension.lower() in ['.jpg', '.png', '.gif']:
                destination_folder = os.path.join(base_directory, 'Images')
            elif extension.lower() in ['.mp4', '.avi', '.mkv']:
                destination_folder = os.path.join(base_directory, 'Videos')
            elif extension.lower() in ['.mp3', '.wav']:
                destination_folder = os.path.join(base_directory, 'Audio')
            elif extension.lower() in ['.txt', '.doc', '.pdf']:
                destination_folder = os.path.join(base_directory, 'Text-Docs')
            elif extension.lower() in ['.docx']:
                destination_folder = os.path.join(base_directory, 'Word')
            elif extension.lower() in ['.xlsx']:
                destination_folder = os.path.join(base_directory, 'Excel')
            elif extension.lower() in ['.ppt', '.pptx']:
                destination_folder = os.path.join(base_directory, 'PowerPoint')
            elif extension.lower() in ['.zip', '.rar']:
                destination_folder = os.path.join(base_directory, 'Compressed')
            else:
                destination_folder = os.path.join(base_directory, 'Others')

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            log_text.insert(tk.END, f"Moved {file} to {destination_folder}\n")

base_directory = 'General'
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

root = tk.Tk()
root.title("File Sorter")

start_button = tk.Button(root, text="Start Sorting", command=move_files)
start_button.pack(pady=20)

# Text widget to display log
log_text = tk.Text(root, height=10, width=50)
log_text.pack(pady=10)

root.mainloop()
